# __Introduction to the Peirce Basis over C__

## Introduction

The carrier of complex dimension $2$ is not a subspace of the algebra: it is a **basis**. Take a unit real axis, form the square root of the unit at that axis, split it into the two complementary idempotents $e$ and $f$, and read off the four Peirce corners. Each corner is a complex line. The four lines together span the algebra, and in that basis the multiplication is the multiplication of matrix units:

$$
e,\ \nu,\ \nu',\ f\qquad\leftrightarrow\qquad E_{11},\ E_{21},\ E_{12},\ E_{22}.
$$

That identification is the content of the article. It is a statement about the algebra itself, and it is what makes the basis the carrier: every other structure — the norm, the spectrum, the two left ideals, the two right ideals, the two rulings of the null quadric, the conjugation — is read off the same four symbols.

The construction has an input and no convention beyond one. The input is a unit real axis $\vec u$; the convention is the sign of the square root of the unit. Nothing else is chosen, and the axis is a parameter of a family, not a datum of the algebra.

The two summands of the algebra that the basis displays are the carriers of the type in the sense of *The Carriers of the Biquaternion Algebra*: each has complex dimension $2$, each is a minimal left ideal, and the algebra is their direct sum. The basis records them and their interaction at once.

The two companion articles are *The Peirce Basis and Norm Regularity* and *The Peirce Basis and Spectral Regularity*. Nothing below is a statement of physics.

## Conventions

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the units $e_t,\vec e_x,\vec e_y,\vec e_z$, with

$$
e_t^{2}=e_t,\qquad \vec e_k^{2}=-e_t,\qquad \vec e_x\vec e_y=\vec e_z,\qquad \vec e_y\vec e_z=\vec e_x,\qquad \vec e_z\vec e_x=\vec e_y,
$$

and with complex coefficients. An element is $\tilde Q=Q_te_t+\vec Q$ with $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$. The **natural conjugation** is $\tilde Q^{\natural}=Q_t-\vec Q$, the **bar** is conjugation of the complex coefficients, and the **Hermitian conjugation** is

$$
\tilde Q^{*}=\overline{\tilde Q^{\natural}}=\bar Q_t-\bar{\vec Q}.
$$

The units satisfy $e_t^{*}=e_t$ and $\vec e_k^{*}=-\vec e_k$. The algebra is $\mathbb{C}$-central: its centre is $\mathbb{C}e_t$. The matrix model sends $e_t\mapsto\mathrm I_2$ and $\vec e_k\mapsto-i\sigma_k$, so that $\mathbb{B}\cong M_2(\mathbb{C})$ as a complex algebra; the isomorphism is used for reading, not for defining.

Throughout, $\vec u$ is a unit vector of $\mathbb{R}^{3}$ and $\vec u\cdot\vec e=u_x\vec e_x+u_y\vec e_y+u_z\vec e_z$.

## The Square Root of the Unit

**Definition (the unity at an axis).** For a unit real $\vec u$ put

$$
J(\vec u)=i\,\vec u\cdot\vec e .
$$

**Theorem (it squares to the unit).** $J^{2}=e_t$.

*Proof.* Since $\vec u$ is real, $\vec u\cdot\vec e$ is a real pure quaternion of squared length $\lvert\vec u\rvert^{2}=1$. A real pure quaternion satisfies $V^{2}=-\lvert V\rvert^{2}e_t$ by the rule $\vec e_j\vec e_k=-\delta_{jk}e_t+\varepsilon_{jkl}\vec e_l$. Hence $(\vec u\cdot\vec e)^{2}=-e_t$, and $J^{2}=i^{2}(-e_t)=e_t$.

**Corollary (the two roots).** The solutions of $X^{2}=e_t$ inside the span of $e_t$ and $J$ are $J$ and $-J$, and no other element of that plane squares to the unit.

*Proof.* Write $X=\alpha e_t+\beta J$ with $\alpha,\beta\in\mathbb{C}$. Then $X^{2}=(\alpha^{2}+\beta^{2})e_t+2\alpha\beta J$, which equals $e_t$ exactly when $\alpha\beta=0$ and $\alpha^{2}+\beta^{2}=1$. The two solutions are $\pm e_t$ and $\pm J$.

The sign is the only choice. It is not a choice of axis: it is the choice of which of the two roots is called $J$, and it exchanges the two idempotents below.

**Remark (why the root is not central).** $J$ anticommutes with every real pure quaternion orthogonal to $\vec u$: if $\vec w\perp\vec u$ is real and of length one, then $(\vec u\cdot\vec e)(\vec w\cdot\vec e)=-(\vec w\cdot\vec e)(\vec u\cdot\vec e)$, hence $J\vec w\cdot\vec e=-\vec w\cdot\vec e\,J$. A central element would commute. The square root of the unit therefore exists only off the centre, and the algebra is not a product of two copies of $\mathbb{C}$ in any central way.

## The Complementary Pair

**Definition (the two idempotents).**

$$
e=\tfrac12(e_t+J),\qquad f=\tfrac12(e_t-J).
$$

**Theorem (a complete orthogonal pair of projections).**

$$
e^{2}=e,\qquad f^{2}=f,\qquad ef=fe=0,\qquad e+f=e_t .
$$

*Proof.* $e^{2}=\tfrac14(e_t+2J+J^{2})=\tfrac14(2e_t+2J)=e$, and the same with $-J$. The product is $ef=\tfrac14(e_t-J^{2})=0$, and the sum is $e_t$.

**Theorem (they are Hermitian).** $e^{*}=e$ and $f^{*}=f$.

*Proof.* $J^{\natural}=-J$ and $J$ has purely imaginary coefficients, so $\bar J=J$; hence $J^{*}=\overline{J^{\natural}}=\overline{-J}=-J$. Then $e^{*}=\tfrac12(e_t-J)=f$... and $\overline{e}=\tfrac12(e_t+\bar J)=e$, so $e^{*}=\overline{e^{\natural}}=\overline{f}=\tfrac12(e_t+J)=e$. The same computation gives $f^{*}=f$.

**Remark (the pair is not canonical).** The pair depends on the axis through $J$, and the two elements are exchanged by $J\mapsto-J$, that is by $\vec u\mapsto-\vec u$. The unordered pair $\{e,f\}$ is therefore a function of the axis up to sign, and the ordered pair is a function of the axis. This is the only parameter of the construction.

## The Peirce Decomposition

**Theorem (the decomposition into four corners).** With $e,f$ as above,

$$
\mathbb{B}=\mathbb{B}_{ee}\oplus\mathbb{B}_{ef}\oplus\mathbb{B}_{fe}\oplus\mathbb{B}_{ff},\qquad
\mathbb{B}_{ij}=e_i\mathbb{B}e_j,
$$

where $e_1=e$ and $e_2=f$, and each corner is a complex line.

*Proof.* For any $X$, the identity

$$
X=eXe+eXf+fXe+fXf
$$

holds, because $e+f=e_t$ and $e_t$ is the unit; so the four corners span. For the directness, suppose $X$ lies in two corners, say $\mathbb{B}_{ee}$ and $\mathbb{B}_{ef}$. Then $Xe=X$ and $Xf=X$, so $X=X(e+f)=Xe+Xf=2X$, hence $X=0$. For the dimension, each corner is an $e_i\mathbb{B}e_j$ with $e_i,e_j$ rank-one projections in the matrix model, so it consists of matrices with a single possibly non-zero entry and has complex dimension $1$; and $1+1+1+1=4=\dim_{\mathbb{C}}\mathbb{B}$.

**Corollary (the corner membership rule).** If $X\in\mathbb{B}_{ij}$ then

$$
e_iX=X=Xe_j,\qquad e_jX=0=Xe_i\ (i\neq j).
$$

*Proof.* $X=e_iXe_j$, so $e_iX=e_i^{2}Xe_j=X$ and $Xe_j=e_iXe_j^{2}=X$; and $e_jX=e_je_iXe_j=0$ because $e_je_i=0$.

## The Basis

**Definition (the Peirce basis).** At the axis $\vec u=\vec e_z$ put

$$
e=\tfrac12(e_t+i\vec e_z),\qquad f=\tfrac12(e_t-i\vec e_z),\qquad \nu=\tfrac12(i\vec e_x+\vec e_y),\qquad \nu'=\tfrac12(i\vec e_x-\vec e_y).
$$

The four elements are the **Peirce basis** of $\mathbb{B}$ at that axis. The elements $\nu$ and $\nu'$ are the **companion nilpotents** of the axis.

**Theorem (corner membership).**

$$
e\in\mathbb{B}_{ee},\qquad \nu'\in\mathbb{B}_{ef},\qquad \nu\in\mathbb{B}_{fe},\qquad f\in\mathbb{B}_{ff}.
$$

*Proof.* Read the coordinates. The element $e=\tfrac12 e_t+\tfrac i2\vec e_z$ is fixed on the left by $e$ and on the right by $e$, and killed by $f$; a direct multiplication gives $e\,e\,e=e$ and $e\nu'e=\tfrac14(e_t+i\vec e_z)(i\vec e_x-\vec e_y)(e_t+i\vec e_z)=0$. The three remaining statements are the same computation with the roles permuted, and the matrix model gives them at once: the four elements are the four matrix units.

**Theorem (both nilpotents square to zero).**

$$
\nu^{2}=0,\qquad \nu'^{2}=0 .
$$

*Proof.* $\nu^{2}=\tfrac14\bigl(-\vec e_x^{2}+\vec e_y^{2}+i(\vec e_x\vec e_y+\vec e_y\vec e_x)\bigr)=\tfrac14(e_t-e_t+i(\vec e_z-\vec e_z))=0$, and the same with the sign of $\vec e_y$ changed.

**Theorem (the two mixed corners are dual).**

$$
\nu\nu'=f,\qquad \nu'\nu=e .
$$

*Proof.* $\nu\nu'=\tfrac14\bigl(-\vec e_x^{2}+\vec e_y^{2}-i\vec e_x\vec e_y+i\vec e_y\vec e_x\bigr)=\tfrac14\bigl(e_t-e_t-i\vec e_z-i\vec e_z\bigr)=-\tfrac i2\vec e_z$, and $\tfrac12(e_t-i\vec e_z)=f$ equals $-\tfrac i2\vec e_z+\tfrac12 e_t$, so the two agree. The second is the same computation with the sign of the cross terms reversed.

That identity is the whole point of the normalisation. The two nilpotents are not independent: each is the inverse of the other in the corner sense, and their products are the two idempotents.

**Theorem (the multiplication table).** The products of the basis elements are

| $\cdot$ | $e$ | $\nu$ | $\nu'$ | $f$ |
|---|---|---|---|---|
| $e$ | $e$ | $0$ | $\nu'$ | $0$ |
| $\nu$ | $\nu$ | $0$ | $f$ | $0$ |
| $\nu'$ | $0$ | $e$ | $0$ | $\nu'$ |
| $f$ | $0$ | $\nu$ | $0$ | $f$ |

*Proof.* Each entry is a product of two of the four elements, computed from the definitions; the corner rule gives the zeros, and the two identities above give the two entries $f$ and $e$. For instance $\nu e=f\nu e=\nu$ because $\nu\in\mathbb{B}_{fe}$, and $e\nu'=e\nu'f=\nu'$ because $\nu'\in\mathbb{B}_{ef}$.

**Corollary (the basis is the matrix-unit basis).** Under the matrix model the four elements are

$$
e=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
\nu=\begin{pmatrix}0&0\\1&0\end{pmatrix},\quad
\nu'=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
f=\begin{pmatrix}0&0\\0&1\end{pmatrix},
$$

and the table above is the table of matrix units, $E_{ij}E_{kl}=\delta_{jk}E_{il}$.

*Proof.* Substitute $e_t=\mathrm I_2$ and $\vec e_k=-i\sigma_k$ in the four definitions.

**Remark (the basis is a basis, and the table is the algebra).** The four elements are linearly independent, since the corner decomposition is direct and each contributes one line. The table is not a summary of the algebra: together with bilinearity it determines every product, so the algebra is the table. Reading a statement about the algebra in the Peirce basis is therefore reading it about a table of four symbols with sixteen entries.

## The Two Summands

**Definition (the summands).** $S_{+}=\mathbb{B}e$ and $S_{-}=\mathbb{B}f$.

**Theorem (the summands are the column spaces of the corners).**

$$
S_{+}=\mathbb{B}_{ee}\oplus\mathbb{B}_{fe}=\mathbb{C}e\oplus\mathbb{C}\nu,\qquad
S_{-}=\mathbb{B}_{ef}\oplus\mathbb{B}_{ff}=\mathbb{C}\nu'\oplus\mathbb{C}f,
$$

each of complex dimension $2$, with $S_{+}\cap S_{-}=0$ and $S_{+}+S_{-}=\mathbb{B}$.

*Proof.* $\mathbb{B}e=(\mathbb{B}_{ee}\oplus\mathbb{B}_{ef}\oplus\mathbb{B}_{fe}\oplus\mathbb{B}_{ff})e$; the second and fourth summands are killed on the right by $e$, so the first and the third remain. The same for $f$. The intersection is zero because the corner decomposition is direct, and the dimensions add to $4$.

**Theorem (the multiplication respects the pair).**

$$
S_{+}S_{+}\subseteq S_{+},\qquad S_{+}S_{-}\subseteq S_{-},\qquad S_{-}S_{+}\subseteq S_{+},\qquad S_{-}S_{-}\subseteq S_{-}.
$$

*Proof.* Read the table. $S_{+}$ is spanned by $e$ and $\nu$, and the products $e\cdot e=e$, $e\cdot\nu=0$, $\nu\cdot e=\nu$, $\nu\cdot\nu=0$ all lie in $S_{+}$. $S_{-}$ is spanned by $\nu'$ and $f$, and the products with a left factor in $S_{+}$ are $e\nu'=\nu'$, $ef=0$, $\nu\nu'=f$, $\nu f=0$, all in $S_{-}$. The two remaining rows are the same computation.

**Corollary (the left action is block diagonal).** For every $X\in\mathbb{B}$, left multiplication by $X$ preserves each summand. In the ordering $S_{+},S_{-}$ the matrix of $L_X$ is block diagonal.

**Corollary (each summand is a ring).** $(S_{+},+,\cdot)$ is a two-dimensional complex algebra with identity $e$ and with $\nu$ of square zero; it is the algebra of dual numbers $\mathbb{C}[\nu]/(\nu^{2})$. The same holds for $S_{-}$ with identity $f$ and generator $\nu'$.

*Proof.* The product of two elements of $S_{+}$ lies in $S_{+}$ by the theorem, $e$ acts as the identity on $S_{+}$ by the table, and $\nu^{2}=0$ by the nilpotence.

**Remark (why the basis is the carrier).** $S_{+}$ alone is a plane with no trace of $S_{-}$. The basis records both, and it records the two products $\nu\nu'=f$ and $\nu'\nu=e$ that couple them. A statement proved in the Peirce basis is therefore a statement about the pair, and it is available to both summands by the same symbols.

## The Four Corners and the Two Rulings

**Definition (the right summands).** $T_{+}=e\mathbb{B}=\mathbb{C}e\oplus\mathbb{C}\nu'$ and $T_{-}=f\mathbb{B}=\mathbb{C}\nu\oplus\mathbb{C}f$.

**Theorem (the corners give both rulings).** The two left summands and the two right summands are

$$
S_{+}=\mathbb{B}e=\mathbb{C}e\oplus\mathbb{C}\nu,\qquad T_{+}=e\mathbb{B}=\mathbb{C}e\oplus\mathbb{C}\nu',
$$

$$
S_{-}=\mathbb{B}f=\mathbb{C}\nu'\oplus\mathbb{C}f,\qquad T_{-}=f\mathbb{B}=\mathbb{C}\nu\oplus\mathbb{C}f,
$$

so the four corners are the four pairings of one left summand with one right summand, and the two bases of the algebra differ by the exchange of the two mixed corners.

*Proof.* $\mathbb{B}e$ keeps the corners whose right index is $e$, and $e\mathbb{B}$ keeps those whose left index is $e$.

**Corollary (the two rulings of the null quadric).** The family $S_{+}(\vec u)$ over the sphere and the family $T_{+}(\vec u)$ over the sphere are the two rulings, and the Peirce basis displays one plane of each ruling for each axis.

**Corollary (the intersection points).** $S_{+}\cap T_{+}=\mathbb{C}e$ and $S_{-}\cap T_{-}=\mathbb{C}f$, while $S_{+}\cap T_{-}=\mathbb{C}\nu$ and $S_{-}\cap T_{+}=\mathbb{C}\nu'$. Each of the four corners is the intersection of one plane of each ruling.

## The Conjugation

**Theorem (the conjugation on the basis).**

$$
e^{*}=e,\qquad f^{*}=f,\qquad \nu^{*}=\nu',\qquad \nu'^{*}=\nu .
$$

*Proof.* Apply $\tilde Q^{*}=\bar Q_t-\bar{\vec Q}$ to each element. For $e=\tfrac12(e_t+i\vec e_z)$: $\bar e=e$ and $\bar e^{\natural}=\tfrac12(e_t-i\vec e_z)=f$, so the two steps compose to $e$. For $\nu=\tfrac12(i\vec e_x+\vec e_y)$: $\bar\nu=\tfrac12(-i\vec e_x+\vec e_y)=-\nu'$, and its natural conjugate is $-\tfrac12(-i\vec e_x-\vec e_y)=\nu'$, so $\nu^{*}=\nu'$.

**Corollary (the conjugation swaps the two mixed corners and fixes the diagonal ones).** It acts as the identity on $\mathbb{B}_{ee}\oplus\mathbb{B}_{ff}$ and exchanges $\mathbb{B}_{ef}$ with $\mathbb{B}_{fe}$.

**Corollary (the involution is the transpose of the matrix model).** In the Peirce coordinates of §*The Basis* the map $*$ is

$$
\begin{pmatrix}a&c\\ b&d\end{pmatrix}\ \longmapsto\ \begin{pmatrix}\bar a&\bar b\\ \bar c&\bar d\end{pmatrix},
$$

that is, the conjugate transpose.

*Proof.* Read the table and conjugate the coefficients.

**Remark (the natural conjugation is not the transpose).** The map $\natural$ alone fixes $e$? It does not: $e^{\natural}=f$. The natural conjugation exchanges the two diagonal corners and fixes nothing on the diagonal, while $*$ fixes both. This is the difference between the two involutions read in the basis, and it is the reason $*$ is the one adapted to the Peirce coordinates.

## The Family of Bases

**Theorem (the family).** The assignment $\vec u\mapsto\{e(\vec u),f(\vec u)\}$ passes to a map from the real projective plane to the set of unordered pairs of complementary idempotents, and $\vec u\mapsto(e(\vec u),f(\vec u))$ from the sphere to the ordered pairs. Both maps are surjective and two-to-one in the first case, one-to-one up to the sign of the root in the second.

*Proof.* The axis enters only through $J=i\vec u\cdot\vec e$, and $J(-\vec u)=-J$ exchanges $e$ and $f$; conversely a pair $\{e,f\}$ determines $J=e-f$ and hence the axis up to sign. The order of the pair distinguishes $J$ from $-J$, that is the axis with its sign.

**Corollary (the basis is a section of a bundle over the sphere).** Every Peirce basis is obtained from the basis at $\vec e_z$ by conjugation with a unit real quaternion.

*Proof.* A unit real quaternion $u$ maps $\vec e_z$ to a real unit vector $\vec u$ by the adjoint action, and the adjoint action fixes $e_t$ and preserves the products, so it carries the pair of idempotents at $\vec e_z$ to the pair at $\vec u$.

## Reading the Two Summands

**Theorem (the complex dimension, and the type).** Each summand has complex dimension $2$ and real dimension $4$, both summands have the same dimension, and the number attached to the type is

$$
\frac{d-1}{2}=\frac{2-1}{2}=\frac12,\qquad d=\dim_{\mathbb{C}}S_{\pm}=2 .
$$

**Remark (the basis is not a choice of summand).** The Peirce decomposition produces the two summands together, and there is no way to produce one of them alone from the pair of idempotents: each corner belongs to one summand, and the two summands need the two idempotents. The carrier is therefore the pair, and the basis is its record.

## Summary

The construction starts from a unit real axis $\vec u$, forms $J=i\vec u\cdot\vec e$ with $J^{2}=e_t$, and splits it into the complementary Hermitian idempotents $e=\tfrac12(e_t+J)$ and $f=\tfrac12(e_t-J)$.

The Peirce decomposition of the algebra with respect to $e,f$ has four corners, each a complex line, and the four lines form a basis in which the multiplication is the multiplication of matrix units. At the axis $\vec e_z$ the basis is $e,\nu,\nu',f$, with $\nu,\nu'$ the companion nilpotents, $\nu^{2}=\nu'^{2}=0$, $\nu\nu'=f$ and $\nu'\nu=e$.

The multiplication table of the four elements is the algebra. It shows that $S_{+}=\mathbb{C}e\oplus\mathbb{C}\nu$ and $S_{-}=\mathbb{C}\nu'\oplus\mathbb{C}f$ are two-dimensional subalgebras with identities $e$ and $f$, that each is a left ideal, that the left action is block diagonal, and that the two are coupled by the products of the mixed corners.

The corners give both rulings of the null quadric at once: the left summands are $\mathbb{C}e\oplus\mathbb{C}\nu$ and $\mathbb{C}\nu'\oplus\mathbb{C}f$, and the right summands are the same two planes with the two mixed corners exchanged. The Hermitian conjugation fixes the diagonal corners and swaps the mixed ones, and in the Peirce coordinates it is the conjugate transpose.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, $M_2(\mathbb{C})$, complex dimension $4$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the units, $e_t^{2}=e_t$, $\vec e_k^{2}=-e_t$, $\vec e_x\vec e_y=\vec e_z$ |
| $\vec u$ | a unit vector of $\mathbb{R}^{3}$, the axis |
| $J=i\vec u\cdot\vec e$ | the square root of the unit at the axis, $J^{2}=e_t$ |
| $e,f$ | the complementary idempotents $\tfrac12(e_t\pm J)$ |
| $\mathbb{B}_{ij}=e_i\mathbb{B}e_j$ | the four Peirce corners, each a complex line |
| $\nu,\nu'$ | the companion nilpotents $\tfrac12(i\vec e_x\pm\vec e_y)$, $\nu^{2}=\nu'^{2}=0$ |
| $S_{\pm}$ | the left summands $\mathbb{B}e$ and $\mathbb{B}f$, of complex dimension $2$ |
| $T_{\pm}$ | the right summands $e\mathbb{B}$ and $f\mathbb{B}$ |
| $E_{ij}$ | the matrix units of $M_2(\mathbb{C})$ |
| ${}^{*}$ | the Hermitian conjugation $\bar\cdot\circ{}^{\natural}$ |

## Further Reading

- [The Peirce Basis and Norm Regularity](the-peirce-basis-and-norm-regularity.html), for the norm in the Peirce coordinates, where it becomes a determinant.
- [The Peirce Basis and Spectral Regularity](the-peirce-basis-and-spectral-regularity.html), for the spectrum and the degenerate locus in the same coordinates.
- [The Carriers of the Biquaternion Algebra](the-carriers-of-the-biquaternion-algebra.html), for the definition of a carrier and the three types.
- [The Minimal Left Ideals of the Biquaternion Algebra](the-minimal-left-ideals-of-the-biquaternion-algebra.html), for the family of columns over the sphere.
- [The Companion Nilpotents of the Biquaternion Algebra](the-companion-nilpotents-of-the-biquaternion-algebra.html), for the normalisation of $\nu$ and $\nu'$ and their Peirce corners.
- [Special Element and Peirce Conventions](special-element-and-peirce-conventions.html), for the notation of the idempotents and the corners.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the units and the products.
