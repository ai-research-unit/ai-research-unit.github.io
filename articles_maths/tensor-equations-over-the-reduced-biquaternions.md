# __Tensor Equations over the Reduced Biquaternions__

## Introduction

This article solves the tensor equation $A\ast X=B$ over the reduced biquaternions. It gives the solvability criterion, the general solution, the Hermitian solution, the least-squares solutions and the minimum-norm least-squares solution, and it treats the right-handed equation $X\ast A=B$. Every statement reduces to the pair of complex tensor equations carried by the two idempotent coordinates.

The product is *The t-Product of Reduced Biquaternion Tensors*, the inverse is *The Moore-Penrose Inverse of a Reduced Biquaternion Tensor*, and the norms are those of *Reduced Biquaternion Tensors as a Vector Space*. The matrix counterpart is *Matrix Equations and Structured Solutions over the Reduced Biquaternions*; the application is *Color Video Compression and Deblurring with Reduced Biquaternion Tensors*.

The source is Cui-E Yu, Xin Liu, Hui Luo and Yang Zhang, "Reduced biquaternion tensors and applications in color video processing", Section 5.

## The Solvability Criterion

Let $A\in\mathbb{B}_{\mathrm{r}}^{n_1\times n_2\times n_3}$, $B\in\mathbb{B}_{\mathrm{r}}^{n_1\times n_4\times n_3}$ and $X\in\mathbb{B}_{\mathrm{r}}^{n_2\times n_4\times n_3}$. The equation is

$$
A\ast X=B.
$$

The two projectors of *The Moore-Penrose Inverse of a Reduced Biquaternion Tensor* are

$$
L_A=\mathrm I_{n_2}-A^\dagger\ast A,\qquad R_A=\mathrm I_{n_1}-A\ast A^\dagger.
$$

They satisfy $A\ast L_A=0$, $R_A\ast A=0$, $L_A\ast A^\dagger=0$ and $A^\dagger\ast R_A=0$.

**Theorem (solvability and general solution).** The equation $A\ast X=B$ has a solution if and only if

$$
\boxed{\;
R_A\ast B=0
\;}.
$$

When this holds, the general solution is

$$
X=A^\dagger\ast B+L_A\ast Y,
$$

where $Y\in\mathbb{B}_{\mathrm{r}}^{n_2\times n_4\times n_3}$ is arbitrary.

*Proof.* If $X$ is a solution, then $R_A\ast B=R_A\ast A\ast X=0$ because $R_A\ast A=0$. Conversely, if $R_A\ast B=0$, then $A\ast A^\dagger\ast B=B$, so $X_0=A^\dagger\ast B$ is a solution. For an arbitrary solution $X$,

$$
X=A^\dagger\ast A\ast X+L_A\ast X=A^\dagger\ast B+L_A\ast X,
$$

so every solution has the stated form. Conversely, every tensor of that form is a solution because $A\ast L_A=0$ and $A\ast A^\dagger\ast B=B$.

**Corollary (the minimum-norm solution).** When the equation is solvable, the solution of minimum Frobenius norm is $X=A^\dagger\ast B$.

*Proof.* The two terms of the general solution are orthogonal: $L_A\ast A^\dagger=0$, hence $(A^\dagger)^{\mathsf H}\ast L_A=0$, and

$$
\|A^\dagger\ast B+L_A\ast Y\|_{\mathrm F}^2=\|A^\dagger\ast B\|_{\mathrm F}^2+\|L_A\ast Y\|_{\mathrm F}^2.
$$

The minimum is attained at $L_A\ast Y=0$.

## The Least-Squares Solutions

When $R_A\ast B\neq0$ the equation has no solution, and one minimizes the residual instead.

**Theorem (least squares).** The least-squares solutions of $A\ast X=B$ are

$$
\boxed{\;
X=A^\dagger\ast B+L_A\ast W
\;},
$$

where $W$ is arbitrary, and the minimum-norm least-squares solution is $X=A^\dagger\ast B$. The least-squares solutions are exactly the solutions of the normal equation

$$
A^{\mathsf H}\ast(A\ast X-B)=0.
$$

*Proof.* By the norm identity of *The Singular Value Decomposition of a Reduced Biquaternion Tensor*,

$$
\|A\ast X-B\|_{\mathrm F}=\frac1{\sqrt{n_3}}\|\operatorname{diag}(\widehat A)\operatorname{diag}(\widehat X)-\operatorname{diag}(\widehat B)\|_{\mathrm F}.
$$

The minimum is therefore attained slice by slice, and the matrix least-squares solutions of $\widehat A^{(k)}\widehat X^{(k)}=\widehat B^{(k)}$ are

$$
\widehat X^{(k)}=(\widehat A^{(k)})^{\dagger}\widehat B^{(k)}+(\mathrm I-(\widehat A^{(k)})^{\dagger}\widehat A^{(k)})\widehat W^{(k)}.
$$

Assembling the slices and inverting the transform gives the stated form. The normal equation is the derivative of the residual, and it is satisfied by the same expression because $A^{\mathsf H}(\mathrm I-A A^\dagger)=0$. The minimum-norm statement is the orthogonality argument of the previous corollary.

**Remark (the two normal equations).** The equation $A\ast X=B$ and its normal equation have the same least-squares solutions; the normal equation is solvable for every $B$, while the original equation is solvable only when $R_A\ast B=0$. **The pseudoinverse solution $A^\dagger\ast B$ is the canonical one**: it is the least-squares solution of minimum norm, and it is the exact solution whenever an exact solution exists.

## The Hermitian Solution

Let $A,B\in\mathbb{B}_{\mathrm{r}}^{n\times n\times n_3}$ be square, and suppose that $X$ is required to be Hermitian, $X^{\mathsf H}=X$. The equation is $A\ast X=B$ with $B$ square.

**Theorem (Hermitian solutions).** The equation has a Hermitian solution if and only if

$$
\boxed{\;
R_A\ast B=0,\qquad B\ast A^{\mathsf H}=A\ast B^{\mathsf H}
\;}.
$$

When these conditions hold, the general Hermitian solution is

$$
X=A^\dagger\ast B+(A^\dagger\ast B)^{\mathsf H}
-A^\dagger\ast B\ast A^{\mathsf H}\ast(A^\dagger)^{\mathsf H}
+L_A\ast U\ast L_A,
$$

where $U\in\mathbb{B}_{\mathrm{r}}^{n\times n\times n_3}$ is an arbitrary Hermitian tensor.

*Proof.* If $X$ is Hermitian and $A\ast X=B$, then $R_A\ast B=R_A\ast A\ast X=0$, and $B^{\mathsf H}=X^{\mathsf H}\ast A^{\mathsf H}=X\ast A^{\mathsf H}$, so

$$
B\ast A^{\mathsf H}=A\ast X\ast A^{\mathsf H}=A\ast B^{\mathsf H}.
$$

Conversely, assume the two conditions. The tensor $B\ast A^{\mathsf H}$ is Hermitian because its conjugate transpose is $A\ast B^{\mathsf H}$, which equals it by the second condition. The displayed $X$ is Hermitian: the first two terms are conjugate pairs, the third is Hermitian because $B\ast A^{\mathsf H}$ is, and the last is Hermitian because $L_A$ and $U$ are. Applying $A$ kills the last term, and the first term gives $B$ because $R_A\ast B=0$. The second term becomes $A\ast B^{\mathsf H}\ast(A^\dagger)^{\mathsf H}$; the third becomes $A\ast A^\dagger\ast B\ast A^{\mathsf H}\ast(A^\dagger)^{\mathsf H}=A\ast B^{\mathsf H}\ast(A^\dagger)^{\mathsf H}$, using $A\ast A^\dagger\ast A=A$ and $B\ast A^{\mathsf H}=A\ast B^{\mathsf H}$. The two cancel, so $A\ast X=B$.

For the general form, let $X_0$ be any Hermitian solution and set $U=X_0$. Put $P=A^\dagger\ast A$ and $B=A\ast X_0$. The first term of the display is $P\ast X_0$, the second is $X_0\ast P$, the third is

$$
A^\dagger\ast A\ast X_0\ast A^{\mathsf H}\ast(A^\dagger)^{\mathsf H}
=P\ast X_0\ast A^{\mathsf H}\ast(A^\dagger)^{\mathsf H}
=P\ast X_0\ast P,
$$

because $X_0\ast A^{\mathsf H}=B^{\mathsf H}$ and $B^{\mathsf H}\ast(A^\dagger)^{\mathsf H}=(A^\dagger\ast B)^{\mathsf H}=(P\ast X_0)^{\mathsf H}=X_0\ast P$; the last term is $(\mathrm I-P)\ast X_0\ast(\mathrm I-P)$. The sum of the four is $X_0$, so the displayed family contains every Hermitian solution.

**Remark (the source's condition).** The source writes the condition as $A\ast B^{*}=B\ast A^{*}$, with its star the bar-transpose of this branch; this is $A\ast B^{\mathsf H}=B\ast A^{\mathsf H}$, the condition used here. The condition says that $A\ast B^{\mathsf H}$ is Hermitian, and it is what makes the cancellation in the proof work.

**Remark (the rectangular case).** When $A$ is $n_1\times n_2$ with $n_1\neq n_2$, the Hermitian unknown $X$ is $n_2\times n_2$ and $B$ is $n_1\times n_2$; the two sides of the condition $B\ast A^{\mathsf H}=A\ast B^{\mathsf H}$ have different shapes, so the condition is formable only in the square case. The rectangular Hermitian problem requires a different compatibility condition and is not treated here; the rectangular equation without the Hermitian constraint is covered by the solvability and least-squares theorems above.

## The Right-Handed Equation

Let $A\in\mathbb{B}_{\mathrm{r}}^{n_2\times n_4\times n_3}$, $B\in\mathbb{B}_{\mathrm{r}}^{n_1\times n_4\times n_3}$ and $X\in\mathbb{B}_{\mathrm{r}}^{n_1\times n_2\times n_3}$. The equation is

$$
X\ast A=B.
$$

**Theorem (right-handed least squares).** The least-squares solutions of $X\ast A=B$ are

$$
X=B\ast A^\dagger+W\ast R_A,
$$

where $R_A=\mathrm I_{n_2}-A\ast A^\dagger$ and $W\in\mathbb{B}_{\mathrm{r}}^{n_1\times n_2\times n_3}$ is arbitrary. The minimum-norm least-squares solution is $X=B\ast A^\dagger$. The normal equation is

$$
(X\ast A-B)\ast A^{\mathsf H}=0.
$$

*Proof.* Apply the left-handed theorem to the adjoint equation $A^{\mathsf H}\ast X^{\mathsf H}=B^{\mathsf H}$ and take the conjugate transpose. The general solution becomes $X=B\ast A^\dagger+W\ast R_A$ with $W$ arbitrary, and the minimum-norm statement is preserved by the conjugate transpose.

## The Two Idempotent Coordinates

Write $A=A_{(1)}\Pi_++A_{(2)}\Pi_-$, $B=B_{(1)}\Pi_++B_{(2)}\Pi_-$ and $X=X_{(1)}\Pi_++X_{(2)}\Pi_-$. The equation $A\ast X=B$ is equivalent to the two complex tensor equations

$$
A_{(1)}\ast X_{(1)}=B_{(1)},\qquad A_{(2)}\ast X_{(2)}=B_{(2)}.
$$

The projectors, the solvability criterion, the general solution, the least-squares solutions and the minimum-norm solutions are the pairs of their complex counterparts. The Hermitian condition is also coordinatewise: $X^{\mathsf H}=X$ is equivalent to $X_{(1)}^{\mathsf H}=X_{(1)}$ and $X_{(2)}^{\mathsf H}=X_{(2)}$, and the compatibility condition $B\ast A^{\mathsf H}=A\ast B^{\mathsf H}$ is equivalent to the two complex conditions

$$
B_{(1)}\ast A_{(1)}^{\mathsf H}=A_{(1)}\ast B_{(1)}^{\mathsf H},\qquad
B_{(2)}\ast A_{(2)}^{\mathsf H}=A_{(2)}\ast B_{(2)}^{\mathsf H}.
$$

**The algorithm.** Transform both coordinates, solve the matrix equation slice by slice by the matrix pseudoinverse, and invert the transform. The cost is the cost of the pseudoinverse,

$$
O\bigl(n_1n_2n_3\log n_3+n_3\min(n_1^2n_2,n_1n_2^2)\bigr),
$$

plus the slicewise matrix multiplications. The two coordinates are independent and can be solved in parallel.

## Verification

The statements were recomputed on random tensors of sizes $3\times2\times4$ and $3\times3\times4$, with at most $36$ entries. For a consistent system, the norms $\|R_A\ast B\|_{\mathrm F}$ and $\|A\ast X_0-B\|_{\mathrm F}$ were at most $1.6\times10^{-14}$, and the general solution reproduced $B$ to $2.4\times10^{-14}$. For an inconsistent system, the normal equation held to $1.5\times10^{-13}$, and the identity $\|X\|_{\mathrm F}^2=\|A^\dagger\ast B\|_{\mathrm F}^2+\|L_A\ast W\|_{\mathrm F}^2$ held to $1.8\times10^{-29}$. For the Hermitian problem, the residual was $3.1\times10^{-14}$, the symmetry $X^{\mathsf H}-X$ was $4.8\times10^{-15}$, and the completeness with $U=X_0$ held to $3.8\times10^{-15}$; a tensor in the range of $A$ whose product $B\ast A^{\mathsf H}$ was not Hermitian failed the condition by $84.07$. For the right-handed equation, the normal equation held to $1.7\times10^{-13}$, the minimum-norm identity to $2.7\times10^{-15}$, and the consistent solution to $1.9\times10^{-14}$.

## Summary

The equation $A\ast X=B$ is solvable if and only if $R_A\ast B=0$, where $R_A=\mathrm I-A\ast A^\dagger$; its general solution is $X=A^\dagger\ast B+L_A\ast Y$, with $L_A=\mathrm I-A^\dagger\ast A$. The least-squares solutions are the same expression with $W$ in place of $Y$, and the minimum-norm least-squares solution is $A^\dagger\ast B$. For square $A$ and $B$, a Hermitian solution exists if and only if $R_A\ast B=0$ and $B\ast A^{\mathsf H}=A\ast B^{\mathsf H}$; its general form is $A^\dagger\ast B+(A^\dagger\ast B)^{\mathsf H}-A^\dagger\ast B\ast A^{\mathsf H}\ast(A^\dagger)^{\mathsf H}+L_A\ast U\ast L_A$ with $U$ Hermitian. The right-handed equation has the mirror solution $X=B\ast A^\dagger+W\ast R_A$. Every statement is the pair of its two complex idempotent-coordinate statements. **The pseudoinverse is the canonical solution: exact when the equation is solvable, and of minimum norm among the least-squares solutions otherwise.**

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A\ast X=B$ | The tensor equation |
| $A^\dagger$ | The Moore-Penrose inverse of $A$ |
| $L_A=\mathrm I-A^\dagger\ast A$ | The projector onto the kernel of $A$ |
| $R_A=\mathrm I-A\ast A^\dagger$ | The projector onto the cokernel of $A$ |
| $A_{(1)},A_{(2)}$ | The two idempotent coordinates |
| $X\ast A=B$ | The right-handed equation |

## Further Reading

- Cui-E Yu, Xin Liu, Hui Luo and Yang Zhang, "Reduced biquaternion tensors and applications in color video processing", arXiv:2403.01690 (2024), Section 5. The solvability, least-squares and Hermitian solutions of $A\ast_{Ht}X=B$.
- Adi Ben-Israel and Thomas N. E. Greville, *Generalized Inverses: Theory and Applications* (Wiley, 1974; Springer, 2003). The matrix solvability criterion and the least-squares theory that the tensor statements extend.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013). The Hermitian solutions of linear matrix equations and the projector identities.
- Misha E. Kilmer and Carla D. Martin, "Factorization strategies for third-order tensors", *Linear Algebra and its Applications* **435** (2011) 641–658. The t-product and the t-SVD used in the proofs.
