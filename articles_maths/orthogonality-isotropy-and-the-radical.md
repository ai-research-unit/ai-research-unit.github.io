# __Orthogonality, Isotropy and the Radical__

## Introduction

A form of degree two organises the space it acts on by pairing elements, and the pairing yields a second, derived structure: the relation of **orthogonality**, the **isotropic** elements that the form cannot separate, the **totally isotropic** subspaces, and the **radical**, the part of the space that the form does not see at all. This article develops that structure for the forms of *Sesqualgebras with a Form*.

Three facts govern the layer. Orthogonality is a relation and not an inner product: it is symmetric because the form is Hermitian, and a subspace $W$ has two orthogonal complements which coincide, $W^{\perp} = {}^{\perp}W$, and satisfy $W \subseteq W^{\perp\perp}$, with equality for every $W$ as soon as the form is non-degenerate; the radical of the restriction is the intersection $W \cap W^{\perp}$. Isotropy and the radical are different: an isotropic element has $h(x,x) = 0$ and the radical is the set of the elements orthogonal to everything, and a totally isotropic subspace need not lie in the radical — the hyperbolic plane is the standard witness. And the radical is the total orthogonal complement, $A^{\perp} = \operatorname{rad}$, so that the form descends to the quotient $A/\operatorname{rad}$, where it is non-degenerate.

This is the counterpart of the orthogonality theory of *Bilinear Forms* and of the inertia theory of *The Indefinite Case and the Signature*; the classification of the forms by their Witt index is *The Hyperbolic Form and the Witt Index*, and the cancellation theorems are *Witt's Theorems*. Throughout, $(A,*,h)$ is a sesqualgebra with a form over a base $(R,\varsigma)$; the rank statements are made over a field $k$ with an involution $\varsigma$, where the Riesz maps are isomorphisms exactly when the form is non-degenerate, and the general case is stated with the hypothesis that the form be nonsingular, that is, that the Riesz map $x \mapsto h(\cdot, x)$ be an isomorphism.

## Orthogonality

**Definition.** Two elements $x, y$ are **orthogonal** when $h(x,y) = 0$; for a subset $W \subseteq A$ the **right complement** and the **left complement** are

$$
W^{\perp} = \{x : h(w,x) = 0 \ \text{for all } w \in W\}, \qquad
{}^{\perp}W = \{x : h(x,w) = 0 \ \text{for all } w \in W\} .
$$

**Proposition.** For a Hermitian form the two complements coincide, $W^{\perp} = {}^{\perp}W$, and orthogonality is a symmetric relation.

**Proof.** $h(x,w) = 0$ is equivalent to $\varsigma(h(w,x)) = 0$ and $\varsigma$ is injective, so the two sets are equal; the same computation gives symmetry.

**Proposition (the radical of a restriction).** For every subset $W$,

$$
W \cap W^{\perp} = \operatorname{rad}(h|_{W}) ,
$$

and the restriction $h|_{W}$ is non-degenerate exactly when $W \cap W^{\perp} = 0$. For every $W$ one has $W \subseteq W^{\perp\perp}$.

**Proof.** $x \in W \cap W^{\perp}$ means $x \in W$ and $h(x,w) = 0$ for every $w \in W$, which is exactly $x \in \operatorname{rad}(h|_{W})$; the restriction is non-degenerate exactly when that radical vanishes. For the inclusion, if $w \in W$ and $y \in W^{\perp}$ then $h(w,y) = 0$, so every element of $W$ is orthogonal to every element of $W^{\perp}$, which is $W \subseteq W^{\perp\perp}$.

**Corollary.** For a non-degenerate form the complement is an involution on the subspaces, $W^{\perp\perp} = W$ for every $W$. The radical is a different object: for a totally isotropic $W$ one has $\operatorname{rad}(h|_{W}) = W$, the whole of $W$, so the restriction is as degenerate as possible while the double complement is still $W$ and carries no information about the isotropy.

**Proposition (the orthogonal decomposition).** Let $A$ be a vector space of finite dimension over a field and $h$ non-degenerate. A subspace $W$ is non-degenerate exactly when $A = W \oplus W^{\perp}$.

**Proof.** If $W$ is non-degenerate then $W \cap W^{\perp} = \operatorname{rad}(h|_{W}) = 0$. The map $W \to W^{*}$, $w \mapsto h(\cdot,w)|_{W}$, is an isomorphism in finite dimension — injective by the vanishing of the radical and an isomorphism of vector spaces of the same dimension $\dim W$ — so the restriction map $A \to W^{*}$, $x \mapsto h(\cdot,x)|_{W}$, is onto; its kernel is $W^{\perp}$ and the rank–nullity theorem gives $\dim W^{\perp} = \dim A - \dim W$. The sum $W + W^{\perp}$ is then direct and of dimension $\dim A$, hence all of $A$. Conversely, if $A = W \oplus W^{\perp}$ and $x \in W$ is orthogonal to $W$, then $x$ is orthogonal to $W + W^{\perp} = A$, so $x = 0$ by non-degeneracy.

Over a general ring the rank argument is replaced by the hypothesis that $h$ be nonsingular, and the decomposition holds as a direct summand statement.

## Isotropy

**Definition.** An element $x$ is **isotropic** when $h(x,x) = 0$ and **anisotropic** otherwise; a subspace $W$ is **totally isotropic** when $h(x,y) = 0$ for all $x, y \in W$. A form with no non-zero isotropic element is **anisotropic**.

**Proposition.** Every element of the radical is isotropic, and the radical is a totally isotropic subspace. A totally isotropic subspace need not lie in the radical.

**Proof.** If $x \in \operatorname{rad}$ then $h(x,x) = 0$, and $h(x,y) = 0$ for all $x, y \in \operatorname{rad}$ by definition, so the radical is totally isotropic. For the failure, let $A = k^{2}$ with the form $h((a,b),(c,d)) = ad + bc$, the hyperbolic plane of the next article: it is non-degenerate, hence has zero radical, while $e_{1} = (1,0)$ is isotropic with $h(e_{1},e_{1}) = 0$ and the line $ke_{1}$ is totally isotropic.

**Remark (the null set is not the radical).** The set $\{x : h(x,x) = 0\}$ is the **null set** of the form and it is generally much larger than the radical; the two agree only in degenerate situations. The indefinite case is where the difference is visible, and it is the subject of *The Indefinite Case and the Signature*, where the inertia is defined through maximal definite subspaces precisely because the null set is not an invariant.

## The Radical and the Quotient

**Proposition.** The radical is the total orthogonal complement,

$$
\operatorname{rad} = A^{\perp} = {}^{\perp}A ,
$$

and it is invariant under the isometries of the form.

**Proof.** The first clause is the definition of the radical as the set of the elements orthogonal to every element of $A$; the Hermitian property identifies the two sides. If $T$ is an invertible isometry — in finite dimension and for a non-degenerate form every isometry is invertible, by *Isometries and the Unitary Group of a Form* — and $x \in \operatorname{rad}$ then $h(Tx, Ty) = h(x,y) = 0$ for every $y$, and $T$ being onto, $h(Tx, z) = 0$ for every $z$, so $Tx \in \operatorname{rad}$.

**Proposition (the descent).** The form descends to the quotient $A/\operatorname{rad}$ by $h_{\mathrm{red}}(x + \operatorname{rad}, y + \operatorname{rad}) = h(x,y)$, and the descended form is non-degenerate.

**Proof.** Well defined: if $z \in \operatorname{rad}$ then $h(x + z, y) = h(x,y) + h(z,y) = h(x,y)$ and likewise in the second slot. Non-degenerate: if $h(x,y) = 0$ for every $y$ then $x \in \operatorname{rad}$, so the class of $x$ is zero.

The descent is the algebraic reduction of the layer, and the radical is a left ideal of the algebra by *Sesqualgebras with a Form*; when the form is associative the radical is a two-sided ideal and the quotient is again an algebra, which is the quotient construction of *The Completion of a Sesqualgebra with a Form* read without the completion.

## The Witt Index

**Definition.** Let $h$ be a non-degenerate Hermitian form on a vector space of finite dimension over a field with an involution. The **Witt index** of $h$ is the largest dimension of a totally isotropic subspace, $\operatorname{ind}(h) = \max\{\dim W : W$ totally isotropic$\}$.

**Proposition.** Every totally isotropic subspace of a non-degenerate form is contained in a maximal one, and the Witt index is the number of hyperbolic planes in a Witt decomposition $A = H \perp A_{\mathrm{an}}$ with $H$ a sum of hyperbolic planes and $A_{\mathrm{an}}$ anisotropic.

**Proof.** The extension of a totally isotropic subspace to a maximal one is the finite-dimensional case of the extension theorem; the decomposition is the Witt decomposition, which the hyperbolic-plane reduction constructs pair by pair, and the number of pairs is the index. The details, with the cancellation theorem that makes the index and the anisotropic part invariants, are *Witt's Theorems* and *The Hyperbolic Form and the Witt Index*.

**Corollary.** Over an algebraically closed field $k$ with $\varsigma = \mathrm{id}$ the index of a non-degenerate form of dimension $n$ is $\lfloor n/2\rfloor$: the form is the sum of $\lfloor n/2\rfloor$ hyperbolic planes and, for $n$ odd, one anisotropic line. Over $\mathbb{R}$ the index is $\min(p,q)$ where $(p,q)$ is the signature, and the inertial invariant is *The Indefinite Case and the Signature*.

## Examples

### The Hyperbolic Plane

On $k^{2}$ with $h((a,b),(c,d)) = ad + bc$ the form is non-degenerate of Witt index one: the line $ke_{1}$ and the line $ke_{2}$ are totally isotropic, the radical is zero, and the matrix of the form is $\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}$ of determinant $-1$.

### The Matrix Algebra with an Indefinite Form

On $M_{2}(\mathbb{C})$ with $h(X,Y) = \tau(XGY^{*})$, $G = \operatorname{diag}(1,-1)$, the rank-one matrix $E_{11}$ has the positive diagonal $h(E_{11},E_{11}) = 1$ and is **not** isotropic; the sum $E_{11} + E_{22}$ is isotropic, $h(E_{11}+E_{22}, E_{11}+E_{22}) = \tau(G) = 0$, so the null set is not empty although the radical is zero, because the form is non-degenerate. The comparison with the rank-one functional form of the layer, $h_{\varphi}(X,Y) = \varphi(Y^{*}X)$ with $\varphi(Z) = \operatorname{tr}(ZE_{11})$, whose radical is the left ideal $\{X : XE_{11} = 0\}$ of the matrices with the first column zero, separates the two notions.

### The Biquaternion Algebra

On $\mathbb{B}$ with the form $\operatorname{Sc}(\bar{\tilde Q}\tilde Q')$ of signature $(2,6)$ over $\mathbb{R}$, the totally isotropic subspaces have dimension at most $2$; the two null directions are the light cone of the Minkowski reading, and the passage to the definite quotient is *The Form on the Biquaternion Algebra as a General Plain Sesquilinear Form*.

## Summary

- Orthogonality is the symmetric relation $h(x,y) = 0$; the two orthogonal complements coincide for a Hermitian form and $W \subseteq W^{\perp\perp}$, with equality for every $W$ when the form is non-degenerate, while $W \cap W^{\perp} = \operatorname{rad}(h|_{W})$.
- Over a field and for a non-degenerate form, $W$ is non-degenerate exactly when $A = W \oplus W^{\perp}$.
- An element is isotropic when $h(x,x) = 0$; the radical is totally isotropic, and a totally isotropic subspace need not lie in the radical, the hyperbolic plane being the witness.
- The null set is not the radical, and the inertia must be defined through maximal definite subspaces rather than through the null set.
- The radical is the total orthogonal complement $A^{\perp}$ and is isometry-invariant; the form descends to $A/\operatorname{rad}$, where it is non-degenerate.
- The Witt index is the largest dimension of a totally isotropic subspace and the number of hyperbolic planes in a Witt decomposition.
- The bilinear originals are *Bilinear Forms* and *Witt's Theorems*; the index classification is *The Hyperbolic Form and the Witt Index*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $W^{\perp}$, ${}^{\perp}W$ | the right and the left orthogonal complement of $W$ |
| $W^{\perp\perp}$ | the double complement, containing $W$ |
| $\operatorname{rad}$ | the radical $A^{\perp} = {}^{\perp}A$ |
| $h_{\mathrm{red}}$ | the form descended to $A/\operatorname{rad}$ |
| $\operatorname{ind}(h)$ | the Witt index of a non-degenerate form |
| $A_{\mathrm{an}}$ | the anisotropic part of a Witt decomposition |
| $H$ | the hyperbolic part of a Witt decomposition |

## Further Reading

- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for orthogonality, the radical, the descent and the Witt decomposition.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields*, Graduate Studies in Mathematics 67 (American Mathematical Society, 2005), for totally isotropic subspaces and the Witt index over a field.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294 (Springer, 1991), for the non-singular form over a ring and the orthogonal summand statements.
