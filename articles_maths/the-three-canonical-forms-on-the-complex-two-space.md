# __The Three Canonical Forms on $\mathbb{C}^2$__

## Introduction

The complex two-space carries three canonical forms: the Hermitian form $H$, the complex bilinear symmetric form $B$ and the complex bilinear alternating form $\omega$. They are defined in *Complex Two-Space* and announced there; this article computes them. It gives their Gram matrices, their symmetry and nondegeneracy, their isotropic sets, their real and imaginary parts, the relations among them, and the distinction between $\operatorname{Im}H$ and $\omega$, which is the point at which the three are most often confused.

The article treats the forms on the space alone. The isometry groups are *The Classical Groups of $\mathbb{C}^2$*; the Kähler structure they define is *The Flat Kähler Structure of $\mathbb{C}^2$*; the real signatures are also read in *The Realification of $\mathbb{C}^2$*, and the computations are repeated here only where the complex statement needs them. The general theory of bilinear and sesquilinear forms is *Bilinear Forms* and *The Sesquilinear Structure of the Endomorphism Algebra*; this article does not restate it.

**The three forms are of three different kinds and are not three normalisations of one object.** $H$ is sesquilinear and definite; $B$ is symmetric and indefinite; $\omega$ is alternating and nondegenerate. The first carries the metric, the second the isotropic cone, the third the holomorphic symplectic structure. One table at the end of the article collects them.

## The Hermitian Form

**The Hermitian form is the positive definite sesquilinear form of the space; its Gram matrix is the identity and its norm is the Euclidean norm.**

**Definition.** The **Hermitian form** is
$$
H(Q_1,Q_2)=Q_{1\blacktriangle}\overline{Q_{2\blacktriangle}}+Q_{1\blacktriangledown}\overline{Q_{2\blacktriangledown}}.
$$

**Proposition (the Gram matrix).** In the complex basis $e_1,e_2$ the Gram matrix is the identity,
$$
\bigl(H(e_j,e_k)\bigr)_{j,k}=\begin{pmatrix}1&0\\0&1\end{pmatrix}.
$$

*Proof.* $H(e_1,e_1)=1$, $H(e_1,e_2)=0$, $H(e_2,e_1)=0$, $H(e_2,e_2)=1$.

**Proposition (sesquilinearity and positivity).** The form is linear in the first slot and conjugate-linear in the second,
$$
H(\lambda Q_1,Q_2)=\lambda H(Q_1,Q_2),\qquad H(Q_1,\lambda Q_2)=\overline{\lambda}H(Q_1,Q_2),
$$
it is Hermitian, $H(Q_2,Q_1)=\overline{H(Q_1,Q_2)}$, and it is positive definite, $H(Q,Q)>0$ for $Q\neq0$.

*Proof.* The two linearity rules are read on the definition. The Hermitian symmetry is the identity $\overline{Q_{1\blacktriangle}\overline{Q_{2\blacktriangle}}}=Q_{2\blacktriangle}\overline{Q_{1\blacktriangle}}$, and likewise for the descending triangle. The positivity is $\lvert Q_{\blacktriangle}\rvert^2+\lvert Q_{\blacktriangledown}\rvert^2$, a sum of non-negative terms, zero only when both coordinates vanish.

**Remark (the only definite form of the three).** The form $H$ is the only one of the three whose isotropic set is the origin. **Its signature over $\mathbb{R}$ is $(4,0)$, and it is the form that defines the topology of the space.** The other two have non-trivial isotropic sets and indefinite real pictures; their role is geometric and not metric.

The real and imaginary parts of $H$ are computed in *The Realification of $\mathbb{C}^2$*: the real part is the Euclidean metric $g$ of signature $(4,0)$ and the imaginary part is the symplectic form $-\Omega$, where $\Omega=dq_{\blacktriangle}\wedge dq'_{\blacktriangle}+dq_{\blacktriangledown}\wedge dq'_{\blacktriangledown}$ is the Kähler form. The relation is
$$
H(Q_1,Q_2)=g(Q_1,Q_2)-i\Omega(Q_1,Q_2),\qquad \Omega(Q_1,Q_2)=g(JQ_1,Q_2),
$$
and it is the reason the Hermitian form carries both the metric and the symplectic structure of the space.

## The Complex Bilinear Form $B$

**The complex bilinear form is symmetric and nondegenerate; its isotropic set is the union of two complex lines, and in suitable holomorphic coordinates its quadratic form is the product $uv$.**

**Definition.** The **complex bilinear form** is
$$
B(Q_1,Q_2)=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown}.
$$

**Proposition (symmetry, Gram matrix and nondegeneracy).** The form is $\mathbb{C}$-bilinear and symmetric, $B(Q_2,Q_1)=B(Q_1,Q_2)$; its Gram matrix in the complex basis is the identity; and it is nondegenerate.

*Proof.* Bilinearity and symmetry are read on the definition. The Gram matrix is $B(e_j,e_k)=\delta_{jk}$, of determinant $1$, hence invertible, which is nondegeneracy.

**Theorem (the isotropic cone).** The isotropic set of $B$ is the union of the two complex lines
$$
L_+=\{Q:Q_{\blacktriangle}=iQ_{\blacktriangledown}\},\qquad L_-=\{Q:Q_{\blacktriangle}=-iQ_{\blacktriangledown}\},
$$
and the two lines meet only at the origin.

*Proof.* $B(Q,Q)=Q_{\blacktriangle}^2+Q_{\blacktriangledown}^2=(Q_{\blacktriangle}+iQ_{\blacktriangledown})(Q_{\blacktriangle}-iQ_{\blacktriangledown})$. The field $\mathbb{C}$ is a domain, so the product vanishes exactly when one factor does, that is $Q_{\blacktriangle}=-iQ_{\blacktriangledown}$ or $Q_{\blacktriangle}=iQ_{\blacktriangledown}$. A point of both lines satisfies $2Q_{\blacktriangle}=0$ and $2iQ_{\blacktriangledown}=0$, hence is the origin.

**Theorem (the normal form).** In the holomorphic coordinates
$$
u(Q)=Q_{\blacktriangle}+iQ_{\blacktriangledown},\qquad v(Q)=Q_{\blacktriangle}-iQ_{\blacktriangledown},
$$
the form is
$$
B(Q_1,Q_2)=\tfrac12\bigl(u(Q_1)v(Q_2)+u(Q_2)v(Q_1)\bigr),
$$
its quadratic form is $B(Q,Q)=u(Q)v(Q)=Q_{\blacktriangle}^2+Q_{\blacktriangledown}^2$, and the two isotropic lines are the coordinate axes $u(Q)=0$ and $v(Q)=0$.

*Proof.* The change of coordinates is invertible, with $Q_{\blacktriangle}=\tfrac12(u(Q)+v(Q))$ and $Q_{\blacktriangledown}=\tfrac{1}{2i}(u(Q)-v(Q))$, and $u(Q)v(Q)=(Q_{\blacktriangle}+iQ_{\blacktriangledown})(Q_{\blacktriangle}-iQ_{\blacktriangledown})=Q_{\blacktriangle}^2+Q_{\blacktriangledown}^2$. The polarization of this quadratic form is the displayed symmetric expression. The axis $u(Q)=0$ is $Q_{\blacktriangle}=-iQ_{\blacktriangledown}$, and the axis $v(Q)=0$ is $Q_{\blacktriangle}=iQ_{\blacktriangledown}$.

**Remark (a hyperbolic form in complex coordinates).** The normal form $B(Q_1,Q_2)=\tfrac12(u(Q_1)v(Q_2)+u(Q_2)v(Q_1))$ has the quadratic form $B(Q,Q)=u(Q)v(Q)$, the complex analogue of the hyperbolic form $x^2-y^2$ of the split-complex plane. **The form is indefinite in the strongest sense: over $\mathbb{C}$ it has no signature, because a complex number is not ordered, and its realification has signature $(2,2)$ for both the real and the imaginary part.** The absence of a signature over $\mathbb{C}$ is not a defect of the computation: it is the statement that the form has isotropic vectors in abundance, and a definite form has none.

The two isotropic lines are complex lines, hence $J$-invariant, but they are selected by $B$ and not by $J$: every complex line is $J$-invariant, and only two of them are isotropic. They are the two points of $\mathbb{CP}^1$ at which the quadric $B=0$ meets the line at infinity (*The Isotropic Cone of the Bilinear Form on $\mathbb{C}^2$*).

**Proposition (the behaviour under $J$).** The form is anti-invariant under the complex structure,
$$
B(JQ_1,JQ_2)=-B(Q_1,Q_2).
$$

*Proof.* $B(iQ_1,iQ_2)=i^2B(Q_1,Q_2)=-B(Q_1,Q_2)$.

**Remark (two different isometry groups).** The unitary group preserves $H$, and the complex orthogonal group $\mathrm{O}(2,\mathbb{C})$ preserves $B$. The two groups are different, because $U^{*}U=I$ does not imply $U^{T}U=I$: a unitary matrix need not be complex orthogonal. **Their intersection is the real orthogonal group $\mathrm{O}(2)$**, the matrices that are at once real and unitary (*The Classical Groups of $\mathbb{C}^2$*).

## The Holomorphic Symplectic Form $\omega$

**The holomorphic symplectic form is alternating and nondegenerate; it vanishes on every complex line, and it is the form whose powers give the complex volume.**

**Definition.** The **holomorphic symplectic form** is
$$
\omega(Q_1,Q_2)=Q_{1\blacktriangle}Q_{2\blacktriangledown}-Q_{1\blacktriangledown}Q_{2\blacktriangle}.
$$

**Proposition (alternation, Gram matrix and nondegeneracy).** The form is $\mathbb{C}$-bilinear and alternating, $\omega(Q_2,Q_1)=-\omega(Q_1,Q_2)$; its Gram matrix in the complex basis is
$$
\bigl(\omega(e_j,e_k)\bigr)_{j,k}=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
$$
of determinant $1$; and it is nondegenerate.

*Proof.* The alternation is the exchange of the two coordinates. The entries are $\omega(e_1,e_2)=1$, $\omega(e_2,e_1)=-1$ and the two diagonal entries $\omega(e_k,e_k)=0$. The determinant is $1$.

**Proposition (the form is decomposable).** As a complex $2$-form, $\omega=dQ_{\blacktriangle}\wedge dQ_{\blacktriangledown}$; in particular $\omega\wedge\omega=0$ and
$$
\omega\wedge\overline{\omega}=2\,\Omega^2=4\,dq_{\blacktriangle}\wedge dq'_{\blacktriangle}\wedge dq_{\blacktriangledown}\wedge dq'_{\blacktriangledown},
$$
where $\Omega=dq_{\blacktriangle}\wedge dq'_{\blacktriangle}+dq_{\blacktriangledown}\wedge dq'_{\blacktriangledown}$ is the Kähler form.

*Proof.* The evaluation of $dQ_{\blacktriangle}\wedge dQ_{\blacktriangledown}$ on a pair $(Q_1,Q_2)$ is $Q_{1\blacktriangle}Q_{2\blacktriangledown}-Q_{1\blacktriangledown}Q_{2\blacktriangle}$. The square of a $2$-form in two complex variables vanishes because there are only two holomorphic directions. For the last identity, $dQ_{\blacktriangle}\wedge d\overline{Q}_{\blacktriangle}=-2i\,dq_{\blacktriangle}\wedge dq'_{\blacktriangle}$ and likewise for the descending triangle, and the product of the two gives the coefficient $4$ after the sign of the reordering; the computation is one line in the real basis.

**Theorem (the isotropic subspaces).** For $Q_1\neq0$, $\omega(Q_1,Q_2)=0$ exactly when $Q_2$ is a complex multiple of $Q_1$. Hence the complex subspaces isotropic for $\omega$ are exactly the complex lines, and every complex line is isotropic.

*Proof.* If $Q_2=\lambda Q_1$, the alternation gives $\omega(Q_1,\lambda Q_1)=\lambda\omega(Q_1,Q_1)=0$. Conversely, suppose $\omega(Q_1,Q_2)=0$ with $Q_1\neq0$. If $Q_{1\blacktriangledown}\neq0$, the equation reads $Q_{2\blacktriangle}=(Q_{1\blacktriangle}/Q_{1\blacktriangledown})Q_{2\blacktriangledown}$, so $Q_2=(Q_{2\blacktriangledown}/Q_{1\blacktriangledown})\,Q_1$; the case $Q_{1\blacktriangledown}=0$ gives $Q_{1\blacktriangle}\neq0$ and $\omega(Q_1,Q_2)=Q_{1\blacktriangle}Q_{2\blacktriangledown}=0$, so $Q_{2\blacktriangledown}=0$ and $Q_2=(Q_{2\blacktriangle}/Q_{1\blacktriangle})\,Q_1$.

**Remark (the Lagrangian lines).** A **Lagrangian** subspace of a symplectic space is an isotropic subspace of half the dimension. **In complex dimension two the Lagrangian subspaces of $\omega$ are exactly the complex lines**, and the space of them is $\mathbb{CP}^1$. This is the opposite of the behaviour of the Kähler form, on which the complex lines are symplectic and the Lagrangian planes are the totally real ones (*The Subspaces of $\mathbb{C}^2$*).

**Proposition (the behaviour under $J$).** The form is anti-invariant under the complex structure,
$$
\omega(JQ_1,JQ_2)=-\omega(Q_1,Q_2),
$$
so both $\operatorname{Re}\omega$ and $\operatorname{Im}\omega$ change sign under $J$.

*Proof.* $\omega(iQ_1,iQ_2)=i^2\omega(Q_1,Q_2)=-\omega(Q_1,Q_2)$, and the real and imaginary parts inherit the sign.

**Remark (the two real symplectic forms).** The real and imaginary parts of $\omega$ are
$$
\operatorname{Re}\omega=dq_{\blacktriangle}\wedge dq_{\blacktriangledown}-dq'_{\blacktriangle}\wedge dq'_{\blacktriangledown},\qquad \operatorname{Im}\omega=dq_{\blacktriangle}\wedge dq'_{\blacktriangledown}-dq_{\blacktriangledown}\wedge dq'_{\blacktriangle},
$$
both nondegenerate, both anti-invariant under $J$. **They are a pair of symplectic forms orthogonal under the wedge pairing**, $\operatorname{Re}\omega\wedge\operatorname{Im}\omega=0$, and their squares are equal, $\operatorname{Re}\omega\wedge\operatorname{Re}\omega=\operatorname{Im}\omega\wedge\operatorname{Im}\omega$. No one of them is the Kähler form.

## The Relations among the Three

**The three forms are related by the conjugation of the coefficients and by the Lagrange identity; the relations are algebraic and do not make any one of them a function of the others.**

**Proposition (the Hermitian form is the bilinear form on the conjugate).** For $Q_1,Q_2\in\mathbb{C}^2$,
$$
H(Q_1,Q_2)=B(Q_1,\overline{Q}_2),
$$
where $\overline{Q}_2=(\overline{Q}_{2\blacktriangle},\overline{Q}_{2\blacktriangledown})$ is the coefficientwise conjugate.

*Proof.* $B(Q_1,\overline{Q}_2)=Q_{1\blacktriangle}\overline{Q_{2\blacktriangle}}+Q_{1\blacktriangledown}\overline{Q_{2\blacktriangledown}}=H(Q_1,Q_2)$.

**Proposition (the Lagrange identity).** For all $Q_1,Q_2\in\mathbb{C}^2$,
$$
B(Q_1,Q_2)^2+\omega(Q_1,Q_2)^2=B(Q_1,Q_1)\,B(Q_2,Q_2).
$$

*Proof.* Write $a=Q_{1\blacktriangle}$, $b=Q_{1\blacktriangledown}$, $c=Q_{2\blacktriangle}$, $d=Q_{2\blacktriangledown}$. The identity is $(ac+bd)^2+(ad-bc)^2=(a^2+b^2)(c^2+d^2)$, which is the multiplicativity of the complex modulus read on the two complex numbers $a+ib$ and $c+id$.

**Proposition (the normal forms in the coordinates $u,v$).** Let
$$
u(Q)=Q_{\blacktriangle}+iQ_{\blacktriangledown},\qquad v(Q)=Q_{\blacktriangle}-iQ_{\blacktriangledown}
$$
be the two null coordinates of the point $Q$. Then
$$
B(Q_1,Q_2)=\tfrac12\bigl(u(Q_1)v(Q_2)+u(Q_2)v(Q_1)\bigr),\qquad \omega(Q_1,Q_2)=\tfrac{i}{2}\bigl(u(Q_1)v(Q_2)-v(Q_1)u(Q_2)\bigr),
$$
and
$$
H(Q_1,Q_2)=\tfrac12\bigl(u(Q_1)\overline{u(Q_2)}+v(Q_1)\overline{v(Q_2)}\bigr).
$$

*Proof.* The first is the theorem of the previous section. For the second, $u(Q_1)v(Q_2)-v(Q_1)u(Q_2)=-2i(Q_{1\blacktriangle}Q_{2\blacktriangledown}-Q_{1\blacktriangledown}Q_{2\blacktriangle})=-2i\,\omega(Q_1,Q_2)$. For the third, $u(Q_1)\overline{u(Q_2)}+v(Q_1)\overline{v(Q_2)}=2(Q_{1\blacktriangle}\overline{Q_{2\blacktriangle}}+Q_{1\blacktriangledown}\overline{Q_{2\blacktriangledown}})=2H(Q_1,Q_2)$.

**Remark (the three forms in one coordinate system).** In the coordinates $u,v$ the three forms are the product, the symplectic form and the Euclidean metric, and the space is the product of two lines. **The coordinates $u,v$ are holomorphic, so the types of the forms are preserved: $B$ stays symmetric, $\omega$ stays alternating and $H$ stays Hermitian.** The normal form displays the isotropic cone as the union of the axes and the Lagrangian lines as the axes themselves.

## The Distinction between $\operatorname{Im}H$ and $\omega$

**The forms $\operatorname{Im}H$ and $\omega$ are both alternating and both nondegenerate, and they are not the same form; the negative of the first is the Kähler form, the second is the holomorphic symplectic form.**

The two are compared in the table below. The comparison is the answer to the most frequent confusion of the category.

| Property | $\operatorname{Im}H$ | $\omega$ |
|---|---|---|
| valued in | $\mathbb{R}$ | $\mathbb{C}$ |
| type as a complex form | $(1,1)$ | $(2,0)$ |
| behaviour under $J$ | invariant: $\operatorname{Im}H(JQ_1,JQ_2)=\operatorname{Im}H(Q_1,Q_2)$ | anti-invariant: $\omega(JQ_1,JQ_2)=-\omega(Q_1,Q_2)$ |
| on a complex line | minus the area form, nondegenerate | zero |
| Lagrangian subspaces | the $\Omega$-Lagrangian planes: a $3$-parameter family inside the totally real planes | the complex lines, $\mathbb{CP}^1$ |
| role | Kähler form, metric and symplectic structure | holomorphic volume form |
| relation to the metric | $\Omega=-\operatorname{Im}H=g(J\cdot,\cdot)$ | $\omega\wedge\overline{\omega}=2\Omega^2$ |

**Theorem (the two are not proportional).** There is no constant $\lambda\in\mathbb{C}$ with $\operatorname{Im}H=\lambda\omega$; the two forms have different values on the same pair and different isotropic subspaces.

*Proof.* On the pair $Q_1=(1,0)$, $Q_2=(i,0)$ one has $\operatorname{Im}H(Q_1,Q_2)=-1$ and $\omega(Q_1,Q_2)=0$. On the pair $Q_1=(1,0)$, $Q_2=(0,1)$ one has $\operatorname{Im}H(Q_1,Q_2)=0$ and $\omega(Q_1,Q_2)=1$. A proportional pair cannot take a zero and a non-zero value on the same pair, so no constant exists.

**Remark (the geometric content of the distinction).** The form $\operatorname{Im}H$ pairs a vector with the conjugate of another; the form $\omega$ pairs two vectors directly. **The first sees the complex structure and is invariant under it; the second sees the holomorphic structure and changes sign under it.** On a complex line, the first measures area and the second vanishes. This is why the Kähler form is $\Omega=-\operatorname{Im}H$ and the holomorphic symplectic form is $\omega$, and why the two are never substituted one for the other.

**Remark (the consequence for the Lagrangian planes).** A plane that is Lagrangian for $\Omega$ cannot contain a complex line, because $\Omega$ is nondegenerate on every complex line; hence it is totally real. **The $\Omega$-Lagrangian planes are a $3$-parameter family inside the $4$-parameter family of totally real planes, and a complex line is never $\Omega$-Lagrangian.** The two notions of Lagrangian therefore select different classes of planes: the $\omega$-Lagrangian lines are complex, the $\Omega$-Lagrangian planes are totally real.

## Gram Matrices and the Real Pictures

**The Gram matrices in the complex basis are the identity, the identity and the standard symplectic matrix; in the real basis the six real forms take the normal forms collected below.**

**Theorem (the complex Gram matrices).** In the complex basis $e_1,e_2$,
$$
G_H=\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad G_B=\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad G_\omega=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$

*Proof.* The entries are computed in the three propositions above.

The real pictures are read in the real basis $e_1,ie_1,e_2,ie_2$, in this order.

| Real form | Matrix, up to the order of the blocks | Signature or rank |
|---|---|---|
| $\operatorname{Re}H$ | $I_4$ | $(4,0)$ |
| $\operatorname{Im}H$ | $\operatorname{diag}(J_0,J_0)$ with $J_0=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ | symplectic, rank $4$ |
| $\operatorname{Re}B$ | $\operatorname{diag}(1,-1,1,-1)$ | $(2,2)$ |
| $\operatorname{Im}B$ | two blocks $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ | $(2,2)$ |
| $\operatorname{Re}\omega$ | $\begin{pmatrix}0&A\\-A&0\end{pmatrix}$, $A=\operatorname{diag}(1,-1)$ | symplectic, rank $4$ |
| $\operatorname{Im}\omega$ | $\begin{pmatrix}0&B\\-B&0\end{pmatrix}$, $B=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ | symplectic, rank $4$ |

**Remark (the sign of the Kähler form).** The form $\operatorname{Im}H$ is $-\Omega$, with $\Omega=dq_{\blacktriangle}\wedge dq'_{\blacktriangle}+dq_{\blacktriangledown}\wedge dq'_{\blacktriangledown}$. **The sign is not a convention of notation but the statement that $\Omega$ is positive on the complex lines**: on the line spanned by $e_1$, $\Omega(e_1,ie_1)=1$, while $\operatorname{Im}H(e_1,ie_1)=-1$. The Kähler form is taken positive, and the Hermitian form is $H=g-i\Omega$.

## Summary

The space $\mathbb{C}^2$ carries three canonical forms. The Hermitian form $H(Q_1,Q_2)=Q_{1\blacktriangle}\overline{Q_{2\blacktriangle}}+Q_{1\blacktriangledown}\overline{Q_{2\blacktriangledown}}$ is sesquilinear, positive definite, of Gram matrix $I_2$ and of real signature $(4,0)$; it gives the Euclidean norm and, with the complex structure, the decomposition $H=g-i\Omega$ into the metric and the Kähler form. The complex bilinear form $B(Q_1,Q_2)=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown}$ is symmetric, nondegenerate and of Gram matrix $I_2$; its isotropic set is the union of the two complex lines $Q_{\blacktriangle}=\pm iQ_{\blacktriangledown}$, and in the holomorphic coordinates $u(Q)=Q_{\blacktriangle}+iQ_{\blacktriangledown}$, $v(Q)=Q_{\blacktriangle}-iQ_{\blacktriangledown}$ it is the product $B=uv$. The holomorphic symplectic form $\omega(Q_1,Q_2)=Q_{1\blacktriangle}Q_{2\blacktriangledown}-Q_{1\blacktriangledown}Q_{2\blacktriangle}$ is alternating, nondegenerate and of Gram matrix $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$; it vanishes on every complex line, so the complex lines are its Lagrangian subspaces, and its square is zero while $\omega\wedge\overline{\omega}=2\Omega^2$.

The three are related by $H(Q_1,Q_2)=B(Q_1,\overline{Q}_2)$, by the Lagrange identity $B(Q_1,Q_2)^2+\omega(Q_1,Q_2)^2=B(Q_1,Q_1)B(Q_2,Q_2)$, and by their normal forms in the coordinates $u,v$. The distinction between $\operatorname{Im}H$ and $\omega$ is the central one: $\operatorname{Im}H$ is real, of type $(1,1)$, invariant under $J$, nondegenerate on every complex line and equal to $-\Omega$; $\omega$ is complex, of type $(2,0)$, anti-invariant under $J$, zero on every complex line and related to $\Omega$ only by the quadratic identity $\omega\wedge\overline{\omega}=2\Omega^2$. The Kähler form is $\Omega=-\operatorname{Im}H$, never $\omega$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $H(Q_1,Q_2)=Q_{1\blacktriangle}\overline{Q_{2\blacktriangle}}+Q_{1\blacktriangledown}\overline{Q_{2\blacktriangledown}}$ | the Hermitian form, Gram matrix $I_2$, signature $(4,0)$ |
| $g=\operatorname{Re}H$ | the Euclidean metric |
| $\Omega=-\operatorname{Im}H=dq_{\blacktriangle}\wedge dq'_{\blacktriangle}+dq_{\blacktriangledown}\wedge dq'_{\blacktriangledown}$ | the Kähler form, positive on the complex lines |
| $B(Q_1,Q_2)=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown}$ | the complex bilinear symmetric form, Gram matrix $I_2$ |
| $L_\pm=\{Q:Q_{\blacktriangle}=\pm iQ_{\blacktriangledown}\}$ | the two isotropic lines of $B$ |
| $u(Q)=Q_{\blacktriangle}+iQ_{\blacktriangledown}$, $v(Q)=Q_{\blacktriangle}-iQ_{\blacktriangledown}$ | the holomorphic coordinates in which $B=uv$ |
| $\omega(Q_1,Q_2)=Q_{1\blacktriangle}Q_{2\blacktriangledown}-Q_{1\blacktriangledown}Q_{2\blacktriangle}=dQ_{\blacktriangle}\wedge dQ_{\blacktriangledown}$ | the holomorphic symplectic form, Gram matrix $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ |
| $\omega\wedge\overline{\omega}=2\Omega^2$ | the relation between the holomorphic and the Kähler forms |

## Further Reading

- [Complex Two-Space](the-complex-two-space.html), the previous article, for the definitions of the forms and the space.
- [The Realification of $\mathbb{C}^2$](the-realification-of-the-complex-two-space.html), for the real and imaginary parts, the signatures and the dictionary.
- [The Subspaces of $\mathbb{C}^2$](the-subspaces-of-the-complex-two-space.html), for the isotropic lines, the Lagrangian lines and the Lagrangian planes.
- [The Isotropic Cone of the Bilinear Form on $\mathbb{C}^2$](the-isotropic-cone-of-the-bilinear-form.html), for the cone as a real object and its image in $\mathbb{CP}^1$.
- [The Flat Kähler Structure of $\mathbb{C}^2$](the-flat-kahler-structure-of-the-complex-two-space.html), for the metric, the Kähler form and the isometries.
- [The Classical Groups of $\mathbb{C}^2$](the-classical-groups-of-the-complex-two-space.html), for the groups that preserve each form.
- [Bilinear Forms](bilinear-forms.html), for the general theory of symmetric and alternating forms.
- [The Sesquilinear Structure of the Endomorphism Algebra](the-sesquilinear-structure-of-the-endomorphism-algebra.html), for the general theory of Hermitian forms.
