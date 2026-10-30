# __The Numerical Range of the Two-Sided Operators of $M_4(\mathbb{C})$__

## Introduction

For $a,b\in M_4(\mathbb{C})$ the **two-sided operator** is the sandwich

$$
T_{a,b}:M_4(\mathbb{C})\longrightarrow M_4(\mathbb{C}),\qquad T_{a,b}(X)=aXb .
$$

It is the product $L_aR_b$ of a left and a right multiplication, and it acts on the sixteen-dimensional complex vector space $M_4(\mathbb{C})$. The algebra is a Hilbert space for the **Hilbert–Schmidt form**

$$
\langle X,Y\rangle=\operatorname{tr}(X^*Y),
$$

and the **field of values**, or **numerical range**, of the operator is

$$
W(T_{a,b})=\bigl\{\langle X,T_{a,b}(X)\rangle:\ \langle X,X\rangle=1\bigr\}
=\bigl\{\operatorname{tr}(X^*aXb):\ \operatorname{tr}(X^*X)=1\bigr\}.
$$

This article computes it and compares it with the fields of values of the two factors.

The result is not the product of $W(a)$ and $W(b)$. The product set is only a lower bound: its convex hull always lies in $W(T_{a,b})$, and the inclusion is strict already for the smallest nilpotent. The inclusion closes when one factor is normal, and then $W(T_{a,b})=\operatorname{conv}(W(a)W(b))$. The defect is the correlation of the two factors inside a general Hilbert–Schmidt vector, which is a single matrix and not a pair of vectors.

The general theory — compactness, convexity, the support function and the Hermitian and normal cases — is *Hermitian Operators and the Numerical Range*. The four-dimensional case, the elliptical range theorem and the disk of the nilpotent chain are *The Numerical Range and the Field of Values of $M_4(\mathbb{C})$*. The operators $L_a$, $R_a$ and $T_{a,b}$, their $16\times16$ matrices and their spectrum are *The Operators of the Peirce Decomposition of $M_4(\mathbb{C})$*. The same construction on the carrier $\mathbb{B}$ is *$M_4(\mathbb{C})$ Representation : The Two-Sided Operators on the Biquaternion Algebra*, whose $4\times4$ matrices $T_{\mu\nu}$ are a different object. The Kronecker product is *The Kronecker Factorisation $M_4(\mathbb{C})\cong M_2(\mathbb{C})\otimes M_2(\mathbb{C})$*; the difference $L_a-R_b$ is *The Sylvester Operator and the Kronecker Sum of $M_4(\mathbb{C})$*; the Hilbert–Schmidt form is *The Involution and the Hermitian Structure of $M_4(\mathbb{C})$*.

## The Setting

**Definition.** For $a,b\in M_4(\mathbb{C})$ the two-sided operator is $T_{a,b}(X)=aXb$. It is $\mathbb{C}$-linear, and it is the sandwich of *The Operators of the Peirce Decomposition of $M_4(\mathbb{C})$*, where the operator families are introduced.

**Proposition (the laws of composition).** For all $a,b,c,d$,

$$
T_{a,b}T_{c,d}=T_{ac,db},\qquad T_{a,b}^{*}=T_{a^{*},b^{*}} .
$$

The operator $T_{a,b}$ is invertible exactly when $a$ and $b$ are, and then $T_{a,b}^{-1}=T_{a^{-1},b^{-1}}$.

**Proof.** The composition is $X\mapsto a(cXd)b=(ac)X(db)$. For the adjoint, $\langle Y,aXb\rangle=\operatorname{tr}(Y^*aXb)=\operatorname{tr}\bigl((a^*Yb^*)^*X\bigr)=\langle a^*Yb^*,X\rangle$. The inverse is the product law with $T_{a,b}T_{a^{-1},b^{-1}}=T_{I,I}$.

**The matrix.** In the row-stacking basis,

$$
L_a=a\otimes I_4,\qquad R_b=I_4\otimes b^{\mathsf T},\qquad T_{a,b}=a\otimes b^{\mathsf T},
$$

which are the displays of *The Operators of the Peirce Decomposition of $M_4(\mathbb{C})$*. In the column-stacking basis the same operator is $b^{\mathsf T}\otimes a$. The two orderings differ by the flip $X\otimes Y\mapsto Y\otimes X$, a unitary permutation of $\mathbb{C}^{16}$, so the field of values and every invariant below are the same in the two conventions. This article writes the row-stacking form.

**Proposition (the invariants).**

$$
\operatorname{spec}T_{a,b}=\bigl\{\lambda_i(a)\lambda_j(b)\bigr\}_{i,j=1}^{4},
\qquad
\operatorname{tr}T_{a,b}=\operatorname{tr}a\,\operatorname{tr}b,
\qquad
\det T_{a,b}=(\det a\,\det b)^{4},
$$

$$
\operatorname{rank}T_{a,b}=\operatorname{rank}a\,\operatorname{rank}b,
\qquad
\bigl\{s_k(T_{a,b})\bigr\}_{k=1}^{16}=\bigl\{s_i(a)s_j(b)\bigr\}_{i,j=1}^{4},
$$

and for every Schatten index $p\in[1,\infty]$,

$$
\|T_{a,b}\|_p=\|a\|_p\,\|b\|_p .
$$

**Proof.** A Kronecker product $A\otimes B$ has spectrum $\{\alpha_i\beta_j\}$, trace $\operatorname{tr}A\operatorname{tr}B$, determinant $(\det A)^{n}(\det B)^{m}$ for $A\in M_m$, $B\in M_n$, rank $\operatorname{rank}A\operatorname{rank}B$, and singular values $s_i(A)s_j(B)$. Here $A=a$ and $B=b^{\mathsf T}$, of size four, and $\operatorname{tr}b^{\mathsf T}=\operatorname{tr}b$, $\det b^{\mathsf T}=\det b$, $s_j(b^{\mathsf T})=s_j(b)$. The Schatten norm is the $\ell^{p}$ norm of the singular values, and a pairwise product of two lists has $\ell^{p}$ norm the product of the two $\ell^{p}$ norms.

**Corollary.** $\|T_{a,b}\|=\|a\|\,\|b\|$ and $\|T_{a,b}\|_{\mathrm{HS}}=\|a\|_{\mathrm{HS}}\|b\|_{\mathrm{HS}}$.

**Remark (the notation).** The letters $T_{a,b}$ also denote the $4\times4$ matrices $T_{\mu\nu}=L_\mu R_\nu$ of *The Two-Sided Operators Method to Build $M_4(\mathbb{C})$* and *$M_4(\mathbb{C})$ Representation : The Two-Sided Operators on the Biquaternion Algebra*, acting on the carrier $\mathbb{B}\cong\mathbb{C}^4$. The two are the same sandwich construction applied to the algebra $M_4(\mathbb{C})$ and to the algebra $\mathbb{B}$; the present article always means the operator on the sixteen-dimensional algebra. The same convention is used in *The Operators of the Peirce Decomposition of $M_4(\mathbb{C})$*.

**The field of values.** By the general theory, $W(T_{a,b})$ is compact, connected and convex, it contains the spectrum, and its support function is

$$
h(\alpha)=\max_{z\in W(T_{a,b})}\operatorname{Re}\bigl(e^{-i\alpha}z\bigr)
=\lambda_{\max}\bigl(\operatorname{Re}(e^{-i\alpha}T_{a,b})\bigr),
\qquad
\operatorname{Re}M=\tfrac12(M+M^{*}),
$$

where the adjoint in $\operatorname{Re}M$ is the Hilbert–Schmidt adjoint.

## The Product Bound

**Theorem (the product bound).** For all $a,b$,

$$
\operatorname{conv}\bigl(W(a)W(b)\bigr)\subseteq W(T_{a,b}),
\qquad
W(a)W(b)=\{xy:\ x\in W(a),\ y\in W(b)\}.
$$

**Proof.** Let $x=u^{*}au\in W(a)$ and $y=v^{*}bv\in W(b)$ with $\|u\|=\|v\|=1$, and put $X=uv^{*}$. Then $\|X\|_{\mathrm{HS}}=\|u\|\,\|v\|=1$ and

$$
\langle X,T_{a,b}(X)\rangle
=\operatorname{tr}(vu^{*}auv^{*}b)
=(u^{*}au)\operatorname{tr}(vv^{*}b)
=(u^{*}au)(v^{*}bv)=xy .
$$

Hence $W(a)W(b)\subseteq W(T_{a,b})$, and the convexity of the field of values gives the convex hull.

**Corollary.** $w(a)w(b)\le w(T_{a,b})$, where $w$ is the numerical radius.

**Theorem (the normal factor).** If $a$ is normal, then for every $b$

$$
W(T_{a,b})=\operatorname{conv}\bigl(W(a)W(b)\bigr).
$$

**Proof.** Write $a=U\Lambda U^{*}$ with $\Lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_4)$ and $U$ unitary. The matrix $a\otimes b^{\mathsf T}$ is unitarily similar to $\Lambda\otimes b^{\mathsf T}$, and

$$
\Lambda\otimes b^{\mathsf T}=\bigoplus_{i=1}^{4}\lambda_i b^{\mathsf T},
$$

a block-diagonal matrix. The field of values of a direct sum is the convex hull of the fields of values of the summands, by the block rule of *The Numerical Range and the Field of Values of $M_4(\mathbb{C})$*; hence

$$
W(T_{a,b})=\operatorname{conv}\left(\bigcup_{i=1}^{4}\lambda_i W(b^{\mathsf T})\right)
=\operatorname{conv}\left(\bigcup_{i=1}^{4}\lambda_i W(b)\right)
=\operatorname{conv}\bigl(W(a)W(b)\bigr),
$$

because $W(b^{\mathsf T})=W(b)$ and $W(a)=\operatorname{conv}\{\lambda_1,\dots,\lambda_4\}$.

**Corollary.** If $a$ or $b$ is normal, then $W(T_{a,b})=\operatorname{conv}(W(a)W(b))$.

**Proof.** The case of $a$ normal is the theorem; the case of $b$ normal follows from the symmetry below.

**Proposition (symmetry in the two factors).** $W(T_{a,b})=W(T_{b,a})$.

**Proof.** By the model, $T_{a,b}\cong a\otimes b^{\mathsf T}$ and $T_{b,a}\cong b\otimes a^{\mathsf T}$. The flip $X\otimes Y\mapsto Y\otimes X$ is a unitary similarity, so $W(b\otimes a^{\mathsf T})=W(a^{\mathsf T}\otimes b)$; transposition preserves the field of values and $a^{\mathsf T}\otimes b=(a\otimes b^{\mathsf T})^{\mathsf T}$; hence the two fields of values agree.

## The Failure of the Product Rule

**Proposition (the smallest nilpotent).** Let $E_{12}$ be the matrix unit. For $a=b=E_{12}$,

$$
W(T_{a,b})=\overline{D}\bigl(0,\tfrac12\bigr),
\qquad
\operatorname{conv}\bigl(W(a)W(b)\bigr)=\overline{D}\bigl(0,\tfrac14\bigr),
$$

where $\overline{D}(c,r)$ is the closed disk of centre $c$ and radius $r$.

**Proof.** The operator is $T(X)=E_{12}XE_{12}=x_{21}E_{12}$, so

$$
\langle X,T(X)\rangle=x_{21}\,\overline{x_{12}} .
$$

For $\operatorname{tr}(X^{*}X)=\sum_{i,j}|x_{ij}|^{2}=1$ the Cauchy–Schwarz inequality gives $|x_{21}\overline{x_{12}}|\le\tfrac12\bigl(|x_{21}|^{2}+|x_{12}|^{2}\bigr)\le\tfrac12$, and the value $\tfrac12$ is attained at $|x_{12}|=|x_{21}|=1/\sqrt2$ with the other entries zero. The phase is free, because $x_{21}\overline{x_{12}}$ has the argument $\arg x_{21}-\arg x_{12}$; varying the phases of the two entries with $|x_{12}|=|x_{21}|=1/\sqrt2$ gives every point of the closed disk of radius $\tfrac12$. Hence $W(T_{a,b})$ is that disk.

For the factors, $W(E_{12})$ is the disk of radius $\tfrac12$: the block $E_{12}$ is $J_2(0)\oplus0_2$, and the elliptical range theorem with the block rule, or the nilpotent chain of *The Numerical Range and the Field of Values of $M_4(\mathbb{C})$*, gives the disk. The product set is therefore $\{xy:|x|\le\tfrac12,\ |y|\le\tfrac12\}$, the closed disk of radius $\tfrac14$.

**Remark (the origin of the gap).** The product bound is computed on the rank-one matrices $X=uv^{*}$, where the Hilbert–Schmidt unit sphere meets the rank-one variety. A general unit vector $X$ is not of that form, and its value $\operatorname{tr}(X^{*}aXb)$ mixes the two factors. In the example the gap is a factor two in the radius, and it is produced by a matrix $X$ of rank two: the two nonzero entries $x_{12}$ and $x_{21}$ belong to one matrix, not to one vector of each factor.

## The Rank-One Case

**Theorem (the ellipse of a rank-one sandwich).** Let $a=uv^{*}$ and $b=xy^{*}$ with $u,v,x,y\ne0$. Then $T_{a,b}$ has rank one, $T_{a,b}(X)=\langle vx^{*},X\rangle\,uy^{*}$, and $W(T_{a,b})$ is the closed ellipse with foci $0$ and $\operatorname{tr}a\,\operatorname{tr}b$ and semi-minor axis

$$
\frac12\sqrt{\|a\|_{\mathrm{HS}}^{2}\|b\|_{\mathrm{HS}}^{2}
-\bigl|\operatorname{tr}a\,\operatorname{tr}b\bigr|^{2}} .
$$

**Proof.** $aXb=u(v^{*}Xx)y^{*}$, so $T_{a,b}(X)=\langle V,X\rangle\,U$ with $U=uy^{*}$ and $V=vx^{*}$ in the Hilbert–Schmidt form. The operator is rank one with

$$
\operatorname{tr}T_{a,b}=\langle V,U\rangle
=(v^{*}u)(y^{*}x)=\operatorname{tr}a\,\operatorname{tr}b,
\qquad
\|T_{a,b}\|_{\mathrm{HS}}=\|u\|\,\|y\|\,\|v\|\,\|x\|=\|a\|_{\mathrm{HS}}\|b\|_{\mathrm{HS}} .
$$

The compression to the two-dimensional span of $U$ and $V$ — the rank-one case of *The Numerical Range and the Field of Values of $M_4(\mathbb{C})$* — gives the ellipse with foci the two eigenvalues, $0$ and $\operatorname{tr}T_{a,b}$, and twice the semi-minor axis $\sqrt{\|T\|_{\mathrm{HS}}^{2}-|\operatorname{tr}T|^{2}}$.

**Corollary (the matrix units).** For $a=E_{ij}$ and $b=E_{kl}$:

- if $i\ne j$ or $k\ne l$, then $W(T_{a,b})$ is the closed disk of radius $\tfrac12$ centred at $0$;
- if $i=j$ and $k=l$, then $T_{a,b}$ is an orthogonal projection of rank one and $W(T_{a,b})=[0,1]$.

**Proof.** The trace is $\delta_{ij}\delta_{kl}$ and the Hilbert–Schmidt norm is $1$. In the first case the foci coincide at $0$ and the ellipse is the disk of radius $\tfrac12$. In the second case $T_{a,b}(X)=X_{ik}E_{ik}$ is the orthogonal projection onto the line $\mathbb{C}E_{ik}$, and the field of values of a rank-one projection is $[0,1]$.

**Corollary (the trace-zero disk).** If $T_{a,b}$ has rank one and trace zero, then $W(T_{a,b})$ is the closed disk of radius $\tfrac12\|T_{a,b}\|_{\mathrm{HS}}$.

**Proof.** The ellipse of the theorem has coincident foci at the origin and semi-minor axis $\tfrac12\|T\|_{\mathrm{HS}}$.

## The Hermitian, the Projection and the Unitary Cases

**Proposition (Hermitian factors).** If $a$ and $b$ are Hermitian, then $T_{a,b}$ is self-adjoint for the Hilbert–Schmidt form and

$$
W(T_{a,b})=\Bigl[\min_{i,j}\alpha_i\beta_j,\ \max_{i,j}\alpha_i\beta_j\Bigr],
$$

where $\alpha_i=\lambda_i(a)$ and $\beta_j=\lambda_j(b)$. In particular the product rule is exact.

**Proof.** $T_{a,b}^{*}=T_{a^{*},b^{*}}=T_{a,b}$. Its eigenvalues are the products $\alpha_i\beta_j$, real; the field of values of a Hermitian matrix is the interval between its extreme eigenvalues.

**Proposition (a projection factor).** If $b$ is a projection of rank $r$, then $W(T_{a,b})=W(a)$. If $a$ is a projection of rank $r$, then $W(T_{a,b})=W(b)$.

**Proof.** Let $b=P$ be a projection of rank $r$. A unitary $V$ puts $VP^{\mathsf T}V^{*}=\operatorname{diag}(I_r,0)$, so $T_{a,b}$ is unitarily similar to $a\otimes\operatorname{diag}(I_r,0)\cong a^{\oplus r}$. The field of values of a direct sum is the convex hull of the fields of values of the summands, and the convex hull of $r$ copies of $W(a)$ is $W(a)$. The case of a projection $a$ follows by symmetry.

**Proposition (unitary factors).** If $a$ and $b$ are unitary, then $T_{a,b}$ is unitary. Its spectrum lies on the unit circle, $W(T_{a,b})$ lies in the closed unit disk, and

$$
W(T_{a,b})=\operatorname{conv}\bigl\{\lambda_i(a)\lambda_j(b)\bigr\}.
$$

**Proof.** $T_{a,b}^{*}T_{a,b}=T_{a^{*}a,bb^{*}}=T_{I,I}$. The spectrum is the set of products of eigenvalues of modulus one, and a unitary matrix has its spectrum in its field of values, which lies in the disk of radius its norm, one. The formula is the corollary of the normal-factor theorem, since unitary matrices are normal.

## The Numerical Radius

**Theorem (the two-sided radius).** For all $a,b$,

$$
w(a)w(b)\ \le\ w(T_{a,b})\ \le\ \|a\|\,\|b\|\ \le\ 4\,w(a)w(b).
$$

**Proof.** The first inequality is the product bound, because $|xy|$ attains $w(a)w(b)$ on $W(a)W(b)$. The second is $w(T)\le\|T\|=\|a\|\|b\|$, with the norm equality of the corollary above. The third is the general inequality $\|M\|\le 2w(M)$, applied to $a$ and to $b$.

**Remark (the constant four).** The constant is the square of the general norm–radius constant and is not sharp for the two-sided operators. For the matrix unit of the failure example, $w(T)=\tfrac12$ and $w(a)w(b)=\tfrac14$, so the ratio is two. The product bound is attained whenever one factor is normal, by the normal-factor theorem.

## The Two-Sided Matrix Unit and the Three Radii

**Lemma (nilpotent partial isometries).** Let $V\ne0$ be a partial isometry with $V^{2}=0$. Then $W(V)$ is the closed disk of radius $\tfrac12$.

**Proof.** Decompose $x=x_1+x_0$ with $x_1\in\operatorname{ran}V^{*}$ and $x_0\in\ker V$. Then $Vx=Vx_1$, and $Vx_1\in\operatorname{ran}V\subseteq\ker V$ because $V^{2}=0$; also $x_1\perp\operatorname{ran}V$, so $x_1\perp Vx_1$. Hence

$$
\langle x,Vx\rangle=\langle x_0,Vx_1\rangle,
\qquad
|\langle x,Vx\rangle|\le\|x_0\|\,\|Vx_1\|
\le\tfrac12\bigl(\|x_0\|^{2}+\|Vx_1\|^{2}\bigr)=\tfrac12\|x\|^{2},
$$

because $V$ is isometric on $\operatorname{ran}V^{*}$. For the converse, take a unit $x_1\in\operatorname{ran}V^{*}$ and $x=(x_1+e^{i\varphi}Vx_1)/\sqrt2$; then $\|x\|=1$ and $\langle x,Vx\rangle=\tfrac12 e^{-i\varphi}$. Hence the field of values is the closed disk.

**Proposition (the rank blindness).** $W(T_{E_{12},E_{12}})$ and $W(T_{E_{12}+E_{34},E_{12}+E_{34}})$ are both the closed disk of radius $\tfrac12$, while the ranks of the two operators are $1$ and $4$.

**Proof.** Each factor is a partial isometry with square zero: $E_{12}$ and $E_{12}+E_{34}$ satisfy $AA^{*}A=A$ and $A^{2}=0$. For partial isometries $a,b$, the operator $T_{a,b}$ is a partial isometry, because $T_{a,b}^{*}T_{a,b}=T_{a^{*}a,bb^{*}}$ and $T_{P,Q}(X)=PXQ$ is idempotent and self-adjoint when $P,Q$ are projections. With $a^{2}=b^{2}=0$ one has $T_{a,b}^{2}=T_{a^{2},b^{2}}=0$. The lemma gives the disk, and the rank is $\operatorname{rank}a\operatorname{rank}b$.

**The three radii.** The operator $T_{E_{12},E_{12}}$ reproduces the invariants of the nilpotent block $J_2$:

| quantity | $T_{E_{12},E_{12}}$ | $J_2$ | $J_4$ | $T_{J_4,I}$ |
|---|---|---|---|---|
| rank | $1$ | $1$ | $3$ | $12$ |
| spectrum | $\{0\}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ |
| spectral radius | $0$ | $0$ | $0$ | $0$ |
| numerical radius | $\tfrac12$ | $\tfrac12$ | $\cos(\pi/5)$ | $\cos(\pi/5)$ |
| operator norm | $1$ | $1$ | $1$ | $1$ |
| field of values | disk $\tfrac12$ | disk $\tfrac12$ | disk $\cos(\pi/5)$ | disk $\cos(\pi/5)$ |

The last column is the left multiplication $L_{J_4}=T_{J_4,I}$, whose field of values is $W(J_4)$ by the projection factor rule, or by the block form $J_4\otimes I_4$. The sandwich carries the nilpotent chain into the operator algebra without changing its three radii.

## The Place in the Category

**The one-sided limits.** $T_{a,I}=L_a$ and $T_{I,b}=R_b$, so

$$
W(L_a)=W(a),\qquad W(R_b)=W(b)
$$

by the projection rule with the identity, or directly from the block forms $a\otimes I_4$ and $I_4\otimes b^{\mathsf T}$. The two-sided operator is therefore a two-parameter interpolation between the two one-sided operators, and its field of values is controlled by the two but not determined by their product.

**The bounds as a summary.** The spectrum, the product set and the numerical radius are ordered by

$$
\{\lambda_i(a)\lambda_j(b)\}\subseteq W(T_{a,b}),
\qquad
\operatorname{conv}\bigl(W(a)W(b)\bigr)\subseteq W(T_{a,b})\subseteq\overline{D}\bigl(0,\|a\|\,\|b\|\bigr),
$$

and

$$
w(a)w(b)\le w(T_{a,b})\le\|a\|\,\|b\|\le4w(a)w(b).
$$

The first inclusion is the spectrum theorem, the second the product bound, the third the norm bound.

**What the field of values does not see.** It does not determine the rank, by the two matrix-unit sandwiches above, and it does not determine either factor: $T_{a,b}=T_{ua,vb}$ for scalars with $uv=1$. It is also tied to the Hilbert–Schmidt form: the field of values is computed with the adjoint of the chosen involution, while the spectrum, the trace, the determinant and the rank do not depend on that choice. The spectrum, the determinant and the rank are invariants of the operator alone; the field of values is an invariant of the operator together with the Hilbert-space structure of the algebra.

**The computation.** The support function is the largest eigenvalue of the $16\times16$ Hermitian matrix $\operatorname{Re}(e^{-i\alpha}a\otimes b^{\mathsf T})$, so the field of values is read from the single matrix $a\otimes b^{\mathsf T}$; no search over the unit sphere of $M_4(\mathbb{C})$ is needed.

## Summary

The two-sided operator $T_{a,b}(X)=aXb$ acts on the sixteen-dimensional Hilbert space $M_4(\mathbb{C})$ with the Hilbert–Schmidt form. Its matrix is $a\otimes b^{\mathsf T}$; its spectrum is the set of products $\lambda_i(a)\lambda_j(b)$; its trace is $\operatorname{tr}a\operatorname{tr}b$, its determinant $(\det a\,\det b)^{4}$, its rank $\operatorname{rank}a\operatorname{rank}b$, its singular values are the products $s_i(a)s_j(b)$, and every Schatten norm is multiplicative, $\|T_{a,b}\|_p=\|a\|_p\|b\|_p$.

The field of values contains the convex hull of the product set $W(a)W(b)$, and the inclusion is strict in general: for $a=b=E_{12}$ the field of values is the disk of radius $\tfrac12$ while the product hull is the disk of radius $\tfrac14$. The inclusion is an equality when one factor is normal, and then $W(T_{a,b})=\operatorname{conv}(W(a)W(b))$. For Hermitian factors the field of values is the interval between the extreme products; for a projection factor it collapses to the field of values of the other factor; for unitary factors the operator is unitary. The numerical radius is squeezed between $w(a)w(b)$ and $\|a\|\|b\|$, and the latter is at most four times the former. The matrix-unit sandwich is a nilpotent partial isometry with the three radii of $J_2$: spectral radius zero, numerical radius $\tfrac12$, norm one.

| Quantity | Value for $M_4(\mathbb{C})$ |
|---|---|
| $T_{a,b}$ | $X\mapsto aXb$ on $M_4(\mathbb{C})$, Hilbert–Schmidt form |
| matrix | $a\otimes b^{\mathsf T}$ |
| spectrum | $\lambda_i(a)\lambda_j(b)$ |
| trace | $\operatorname{tr}a\,\operatorname{tr}b$ |
| determinant | $(\det a\,\det b)^{4}$ |
| rank | $\operatorname{rank}a\,\operatorname{rank}b$ |
| singular values | $s_i(a)s_j(b)$ |
| Schatten norms | $\|a\|_p\|b\|_p$ |
| lower bound | $\operatorname{conv}(W(a)W(b))\subseteq W(T_{a,b})$ |
| normal factor | equality |
| Hermitian factors | $[\min\alpha_i\beta_j,\max\alpha_i\beta_j]$ |
| projection factor | $W(T_{a,b})=W(a)$ |
| rank-one factors | ellipse with foci $0$ and $\operatorname{tr}a\operatorname{tr}b$ |
| radius bounds | $w(a)w(b)\le w(T_{a,b})\le\|a\|\|b\|\le4w(a)w(b)$ |
| $W(T_{E_{12},E_{12}})$ | disk of radius $\tfrac12$ |
| $W(T_{J_4,I})$ | disk of radius $\cos(\pi/5)$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T_{a,b}$ | the two-sided operator $X\mapsto aXb$ on $M_4(\mathbb{C})$ |
| $L_a,R_b$ | left and right multiplication, $T_{a,I}$ and $T_{I,b}$ |
| $\langle X,Y\rangle$ | the Hilbert–Schmidt form $\operatorname{tr}(X^{*}Y)$ |
| $W(A)$ | the field of values: $\{x^{*}Ax:\|x\|=1\}$ for a matrix, $\{\langle X,AX\rangle:\|X\|=1\}$ for an operator on $M_4(\mathbb{C})$ |
| $w(A)$ | the numerical radius $\max_{z\in W(A)}|z|$ |
| $h(\alpha)$ | the support function $\max_{z\in W}\operatorname{Re}(e^{-i\alpha}z)$ |
| $\operatorname{Re}M$ | the Hermitian part $\tfrac12(M+M^{*})$ |
| $\operatorname{conv}$ | the convex hull |
| $E_{ij}$ | the matrix unit |
| $J_n$ | the nilpotent Jordan block of size $n$ |
| $s_i(A)$ | the singular values |
| $\|A\|_p$ | the Schatten $p$-norm |

## Further Reading

- [Hermitian Operators and the Numerical Range](hermitian-operators-and-the-numerical-range.html), for the general theory, the support function and the Toeplitz–Hausdorff theorem.
- [The Numerical Range and the Field of Values of $M_4(\mathbb{C})$](the-numerical-range-and-the-field-of-values-of-m4c.html), for the elliptical range theorem, the block rule, the rank-one case and the nilpotent chain.
- [The Operators of the Peirce Decomposition of $M_4(\mathbb{C})$](the-operators-of-the-peirce-decomposition-of-m4c.html), for $L_a$, $R_a$, $T_{a,b}$, their matrices and their spectrum.
- [The Kronecker Factorisation $M_4(\mathbb{C})\cong M_2(\mathbb{C})\otimes M_2(\mathbb{C})$](the-kronecker-factorisation-of-m4c.html), for the Kronecker product and the identity $W(I\otimes M)=W(M)$.
- [The Two-Sided Operators Method to Build $M_4(\mathbb{C})$](the-two-sided-operators-method-to-build-m4c.html), for the construction of the algebra from the $4\times4$ matrices $T_{\mu\nu}$.
- [$M_4(\mathbb{C})$ Representation : The Two-Sided Operators on the Biquaternion Algebra](m4c-representation-the-two-sided-operators-on-the-biquaternion-algebra.html), for the same sandwich on the carrier $\mathbb{B}$.
- [The Forms, the Norms and the Singular Set of $M_4(\mathbb{C})$](the-forms-the-norms-and-the-singular-set-of-m4c.html), for the Schatten norms and the singular values.
- [The Involution and the Hermitian Structure of $M_4(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m4c.html), for the Hilbert–Schmidt form and the adjoint.
- [The Sylvester Operator and the Kronecker Sum of $M_4(\mathbb{C})$](the-sylvester-operator-and-the-kronecker-sum-of-m4c.html), for the difference $L_a-R_b$ and the equations $aX\pm Xb=C$.
- Roger A. Horn and Charles R. Johnson, *Topics in Matrix Analysis* (Cambridge University Press, 1991), for the field of values, the Kronecker product and the elliptical range theorem.
- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the numerical radius and the norm–radius inequalities.
- Karl E. Gustafson and Duggirala K. M. Rao, *Numerical Range: The Field of Values of Linear Operators and Matrices* (Springer, 1997), for the general theory.
