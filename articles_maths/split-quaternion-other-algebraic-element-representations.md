
# __Split-Quaternion Other Algebraic Element Representations__

## Introduction

The algebra article defined $\mathbb{H}_{\mathrm{s}}$, its three involutions, its split-quaternion norm and its distinguished real subspaces $S$, $V$, $\mathbb{D}_2$ and $\mathbb{D}_3$. This article describes the **algebraic realizations** of $\mathbb{H}_{\mathrm{s}}$ that are not the subject of a dedicated article of their own:

1. **Clifford algebra representation.** A split-quaternion as an element of the Clifford algebra $\mathrm{Cl}_{1,1}$, so that the three involutions of the algebra are the standard Clifford involutions.
2. **Clifford module representation.** The algebra acting on the split-complex planes and on its two-component module, the split signature analogue of the spinor representation.
3. **Relations among the split-complex and matrix models.** The identification of the Clifford, split-complex and matrix pictures of the same element.

The remaining realizations are the subjects of their own articles:

| realization | article |
|---|---|
| four-vector | *Split-Quaternion Four-Vector Element Representation* |
| $2 \times 2$ matrix | *Split-Quaternion Matrix Element Representations* |
| operator on the algebra | *Split-Quaternion Rotations and the Lorentz Group* |
| polar | *Split-Quaternion Polar Element Representation* |

and the technical representation theory is the subject of *Split-Quaternion Element Representations*. Each of those articles owns its realization; this article records only the relations that involve the three studied here.

The word **representation** is used in the sense of a concrete realization of the algebra as computable objects, not in the technical sense of a vector space carrying an algebra homomorphism into its endomorphisms. The word **algebraic** contrasts with **polar**: the realizations here use only the algebra operations and the underlying real vector space, not the exponential or the roots of $-1$.

**Objects and operators.** A realization writes the element as an array and decides nothing about how the array is used. The same $2 \times 2$ matrix $\Phi(\tilde q)$ is the split-quaternion written as an **object** — an array whose entries are its coordinates — and, once a column is placed beside it, the **operator** acting on that column. An operator appears exactly where an action on a carrier is specified; the carrier may be $\mathbb{R}^2$, a plane, or the algebra itself. This article supplies realizations and the module structures they define; the operator reading on the algebra — the adjoint action and the left and right multiplication operators — is the subject of *Split-Quaternion Rotations and the Lorentz Group*.

**Notation.** A general split-quaternion is

$$
\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q_0, q_1, q_2, q_3 \in \mathbb{R},
$$

with $q_0 = \operatorname{Sc}(\tilde q)$ the scalar part and $q_1 e_1 + q_2 e_2 + q_3 e_3 \in V$ the vector part. The basis satisfies $e_1^2 = -1$, $e_2^2 = e_3^2 = +1$, $e_3 = e_1 e_2$, $e_1 e_2 = -e_2 e_1$.

## The Clifford Algebra Representation

**Theorem.** The split-quaternion algebra is isomorphic to the Clifford algebra $\mathrm{Cl}_{1,1}$ of the form of signature $(1,1)$:

$$
\mathbb{H}_{\mathrm{s}} \;\cong\; \mathrm{Cl}_{1,1} \;\cong\; M_2(\mathbb{R}),
$$

the isomorphism sending the generators $f_1, f_2$ of $\mathrm{Cl}_{1,1}$ (with $f_1^2 = +1$, $f_2^2 = -1$, $f_1 f_2 = -f_2 f_1$) to $e_2, e_1$ respectively.

**Proof.** The elements $e_2$ and $e_1$ anticommute, with $e_2^2 = +1$ and $e_1^2 = -1$; they therefore satisfy the defining relations of the generators of $\mathrm{Cl}_{1,1}$ under the identification $f_1 = e_2$, $f_2 = e_1$. The products $1, e_1, e_2, e_1 e_2 = e_3$ form a real basis of $\mathbb{H}_{\mathrm{s}}$, matching the four basis monomials $1, f_2, f_1, f_1 f_2$ of $\mathrm{Cl}_{1,1}$; hence the map extends to an isomorphism. Both algebras are four-dimensional central simple and are isomorphic to $M_2(\mathbb{R})$, the unique such algebra of degree two.

**Proposition (the involutions are the Clifford involutions).** Under this isomorphism the three involutions of $\mathbb{H}_{\mathrm{s}}$ are the standard involutions of the Clifford algebra:

| involution of $\mathbb{H}_{\mathrm{s}}$ | Clifford involution |
|---|---|
| principal involution $\alpha$ | the grade (main) involution, $f_i \mapsto -f_i$ on vectors |
| reversal $\rho$ | the reversal (transpose) anti-automorphism |
| conjugation $\bar{\cdot}$ | the Clifford conjugation $= \alpha \circ \rho$ |

**Proof.** The grade involution negates the degree-one part, so it sends $e_1, e_2 \mapsto -e_1, -e_2$ and fixes $e_3 = e_1 e_2$, which is exactly $\alpha$. The reversal reverses each product of vectors, so it fixes $e_1, e_2$ and sends $e_3 = e_1 e_2 \mapsto e_2 e_1 = -e_3$, which is exactly $\rho$. The Clifford conjugation $\alpha\rho$ then negates all of $e_1, e_2, e_3$ and fixes $1$, which is exactly $\bar{\cdot}$.

### The Even Subalgebra

The **even subalgebra** $\mathrm{Cl}_{1,1}^+$ has basis $1, f_1 f_2 = e_2 e_1 = -e_3$, and is the two-dimensional commutative algebra with $(f_1f_2)^2 = f_1 f_2 f_1 f_2 = -f_1^2 f_2^2 = +1$, i.e. $\mathrm{Cl}_{1,1}^+ \cong \mathbb{D}$, the split-complex numbers. In $\mathbb{H}_{\mathrm{s}}$ this is the plane $\operatorname{span}\{1, e_3\} = \mathbb{D}_3$; the other split-complex plane $\mathbb{D}_2 = \operatorname{span}\{1, e_2\}$ is not generated by the chosen vector generators but is the even subalgebra of a differently based presentation of the same Clifford algebra (the two choices correspond to the two orderings of the generators, see the section on choices).

### The Split-Quaternion Norm and the Clifford Norm

The **Clifford norm** $\tilde q \mapsto \tilde q\bar{\tilde q}$ is the split-quaternion norm $N(\tilde q) = q_0^2 + q_1^2 - q_2^2 - q_3^2$ of signature $(2,2)$; it agrees with the split-quaternion norm and is the standard norm on $\mathrm{Cl}_{1,1}$. The norm-one elements $U = \{\, g : g\bar{g} = 1 \,\}$ are the group of **versors**, of dimension three, a proper subgroup of the unit group; they act on $V$ by the Lorentz action of *Split-Quaternion Rotations and the Lorentz Group*. The Clifford condition that $g\bar{g}$ be a scalar is automatic here, since $g\bar{g} = N(g)$ for every $g$, so the whole unit group acts on $V$ and the kernel of the action is the scalar line.

## The Clifford Module Structure

The algebra acts on itself by left multiplication, and the two minimal left ideals are the two **Clifford modules** of the algebra under this action.

**Definition.** A **left module** for $\mathbb{H}_{\mathrm{s}}$ is a real vector space $M$ with a bilinear map $\mathbb{H}_{\mathrm{s}} \times M \to M$, $(\tilde q, m) \mapsto \tilde q \cdot m$, satisfying $\tilde q \cdot (y \cdot m) = (\tilde q y) \cdot m$ and $1 \cdot m = m$.

**Theorem.** The algebra $\mathbb{H}_{\mathrm{s}} \cong M_2(\mathbb{R})$ has a unique simple left module up to isomorphism, of real dimension $2$, and the algebra is the direct sum of two copies of it as a left module:

$$
\mathbb{H}_{\mathrm{s}} = \mathbb{H}_{\mathrm{s}} \tilde\pi_+ \oplus \mathbb{H}_{\mathrm{s}} \tilde\pi_-, \qquad \tilde\pi_\pm = \tfrac{1}{2}(1 \pm e_2),
$$

the **minimal left ideals**, each $\mathbb{R}$-isomorphic to $\mathbb{R}^2$.

**Proof.** The classification of simple modules over $M_2(\mathbb{R})$ gives the uniqueness and dimension: $M_2(\mathbb{R})$ acts on the column space $\mathbb{R}^2$, and every simple module is isomorphic to it. The idempotents $\tilde\pi_\pm$ are orthogonal and sum to $1$ (verified from $e_2^2 = +1$), so $\mathbb{H}_{\mathrm{s}} = \mathbb{H}_{\mathrm{s}}\tilde\pi_+ \oplus \mathbb{H}_{\mathrm{s}}\tilde\pi_-$ as left modules; each summand is a nonzero left ideal, minimal because it is the image of a primitive idempotent.

The module realization is the split, real analogue of the biquaternion spinor representation: the simple module is real two-dimensional (where $\mathbb{B}$'s is complex two-dimensional), and the algebra acts on it by the $2 \times 1$ columns of the matrix model. The minimal left ideals and the idempotents are treated in *Split-Quaternion Idempotents and Projections* and *Split-Quaternion Ideals and Peirce Decomposition*.

### Module over the Split-Complex Algebra

Each split-complex plane $\mathbb{D}_k$ is a commutative subalgebra, and the algebra is a module over it by restriction of scalars: $\mathbb{D}_k \times \mathbb{H}_{\mathrm{s}} \to \mathbb{H}_{\mathrm{s}}$, $(z, \tilde q) \mapsto zx$. Since $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$, this makes $\mathbb{H}_{\mathrm{s}}$ a free module of rank two over $\mathbb{D}_k$, with basis $\{1, e_1\}$; the idempotent decomposition $\tilde q = \tilde q \tilde\pi_+ + \tilde q \tilde\pi_-$ is the separate decomposition of the regular module over itself into the two minimal left ideals. This is the module-theoretic form of the product-table entries $\mathbb{D}_k \cdot \mathbb{H}_{\mathrm{s}} \subseteq \mathbb{H}_{\mathrm{s}}$ of *Split-Quaternion Relations Between Subspaces*; the twisted multiplication which makes the plane a left module in a genuinely different way is treated in *Split-Quaternion Split-Complex Subspaces*.

## Relation to the Split-Complex and Matrix Models

The three pictures of the same element are:

| model | $1$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| Clifford $\mathrm{Cl}_{1,1}$ | $1$ | $f_2$ | $f_1$ | $f_1 f_2$ |
| matrix $\Phi$ | $I_2$ | $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ | $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ | $\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$ |
| idempotent components | $\tilde\pi_+ + \tilde\pi_-$ | $\Phi(e_1)$ | $\tilde\pi_+ - \tilde\pi_-$ | $\Phi(e_3)$ |

The first two rows are the Clifford and matrix models of *Split-Quaternion Matrix Element Representations*, where the matrix model is the defining representation $\Phi(q_0+q_1 e_1+q_2 e_2+q_3 e_3) = \begin{pmatrix} q_0-q_3 & q_2-q_1 \\ q_1+q_2 & q_0+q_3\end{pmatrix}$; the identification $\mathrm{Cl}_{1,1} \cong M_2(\mathbb{R})$ is realised concretely by sending $f_1 \mapsto \begin{pmatrix} 0&1\\1&0\end{pmatrix}$ and $f_2 \mapsto \begin{pmatrix} 0&-1\\1&0\end{pmatrix}$, so that the matrix row above is the image of the basis. The third row records the decomposition by the idempotents $\tilde\pi_\pm = \tfrac12(1\pm e_2)$, under which $1$ reads as $\tilde\pi_+ + \tilde\pi_-$ and $e_2$ as $\tilde\pi_+ - \tilde\pi_-$, giving the splitting of the algebra into its two minimal left ideals as left modules; the images under the matrix model are $\Phi(\tilde\pi_+) = \tfrac12\begin{pmatrix} 1&1\\1&1\end{pmatrix}$ and $\Phi(\tilde\pi_-) = \tfrac12\begin{pmatrix} 1&-1\\-1&1\end{pmatrix}$, the two rank-one projections.

## Relation to the Representations of $\mathbb{B}$

The biquaternion article *Biquaternion Other Algebraic Element Representations* treats the spinor, Clifford ($\mathrm{Cl}_{1,3}^+$) and conjugation-action realizations of $\mathbb{B}$. The split-quaternion list is shorter and differs in kind. First, the Clifford model here is $\mathrm{Cl}_{1,1}$, of split signature, in place of the definite $\mathrm{Cl}_{1,3}^+$; the involutions of the algebra become the standard Clifford involutions without any complex structure. Second, the simple module is real two-dimensional, in place of the complex two-dimensional spinor module of $\mathbb{B}$, and the natural module structure is the direct sum of two minimal left ideals from the idempotents $\tilde\pi_\pm$, which are non-central here whereas in $\mathbb{B}$ the corresponding idempotents are central. Third, the conjugation-action realization of $\mathbb{B}$ is, for $\mathbb{H}_{\mathrm{s}}$, the adjoint and multiplication-operator material of *Split-Quaternion Rotations and the Lorentz Group*, and is not repeated here. None of the biquaternion-specific structures — the central unit $i$, the Hermitian pairing, the chiral spinor halves — appears in the split-quaternion realization.

## The Role of Choices

The realizations above depend on choices, which must be recorded because they fix the correspondence between the abstract algebra and the concrete model.

- **The signature.** The identification $\mathbb{H}_{\mathrm{s}} \cong \mathrm{Cl}_{1,1}$ uses the generators with squares $+1$ and $-1$. Because $\mathrm{Cl}_{1,1} \cong \mathrm{Cl}_{2,0} \cong M_2(\mathbb{R})$ as algebras, the same algebra also arises as a Clifford algebra of definite signature; the *reflection* of the form used here is what makes $e_2^2 = +1$ rather than $-1$, and it is the reflection that produces the zero divisors. Either convention describes the same algebra, but the split signature is the one in which the quadratic form is indefinite and the isotropic structure is visible.
- **The naming of the generators.** The assignment $f_1 = e_2$, $f_2 = e_1$ is forced by the requirement that $f_1^2 = +1$; the opposite assignment interchanges the two split-complex planes $\mathbb{D}_2$ and $\mathbb{D}_3$ and the roles of $\tilde\pi_+$ and $\tilde\pi_-$. The basis $1, e_1, e_2, e_3$ of the algebra article is held fixed throughout the corpus.
- **The matrix model.** The matrices displayed for $e_1, e_2, e_3$ are one choice among several, related by conjugation; the invariants — the trace, the determinant, and the split-quaternion norm — are independent of the choice, while the images of the idempotents and of the planes depend on it.

## Summary

The split-quaternion algebra is the Clifford algebra $\mathrm{Cl}_{1,1}$ of split signature, isomorphic to $M_2(\mathbb{R})$; the isomorphism sends the Clifford generators $f_1, f_2$ to $e_2, e_1$. Under this identification the principal involution $\alpha$ is the grade involution, the reversal $\rho$ is the reversal anti-automorphism, and the conjugation $\bar{\cdot}$ is the Clifford conjugation $\alpha\rho$. The even subalgebra $\mathrm{Cl}_{1,1}^+$ is spanned by $1$ and $-e_3$ and is the split-complex algebra $\mathbb{D}_3$; the split-quaternion norm is the Clifford norm of signature $(2,2)$.

As a module over itself the algebra splits as the direct sum of the two minimal left ideals $\mathbb{H}_{\mathrm{s}}\tilde\pi_\pm$ built from the idempotents $\tilde\pi_\pm = \tfrac12(1\pm e_2)$, each the unique simple module of real dimension two; each split-complex plane makes the algebra a free module of rank two over $\mathbb{D}$. The Clifford, matrix and split-complex models of an element are tabulated above, and the realization differs from the biquaternion one in signature ($\mathrm{Cl}_{1,1}$ in place of $\mathrm{Cl}_{1,3}^+$), in the reality of the simple module, and in the non-centrality of the idempotents. The realizations depend on the signature convention, the naming of the generators and the matrix choice, all recorded above; the invariants are independent of the choices.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra | *Split-Quaternion Algebra* |
| $\mathrm{Cl}_{1,1}$ | the Clifford algebra of signature $(1,1)$, $\cong M_2(\mathbb{R})$ | this article |
| $f_1, f_2$ | Clifford generators, $f_1^2 = +1$, $f_2^2 = -1$ | this article |
| $\mathrm{Cl}_{1,1}^+$ | the even subalgebra, $\cong \mathbb{D}$ | this article |
| $\alpha, \rho, \bar{\cdot}$ | grade involution, reversal, Clifford conjugation | *Split-Quaternion Subspaces and the Involutions* |
| $\tilde\pi_\pm = \tfrac12(1\pm e_2)$ | the two idempotents and the minimal left ideals | *Split-Quaternion Idempotents and Projections* |
| $\mathbb{H}_{\mathrm{s}} \tilde\pi_\pm$ | the minimal left ideals | *Split-Quaternion Ideals and Peirce Decomposition* |
| $N(\tilde q)$ | the split-quaternion norm / Clifford norm, signature $(2,2)$ | *Split-Quaternion Norm and Invertibility* |
| $\Phi$ | the $2\times2$ real matrix model | *Split-Quaternion Matrix Element Representations* |
| $\mathbb{D}_2, \mathbb{D}_3$ | the split-complex planes | *Split-Quaternion Split-Complex Subspaces* |

## Further Reading

- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the isomorphism $\mathrm{Cl}_{1,1} \cong M_2(\mathbb{R})$, the Clifford involutions and the Clifford group of versors.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the low-dimensional Clifford algebra identifications and their signature choices.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for the classification of the real Clifford algebras and the role of the signature.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the simple modules over $M_2(\mathbb{R})$ and the idempotent decomposition of the algebra over itself.
