# __The Krein Gram Matrix and the Restrictions of the Form__

## Introduction

The general quaternionic sesquilinear form $\langle\tilde{Q}',\tilde{Q}\rangle_{\natural*}=\sum_{\mu}\varepsilon_{\mu}\bar Q_{\mu}Q'_{\mu}$ of this article is a general plain sesquilinear form of signature $(1,3)$ over $\mathbb{C}$ (respectively $(2,6)$ over $\mathbb{R}$), and its coefficients are the four signs $\varepsilon=(1,-1,-1,-1)$. This article collects the matrix side of that form: its **Gram matrix** in the coefficient basis, which is the sign matrix $E$ itself; the changes of basis that make the form canonical; the **Gram matrices and signatures of its restrictions** to the six distinguished subspaces of *Introduction to the Six Subspaces*; the orthogonality pattern of those restrictions; and the discriminant. The article is the matrix companion of the two articles of the same layer, *Krein Orthogonality and the Fundamental Decomposition* and *The Isotropic Structure of the General Quaternionic Sesqualgebra*, and it fixes the conventions for all three.

**Conventions.** $e_0=1$, $e_k^{2}=-e_0$, central scalar imaginary $i$, $\mathrm{Sc}$ the scalar part, $E=\mathrm{diag}(1,-1,-1,-1)$, and $\Phi$ the $2\times2$ matrix representation of *Biquaternion 2×2 Matrix Element Representation*, so that $\mathrm{Sc}(\tilde R\tilde S)=\tfrac12\operatorname{Tr}(\Phi(\tilde R)\Phi(\tilde S))$ and $\Phi(\tilde{Q}^{\natural})=\operatorname{adj}\Phi(\tilde{Q})$.

## The Gram Matrix in the Coefficient Basis

**Definition.** The **Gram matrix** of the general quaternionic sesquilinear form in the basis $e_0,e_1,e_2,e_3$ is $G_{\mu\nu}=\langle e_{\nu},e_{\mu}\rangle_{\natural*}$.

**Theorem (the Gram matrix is the sign matrix).** In the coefficient basis

$$
G=\mathrm{diag}(1,-1,-1,-1)=E ,
$$

so the diagonal entries are $+1,-1,-1,-1$, the off-diagonal entries vanish, and $\det G=-1$. In the real basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ of $\mathbb{B}_{\mathbb{R}}$ the Gram matrix is

$$
G_{\mathbb{R}}=\mathrm{diag}(1,-1,-1,-1,\,1,-1,-1,-1),
$$

of signature $(2,6)$.

**Proof.** $\langle e_{\nu},e_{\mu}\rangle_{\natural*}=\sum_{\lambda}\varepsilon_{\lambda}\overline{(e_{\mu})_{\lambda}}(e_{\nu})_{\lambda}=\varepsilon_{\mu}\delta_{\mu\nu}$: the units are orthogonal and each has its own sign. The determinant is $\varepsilon_0\varepsilon_1\varepsilon_2\varepsilon_3=-1$. In the real basis the coefficient $i$ contributes $|i|^{2}=1$ to every entry, so the Gram matrix repeats the block $E$ on the two coefficient blocks, whence the signature $(2+0,\,6)$ by counting the signs.

**Remark (the three Gram matrices).** The three pairings of *The Four Pairings of the Biquaternion Algebra* have Gram matrices $\mathrm{I}_4$ (bilinear), $\mathrm{I}_4$ (Hermitian) and $E$ (Krein): the general quaternionic sesquilinear form is the only one of the three whose coefficient basis is already orthogonal with signs. The matrix $E$ is also the Gram matrix of the product form $\mathrm{Sc}(\tilde{P}\tilde{Q})$, and it is the fundamental symmetry of the next article written in the coefficient basis.

## The Krein Form in the Matrix Representation

**Proposition (the form as a matrix trace).** For all biquaternions,

$$
\langle\tilde{Q}',\tilde{Q}\rangle_{\natural*}=\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\Phi(\tilde{Q})^{\dagger}\,\Phi(\tilde{Q}')\bigr)
=\tfrac12\operatorname{Tr}\bigl(\Phi(\tilde{Q}^{\natural})^{\dagger}\Phi(\tilde{Q}')\bigr),
$$

where $\dagger$ is the conjugate transpose in the matrix algebra.

**Proof.** $\langle\tilde{Q}',\tilde{Q}\rangle_{\natural*}=\mathrm{Sc}(\bar{\tilde{Q}}\tilde{Q}')=\mathrm{Sc}\bigl((\tilde{Q}^{\natural})^{*}\tilde{Q}'\bigr)$, because $(\tilde{Q}^{\natural})^{*}=\overline{\tilde{Q}}$; the trace identity $\mathrm{Sc}(\tilde R\tilde S)=\tfrac12\operatorname{Tr}(\Phi(\tilde R)\Phi(\tilde S))$ of *The Matrix Representation and the Biquaternion Dynamics* then gives the result, and $\Phi(\tilde{Q}^{\natural})=\operatorname{adj}\Phi(\tilde{Q})$ with $\Phi$ a $*$-homomorphism gives the second form.

**Corollary (the three trace expressions).** The bilinear form, the general plain sesquilinear form and the general quaternionic sesquilinear form are the three pairings

$$
\tfrac12\operatorname{Tr}\bigl(\Phi(\tilde P)\operatorname{adj}\Phi(\tilde Q)\bigr),
\qquad
\tfrac12\operatorname{Tr}\bigl(\Phi(\tilde P)^{\dagger}\Phi(\tilde Q)\bigr),
\qquad
\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\Phi(\tilde P)^{\dagger}\Phi(\tilde Q)\bigr),
$$

so that each pairing is a Hilbert–Schmidt pairing of $\Phi(\tilde P)$ with $\Phi(\tilde Q)$, preceded by adjugation for the first and by adjugation of the conjugate transpose for the third.

## The Canonical Basis and Sylvester's Law

**Definition.** A basis is **orthogonal** for the general quaternionic sesquilinear form when $\langle u_k,u_j\rangle_{\natural*}=0$ for $j\neq k$, and **orthonormal** when in addition each $\langle u_j,u_j\rangle_{\natural*}=\pm1$. A subspace $\mathbb{W}$ is **positive definite** when $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}>0$ for its nonzero elements, **negative definite** when $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}<0$, and **definite** when it is one of the two.

**Theorem (Sylvester).** Every basis can be replaced by an orthonormal one, and the numbers $p$ of $+1$ and $q$ of $-1$ are invariants of the form: over $\mathbb{C}$, $(p,q)=(1,3)$; over $\mathbb{R}$, $(p,q)=(2,6)$. The coefficient basis is already orthonormal with $p$ entries $+1$ and $q$ entries $-1$, and the maximal positive definite subspaces are the lines $\mathbb{C}(e_0+\tilde V)$ with $\|\tilde V\|_E<1$ over $\mathbb{C}$ and the real planes $\mathrm{span}_{\mathbb{R}}\{e_0+\tilde V,i(e_0+\tilde V)\}$ of the same form over $\mathbb{R}$, of dimensions $p$.

**Proof.** Diagonalising by congruence and then scaling each basis vector to have square $\pm1$ gives an orthonormal basis, and inertia is invariant by Sylvester's law (*Quadratic Forms and Polarisation*, §*Sylvester's Law of Inertia*). For the maximality, a positive definite subspace meets the maximal negative definite subspace $\mathbb{V}_{\mathbb{B}}$ only at $0$, so its complex dimension is at most the codimension $1$ of $\mathbb{V}_{\mathbb{B}}$; the centre $\mathbb{C}e_0$ achieves the bound, and every line $\mathbb{C}(e_0+\tilde V)$ with $\|\tilde V\|_E<1$ is another maximal positive definite subspace (*The Fundamental Symmetry of the Biquaternion Algebra*). Over $\mathbb{R}$ the maximal positive definite subspaces are the real planes $\mathrm{span}_{\mathbb{R}}\{e_0+\tilde V,i(e_0+\tilde V)\}$ with $\|\tilde V\|_E<1$, of which $\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$ is the member $\tilde V=0$.

## The Restrictions to the Six Subspaces

The six subspaces are defined in *Introduction to the Six Subspaces*: the **centre** $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$, the **vector subspace** $\mathbb{V}_{\mathbb{B}}=\mathrm{span}_{\mathbb{C}}\{e_1,e_2,e_3\}$, the **quaternion subspace** $\mathbb{H}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,e_1,e_2,e_3\}$, the **anti-quaternion subspace** $i\mathbb{H}_{\mathbb{B}}$, the **Hermitian subspace** $\mathbb{M}_{+}=\{\tilde{Q}:\tilde{Q}^{*}=\tilde{Q}\}$, and the **anti-Hermitian subspace** $\mathbb{M}_{-}=\{\tilde{Q}:\tilde{Q}^{*}=-\tilde{Q}\}$.

**Theorem (the restrictions).** With $Q_{\mu}=q_{\mu}+iq'_{\mu}$ the general quaternionic sesquilinear form restricts as follows.

| subspace | real dimension | $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}$ | signature |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $2$ | $q_0^2+(q'_0)^2$ | $(2,0)$ |
| $\mathbb{V}_{\mathbb{B}}$ | $6$ | $-\sum_{k}\bigl(q_k^2+(q'_k)^2\bigr)$ | $(0,6)$ |
| $\mathbb{H}_{\mathbb{B}}$ | $4$ | $q_0^2-q_1^2-q_2^2-q_3^2$ | $(1,3)$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $4$ | $(q'_0)^2-(q'_1)^2-(q'_2)^2-(q'_3)^2$ | $(1,3)$ |
| $\mathbb{M}_{+}$ | $4$ | $q_0^2-(q'_1)^2-(q'_2)^2-(q'_3)^2$ | $(1,3)$ |
| $\mathbb{M}_{-}$ | $4$ | $(q'_0)^2-q_1^2-q_2^2-q_3^2$ | $(1,3)$ |

**Proof.** The centre and the vector subspace are spanned by $e_0,ie_0$ and by $e_k,ie_k$; there $\langle e_{\mu},e_{\mu}\rangle_{\natural*}=\varepsilon_{\mu}$ and $\langle ie_{\mu},ie_{\mu}\rangle_{\natural*}=\varepsilon_{\mu}$, which gives $\pm1$ on each basis vector and the first two rows. A real quaternion has $Q_{\mu}=q_{\mu}$, a purely imaginary one has $Q_{\mu}=iq'_{\mu}$; on the Hermitian subspace $Q_0=q_0$ and $Q_k=iq'_k$, on the anti-Hermitian subspace $Q_0=iq'_0$ and $Q_k=q_k$; substituting $\varepsilon$ in $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=\sum_{\mu}\varepsilon_{\mu}|Q_{\mu}|^{2}$ gives the last four rows.

**Corollary (the common signature of the four (1,3) subspaces).** The quaternion subspace, the anti-quaternion subspace and the two sectors carry the same signature $(1,3)$: each is a copy of Minkowski space, with the general quaternionic sesquilinear form as its Krein form. The two remaining subspaces are definite, the centre positive and the vector subspace negative.

**Remark (the general quaternionic sesquilinear form versus the norm on the same subspace).** The comparison with the restriction of the *norm* $N=\sum Q_{\mu}^{2}$, tabulated in *The Six Subspaces under the General Quaternionic Algebra of Biquaternions*, is instructive: on $\mathbb{H}_{\mathbb{B}}$ the norm is $N=\sum q_{\mu}^{2}$ of signature $(4,0)$ while the general quaternionic sesquilinear form is $\sum_{\mu}\varepsilon_{\mu}q_{\mu}^{2}$ of signature $(1,3)$; the two differ by the sign vector $\varepsilon$, which is exactly the difference between the bilinear and the Krein pairing. On the two sectors the norm is already of signature $(1,3)$ and $(3,1)$, and the general quaternionic sesquilinear form again differs by the sign of the vector part.

## The Real Forms of the Form

**Definition.** The **real forms** of the general quaternionic sesquilinear form are the four real four-dimensional subspaces on which the form is real-valued and symmetric: the **quaternion form** $\mathbb{H}_{\mathbb{B}}$, the **anti-quaternion form** $i\mathbb{H}_{\mathbb{B}}$, the **Hermitian form** $\mathbb{M}_{+}$ and the **anti-Hermitian form** $\mathbb{M}_{-}$.

**Theorem (the four real forms).** On each of the four subspaces the form restricts to a real symmetric bilinear form of signature $(1,3)$, the Krein form of the subspace; the four are exactly the four $(1,3)$ rows of the restriction table, and multiplication by $i$ exchanges them in the two pairs $\mathbb{H}_{\mathbb{B}}\leftrightarrow i\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_{+}\leftrightarrow\mathbb{M}_{-}$. Each carries isotropic elements, and inside a form of signature $(1,3)$ the maximal totally isotropic real dimension is $\min(1,3)=1$, so none of them contains a totally isotropic subspace of real dimension greater than one.

**Proof.** The four rows of the table are the four $(1,3)$ rows, and on each of them every coefficient pair $Q_\mu^{*}P_\mu$ is real, because the coefficients are either both real or both purely imaginary, so the form is real and symmetric; multiplication by $i$ multiplies the scalar coefficient of an element of $\mathbb{M}_{+}$ by $i$ and leaves the vector coefficients, exchanging the two sectors, and carries the quaternion subspace onto the anti-quaternion subspace; the index bound is $\min(p,q)$ for the signature $(1,3)$.

**Theorem (the real basis and the sign matrix).** In the real basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ of the realification $\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$ the entries of the form are

$$
\langle e_\mu,e_\nu\rangle_{\natural*}=\varepsilon_\mu\delta_{\mu\nu},\qquad
\langle e_\mu,ie_\nu\rangle_{\natural*}=i\varepsilon_\mu\delta_{\mu\nu},\qquad
\langle ie_\mu,ie_\nu\rangle_{\natural*}=\varepsilon_\mu\delta_{\mu\nu},
$$

the mixed entries are purely imaginary, and the realified Gram matrix is $\mathrm{diag}(1,-1,-1,-1,1,-1,-1,-1)$ of signature $(2,6)$.

**Proof.** Coefficient computation as in §*The Gram Matrix in the Coefficient Basis*, with $|i|^{2}=1$ contributing to the second block and the cross term $(1)^{*}(i)=i$ giving the mixed entries; a purely imaginary entry does not contribute to the real symmetric form read on the real basis, so the realified matrix is block diagonal with two copies of $\mathrm{diag}(1,-1,-1,-1)$.

**Corollary (the complex and the real signature, and the relation to $J$).** The algebra is the complexification of either of the two slices $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, and the complex form is the complexification of the real Krein form on a slice: complexifying a real form of signature $(1,3)$ gives the complex form of signature $(1,3)$, the coefficient signature of §*The Gram Matrix in the Coefficient Basis*, while realifying the same complex form of complex dimension four gives the real form of signature $(2,6)$. In the real basis the fundamental symmetry $J={}^{\natural}$ is diagonal, fixing the centre and reversing the vector subspace, and the form is the definite form twisted by $J$,

$$
\langle\tilde P,\tilde Q\rangle_{\natural*}=\langle\tilde P,J\tilde Q\rangle_{*},
$$

the bridge identity of *The Fundamental Symmetry of the Biquaternion Algebra*.

**Proof.** The tensor product $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}_{\mathbb{B}}$ and the complexification statement are the theorem; $J$ multiplies the coefficient of $e_\mu$ by $\varepsilon_\mu$, hence is diagonal in the real basis and reads as the sign matrix on the diagonal; the bridge is the identity of the fundamental-symmetry article.

**Remark (what the real forms are not).** The four real forms are not four more of the six subspaces: the centre $\mathbb{C}_{\mathbb{B}}$ and the vector subspace $\mathbb{V}_{\mathbb{B}}$ are complex subspaces, of signatures $(2,0)$ and $(0,6)$, and are not real forms. The four real forms are the four $(1,3)$ slices, and their two pairs are exchanged by multiplication by $i$, while the centre and the vector subspace are exchanged by the fundamental symmetry $J$.

## Orthogonality of the Distinctions

**Definition.** Two subspaces are **Krein-orthogonal**, written $\mathbb{W}\perp_{K}\mathbb{U}$, when $\langle\tilde{T},\tilde{Q}\rangle_{\natural*}=0$ for all $\tilde{Q}\in\mathbb{W}$ and $\tilde{T}\in\mathbb{U}$. The **Krein-orthogonal complement** is $\mathbb{W}^{\perp_{K}}=\{\tilde{T}:\langle\tilde{T},\tilde{Q}\rangle_{\natural*}=0\ \forall\tilde{Q}\in\mathbb{W}\}$.

**Theorem (the orthogonal splitting).** The general quaternionic sesquilinear form splits the algebra as an orthogonal sum

$$
\mathbb{B}=\mathbb{C}_{\mathbb{B}}\perp_{K}\mathbb{V}_{\mathbb{B}},
\qquad
\mathbb{C}_{\mathbb{B}}^{\perp_{K}}=\mathbb{V}_{\mathbb{B}},\qquad
\mathbb{V}_{\mathbb{B}}^{\perp_{K}}=\mathbb{C}_{\mathbb{B}},
$$

and the four subspaces of signature $(1,3)$ are **non-degenerate**, $\mathbb{W}\cap\mathbb{W}^{\perp_{K}}=\{0\}$, and are pairwise **not** Krein-orthogonal.

**Proof.** $\langle e_k,e_0\rangle_{\natural*}=0$ and $\langle e_k,ie_0\rangle_{\natural*}=0$ give the splitting and the two complements. In coefficients $\langle\tilde{T},e_{\mu}\rangle_{\natural*}=\varepsilon_{\mu}T_{\mu}$ and $\langle\tilde{T},ie_{\mu}\rangle_{\natural*}=-i\varepsilon_{\mu}T_{\mu}$, so an element of one of the four subspaces that is Krein-orthogonal to that subspace has all its coefficients zero, hence vanishes: those four subspaces are non-degenerate. For the failure of mutual orthogonality, $\langle ie_0,e_0\rangle_{\natural*}=i\neq0$ shows that $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ are not orthogonal, and $\langle e_0,ie_0\rangle_{\natural*}=-i\neq0$ does the same for $\mathbb{M}_{+}$ and $\mathbb{M}_{-}$.

## The Discriminant

**Definition.** The **discriminant** of a non-degenerate symmetric or general plain sesquilinear form of rank $n$ and Gram matrix $G$ is the class of $(-1)^{n(n-1)/2}\det G$ modulo squares of the field.

**Theorem (the discriminant of the form and of its restrictions).** Over $\mathbb{R}$ the discriminant of the general quaternionic sesquilinear form, and of each of the six restrictions, is the class of $-1$; over $\mathbb{C}$ every one of them has trivial discriminant, since $-1=(i)^{2}$ is a square.

**Proof.** For the form itself $n=4$ and $\det G=-1$, so $(-1)^{6}(-1)=-1$. The centre has $n=2$ and $\det=1$, giving $(-1)^{1}\cdot1=-1$; the vector subspace has $n=6$ and $\det(-I_6)=+1$, giving $(-1)^{15}\cdot1=-1$; each $(1,3)$ subspace has Gram matrix $\operatorname{diag}(1,-1,-1,-1)$ of determinant $-1$, giving $-1$. Over $\mathbb{C}$ the class of $-1$ is the class of $1$ because $i^{2}=-1$.

**Remark.** The invariance of the sign is not accidental: the six restrictions are the forms of a Minkowski plane, a six-dimensional definite space and four copies of Minkowski space, and each of these has discriminant $-1$ over $\mathbb{R}$. The unimodularity of the coefficient lattice, $\det G=\pm1$, is the same statement read on the units.

## Worked Examples

**A positive vector.** $\tilde{Q}=e_0+2ie_0$: $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=|1|^{2}+|2|^{2}=5>0$, in the centre, one of the maximal positive definite subspaces over $\mathbb{C}$.

**A negative vector.** $\tilde{Q}=e_1+e_2$: $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=-1-1=-2<0$, in the vector subspace.

**A Minkowski causal vector.** $\tilde{Q}=e_0+\tfrac12e_1$, a real quaternion: $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=1-\tfrac14=\tfrac34>0$, timelike in the $(1,3)$ slice.

**A null element of the norm only.** $\tilde{Q}=e_1+ie_2$: $\langle\tilde{Q},\,\tilde{Q}\rangle_{\natural*}=-2$ while $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=0$; the element is a zero divisor and definite for the general quaternionic sesquilinear form.

**A null element of the general quaternionic sesquilinear form only.** $\tilde{Q}=e_0+e_1$: $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=0$ while $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=2$.

**A real quaternion of each sign.** $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}$ on $\mathbb{H}_{\mathbb{B}}$ is the Krein form: positive on $e_0$, negative on $e_1$, null on $e_0+e_1$ — the three causal types of the Minkowski slice in one basis.

**The two readings of one vector.** $\tilde{Q}=e_1$: $\langle\tilde{Q},\tilde{Q}\rangle_{*}=1>0$ while $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=-1$; the vector is positive in the algebra reading and negative in the form reading, the explicit divergence of the two forms on the same subspace.

**A real form.** $\tilde{Q}=e_0+\tfrac12e_1$ in the slice $\mathbb{H}_{\mathbb{B}}$: $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=1-\tfrac14=\tfrac34$, real as the theorem on the real forms requires, and positive.

**A purely imaginary slice.** $\tilde{Q}=i(e_0+e_1)$ in $i\mathbb{H}_{\mathbb{B}}$: $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=1-1=0$, a null vector of the second real form as $e_0+e_1$ is one of the first.

## Summary

In the coefficient basis the general quaternionic sesquilinear form has the Gram matrix $G=\mathrm{diag}(1,-1,-1,-1)=E$, of determinant $-1$; in the real basis it is $\mathrm{diag}(1,-1,-1,-1,1,-1,-1,-1)$ of signature $(2,6)$. In the $2\times2$ matrix representation the form is the Hilbert–Schmidt pairing $\langle\tilde{Q}',\tilde{Q}\rangle_{\natural*}=\tfrac12\operatorname{Tr}(\operatorname{adj}\Phi(\tilde{Q})^{\dagger}\Phi(\tilde{Q}'))$, the adjugate and the conjugate transpose marking the Krein case among the three pairings. Sylvester's law gives $(p,q)=(1,3)$ over $\mathbb{C}$ and $(2,6)$ over $\mathbb{R}$, the coefficient basis already being orthonormal. The restrictions to the six subspaces are the positive definite centre $(2,0)$, the negative definite vector subspace $(0,6)$, and four copies of Minkowski space $(1,3)$ on the quaternion subspace, the anti-quaternion subspace and the two sectors; the centre and the vector subspace are mutual Krein-orthogonal complements, while the four $(1,3)$ subspaces are non-degenerate and not mutually orthogonal. The discriminant is the class of $-1$ over $\mathbb{R}$ for the form and for each restriction, and is trivial over $\mathbb{C}$. The same six subspaces carry a second form reading, the positive definite general plain sesquilinear form, positive definite on every one of them, so that four of the six are indefinite for the quaternion form and definite for the complex one; the comparison of the two readings is *The Six Subspaces and the Four General Products*, §*The Two Splits and the Two Readings*. The four real forms — the quaternion, anti-quaternion, Hermitian and anti-Hermitian subspaces — are the slices on which the form is real, each of signature $(1,3)$; in the real basis the mixed entries are purely imaginary, the realified Gram matrix is $\mathrm{diag}(1,-1,-1,-1,1,-1,-1,-1)$, and $(1,3)$ and $(2,6)$ are the complex and the real signature of one form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G=E=\mathrm{diag}(1,-1,-1,-1)$ | The Gram matrix of the general quaternionic sesquilinear form in the coefficient basis |
| $G_{\mathbb{R}}=\mathrm{diag}(1,-1,-1,-1,1,-1,-1,-1)$ | The Gram matrix over $\mathbb{R}$; signature $(2,6)$ |
| $\tfrac12\operatorname{Tr}(\operatorname{adj}\Phi(\tilde{Q})^{\dagger}\Phi(\tilde{Q}'))$ | The general quaternionic sesquilinear form in the $2\times2$ matrix representation |
| $(p,q)=(1,3)$ over $\mathbb{C}$, $(2,6)$ over $\mathbb{R}$ | The inertia (Sylvester) |
| $\mathbb{C}_{\mathbb{B}}$, $\mathbb{V}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_{+}$, $\mathbb{M}_{-}$ | The six subspaces and their restrictions |
| $\mathbb{W}^{\perp_{K}}$ | The Krein-orthogonal complement |
| $(-1)^{n(n-1)/2}\det G$ | The discriminant; the class of $-1$ over $\mathbb{R}$ |
| $\langle\tilde P,\tilde Q\rangle_{*}=\sum_\mu Q_\mu^{*}P_\mu$ | The general plain sesquilinear form, the definite companion of the Krein form |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_{+}$, $\mathbb{M}_{-}$ | The four real forms, each of signature $(1,3)$ |

## Further Reading

- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the three Gram matrices compared, and for the four pairings on the six subspaces
- *The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Representation* (`articles_maths/the-general-quaternionic-sesqualgebra-in-the-2x2-matrix-representation.md`), for the adjugated trace identities used here
- *The Six Subspaces under the General Quaternionic Algebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-quaternionic-algebra-of-biquaternions.md`), for the restriction of the norm to the same six subspaces
- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the definitions and dimensions of the six subspaces
- *Comparison of the Six Subspaces* (`articles_maths/comparison-of-the-six-subspaces.md`), for the definitions and the coordinate blocks of the six subspaces
- *The Six Subspaces under the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the restrictions as subspaces, their null cones and their automorphism groups
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the positive definite general plain sesquilinear form
- *Krein Orthogonality and the Fundamental Decomposition* (`articles_maths/krein-orthogonality-and-the-fundamental-decomposition.md`) and *The Isotropic Structure of the General Quaternionic Sesqualgebra* (`articles_maths/the-isotropic-structure-of-the-general-quaternionic-sesqualgebra.md`), for the two companion articles of this layer
- *Quadratic Forms and Polarisation* (`articles_maths/quadratic-forms-and-polarisation.md`), for Sylvester's law, congruence and the discriminant
