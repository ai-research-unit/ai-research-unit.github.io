# __The Six Subspaces and the Four Forms__

## Introduction

The biquaternion algebra carries four pairings, the scalar parts of the four products of *The Four Biquaternion Complex Products*, and this article reads all four against the six distinguished subspaces.

$$
\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu Q_\mu,
\qquad
\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=\sum_\mu P_\mu Q_\mu,
$$
$$
\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_\mu P_\mu\overline{Q_\mu},
\qquad
\langle\tilde P,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu},
$$

with $\varepsilon=(1,-1,-1,-1)$. The first is the $\mathbb{C}$-**bilinear** form, symmetric and complex-valued, the scalar part of the plain product; the second is the $\mathbb{C}$-**bilinear** form built on the natural conjugation ${}^{\natural}$, symmetric and complex-valued, whose diagonal is the norm $\sum_\mu Q_\mu^{2}$; the third is the $\mathbb{C}$-**sesquilinear** form built on the Hermitian conjugation ${}^{*}$, positive definite; and the fourth is the $\mathbb{C}$-sesquilinear **quaternion sesquilinear form** built on ${}^{\natural}\circ\bar{\cdot}$, indefinite. They are treated in the whole algebra in *The Complex Bilinear Form on the Biquaternion Algebra*, *The Bilinear Form on the Biquaternion Algebra*, *The Hermitian Form on the Biquaternion Algebra* and *The Biquaternion Krein Form and Its Signature*, and in the matrix models in *The Forms in the Matrix Representation of the Biquaternion Algebra*; what is added here is the restriction to the six, the orthogonality of the six with one another, and the isotropic subspaces.

Two structural facts organise everything below. The first is that **all four pairings are diagonal in the complex coefficient system**: their Gram matrices in the basis $e_0, e_1, e_2, e_3$ are

$$
\bigl(\langle e_\mu,e_\nu\rangle\bigr) = \mathrm{E}, \qquad
\bigl(\langle e_\mu,e_\nu\rangle_{\natural}\bigr) = \mathrm{I}_4, \qquad
\bigl(\langle e_\mu,e_\nu\rangle_{*}\bigr) = \mathrm{I}_4, \qquad
\bigl(\langle e_\mu,e_\nu\rangle_{\natural*}\bigr) = \mathrm{E},
$$

the sign pattern $\varepsilon,1,1,\varepsilon$ against the four pairs of coefficients, with $\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$. The second is that the real parts of the first, the second and the fourth are diagonal in the **real** basis $e_0, e_1, e_2, e_3, ie_0, ie_1, ie_2, ie_3$, with the sign patterns

$$
\mathrm{Re}\,\langle\cdot,\cdot\rangle : \ +,-,-,-,-,+,+,+ , \qquad
\mathrm{Re}\,\langle\cdot,\cdot\rangle_{\natural} : \ +,+,+,+,-,-,-,- , \qquad
\mathrm{Re}\,\langle\cdot,\cdot\rangle_{\natural*} : \ +,-,-,-,+,-,-,- ,
$$

so that these two bilinear forms and the quaternion sesquilinear form have signatures $(4,4)$, $(4,4)$ and $(2,6)$ on $\mathbb{B}=\mathbb{R}^{8}$, while the complex sesquilinear form is positive definite, of signature $(8,0)$, with every entry $1$. The six subspaces are unions of coordinate sets in these real basis systems, so every restriction is read off the sign strings. This gives the following table, the five middle columns being real signatures.

| subspace | $\dim_{\mathbb{R}}$ | $\langle\cdot,\cdot\rangle$ | $\langle\cdot,\cdot\rangle_{\natural}$ | $\langle\cdot,\cdot\rangle_{*}$ | $\langle\cdot,\cdot\rangle_{\natural*}$ |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $2$ | $(1,1)$ | $(1,1)$ | $(2,0)$ | $(2,0)$ |
| $\mathrm{Vect}(\mathbb{B})$ | $6$ | $(3,3)$ | $(3,3)$ | $(6,0)$ | $(0,6)$ |
| $\mathbb{H}_{\mathbb{B}}$ | $4$ | $(1,3)$ | $(4,0)$ | $(4,0)$ | $(1,3)$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $4$ | $(3,1)$ | $(0,4)$ | $(4,0)$ | $(1,3)$ |
| $\mathbb{M}_+$ | $4$ | $(4,0)$ | $(1,3)$ | $(4,0)$ | $(1,3)$ |
| $\mathbb{M}_-$ | $4$ | $(0,4)$ | $(3,1)$ | $(4,0)$ | $(1,3)$ |

Four features of the table are worth naming before the sections. The complex sesquilinear form is **positive definite on every one of the six**, so it distinguishes nothing among them. The complex bilinear form and the quaternion bilinear form **agree in signature on the centre and the vector subspace** and part company on the four four-dimensional subspaces, where the complex bilinear form is indefinite and the quaternion bilinear form is definite or anti-definite. The quaternion sesquilinear form has the **same** signature $(1,3)$ on each of the four four-dimensional subspaces, which is the form statement of their common real dimension. And each of the two indefinite bilinear forms is **definite on exactly one pair** of the four-dimensional subspaces: the quaternion bilinear form is positive definite on $\mathbb{H}_{\mathbb{B}}$ and negative definite on $i\mathbb{H}_{\mathbb{B}}$, while the complex bilinear form is positive definite on $\mathbb{M}_+$ and negative definite on $\mathbb{M}_-$.

The null sets are read off the diagonal forms in the same way. On the centre all four vanish only at $0$. On the vector subspace the complex and the quaternion bilinear forms share the **complex null cone** $\sum_k P_k^{2}=0$ of real dimension $4$, while both sesquilinear forms are definite there and vanish only at $0$. On the quaternion and anti-quaternion subspaces the complex bilinear form and the quaternion sesquilinear form share the **real cone** $h_0^{2}=h_1^{2}+h_2^{2}+h_3^{2}$ of real dimension $3$, while the quaternion bilinear form is definite there. On the two Hermitian subspaces the quaternion bilinear form and the quaternion sesquilinear form coincide up to sign and share the same cone of real dimension $3$, $a_0^{2}=(\mathbf{p},\mathbf{p})$ on $\mathbb{M}_+$ and $b_0^{2}=(\mathbf{q},\mathbf{q})$ on $\mathbb{M}_-$, while the complex bilinear form is definite there.

## The Four Pairings

**Definition.** For $\tilde P, \tilde Q \in \mathbb{B}$ the four pairings are the coefficient sums above. The first two are $\mathbb{C}$-bilinear and symmetric; the last two are $\mathbb{C}$-sesquilinear with the first argument conjugate-linear and the second linear, and Hermitian in the sense $\langle\tilde P,\tilde Q\rangle_{*} = \overline{\langle\tilde Q,\tilde P\rangle_{*}}$ and likewise for $\langle\cdot,\cdot\rangle_{\natural*}$. All four are non-degenerate.

**Proposition (the diagonalizations).** In the complex basis $e_0, e_1, e_2, e_3$ all four pairings are diagonal with entries $\varepsilon_\mu$ for the first and the fourth and $1$ for the second and the third; in the real basis $e_0, e_1, e_2, e_3, ie_0, ie_1, ie_2, ie_3$ the real parts of the first, the second and the fourth are diagonal with the displayed sign patterns, and the complex sesquilinear form is diagonal with every entry $1$.

**Proof.** Each pairing is a sum over the four coefficients of a product of one coefficient of $\tilde P$ with one of $\tilde Q$, so the cross terms vanish when the two basis vectors are distinct. For the real parts, the real basis vectors $ie_\mu$ have coefficients equal to $i$ in the complex basis, so
$$
\langle ie_\mu,ie_\mu\rangle = i^{2} = -1,
\qquad
\langle ie_\mu,ie_\mu\rangle_{\natural} = i^{2} = -1,
\qquad
\langle ie_\mu,ie_\mu\rangle_{\natural*} = \varepsilon_\mu\lvert i\rvert^{2} = \varepsilon_\mu,
\qquad
\langle ie_\mu,ie_\mu\rangle_{*} = \lvert i\rvert^{2} = 1 .
$$
$\square$

**Remark (the pairings in the matrix models).** Transported by the isomorphism $\Phi$ of *Biquaternion 2×2 Matrix Element Representation*, the complex bilinear form is the plain trace pairing $\tfrac12\operatorname{Tr}(\Phi(\tilde P)\Phi(\tilde Q))$, the quaternion bilinear form is the pairing with the adjugate $\tfrac12\operatorname{Tr}(\Phi(\tilde P)\operatorname{adj}\Phi(\tilde Q))$, the complex sesquilinear form is the Hilbert–Schmidt pairing $\tfrac12\operatorname{Tr}(\Phi(\tilde P)^{\dagger}\Phi(\tilde Q))$ read with the arguments in the other order, and the quaternion sesquilinear form is the pairing with the conjugate transpose of the adjugate; this dictionary is the content of *The Forms in the Matrix Representation of the Biquaternion Algebra*. The two matrix models of *Introduction to the 2×2 Matrix Representation of Biquaternions* and *Introduction to the 4×4 Regular Matrix Representation of Biquaternions* carry two of these pairings as their trace and determinant invariants: $\langle\tilde Q,\tilde Q\rangle_{\natural} = \det\Phi(\tilde Q)$ and $\langle\tilde Q,\tilde Q\rangle_{\natural*} = \det\Phi(\tilde Q)^{*}$ up to the normalisation of the Hilbert–Schmidt form.

Three facts about the six are read from the diagonalizations at once. The **restriction of each of the four pairings to each of the six is non-degenerate**, with Gram determinant $\pm 1$ in the natural basis for the first, the second and the fourth. The **restriction of the quaternion sesquilinear form is definite exactly on the centre and the vector subspace**, with opposite signs, and has signature $(1,3)$ on each of the other four. And the **restriction of the quaternion bilinear form is definite exactly on the quaternion and anti-quaternion subspaces**, with opposite signs, and has signature $(1,3)$ on each of the other four.

## The Centre Subspace

A central element is $\tilde Q = Ae_0$ with $A = q_0 + iq'_0$, and the four diagonal values are

$$
\langle Ae_0,Ae_0\rangle = A^{2}, \qquad
\langle Ae_0,Ae_0\rangle_{\natural} = A^{2}, \qquad
\langle Ae_0,Ae_0\rangle_{*} = \lvert A\rvert^{2}, \qquad
\langle Ae_0,Ae_0\rangle_{\natural*} = \lvert A\rvert^{2} .
$$

The two bilinear forms are **complex-valued** on the centre, their common real part $q_0^{2} - (q'_0)^{2}$ has signature $(1,1)$, and the centre is a hyperbolic plane; but neither has a nonzero null element, since $A^{2} = 0$ forces $A = 0$. The two sesquilinear forms are **positive definite**, both equal to $\lvert A\rvert^{2} = q_0^{2}+(q'_0)^{2}$ restricted to the centre, and the centre is the smallest of the six. The centre is thus the only one of the six on which the quaternion bilinear form is complex-valued and on which the quaternion sesquilinear form is positive definite, the two properties that make it the hyperbolic plane of the fundamental decomposition of the quaternion sesquilinear form.

## The Vector Subspace

A pure element is $\tilde Q = \mathbf{P} = \sum_k P_ke_k$ with complex coefficients $P_k = q_k + iq'_k$, and the four diagonal values are

$$
\langle\mathbf{P},\mathbf{P}\rangle = -\sum_k P_k^{2}, \qquad
\langle\mathbf{P},\mathbf{P}\rangle_{\natural} = \sum_k P_k^{2}, \qquad
\langle\mathbf{P},\mathbf{P}\rangle_{\natural*} = -\sum_k \lvert P_k\rvert^{2}, \qquad
\langle\mathbf{P},\mathbf{P}\rangle_{*} = \sum_k \lvert P_k\rvert^{2} .
$$

The two bilinear forms are **complex-valued**, of real parts of opposite signs, $\sum_k(q_k^{2} - (q'_k)^{2})$ and its negative, each of signature $(3,3)$, and neither is a null cone of the other: they share the complex null cone $\sum_k P_k^{2} = 0$, of real dimension $4$. The complex sesquilinear form is **positive definite** of signature $(6,0)$ and the quaternion sesquilinear form is **negative definite** of signature $(0,6)$, so the vector subspace is where the two sesquilinear pairings part company, the definite form being positive and the indefinite one negative; and together with the centre they make up the fundamental decomposition of the quaternion sesquilinear form, of signature $(2,0) + (0,6) = (2,6)$.

## The Quaternion Subspace

A real quaternion is $\tilde Q = h = h_0e_0 + h_1e_1 + h_2e_2 + h_3e_3$ with real $h_\mu$, and the diagonal values are

$$
\langle h,h\rangle = h_0^{2} - h_1^{2} - h_2^{2} - h_3^{2}, \qquad
\langle h,h\rangle_{\natural} = \sum_\mu h_\mu^{2} > 0,
$$
$$
\langle h,h\rangle_{*} = \sum_\mu h_\mu^{2}, \qquad
\langle h,h\rangle_{\natural*} = h_0^{2} - h_1^{2} - h_2^{2} - h_3^{2} .
$$

The quaternion bilinear form is **real-valued and positive definite** on the quaternion subspace, of signature $(4,0)$, so **no nonzero real quaternion is null**: this is the definiteness version of the quaternion subspace being free of zero divisors. The complex sesquilinear form is positive definite and equal to the same $\sum_\mu h_\mu^{2}$. The complex bilinear form and the quaternion sesquilinear form are **indefinite and equal**, of signature $(1,3)$, with the common null cone $h_0^{2} = h_1^{2} + h_2^{2} + h_3^{2}$ of real dimension $3$, the cone of the zero divisors of the algebra that happen to lie in this subspace.

**The quaternion subspace is the subspace on which the quaternion bilinear form and the quaternion sesquilinear form swap roles**: the quaternion bilinear form is definite there and the quaternion sesquilinear form indefinite, exactly the reverse of the vector subspace. The complex sesquilinear form is positive definite throughout, and the complex bilinear form is the second indefinite form here, so this is the subspace on which the two bilinear forms differ most sharply.

## The Anti-Quaternion Subspace

An element of $i\mathbb{H}_{\mathbb{B}}$ is $\tilde Q = ih$ with $h$ a real quaternion, and the diagonal values follow from the coefficients being $i$ times real numbers:

$$
\langle ih,ih\rangle = h_0^{2} - h_1^{2} - h_2^{2} - h_3^{2}, \qquad
\langle ih,ih\rangle_{\natural} = -\sum_\mu h_\mu^{2} < 0,
$$
$$
\langle ih,ih\rangle_{*} = \sum_\mu h_\mu^{2}, \qquad
\langle ih,ih\rangle_{\natural*} = h_0^{2} - h_1^{2} - h_2^{2} - h_3^{2} .
$$

The quaternion bilinear form is **real-valued and negative definite** on the anti-quaternion subspace, of signature $(0,4)$, so no nonzero element of it is null: this is the definiteness version of the absence of zero divisors there, and it is the exact mirror of the quaternion subspace. The complex sesquilinear form is positive definite. The complex bilinear form and the quaternion sesquilinear form are indefinite, of signatures $(3,1)$ and $(1,3)$, the complex bilinear form being the negative of its value on the quaternion subspace by the factor $i^{2}$, and they share the same null cone $h_0^{2} = h_1^{2} + h_2^{2} + h_3^{2}$ of real dimension $3$.

So the quaternion subspace and the anti-quaternion subspace have the **same complex sesquilinear and quaternion sesquilinear forms and opposite quaternion bilinear forms**: the indefinite pairing does not tell them apart, and the quaternion bilinear form tells them apart by its sign alone. The complex bilinear form is the one indefinite form whose signature differs between the two, $(1,3)$ against $(3,1)$.

## The Hermitian Subspace

A Hermitian element is $\tilde Q = a_0e_0 + i\mathbf{p}$ with $a_0$ real and $\mathbf{p}$ a real vector, and the diagonal values are

$$
\langle\tilde Q,\tilde Q\rangle = a_0^{2} + (\mathbf{p},\mathbf{p}), \qquad
\langle\tilde Q,\tilde Q\rangle_{\natural} = a_0^{2} - (\mathbf{p},\mathbf{p}),
$$
$$
\langle\tilde Q,\tilde Q\rangle_{*} = a_0^{2} + (\mathbf{p},\mathbf{p}), \qquad
\langle\tilde Q,\tilde Q\rangle_{\natural*} = a_0^{2} - (\mathbf{p},\mathbf{p}) .
$$

**On the Hermitian subspace the quaternion sesquilinear form is the quaternion bilinear form**, the same real-valued form of signature $(1,3)$, and the two have the same null elements: $a_0^{2} = (\mathbf{p},\mathbf{p})$, a cone of real dimension $3$ whose nonzero elements are the zero divisors of the subspace. The complex bilinear form and the complex sesquilinear form are **equal and positive definite**, of signature $(4,0)$, so the Hermitian subspace is the exact counterpart of the quaternion subspace with the roles of the two bilinear forms exchanged: there the quaternion bilinear form is definite, here the complex bilinear form is.

The polar form of the quaternion bilinear form on the Hermitian subspace is

$$
\langle\tilde Q,\tilde R\rangle_{\natural} = a_0r_0 - (\mathbf{p},\mathbf{r}),
$$

the indefinite symmetric form whose diagonal gives the signature $(1,3)$, and it is the form whose totally isotropic lines are the null directions of $\mathbb{M}_+$, treated below.

## The Anti-Hermitian Subspace

An anti-Hermitian element is $\tilde Q = ib_0e_0 + \mathbf{q}$ with $b_0$ real and $\mathbf{q}$ a real vector, and the diagonal values are

$$
\langle\tilde Q,\tilde Q\rangle = -b_0^{2} - (\mathbf{q},\mathbf{q}), \qquad
\langle\tilde Q,\tilde Q\rangle_{\natural} = -b_0^{2} + (\mathbf{q},\mathbf{q}),
$$
$$
\langle\tilde Q,\tilde Q\rangle_{*} = b_0^{2} + (\mathbf{q},\mathbf{q}), \qquad
\langle\tilde Q,\tilde Q\rangle_{\natural*} = b_0^{2} - (\mathbf{q},\mathbf{q}) .
$$

**On the anti-Hermitian subspace the quaternion sesquilinear form is the negative of the quaternion bilinear form**, so again the two have the same null elements, $b_0^{2} = (\mathbf{q},\mathbf{q})$, the cone of real dimension $3$ of the zero divisors of $\mathbb{M}_-$. The complex bilinear form is **negative definite** of signature $(0,4)$, and the complex sesquilinear form is positive definite of signature $(4,0)$; the anti-Hermitian subspace is therefore the mirror of the Hermitian one for the two bilinear forms, exactly as the anti-quaternion subspace is the mirror of the quaternion one.

So the two Hermitian subspaces are the two subspaces of the six on which the quaternion bilinear form and the quaternion sesquilinear form have the **same null set** and differ by a sign of the whole form: they agree on $\mathbb{M}_+$ and are opposite on $\mathbb{M}_-$, while the complex bilinear form is definite with opposite signs on the two.

## The Orthogonal Decomposition

Because all four pairings are diagonal in the complex coefficient system, two of the six are orthogonal exactly when their coefficient supports are disjoint. The supports are

$$
\mathbb{C}_{\mathbb{B}} : \{0\}, \qquad
\mathrm{Vect}(\mathbb{B}) : \{1,2,3\}, \qquad
\mathbb{H}_{\mathbb{B}}, \ i\mathbb{H}_{\mathbb{B}}, \ \mathbb{M}_+, \ \mathbb{M}_- : \{0,1,2,3\},
$$

so **the centre and the vector subspace are orthogonal for all four pairings, and they are the only pair of the six that is**. Every other pair of the six shares a coefficient, and the corresponding entry of the pairing is a product that does not vanish identically. Since each diagonal entry is nonzero, the decomposition is one of non-degenerate summands, and the forms restrict to each without degenerating.

**Corollary (the orthogonal decomposition).** For each of the four pairings, the scalar-vector decomposition is orthogonal,

$$
\mathbb{B} = \mathbb{C}_{\mathbb{B}} \perp \mathrm{Vect}(\mathbb{B}),
$$

and the signatures add: $(1,1) + (3,3) = (4,4)$ for the complex bilinear form, $(1,1) + (3,3) = (4,4)$ for the quaternion bilinear form, $(2,0) + (6,0) = (8,0)$ for the complex sesquilinear form, and $(2,0) + (0,6) = (2,6)$ for the quaternion sesquilinear form; the last of these is the fundamental decomposition of the Krein space of *The Biquaternion Krein Form and Its Signature*.

## The Isotropic Lines and the Ideals

The isotropic structure of the four forms is read from their null cones. The **complex bilinear form** has the null cone $\sum_\mu\varepsilon_\mu Q_\mu^{2} = 0$, which on the vector subspace is the complex cone $\sum_k P_k^{2} = 0$ and on the quaternion and anti-quaternion subspaces the real cone $h_0^{2} = h_1^{2} + h_2^{2} + h_3^{2}$. The **quaternion bilinear form** has the null cone $\sum_\mu Q_\mu^{2} = 0$, the zero divisors of the algebra, which is the complex cone on the vector subspace and empty on the quaternion and anti-quaternion subspaces. The **quaternion sesquilinear form** has the null cone $\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2} = 0$, empty on the centre and the vector subspace and the cone $h_0^{2} = h_1^{2} + h_2^{2} + h_3^{2}$ on the four four-dimensional subspaces. The **complex sesquilinear form** has no nonzero null element anywhere. On the quaternion subspace the complex bilinear and the quaternion sesquilinear forms share the real cone $h_0^{2} = h_1^{2} + h_2^{2} + h_3^{2}$ and the quaternion bilinear form has no null element, so the three nonzero cones are not distinct there.

**Proposition (a line is isotropic exactly when it is spanned by a null element).** For $\tilde P \neq 0$ the complex line $\mathbb{C}\tilde P$ is totally isotropic for one of the two bilinear forms exactly when the corresponding diagonal value $\langle\tilde P,\tilde P\rangle$ or $\langle\tilde P,\tilde P\rangle_{\natural}$ vanishes.

**Proof.** $\langle\lambda\tilde P,\mu\tilde P\rangle_{\natural} = \lambda\mu \langle\tilde P,\tilde P\rangle_{\natural}$ by bilinearity, and this vanishes for all $\lambda,\mu$ exactly when $\langle\tilde P,\tilde P\rangle_{\natural} = 0$; the same computation gives the complex bilinear case. For a sesquilinear form the vanishing is the vanishing of the diagonal, since $\langle\lambda\tilde P,\lambda\tilde P\rangle_{\natural*} = \lvert\lambda\rvert^{2}\langle\tilde P,\tilde P\rangle_{\natural*}$ is real. $\square$

Since the null elements of the quaternion bilinear form are exactly the zero divisors, its isotropic lines of the six are their **zero-divisor lines**: none in the centre, the quaternion subspace and the anti-quaternion subspace, which have no nonzero null element; the complex lines of the nilpotents in the vector subspace and the cone of the real multiples of the Hermitian idempotents in the two Hermitian subspaces.

**Theorem (the minimal ideals are the maximal isotropic one-sided ideals).** Every minimal left ideal and every minimal right ideal of $\mathbb{B}$ is a maximal totally isotropic subspace of the quaternion bilinear form. Conversely, a maximal totally isotropic subspace that is a left ideal is a minimal left ideal, and likewise on the right.

**Proof.** Let $\tilde Q \neq 0$ be null for the quaternion bilinear form and let $\tilde X, \tilde Y \in \mathbb{B}$. Then

$$
\langle\tilde X\tilde Q,\tilde Y\tilde Q\rangle_{\natural} = \mathrm{Sc}\!\left(\tilde X\tilde Q\tilde Q^{\natural}\tilde Y^{\natural}\right) = \mathrm{Sc}\!\left(\tilde X \langle\tilde Q,\tilde Q\rangle_{\natural}\tilde Y^{\natural}\right) = \langle\tilde Q,\tilde Q\rangle_{\natural}\,\mathrm{Sc}\!\left(\tilde X\tilde Y^{\natural}\right) = 0,
$$

so the left ideal $\mathbb{B}\tilde Q$ is totally isotropic; it has complex dimension $2$ by *The Six Subspaces and the Structure*, and a totally isotropic subspace of the four-dimensional complex algebra has complex dimension at most $2$, since the form is non-degenerate and of Witt index $2$. So $\mathbb{B}\tilde Q$ is maximal. Conversely a maximal totally isotropic left ideal is generated by a null element and is therefore minimal. The right-handed statements are the mirror. $\square$

The theorem is not an equality of families: the maximal totally isotropic subspaces form a larger family than the one-sided ideals, and the two families meet in the minimal ideals. In the Peirce basis $\tilde\Pi, \tilde R, f, \tilde T$ of *The Six Subspaces and the Structure*, where $\tilde\Pi = \tfrac{1}{2}(e_0 + ie_1)$, $f = e_0 - \tilde\Pi$, $\tilde R = e_3 + ie_2$ and $\tilde T = e_3 - ie_2$, the Gram matrix of the quaternion bilinear form is

$$
\begin{pmatrix}
0 & 0 & \tfrac{1}{2} & 0 \\
0 & 0 & 0 & 2 \\
\tfrac{1}{2} & 0 & 0 & 0 \\
0 & 2 & 0 & 0
\end{pmatrix},
$$

an antidiagonal matrix: **the form is hyperbolic in the Peirce basis, and the four Peirce lines are paired by it**, the idempotent line $\mathbb{C}\tilde\Pi$ with the idempotent line $\mathbb{C}f$ and the nilpotent line $\mathbb{C}\tilde R$ with the nilpotent line $\mathbb{C}\tilde T$. The two minimal left ideals $\mathbb{B}\tilde\Pi = \mathbb{C}\tilde\Pi \oplus \mathbb{C}\tilde R$ and $\mathbb{B}f = \mathbb{C}f \oplus \mathbb{C}\tilde T$ are maximal totally isotropic by the theorem, and the span of $\tilde\Pi$ and $\tilde T$, one line from each, is a maximal totally isotropic subspace that is **not** a left ideal: it mixes the two. Note that this is the isotropic structure of the **quaternion bilinear form**; the complex bilinear and the quaternion sesquilinear forms have different null cones, and their maximal totally isotropic subspaces need not be ideals.

Finally, the isotropic subspaces lying inside a **single** one of the six are no more than lines. Each restriction of each of the four forms to each of the six is non-degenerate, of Gram determinant $\pm 1$ for the three indefinite forms and positive for the complex sesquilinear form; the complex subspaces of the six are the centre of complex dimension $1$ and the vector subspace of complex dimension $3$, and by non-degeneracy a totally isotropic complex subspace of a non-degenerate form on a complex space of dimension $d$ has dimension at most $d/2$, so at most $0$ in the centre and at most $1$ in the vector subspace; and the four four-dimensional subspaces are **totally real**, in the sense that $i\tilde Q$ lies in none of them when $\tilde Q \neq 0$ is in one, so they contain no complex subspace at all, and their real forms are definite on the quaternion and anti-quaternion subspaces for the bilinear form and on the two Hermitian subspaces for the other, and of real Witt index $1$ on the two Hermitian subspaces for the quaternion bilinear form and on the quaternion and anti-quaternion subspaces for the complex bilinear form. So each of the vector subspace, the quaternion subspace, the anti-quaternion subspace and the Hermitian and anti-Hermitian subspaces contains isotropic lines for some of the forms and no isotropic plane, and the other restrictions are anisotropic.

## Summary

The algebra carries four pairings, the scalar parts of the four products of *The Four Biquaternion Complex Products*: the complex bilinear form, the quaternion bilinear form whose diagonal is the norm, the positive definite complex sesquilinear form and the indefinite quaternion sesquilinear form. All four are diagonal in the complex coefficient system, with Gram matrices $\mathrm{E}$, $\mathrm{I}_4$, $\mathrm{I}_4$ and $\mathrm{E}$; the real parts of the first, the second and the fourth are diagonal in the real basis with sign patterns $+,-,-,-,-,+,+,+$, $+,+,+,+,-,-,-,-$ and $+,-,-,-,+,-,-,-$, of signatures $(4,4)$, $(4,4)$ and $(2,6)$, and the third is positive definite of signature $(8,0)$. Restricted to the six, the complex bilinear form has signatures $(1,1)$, $(3,3)$, $(1,3)$, $(3,1)$, $(4,0)$ and $(0,4)$; the quaternion bilinear form has $(1,1)$, $(3,3)$, $(4,0)$, $(0,4)$, $(1,3)$ and $(3,1)$; the quaternion sesquilinear form has $(2,0)$ on the centre, $(0,6)$ on the vector subspace and $(1,3)$ on each of the other four, so that it is definite on the two subspaces that make up the fundamental decomposition and of the same signature on the four four-dimensional ones; and the complex sesquilinear form is positive definite on all six and distinguishes nothing. The two indefinite bilinear forms are each definite exactly on one pair of the four-dimensional subspaces: the quaternion bilinear form on the quaternion and anti-quaternion subspaces, the complex bilinear form on the two Hermitian ones. The bilinear forms are complex-valued on the centre and the vector subspace and real-valued on the other four. All four pairings being diagonal in the coefficient system, the centre and the vector subspace are orthogonal and they are the only orthogonal pair among the six, and the scalar-vector decomposition is orthogonal for all four, with signature arithmetic $(1,1)+(3,3)=(4,4)$, $(1,1)+(3,3)=(4,4)$, $(2,0)+(6,0)=(8,0)$ and $(2,0)+(0,6)=(2,6)$. A complex line is totally isotropic for a bilinear form exactly when it is spanned by a null element, so the isotropic lines of the quaternion bilinear form are the lines of the zero divisors; every minimal left ideal and every minimal right ideal is a maximal totally isotropic subspace of the quaternion bilinear form, and conversely every maximal totally isotropic subspace of it that is a one-sided ideal is a minimal one; the form is hyperbolic in the Peirce basis, pairing the two idempotent lines and the two nilpotent lines; and no isotropic subspace beyond a line lies inside a single one of the six, whose restrictions are all non-degenerate. The four pairings themselves, their matrix forms and their signatures on the whole algebra are the business of *The Complex Bilinear Form on the Biquaternion Algebra*, *The Bilinear Form on the Biquaternion Algebra*, *The Hermitian Form on the Biquaternion Algebra*, *The Biquaternion Krein Form and Its Signature* and *The Forms in the Matrix Representation of the Biquaternion Algebra*; what is added here is the restriction to the six, the orthogonality table and the isotropic structure.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra |
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B})$ | the centre and the vector subspace |
| $\mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces |
| $\mathbb{M}_+, \mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces |
| $\langle\tilde P,\tilde Q\rangle$ | the complex bilinear form, the scalar part of $\tilde P\tilde Q$ |
| $\langle\tilde P,\tilde Q\rangle_{\natural}$ | the quaternion bilinear form, the polarisation of the norm |
| $\langle\tilde P,\tilde Q\rangle_{*}$ | the complex sesquilinear form, built on ${}^{*}$ |
| $\langle\tilde P,\tilde Q\rangle_{\natural*}$ | the quaternion sesquilinear form, built on ${}^{\natural}\circ\bar{\cdot}$ |
| $\varepsilon,\ \mathrm{E}$ | the sign vector $(1,-1,-1,-1)$ and its diagonal matrix |
| $\tilde\Pi, \tilde R, f, \tilde T$ | the Peirce basis, in which the quaternion bilinear form is hyperbolic |

## Further Reading

- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the six subspaces themselves, one to a section
- *The Six Subspaces and the Elements* (`articles_maths/the-six-subspaces-and-the-elements.md`), for the null elements, which are the zero divisors whose lines are the isotropic lines
- *The Six Subspaces and the Structure* (`articles_maths/the-six-subspaces-and-the-structure.md`), for the minimal left and right ideals, which are the maximal totally isotropic one-sided ideals, and for the Peirce basis
- *Introduction to the 2×2 Matrix Representation of Biquaternions* and *Introduction to the 4×4 Regular Matrix Representation of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-representation-of-biquaternions.md`, `articles_maths/introduction-to-the-4x4-regular-matrix-representation-of-biquaternions.md`), for the models in which the trace and the determinant carry the same information
- *The Six Subspaces and the Analysis* (`articles_maths/the-six-subspaces-and-the-analysis.md`), for the reading of these signatures as the types of the second-order operator on each subspace
- *The Complex Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-complex-bilinear-form-on-the-biquaternion-algebra.md`), for the complex bilinear form and its restriction table
- *The Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-bilinear-form-on-the-biquaternion-algebra.md`), for the quaternion bilinear form, its polarisation and its restriction table in the whole algebra
- *The Hermitian Form on the Biquaternion Algebra* (`articles_maths/the-hermitian-form-on-the-biquaternion-algebra.md`), for the complex sesquilinear form, its inner product and the Euclidean structure
- *The Biquaternion Krein Form and Its Signature* (`articles_maths/the-biquaternion-krein-form-and-its-signature.md`), for the quaternion sesquilinear form, its signature and the fundamental decomposition
- *The Forms in the Matrix Representation of the Biquaternion Algebra* (`articles_maths/the-forms-in-the-matrix-representation-of-the-biquaternion-algebra.md`), for the four pairings in the matrix models
