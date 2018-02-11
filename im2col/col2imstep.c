#include "mex.h"
#include <math.h>
#include <string.h>

/* Input Arguments */

#define	X_IN	 prhs[0]
#define SZ_IN   prhs[1]
#define SZ_OUT  prhs[2]
#define S_IN    prhs[3]


/* Output Arguments */

#define	B_OUT	plhs[0]

void mexFunction(int nlhs, mxArray *plhs[], int nrhs, const mxArray *prhs[])
{
	double *x, *b, *sz, *s, *c;
    mxArray *C;
    mwSize sz_in[3], sz_out[3], stepsize[3], ndims;
    mwIndex i, j, k, m, n, p, q, xy, ch, Pixels, N_patches;
    
    /* Check for proper number of arguments */
    
    if (nrhs < 3 || nrhs > 4) {
      mexErrMsgTxt("Invalid number of input arguments."); 
    } else if (nlhs > 1) {
      mexErrMsgTxt("Too many output arguments."); 
    } 
    
    
    /* Check the the input dimensions */ 
    
    ndims = mxGetNumberOfDimensions(X_IN);  /* 2 */
    
    if (!mxIsDouble(X_IN) || mxIsComplex(X_IN) || ndims>2) {
      mexErrMsgTxt("X should be a 2-D double matrix.");
    }
    if (!mxIsDouble(SZ_IN) || mxIsComplex(SZ_IN) || mxGetNumberOfDimensions(SZ_IN)>2 || mxGetM(SZ_IN)*mxGetN(SZ_IN)!=3) {
      mexErrMsgTxt("Invalid block size.");
    }
    if (nrhs == 3) {
      if (!mxIsDouble(S_IN) || mxIsComplex(S_IN) || mxGetNumberOfDimensions(S_IN)>2 || mxGetM(S_IN)*mxGetN(S_IN)!=3) {
        mexErrMsgTxt("Invalid step size.");
      }
    }
    
    /* Get parameters */
    s = mxGetPr(SZ_IN);
    if (s[0]<1 || s[1]<1 || (ndims==3 && s[2]<1)) {
      mexErrMsgTxt("Invalid block size.");
    }
    sz_in[0] = (mwSize)(s[0] + 0.01);
    sz_in[1] = (mwSize)(s[1] + 0.01);
    sz_in[2] = ndims==3 ? (mwSize)(s[2] + 0.01) : 1;
    
    /* Get out image size */
    s = mxGetPr(SZ_OUT);
    if (s[0]<sz_in[0] || s[1]<sz_in[1]) {
      mexErrMsgTxt("Block size too large(than image size).");
    }
    sz_out[0] = (mwSize)(s[0] + 0.01);
    sz_out[1] = (mwSize)(s[1] + 0.01);
    sz_out[2] = (mwSize)(s[2] + 0.01);
    
    if (nrhs == 4) {
      s = mxGetPr(S_IN);
      if (s[0]<1 || s[1]<1 || (ndims==3 && s[2]<1)) {
        mexErrMsgTxt("Invalid step size.");
      }
      stepsize[0] = (mwSize)(s[0] + 0.01);
      stepsize[1] = (mwSize)(s[1] + 0.01);
      stepsize[2] = ndims==3 ? (mwSize)(s[2] + 0.01) : 1;
    }
    else {
      stepsize[0] = stepsize[1] = stepsize[2] = 1;
    }
    
    Pixels = (mxGetDimensions(X_IN))[0];
    N_patches = (mxGetDimensions(X_IN))[1];
    
    /* Create a matrix for the return argument */
    
    const mwSize dims[3]={sz_out[0], sz_out[1], sz_out[2]};
    B_OUT = mxCreateNumericArray(3, dims, mxDOUBLE_CLASS, mxREAL);
    C = mxCreateNumericArray(3, dims, mxDOUBLE_CLASS, mxREAL);
    
    /* Assign pointers */
    
    x = mxGetPr(X_IN);
    b = mxGetPr(B_OUT);
    c = mxGetPr(C);
    /* iterate over all blocks */
    
    
    k = sz_out[0]-sz_in[0] + 1;
    for (i=0; i < N_patches; i++) {
        m = i % k;  /* row index of left-up point */
        n = (i-m) / k;  /* column index of left-up point */
        for(j=0; j < Pixels; j++){
            xy = j % (sz_in[0] * sz_in[1]);
            p = xy % sz_in[0];  /* row index */
            q = (xy-p)/sz_in[0];    /* column index */
            ch = (j - xy) / (sz_in[0] * sz_in[1]);  /* channel index */
            b[sz_out[0] * sz_out[1] * ch + (n+q)*sz_out[0] + m + p] += x[i * Pixels + j];
			c[sz_out[0] * sz_out[1] * ch + (n+q)*sz_out[0] + m + p] += 1;
            /*mexPrintf("%d, %f \n", (sz_out[0] * sz_out[1] * ch + (n+q)*sz_out[0] + m + p), x[i * Pixels + j]);
             */
		}
	}
    
    for (i=0; i<sz_out[0]*sz_out[1]*sz_out[2];i++){
        b[i] = b[i] / (c[i] + 0.000000);
    }
	return ;
}            