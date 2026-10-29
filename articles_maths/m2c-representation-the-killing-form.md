# __$M_2(\mathbb{C})$ Representation : The Killing Form__

## Introduction

The unit group of the biquaternion algebra is a real Lie group of real dimension eight, and the Killing form of its Lie algebra is the invariant bilinear form that measures the algebra's failure to be semisimple. In the matrix model the Lie algebra is $M_2(\mathbb{C})$ with the commutator, and the Killing form is a real bilinear form whose radical is the centre and whose restriction to the trace-free part has signature $(3,3)$.

This article develops the adjoint operator, the formula, the radical, the signature on the trace-free part, the invariance and the relation to the trace form. It is the matrix form of *Biquaternion Lie Group and Exponential Structure*, §*The Killing Form*.

**Conventions.** The algebra and the model are those of *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant*. The Lie algebra is $M_2(\mathbb{C})$ read as a real vector space, with bracket $[X,Y]=XY-YX$; the trace is the complex trace, the real part is written $\operatorname{Re}$, and $X=\mathsf M_2(\tilde X)$.

**Boundaries.** The Killing form of the algebra, its radical and its signature are *Biquaternion Lie Group and Exponential Structure*, §*The Killing Form*; the plain, quaternionic, Hermitian and Krein forms are *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the trace pairing is *$M_2(\mathbb{C})$ Representation : The Four Words and the Four Traces*.

## The Adjoint Operator

For $X\in M_2(\mathbb{C})$ the **adjoint operator** is

$$
\operatorname{ad}_X:M_2(\mathbb{C})\longrightarrow M_2(\mathbb{C}),\qquad
\operatorname{ad}_X(Y)=[X,Y]=XY-YX .
$$

It is complex linear, hence real linear on the eight real dimensions, and it is a derivation of the algebra: $\operatorname{ad}_X(YZ)=(\operatorname{ad}_XY)Z+Y(\operatorname{ad}_XZ)$.

On the matrix units,

$$
\operatorname{ad}_X(E_{ij})=(x_i-x_j)E_{ij}
$$

when $X$ is diagonal with eigenvalues $x_1,x_2$. The adjoint operator is therefore diagonal in the matrix-unit basis for diagonal $X$, with the four eigenvalues $0,x_1-x_2,x_2-x_1,0$.

**The bracket is a commutator.** The Jacobi identity is the associativity of the matrix product, and the Lie algebra is $\mathfrak{gl}_2(\mathbb{C})$ read over $\mathbb{R}$, of real dimension eight.

## The Formula

The **Killing form** is

$$
\kappa(X,Y)=\operatorname{tr}\bigl(\operatorname{ad}_X\operatorname{ad}_Y\bigr),
$$

the trace being the real trace on the eight-dimensional space.

**Theorem.** For all $X,Y\in M_2(\mathbb{C})$,

$$
\boxed{\;
\kappa(X,Y)=8\operatorname{Re}\operatorname{tr}(XY)-4\operatorname{Re}\bigl(\operatorname{tr}X\,\operatorname{tr}Y\bigr)
\;}
$$

*Proof.* The centre lies in the radical, because $\operatorname{ad}_{\mathrm I_2}=0$. On $\mathfrak{sl}_2(\mathbb{C})$ use the basis

$$
H=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad F=\begin{pmatrix}0&0\\1&0\end{pmatrix},
$$

with brackets $[H,E]=2E$, $[H,F]=-2F$ and $[E,F]=H$. In this basis the adjoint operators are

$$
\operatorname{ad}_H=\operatorname{diag}(0,2,-2),\qquad
\operatorname{ad}_E=\begin{pmatrix}0&0&1\\-2&0&0\\0&0&0\end{pmatrix},\qquad
\operatorname{ad}_F=\begin{pmatrix}0&-1&0\\0&0&0\\2&0&0\end{pmatrix}.
$$

Hence

$$
\operatorname{ad}_H^2=\operatorname{diag}(0,4,4),\qquad
\operatorname{ad}_E\operatorname{ad}_F=\operatorname{diag}(2,2,0),
$$

and the products $\operatorname{ad}_H\operatorname{ad}_E$, $\operatorname{ad}_H\operatorname{ad}_F$, $\operatorname{ad}_E^2$ and $\operatorname{ad}_F^2$ have zero complex trace. With the complex trace, therefore,

$$
\kappa_{\mathbb{C}}(H,H)=8,\qquad \kappa_{\mathbb{C}}(E,F)=4,\qquad
\kappa_{\mathbb{C}}(H,E)=\kappa_{\mathbb{C}}(H,F)=\kappa_{\mathbb{C}}(E,E)=\kappa_{\mathbb{C}}(F,F)=0 .
$$

The form $4\operatorname{tr}(XY)$ takes exactly the same values on the basis, since $\operatorname{tr}(H^2)=2$, $\operatorname{tr}(EF)=\operatorname{tr}(FE)=1$ and the remaining products are traceless. Both forms are complex bilinear, so they agree on $\mathfrak{sl}_2(\mathbb{C})$:

$$
\kappa_{\mathbb{C}}(X,Y)=4\operatorname{tr}(XY).
$$

The real Killing form is twice the real part of the complex one, so

$$
\kappa(X,Y)=8\operatorname{Re}\operatorname{tr}(XY)
$$

on $\mathfrak{sl}_2(\mathbb{C})$. For general $X=a\mathrm I_2+U$ and $Y=b\mathrm I_2+V$ with $U,V$ traceless, the centre contributes nothing, so

$$
\kappa(X,Y)=\kappa(U,V)=8\operatorname{Re}\operatorname{tr}(UV)
=8\operatorname{Re}\bigl(\operatorname{tr}(XY)-\tfrac12\operatorname{tr}X\operatorname{tr}Y\bigr),
$$

which is the displayed formula. $\square$

**The complex form.** The same computation over $\mathbb{C}$ gives the complex bilinear form

$$
\kappa_{\mathbb{C}}(X,Y)=4\operatorname{tr}(XY)-2\operatorname{tr}X\operatorname{tr}Y,
$$

whose real part is twice the real Killing form, $\kappa=2\operatorname{Re}\kappa_{\mathbb{C}}$. The factor two is the realification of the complex trace.

**A direct check.** For $X=Y=\mathrm I_2$ both sides vanish. For $X=Y=\operatorname{diag}(1,0)$ the value is $4$; for $X=E_{12}$ and $Y=E_{21}$ the value is $8$; for $X=Y=\vec e_x$ in the algebra, that is $X=-i\sigma_1$, the value is $-16$.

## The Radical

**Theorem.** The radical of $\kappa$ is the centre,

$$
\operatorname{rad}\kappa=\mathbb{C}\mathrm I_2 .
$$

*Proof.* For $X=\mathrm I_2$ the formula gives $\kappa(\mathrm I_2,Y)=8\operatorname{Re}\operatorname{tr}Y-8\operatorname{Re}\operatorname{tr}Y=0$. Conversely write $X=a\mathrm I_2+U$ with $\operatorname{tr}U=0$. Then

$$
\kappa(X,Y)=8\operatorname{Re}\operatorname{tr}(UY),
$$

because the scalar parts cancel. If this vanishes for every $Y$, then $\operatorname{Re}\operatorname{tr}(UY)=0$ for every $Y$; taking $Y=U^{\dagger}$ gives $\operatorname{Re}\operatorname{tr}(UU^{\dagger})=\lVert U\rVert^2=0$, so $U=0$. $\square$

**The degeneration.** The Killing form is degenerate exactly along the centre, of real dimension two. This is the matrix form of the fact that $\mathfrak{gl}_2$ is reductive and not semisimple: the centre is an abelian ideal, and the Killing form vanishes on it.

## The Trace-Free Part and the Signature

On the trace-free part $\mathfrak{sl}_2(\mathbb{C})=\{X:\operatorname{tr}X=0\}$ the second term vanishes and

$$
\kappa(X,Y)=8\operatorname{Re}\operatorname{tr}(XY).
$$

This is nondegenerate, because $\operatorname{tr}(XY)$ is the nondegenerate trace pairing on $\mathfrak{sl}_2$ and the real part of a nondegenerate complex bilinear form is nondegenerate.

**The two real subspaces.** Every traceless matrix splits into a Hermitian and an anti-Hermitian part,

$$
X=\tfrac12(X+X^{\dagger})+\tfrac12(X-X^{\dagger}),
$$

and both parts are traceless. Write

$$
\mathfrak{u}=\{X:X^{\dagger}=-X,\ \operatorname{tr}X=0\},\qquad
\mathfrak{p}=\{X:X^{\dagger}=X,\ \operatorname{tr}X=0\},
$$

both of real dimension three, the Lie algebra of $SU(2)$ and its complementary subspace.

**Theorem.** The two subspaces are orthogonal for $\kappa$, and

$$
\kappa(X,X)=-8\operatorname{tr}(XX^{\dagger})<0\quad(X\in\mathfrak{u},\ X\neq0),
\qquad
\kappa(X,X)=8\operatorname{tr}(XX^{\dagger})>0\quad(X\in\mathfrak{p},\ X\neq0).
$$

Hence the signature of $\kappa$ on $\mathfrak{sl}_2(\mathbb{C})$ is $(3,3)$, negative on the compact real form and positive on its complement.

*Proof.* For $X\in\mathfrak{u}$ and $Y\in\mathfrak{p}$, the product $XY$ is anti-Hermitian, so $\operatorname{tr}(XY)$ is purely imaginary and $\operatorname{Re}\operatorname{tr}(XY)=0$; the subspaces are orthogonal. For $X\in\mathfrak{u}$, $\operatorname{tr}(X^2)=-\operatorname{tr}(XX^{\dagger})$ is real and negative; for $X\in\mathfrak{p}$, $\operatorname{tr}(X^2)=\operatorname{tr}(XX^{\dagger})$ is real and positive. $\square$

**The model matrices.** In the algebra model, $\mathfrak{u}=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$ and $\mathfrak{p}=\operatorname{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\}$, and

$$
\kappa(\vec e_j,\vec e_k)=-16\,\delta_{jk},\qquad
\kappa(i\vec e_j,i\vec e_k)=+16\,\delta_{jk}.
$$

The full form on $M_2(\mathbb{C})$ therefore has signature $(3,3)$ with two zero directions, the two real dimensions of the centre.

## The Real Forms and the Signature

**The two real forms.** The complex Lie algebra $\mathfrak{sl}_2(\mathbb{C})$ has two real forms up to isomorphism: the compact form $\mathfrak{su}(2)$ and the split form $\mathfrak{sl}_2(\mathbb{R})$, the latter isomorphic to $\mathfrak{su}(1,1)$. The Killing form is negative definite on the compact form, of signature $(2,1)$ on the split form, and of signature $(3,3)$ on the complex algebra read over $\mathbb{R}$.

| Real form | Matrix condition | $\kappa$ signature |
|---|---|---|
| $\mathfrak{su}(2)$ | $X^{\dagger}=-X$, $\operatorname{tr}X=0$ | $(0,3)$ |
| $\mathfrak{sl}_2(\mathbb{R})$ | $X$ real, $\operatorname{tr}X=0$ | $(2,1)$ |
| $\mathfrak{sl}_2(\mathbb{C})$ over $\mathbb{R}$ | $\operatorname{tr}X=0$ | $(3,3)$ |

**The compact form.** On $\mathfrak{su}(2)$ the form is $\kappa(X,X)=-8\operatorname{tr}(XX^{\dagger})$, negative for every nonzero $X$, so the signature is $(0,3)$. In the biquaternion model this is the subspace $\mathrm{K}=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$.

**The split form.** On real traceless matrices the form is $\kappa(X,Y)=8\operatorname{tr}(XY)$. In the basis

$$
H=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
F=\begin{pmatrix}0&0\\1&0\end{pmatrix},
$$

the matrix of the form is

$$
\begin{pmatrix}8&0&0\\0&0&4\\0&4&0\end{pmatrix},
$$

whose eigenvalues $8,4,-4$ give the signature $(2,1)$. The split form is therefore indefinite, and the null directions are the real matrices $X$ with $\operatorname{tr}(X^2)=0$.

**The complex form.** On $\mathfrak{sl}_2(\mathbb{C})$ read over $\mathbb{R}$ the Hermitian and anti-Hermitian subspaces are orthogonal and carry opposite signs, so the signature is $(3,3)$; the real form $\mathfrak{su}(1,1)$ is conjugate to $\mathfrak{sl}_2(\mathbb{R})$ and does not give a third signature.

## Invariance

**Theorem.** The Killing form is invariant under the adjoint action:

$$
K\bigl([X,Y],Z\bigr)+K\bigl(Y,[X,Z]\bigr)=0 .
$$

*Proof.* This is the standard invariance of the trace of a product of adjoint operators, $\operatorname{tr}(\operatorname{ad}_{[X,Y]}\operatorname{ad}_Z)=-\operatorname{tr}(\operatorname{ad}_Y\operatorname{ad}_{[X,Z]})$, which follows from $\operatorname{ad}_{[X,Y]}=[\operatorname{ad}_X,\operatorname{ad}_Y]$ and the cyclicity of the trace. $\square$

**Corollary.** For every invertible $P$,

$$
\kappa(PXP^{-1},PYP^{-1})=\kappa(X,Y).
$$

The form is therefore a function of the conjugation class, and it descends to the adjoint group $PGL_2(\mathbb{C})=\operatorname{Aut}_{\mathbb{C}}(\mathbb{B})$. In the algebra it is invariant under every automorphism.

## Relation to the Trace Form

The **trace form** of the matrix model is the pairing

$$
\tau(X,Y)=\operatorname{tr}(XY),
$$

whose real part is twice the plain bilinear form of the biquaternion algebra, $\operatorname{Re}\operatorname{tr}(XY)=2\operatorname{Re}\operatorname{Sc}(\tilde X\tilde Y)$ (*$M_2(\mathbb{C})$ Representation : The Four Words and the Four Traces*). The Killing form is the trace form with its projection to the trace-free part made explicit:

$$
\kappa(X,Y)=8\operatorname{Re}\operatorname{tr}\bigl(X_{\mathrm{sl}}Y_{\mathrm{sl}}\bigr),
\qquad
X_{\mathrm{sl}}=X-\tfrac12(\operatorname{tr}X)\mathrm I_2 .
$$

**The two forms compared.**

| Property | Trace form $\operatorname{Re}\operatorname{tr}(XY)$ | Killing form $\kappa$ |
|---|---|---|
| Nondegenerate on $M_2(\mathbb{C})$ | yes | no; radical $\mathbb{C}\mathrm I_2$ |
| Nondegenerate on $\mathfrak{sl}_2$ | yes | yes |
| Signature on $\mathfrak{sl}_2$ | $(3,3)$ | $(3,3)$ |
| Invariant under all automorphisms | yes | yes |
| Invariant under the adjoint action | yes | yes |

On $\mathfrak{sl}_2$ the two forms are proportional, $\kappa=8\operatorname{Re}\operatorname{tr}(XY)$, and the factor eight is the normalization of the Killing form. On the centre the trace form is nonzero and the Killing form vanishes; that difference is the whole content of the radical.

## Summary

The Killing form of $\mathfrak{gl}_2(\mathbb{C})$ read over $\mathbb{R}$ is $\kappa(X,Y)=8\operatorname{Re}\operatorname{tr}(XY)-4\operatorname{Re}(\operatorname{tr}X\operatorname{tr}Y)$. Its radical is the centre $\mathbb{C}\mathrm I_2$, of real dimension two. On the trace-free part it is $8\operatorname{Re}\operatorname{tr}(XY)$, nondegenerate, with signature $(3,3)$: negative on the anti-Hermitian traceless matrices, the Lie algebra of $SU(2)$, and positive on the Hermitian traceless ones. The form is invariant under the adjoint action and under conjugation, so it is a function of the conjugation class, and its restriction to $\mathfrak{sl}_2$ is eight times the trace form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{ad}_X(Y)=[X,Y]$ | the adjoint operator |
| $\kappa(X,Y)=\operatorname{tr}(\operatorname{ad}_X\operatorname{ad}_Y)$ | the Killing form |
| $\kappa_{\mathbb{C}}(X,Y)=4\operatorname{tr}(XY)-2\operatorname{tr}X\operatorname{tr}Y$ | the complex bilinear form |
| $\operatorname{rad}\kappa=\mathbb{C}\mathrm I_2$ | the radical, the centre |
| $\mathfrak{sl}_2(\mathbb{C})$ | the trace-free part |
| $\mathfrak{u},\mathfrak{p}$ | the anti-Hermitian and Hermitian traceless subspaces, real dimension three each |
| $\tau(X,Y)=\operatorname{tr}(XY)$ | the trace form |

## Further Reading

- [Biquaternion Lie Group and Exponential Structure](biquaternion-lie-group-and-exponential-structure.html), for the Killing form of the algebra and its signature
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the plain form and its signature
- [$M_2(\mathbb{C})$ Representation : The Four Words and the Four Traces](m2c-representation-the-four-words-and-the-four-traces.html), for the trace pairing
- [$M_2(\mathbb{C})$ Model : The Centraliser and the Double Centraliser](m2c-model-the-centraliser-and-the-double-centraliser.html), for the commutant and the centre
- [Biquaternion Automorphisms and Derivations](biquaternion-automorphisms-and-derivations.html), for the automorphism group and its action
- [Structure of Lie Algebras](structure-of-lie-algebras.html), for the general theory of the Killing form and semisimplicity
