# __The Isotropic Structure of the General Quaternionic Algebra__

## Introduction

The general quaternionic bilinear product $\tilde p \star \tilde q = \tilde p^{\natural}\tilde q$ of *Introduction to the General Quaternionic Algebra of Quaternions* carries a degree-two structure, and it is the **quaternionic bilinear form** of the space: the polar form of the norm, equivalently the central coefficient of the symmetrisation,

$$
N(\tilde p,\tilde q) = \beta(\tilde p,\tilde q) = \tfrac12\bigl(N(\tilde p+\tilde q) - N(\tilde p) - N(\tilde q)\bigr) = p_0q_0 + \mathbf p \cdot \mathbf q , \qquad \tilde p \bullet \tilde q = \beta(\tilde p,\tilde q)e_0 .
$$

The form is one of the two degree-two forms of the quaternion real space (*The 2 Forms over the Quaternion $\mathbb{R}$ Space*), and its diagonal is the second of the two algebraic norms (*The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space*); it is quoted from those articles and not re-derived.

The structure is trivial in one sense and not in another. Over $\mathbb{R}$ the quaternionic form is **positive definite**, so its isotropic elements reduce to the origin and its radical is trivial: the isotropic structure of this block is empty. But the plain form of the *same* space is indefinite of signature $(1,3)$, with an isotropic cone of real dimension three; the two forms are different degree-two structures on one and the same vector space, and the article is written for that disagreement. The definiteness of the quaternionic form is also the algebraic content of the division property of $\mathbb{H}$, and it is what the change of scalars to $\mathbb{C}$, which makes the form isotropic, undoes.

## The Form of the Quaternionic Product

**Definition.** The **quaternionic bilinear form** of the block is the symmetric $\mathbb{R}$-bilinear form

$$
N(\tilde p,\tilde q) = p_0q_0 + \mathbf p \cdot \mathbf q ,
$$

the polar form of the quaternionic bilinear algebraic norm $N(\tilde p) = N(\tilde p,\tilde p) = p_0^2 + \mathbf p \cdot \mathbf p$.

**Theorem (the class of the form).** The form is symmetric, $\mathbb{R}$-bilinear, positive definite and non-degenerate. It is the symmetrisation of the product in the sense that $\tfrac12(\tilde p \star \tilde q + \tilde q \star \tilde p) = N(\tilde p,\tilde q)e_0$; it is the quadratic form associated with the product by the standard polarisation, and its diagonal is the norm that the product carries.

*Proof.* The coordinate expression is symmetric and bilinear; positive definiteness is the sum of squares $p_0^2 + p_1^2 + p_2^2 + p_3^2$, which vanishes only at $\tilde p = 0$; non-degeneracy follows, since a definite form has trivial radical. The identification with the symmetrisation is the lemma of *The Symmetrised Quaternionic Product and the Hermitian Subspace*.

**Remark.** The form is the Euclidean inner product of the coordinate space $\mathbb{H} \cong \mathbb{R}^4$ read in the basis of units, so its Gram matrix in the basis $e_0,e_1,e_2,e_3$ is the identity and its signature is $(4,0)$.

## The Isotropic Elements

**Definition.** An element $\tilde p$ is **isotropic** for the form when $N(\tilde p,\tilde p) = 0$, that is when $N(\tilde p) = 0$.

**Theorem (no isotropic element but zero).** Over $\mathbb{R}$ the only isotropic element of the quaternionic form is $\tilde p = 0$. The form is anisotropic, and the isotropic set is the origin of $\mathbb{H}$.

*Proof.* $N(\tilde p)$ is a sum of four squares of real numbers, and a sum of squares of reals vanishes only when every square vanishes.

**Corollary (the radical).** The radical of the form, the set of elements orthogonal to the whole space, is trivial: $\{\tilde p : N(\tilde p,\tilde q) = 0 \ \text{for every} \ \tilde q\} = \{0\}$. The form is non-degenerate, its Gram matrix is invertible, and there is no isotropic direction and no null line in the block.

*Proof.* Positive definiteness gives non-degeneracy at once; explicitly, an element orthogonal to each $e_\mu$ has all four coordinates zero.

**Corollary (the reading on the product).** The form is the exact measure of the division property. An element is a zero divisor of the product exactly when it is isotropic or orthogonal to an isotropic element, and there are none: $\tilde p \star \tilde q = 0$ implies $N(\tilde p)N(\tilde q) = 0$, hence $\tilde p = 0$ or $\tilde q = 0$ (*Norm and Invertibility in the General Quaternionic Algebra*). The absence of isotropic elements and the absence of zero divisors are the same statement about the form.

## The Comparison with the Plain Form

The plain product of the same space carries the other degree-two form, the **plain bilinear form**, whose diagonal is the plain algebraic norm $\tilde p^2$ with scalar part $p_0^2 - \mathbf p \cdot \mathbf p$ and whose signature is $(1,3)$ (*The 2 Forms over the Quaternion $\mathbb{R}$ Space*).

| | quaternionic form $N$ | plain form $B$ |
|---|---|---|
| coordinate expression | $p_0q_0 + \mathbf p \cdot \mathbf q$ | $p_0q_0 - \mathbf p \cdot \mathbf q$ |
| signature | $(4,0)$ | $(1,3)$ |
| definiteness | positive definite | indefinite |
| isotropic elements | $\{0\}$ only | the cone $p_0^2 = \mathbf p \cdot \mathbf p$ |
| radical | $\{0\}$ | $\{0\}$ |
| Gram matrix | $\mathrm I_4$ | $\mathrm{diag}(1,-1,-1,-1)$ |

**Theorem (the two forms disagree).** The two forms have the same radical and opposite definiteness. The isotropic set of the plain form is the **null cone** $p_0^2 = \mathbf p \cdot \mathbf p$, a set of real dimension three in $\mathbb{H} \cong \mathbb{R}^4$; the isotropic set of the quaternionic form is the origin alone. Both forms are non-degenerate and their Gram matrices are invertible.

*Proof.* The two coordinate expressions differ in the sign of the vector part, so their signatures are $(4,0)$ and $(1,3)$; the null cone of a form of signature $(1,3)$ is the level set $p_0^2 - \mathbf p \cdot \mathbf p = 0$, nonempty and three-dimensional, and the definite form has no nonzero zero.

**Remark.** The article exists for this table and for nothing else. On one and the same four-dimensional real space there are two degree-two forms, one with an isotropic cone and one without, and the two arise from the two bilinear products of the space: the quaternionic product symmetrises to the definite one, the plain product to the indefinite one. The choice of the product is therefore also the choice of the form, and the definiteness of the quaternionic form is the algebraic face of the division property of $\mathbb{H}$.

## The Relation to the Norm

**Theorem (multiplicativity and the form).** The product scales the form by the product of the norms: $N(\tilde p \star \tilde q) = N(\tilde p)N(\tilde q)$, so the product is a similarity of the form with ratio $N(\tilde q)$ on the left factor and $N(\tilde p)$ on the right one. The group of linear maps $T$ of $\mathbb{H}$ preserving the form is given algebraically by the matrix condition $T^{\mathsf T}T = \mathrm I_4$.

*Proof.* Multiplicativity is the theorem of *Norm and Invertibility in the General Quaternionic Algebra*; the matrix condition is the preservation of the quadratic form $N$, whose Gram matrix is $\mathrm I_4$; a linear map preserves $N$ exactly when its matrix $T$ satisfies $T^{\mathsf T}T = \mathrm I_4$.

**Corollary (the shells).** The level sets $N = \lambda$ of the form are the shells of the norm, and they are the root sets of the central values of the square, the shell $N = 1$ being the root set of $+1$ (*Square Roots of One and the Idempotents of the General Quaternionic Algebra*). The shells of the form are the sets that the pin and spin construction of the block uses, and they are nonempty only for $\lambda \geq 0$; the construction is *The Pin and Spin Groups of the General Quaternionic Algebra of Quaternions*, below this article in this category.

**Remark.** The form is definite, so its shells are the level sets of a proper quadratic form and carry no null direction; a generator of a shell is an element with $N \neq 0$, hence with an inverse in the sense of the two one-sided equations, and the group of linear maps preserving the form carries one shell to another. The metric language of the shells, with its limits and its topology, is not used here and belongs to the topology of the quaternions.

## Summary

The form of the general quaternionic algebra is the quaternionic bilinear form $N(\tilde p,\tilde q) = p_0q_0 + \mathbf p \cdot \mathbf q$, the polar form of the norm and the central coefficient of the symmetrisation. It is symmetric, positive definite, non-degenerate, of signature $(4,0)$ and Gram matrix $\mathrm I_4$; its only isotropic element is $0$ and its radical is trivial, so the isotropic structure of the block is empty. The plain form of the same space is the same expression with the sign of the vector part reversed, of signature $(1,3)$ and with the null cone $p_0^2 = \mathbf p \cdot \mathbf p$ as its isotropic set; the two forms have the same radical, opposite definiteness, and they are the degree-two structures of the two bilinear products of the space. The form scales under the product, $N(\tilde p \star \tilde q) = N(\tilde p)N(\tilde q)$, its shells are the root sets of the squares, and its preservation is the matrix condition $T^{\mathsf T}T = \mathrm I_4$. Over $\mathbb{C}$ the form becomes isotropic, with a cone for its isotropic set and zero divisors for the product; the emptiness of the isotropic structure is therefore a property of the real member alone.

## Summary of Notation

| symbol | meaning |
|---|---|
| $N(\tilde p,\tilde q) = p_0q_0 + \mathbf p \cdot \mathbf q$ | the quaternionic bilinear form of the block |
| $N(\tilde p) = N(\tilde p,\tilde p) = \sum_\mu p_\mu^2$ | its diagonal, the quaternionic bilinear algebraic norm |
| $B(\tilde p,\tilde q) = p_0q_0 - \mathbf p \cdot \mathbf q$ | the plain bilinear form of the same space |
| isotropic element | an element with $N(\tilde p) = 0$, here only $0$ |
| radical | the set orthogonal to the whole space, here $\{0\}$ |
| shell | a level set $N = \lambda$ of the form |

## Further Reading

- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the definite norm form of the quaternion algebra and its unit shells.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the norm form of a quaternion algebra and its isotropy over a splitting field.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the quadratic form of a nonassociative algebra and its radical.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the isotopy of a product and the isometry of its norm form.
