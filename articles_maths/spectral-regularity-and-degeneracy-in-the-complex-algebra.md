# __Spectral Regularity and Degeneracy in the Complex Algebra__

## Introduction

The complex algebra $\mathbb{C}=\mathbb{R}[i]/(i^2+1)$ is a field of real dimension two. It carries two quadratic conditions on one element. The **modulus squared** is

$$
|z|^2=z\bar z=t^2+b^2,\qquad z=t+bi,
$$

it is the natural norm, it is multiplicative, and it vanishes only at the origin. The **square of the imaginary part** is $b^2$; it carries no real term, it is not multiplicative, and it vanishes exactly on the real axis. The first decides invertibility, the second the separation of eigenvalues. This article studies the second condition and the eigenvalue problem that produces it.

The eigenvalue problem is posed on the regular representation: $L_z$ is multiplication by $z$ on $\mathbb{C}\cong\mathbb{R}^2$, extended complex-linearly to $V_{\mathbb{C}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$. In the real basis $1,i$ its matrix is the Cayley matrix

$$
A=\begin{pmatrix}t&-b\\ b&t\end{pmatrix}=tI+bJ,\qquad J=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix},\qquad J^2=-I .
$$

Its characteristic polynomial is $(\lambda-t)^2+b^2$, of discriminant $-4b^2$, and its eigenvalues are $\lambda_\pm=t\pm ib$. The element is **spectrally regular** when $b\neq0$ and **spectrally degenerate** when $b=0$, that is, exactly on the real axis. Because $\mathbb{C}$ is a field, every element is semisimple: there are no defective elements, and the spectral condition is a condition on the separation of the eigenvalues only.

**Conventions.** The element is $z=t+bi$ with $t,b\in\mathbb{R}$, the conjugation is $\bar z=t-bi$, the modulus squared is $|z|^2=z\bar z=t^2+b^2$, and the modulus is $|z|=\sqrt{t^2+b^2}$. The phrase *modulus-regular* means $|z|^2\neq0$. The companion articles write the same element $Q=q+iq'$ with norm $\langle Q\rangle_*=Q\bar Q$; the translation is $t=q$, $b=q'$, $|z|^2=\langle Q\rangle_*$. The algebra is *Complex Algebra*, the matrix is *Complex Regular Element Representation*, and invertibility is *Complex Norm and Invertibility*.

## The Regular Representation and the Eigenvalue Problem

**Definition (left regular representation).** The **left regular representation** of $\mathbb{C}$ is

$$
L:\mathbb{C}\longrightarrow\operatorname{End}_{\mathbb{R}}(\mathbb{C}),\qquad L_z(v)=zv.
$$

**Proposition (the Cayley matrix).** In the real basis $1,i$,

$$
L_z(1)=z=t\cdot1+b\cdot i,\qquad L_z(i)=zi=-b\cdot1+t\cdot i,
$$

so the matrix of $L_z$ is $A=\begin{pmatrix}t&-b\\ b&t\end{pmatrix}$.

*Proof.* The columns of the matrix are the images of the basis vectors. The first column is $(t,b)$ and the second is $(-b,t)$, as displayed.

**Definition (complexified representation).** The **complexification** of $L_z$ is the complex-linear map

$$
L_z^{\mathbb{C}}=L_z\otimes\mathrm{id}_{\mathbb{C}}:V_{\mathbb{C}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\longrightarrow V_{\mathbb{C}},\qquad L_z^{\mathbb{C}}(\alpha\otimes v)=\alpha\otimes zv .
$$

In the complex basis $1\otimes1,\ 1\otimes i$ its matrix is again $A$. The two factors play different roles: a complex scalar $\lambda$ of the first copy acts by $\lambda I$, while the algebra element $\lambda$ of the second copy acts by $L_\lambda$; the two operators differ, and the eigenvalue problem uses the first.

**Definition (eigenvalue and eigenvector).** A complex number $\lambda$ is an **eigenvalue** of $z$ if there is a non-zero $v\in V_{\mathbb{C}}$ with $L_z^{\mathbb{C}}v=\lambda v$. Such a $v$ is an **eigenvector** for $\lambda$, and the set of eigenvectors with the origin is the **eigenspace**. The **spectrum** $\sigma(z)$ is the set of eigenvalues.

**Proposition (the eigenvalue criterion).** For $\lambda\in\mathbb{C}$, the following are equivalent: $\lambda$ is an eigenvalue; $A-\lambda I$ is not invertible; $\det(A-\lambda I)=0$.

*Proof.* A non-zero solution of $(A-\lambda I)v=0$ exists exactly when the matrix is singular, and a square complex matrix is singular exactly when its determinant vanishes.

## The Characteristic Polynomial and the Criterion

**Theorem (the characteristic polynomial).** For $z=t+bi$,

$$
p_z(X)=\det(XI-A)=X^2-2tX+(t^2+b^2)=X^2-2tX+|z|^2,
$$

of discriminant

$$
\operatorname{disc}p_z=4t^2-4|z|^2=-4b^2,
$$

and eigenvalues

$$
\lambda_\pm=t\pm ib.
$$

*Proof.* The determinant of $XI-A=\begin{pmatrix}X-t&b\\ -b&X-t\end{pmatrix}$ is $(X-t)^2+b^2=X^2-2tX+t^2+b^2$. The discriminant of $X^2-2tX+(t^2+b^2)$ is $4t^2-4(t^2+b^2)=-4b^2$, and the quadratic formula gives $\lambda_\pm=t\pm\sqrt{-b^2}=t\pm ib$.

**Corollary (the criterion).** For $z\in\mathbb{C}$ the following are equivalent:

1. $b\neq0$;
2. the eigenvalues $\lambda_+$ and $\lambda_-$ are distinct;
3. $\operatorname{disc}p_z\neq0$;
4. the two eigenlines of $L_z^{\mathbb{C}}$ are distinct.

*Proof.* The equivalence of (1), (2) and (3) is immediate from $\lambda_+-\lambda_-=2ib$ and $\operatorname{disc}p_z=-4b^2$. Two eigenvalues are distinct exactly when their eigenspaces are distinct lines, which gives (4).

**Definition (spectral regularity and degeneracy).** An element is **spectrally regular** when $b\neq0$ and **spectrally degenerate** when $b=0$. The degenerate set is the real axis $\mathbb{R}\subset\mathbb{C}$.

**Remark (the characteristic polynomial reads both invariants).** The constant term of $p_z$ is the modulus squared $|z|^2$, and its discriminant is $-4b^2$. The spectrum therefore carries the modulus in its product, $\lambda_+\lambda_-=|z|^2$, and the spectral condition in its separation, $(\lambda_+-\lambda_-)^2=-4b^2$. The two quadratic conditions of the introduction are the two coefficients of one polynomial.

## Eigenspaces and Semisimplicity

**Theorem (the eigenspaces).** If $b\neq0$, each eigenvalue has a one-dimensional complex eigenspace:

$$
\ker(A-\lambda_+I)=\mathbb{C}\,(1,-i),\qquad \ker(A-\lambda_-I)=\mathbb{C}\,(1,i).
$$

If $b=0$, the only eigenvalue is $t$ and the eigenspace is all of $V_{\mathbb{C}}$.

*Proof.* For $\lambda_+=t+ib$, the matrix $A-\lambda_+I=\begin{pmatrix}-ib&-b\\ b&-ib\end{pmatrix}$ has rank one, since its second row is $i$ times its first; its kernel is the line $y=-ix$, that is $\mathbb{C}(1,-i)$. For $\lambda_-$ the computation is the same with $i$ replaced by $-i$, and the kernel is $\mathbb{C}(1,i)$. If $b=0$ then $A=tI$, so every vector is an eigenvector with eigenvalue $t$.

**Corollary (the eigenbasis exists off the real axis).** If $b\neq0$, the pair $(1,-i),(1,i)$ is a complex basis of $V_{\mathbb{C}}$ consisting of eigenvectors. Its determinant is $2i\neq0$.

*Proof.* The two vectors are eigenvectors for distinct eigenvalues, hence independent; explicitly $\det\begin{pmatrix}1&1\\ -i&i\end{pmatrix}=i+i=2i$.

**Theorem (every element is semisimple).** For every $z\in\mathbb{C}$, the minimal polynomial of $z$ over $\mathbb{R}$ is

$$
m_z(X)=
\begin{cases}
X-t, & b=0,\\
(X-t)^2+b^2, & b\neq0,
\end{cases}
$$

and it is squarefree. Thus $L_z^{\mathbb{C}}$ is diagonalisable and $z$ is not defective.

*Proof.* If $b=0$ then $z=t$ is real and $X-t$ annihilates it, and no constant polynomial does. If $b\neq0$, the polynomial $(X-t)^2+b^2$ annihilates $z$ by Cayley–Hamilton, and it is the minimal polynomial because $z$ is not real and the only real polynomials of degree at most one that could annihilate it are constant. Its roots are $t\pm ib$, which are distinct because $b\neq0$. It is squarefree, and an operator with a squarefree minimal polynomial is diagonalisable over $\mathbb{C}$.

**Corollary (no defective element).** The algebra $\mathbb{C}$ has no defective element. Every element is semisimple, and the Jordan form of $L_z^{\mathbb{C}}$ is diagonal.

*Proof.* An element is defective when its minimal polynomial has a repeated root. By the theorem the minimal polynomial is squarefree in both cases, so no element is defective.

**Remark (the contrast with the biquaternion algebra).** In the biquaternion algebra the spectral condition separates the semisimple elements from the defective ones, because the degenerate cone contains non-scalar nilpotent and unipotent strata. Here the algebra is a field, so the separation is automatic and the spectral condition measures only whether the two eigenvalues coincide. The word *degenerate* therefore does not mean *defective* in this article.

## The Scalar Stratum

**Proposition (the real axis).** Let $z=t$ be real. Then:

1. $L_z=tI$ and $\sigma(z)=\{t\}$;
2. the eigenspace is $V_{\mathbb{C}}$;
3. every complex basis of $V_{\mathbb{C}}$ is an eigenbasis;
4. the minimal polynomial is $X-t$;
5. every idempotent of the complexified algebra is a spectral idempotent.

*Proof.* The first four statements are immediate from $A=tI$. For the fifth, the complexified algebra is commutative, so every idempotent $e$ satisfies $ze=te$; the spectral idempotents are exactly the idempotents commuting with $z$, which is all of them.

**Remark (the real axis).** On the axis the canonical spectral decomposition is the one-term writing $z=t\cdot1$. In the complexified algebra the idempotents $e_\pm=\tfrac12(1\mp i\iota)$, with $\iota=1\otimes i$, still satisfy $e_++e_-=1$ and give

$$
z=t\,e_+ + t\,e_-,
$$

but the two coefficients are equal: the terms are not separated by the spectrum and the splitting is not unique. The axis is the fixed algebra of the conjugation and the analogue of the scalar stratum of the biquaternion algebra. Its elements are central and semisimple, so the axis is a stratum of the spectral condition, not a failure of the algebra.

## What the Spectral Condition Sees

**Proposition (the spectral type depends only on $b$).** Two elements with the same imaginary part have the same spectral type. The modulus squared depends on both coordinates.

*Proof.* The discriminant is $-4b^2$ and the eigenvalues are $t\pm ib$; the spectral type is fixed by the vanishing of $b$. The modulus squared is $t^2+b^2$, which changes with $t$ at fixed $b$.

**Example.** The elements $1+i$ and $7+i$ are both spectrally regular, with moduli squared $2$ and $50$; the elements $3$ and $-3$ are both spectrally degenerate, with moduli squared $9$.

**Corollary (the one-way implication).** If $z$ is spectrally regular then $z$ is modulus-regular. The converse fails: the non-zero real numbers are modulus-regular and spectrally degenerate.

*Proof.* $b\neq0$ gives $|z|^2=t^2+b^2\geq b^2>0$. The converse fails at $z=1$, where $|z|^2=1$ and $b=0$.

**Remark (the asymmetry).** The spectral condition is blind to the real part, so it cannot see the modulus; the modulus sees both coordinates. The spectrally regular set is therefore contained in the modulus-regular set, and the inclusion is strict. The comparison is *Relations between the Modulus and Spectral Regularity and Degeneracy*, and the count of cells is *The Three Sectors of the Complex Algebra*.

## Summary

The complex algebra carries two quadratic conditions. The modulus squared $|z|^2=t^2+b^2$ is multiplicative and vanishes only at the origin. The square of the imaginary part $b^2$ is not multiplicative and vanishes on the real axis. The eigenproblem of the regular representation is governed by the second: the Cayley matrix of $z=t+bi$ is $\begin{pmatrix}t&-b\\ b&t\end{pmatrix}$, its characteristic polynomial is $X^2-2tX+|z|^2=(X-t)^2+b^2$, its discriminant is $-4b^2$, and its eigenvalues are $\lambda_\pm=t\pm ib$.

The element is spectrally regular exactly when $b\neq0$, off the real axis, and spectrally degenerate exactly when $b=0$, on it. Off the axis the eigenvalues are distinct and the eigenspaces are the lines $\mathbb{C}(1,-i)$ and $\mathbb{C}(1,i)$; on the axis the operator is the scalar $tI$, the only eigenvalue is $t$, and the eigenspace is the whole complexified plane.

Every element of $\mathbb{C}$ is semisimple. The minimal polynomial is $X-t$ on the real axis and $(X-t)^2+b^2$ off it, squarefree in both cases. There is no defective element and no Jordan block of size two, because the algebra is a field. The spectral condition measures the separation of the eigenvalues, not the existence of an eigenbasis. It sees only $b$, while the modulus sees both $t$ and $b$; the characteristic polynomial carries the two in its coefficients, the constant term $|z|^2$ and the discriminant $-4b^2$. Every spectrally regular element is modulus-regular, and the converse fails on the punctured real axis.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}=\mathbb{R}[i]/(i^2+1)$ | the complex algebra, basis $1,i$ |
| $z=t+bi$ | a complex number, $t=\operatorname{Re}z$, $b=\operatorname{Im}z$ |
| $\bar z=t-bi$ | complex conjugation |
| $\lvert z\rvert^2=z\bar z=t^2+b^2$ | the modulus squared, the natural norm |
| $\lvert z\rvert=\sqrt{t^2+b^2}$ | the modulus |
| $L_z(v)=zv$ | the left regular representation |
| $V_{\mathbb{C}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ | the complexified regular representation |
| $A=\begin{pmatrix}t&-b\\ b&t\end{pmatrix}=tI+bJ$ | the Cayley matrix of $L_z$, $J^2=-I$ |
| $p_z(X)=X^2-2tX+(t^2+b^2)$ | the characteristic polynomial, equal to $(X-t)^2+b^2$ |
| $\operatorname{disc}p_z=-4b^2$ | the discriminant |
| $\lambda_\pm=t\pm ib$ | the eigenvalues |
| $\sigma(z)$ | the spectrum |
| $m_z(X)$ | the minimal polynomial: $X-t$ if $b=0$, $(X-t)^2+b^2$ if $b\neq0$ |
| $\mathbb{R}$ | the real axis, the spectral-degenerate set |
| $\Sigma_{11},\Sigma_{10},\Sigma_{00}$ | the spectral cells, defined in *The Three Sectors of the Complex Algebra* |

## Further Reading

- [Eigenvalue Decomposition and Eigenbasis of a Complex Number](eigenvalue-decomposition-and-eigenbasis-of-a-complex-number.html), for the eigenbasis $(1,-i),(1,i)$, the diagonal form, the idempotents $e_\pm$ and the polar reading.
- [Relations between the Modulus and Spectral Regularity and Degeneracy](relations-between-the-modulus-and-spectral-regularity-and-degeneracy.html), for the comparison of $|z|^2$ and $b^2$, the nesting of the two regular sets and the chain of invariants.
- [The Three Sectors of the Complex Algebra](the-three-sectors-of-the-complex-algebra.html), for the partition $\Sigma_{11},\Sigma_{10},\Sigma_{00}$ and the empty cell $\Sigma_{01}$.
- [Complex Algebra](complex-algebra.html), for the definition, the conjugation and the real and imaginary subspaces.
- [Complex Regular Element Representation](complex-regular-element-representation.html), for the Cayley matrix, its determinant and its trace.
- [Complex Norm and Invertibility](complex-norm-and-invertibility.html), for the modulus, its multiplicativity and the criterion $z\neq0$.
- [The Eigenvalue Decomposition of an Element](the-eigenvalue-decomposition-of-an-element.html), for the general definitions of spectrum, spectral idempotent and semisimplicity.
- [Nilpotent Elements and the Jordan–Chevalley Decomposition](nilpotent-elements-and-the-jordan-chevalley-decomposition.html), for the semisimple and nilpotent parts in the general theory.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (2nd edition, Cambridge University Press, 2013), for the characteristic polynomial, the discriminant and diagonalisability.
