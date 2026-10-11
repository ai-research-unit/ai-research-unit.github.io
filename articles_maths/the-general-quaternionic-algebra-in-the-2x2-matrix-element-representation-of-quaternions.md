# __The General Quaternionic Algebra in the 2×2 Matrix Element Representation $M_2(\mathbb{C})$__

## Introduction

The quaternion algebra is embedded in the $2\times2$ complex matrices by the assignment that sends $e_0$ to the identity and $e_1,e_2,e_3$ to the negative imaginary multiples of the Pauli matrices (*The General Plain Algebra in the 2×2 Matrix Element Representation $M_2(\mathbb{C})$*, the companion reading of the plain algebra of quaternions). On that image the **quaternionic product** of the block is the matrix product with the conjugate transpose in the first slot, the **quaternionic form** is half the trace pairing with the conjugate transpose in the second slot, and the invariants of the element are the trace and the determinant of its image. This article reads the objects of the block — the product, the form, the units, the shell and the inner automorphisms — in the matrix model, and compares with the plain block and with the exact isomorphism of the biquaternion chapter.

**Conventions.** The embedding is $\mathsf{M}_2(e_0) = \mathbb{1}$ and $\mathsf{M}_2(e_k) = -i\sigma_k$; the conjugate transpose of a matrix is written ${}^{\dagger}$; the quaternionic product is $\tilde p \star \tilde q = \tilde p^{\natural}\tilde q$ and the quaternionic form is $N(\tilde p,\tilde q) = \mathrm{Sc}(\tilde p\tilde q^{\natural}) = \sum_\mu p_\mu q_\mu$, of signature $(4,0)$.

## The Embedding

**Definition.** The **matrix element representation** is the map $\mathsf{M}_2 : \mathbb{H} \to M_2(\mathbb{C})$ with $\mathsf{M}_2(e_0) = \mathbb{1}$, $\mathsf{M}_2(e_k) = -i\sigma_k$ for $k = 1,2,3$. In coordinates, $\mathsf{M}_2(\tilde q) = \begin{pmatrix}\alpha&\beta\\-\overline{\beta}&\overline{\alpha}\end{pmatrix}$ with $\alpha = q_0 - iq_3$ and $\beta = -iq_1 - q_2$.

**Theorem.** $\mathsf{M}_2$ is an injective real-algebra homomorphism, $\mathsf{M}_2(\tilde p\tilde q) = \mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q)$, with image the four-dimensional real subspace of matrices of the displayed shape; the plain product is the matrix product, and the conjugation is the conjugate transpose, $\mathsf{M}_2(\tilde q^{\natural}) = \mathsf{M}_2(\tilde q)^{\dagger}$.

*Proof.* The Pauli matrices satisfy $\sigma_k^2 = \mathbb{1}$ and $\sigma_1\sigma_2 = i\sigma_3$ with the cyclic companions, so the defining relations of $\mathbb{H}$ are respected; injectivity is read from the coordinates $q_0 = \mathrm{Re}\,\alpha$, $q_3 = -\mathrm{Im}\,\alpha$, $q_1 = -\mathrm{Im}\,\beta$, $q_2 = -\mathrm{Re}\,\beta$. The conjugate transpose of the displayed matrix has entries $\overline{\alpha}, -\beta$ and their companions, which is $\mathsf{M}_2(\tilde q^{\natural})$.

## The Quaternionic Product

**Theorem (the product in the model).** On the image the quaternionic product is the **transposed product**

$$
\mathsf{M}_2(\tilde p \star \tilde q) = \mathsf{M}_2(\tilde p^{\natural}\tilde q) = \mathsf{M}_2(\tilde p)^{\dagger}\,\mathsf{M}_2(\tilde q) ,
$$

the matrix product with the conjugate transpose taken in the first factor.

*Proof.* By multiplicativity of $\mathsf{M}_2$ and the correspondence of the conjugation with the dagger: $\mathsf{M}_2(\tilde p^{\natural}\tilde q) = \mathsf{M}_2(\tilde p^{\natural})\mathsf{M}_2(\tilde q) = \mathsf{M}_2(\tilde p)^{\dagger}\mathsf{M}_2(\tilde q)$.

**Corollary (the two slots and the two transposes).** The plain product inserts the identity in the first slot, $\mathsf{M}_2(\tilde p\tilde q) = \mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q)$, and the quaternionic product inserts the dagger there; consequently the quaternionic product is the plain product of the conjugated first factor, and the two products agree exactly on the Hermitian parameters, that is on the scalar line $S$.

*Proof.* The first statement is the plain sibling; the second is the definition; the third is $\mathsf{M}_2(\tilde p)^{\dagger} = \mathsf{M}_2(\tilde p)$, which is $\tilde p^{\natural} = \tilde p$, that is $\tilde p \in S$.

**Corollary (the square and the norm).** For every element,

$$
\mathsf{M}_2(\tilde q \star \tilde q) = \mathsf{M}_2(\tilde q)^{\dagger}\mathsf{M}_2(\tilde q) = N(\tilde q)\,\mathbb{1} ,
$$

a positive scalar matrix; the quaternionic square of an element is the scalar of its norm, and it vanishes exactly on the isotropic cone, which over the real quaternions is the single point $0$.

*Proof.* $\mathsf{M}_2(\tilde q^{\natural}\tilde q) = \mathsf{M}_2(N(\tilde q)e_0) = N(\tilde q)\mathbb{1}$, and $A^{\dagger}A$ is positive semidefinite with $\det = |\det A|^2 = N(\tilde q)^2 > 0$ for $\tilde q \neq 0$.

## The Form

**Theorem (the form in the model).** The quaternionic form is half the trace pairing with the dagger,

$$
N(\tilde p,\tilde q) = \mathrm{Sc}(\tilde p\tilde q^{\natural}) = \tfrac12\operatorname{tr}\bigl(\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q)^{\dagger}\bigr) .
$$

*Proof.* $\operatorname{tr}(\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q)^{\dagger}) = \operatorname{tr}(\mathsf{M}_2(\tilde p\tilde q^{\natural})) = 2\,\mathrm{Sc}(\tilde p\tilde q^{\natural}) = 2N(\tilde p,\tilde q)$, because the trace of a quaternion image is twice its scalar part.

**Theorem (the coefficient Gram matrix).** In the basis $e_0,e_1,e_2,e_3$,

$$
G_{\mu\nu} = \tfrac12\operatorname{tr}\bigl(\mathsf{M}_2(e_\mu)\mathsf{M}_2(e_\nu)^{\dagger}\bigr) = \mathbb{1}_4 ,
$$

of signature $(4,0)$; the Gram matrix is the identity and not the diagonal $D$ of the plain block.

*Proof.* $\mathsf{M}_2(e_0) = \mathbb{1}$ is self-adjoint of trace $2$, so the first entry is $1$. For a vector basis element, $\mathsf{M}_2(e_k)^{\dagger} = i\sigma_k = -\mathsf{M}_2(e_k)$, so $\operatorname{tr}(\mathsf{M}_2(e_k)\mathsf{M}_2(e_k)^{\dagger}) = \operatorname{tr}(\sigma_k^2) = 2$; distinct Pauli matrices have product of trace zero, so the off-diagonal entries vanish.

**Corollary (the comparison of the two forms).** The plain form is half the trace pairing without the dagger, $\mathrm B(\tilde p,\tilde q) = \tfrac12\operatorname{tr}(\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q))$, with Gram matrix $D = \operatorname{diag}(1,-1,-1,-1)$ of signature $(1,3)$; the quaternionic form is the same pairing with the dagger in the second slot, with Gram matrix $\mathbb{1}_4$ of signature $(4,0)$. The dagger is the matrix form of the conjugation that the quaternionic product takes in its first slot, and it is the whole difference of the two forms.

*Proof.* The plain statement is the companion reading; the identification of the quaternionic one is the theorem above, and $D$ versus $\mathbb{1}_4$ is read off the two computations.

## The Units, the Shell and the Invariants

**Theorem (trace and determinant).** For every $\tilde q$,

$$
\operatorname{tr}\mathsf{M}_2(\tilde q) = 2q_0 , \qquad \det\mathsf{M}_2(\tilde q) = N(\tilde q) ,
$$

so that the quaternionic form is the determinant of the image, read positively.

*Proof.* The trace is $\alpha + \overline{\alpha} = 2q_0$; the determinant is $\alpha\overline{\alpha} + \beta\overline{\beta} = (q_0^2+q_3^2) + (q_1^2+q_2^2) = N(\tilde q)$.

**Corollary (the units).** $\tilde q$ is a unit exactly when $\det\mathsf{M}_2(\tilde q) \neq 0$, that is exactly when $\mathsf{M}_2(\tilde q) \in GL_2(\mathbb{C})$; the image of the unit group is the group of matrices of the displayed shape with positive determinant, isomorphic to $\mathbb{H}^{\times}$.

*Proof.* $\det\mathsf{M}_2(\tilde q) = N(\tilde q) > 0$ for $\tilde q \neq 0$, and the image is closed under products and inverses.

**Theorem (the shell).** The shell $N = 1$ corresponds to the matrices of the image with $\det = 1$ and $A^{\dagger}A = \mathbb{1}$; it is the special unitary group,

$$
\mathsf{M}_2(\mathbb{H}^1) = SU(2) ,
$$

a compact group of real dimension three.

*Proof.* $A^{\dagger}A = \mathsf{M}_2(\tilde q)^{\dagger}\mathsf{M}_2(\tilde q) = \mathsf{M}_2(\tilde q^{\natural}\tilde q) = N(\tilde q)\mathbb{1}$, so on the shell $A$ is unitary; and $\det A = N(\tilde q) = 1$, so $A \in SU(2)$. Conversely a unitary matrix of the image has $N = \det = 1$.

**Corollary.** The pin and spin groups of the quaternionic form are the shell $\mathbb{H}^1$, by *The Pin and Spin Groups of the General Quaternionic Algebra of Quaternions*, above this article in this category, and the matrix model identifies them with $SU(2)$; the identification is the standard one of the unit quaternions with the special unitary group.

## The Inner Automorphisms

**Theorem (conjugation).** For a unit $\tilde q$ the inner automorphism corresponds to the conjugation by the matrix:

$$
\mathsf{M}_2(\operatorname{Ad}_{\tilde q}\tilde p) = \mathsf{M}_2(\tilde q)\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q)^{-1} .
$$

*Proof.* Multiplicativity of $\mathsf{M}_2$ and $\mathsf{M}_2(\tilde q^{-1}) = \mathsf{M}_2(\tilde q)^{-1}$.

**Corollary.** The inner automorphisms of the block are the conjugations of $M_2(\mathbb{C})$ that leave the real form $\mathsf{M}_2(\mathbb{H})$ stable; they use the plain product of the model, and their effect on the quaternionic form is the identity, since conjugation preserves the determinant and hence $N$.

## Comparison with the Plain Block and with the Biquaternion Chapter

**Proposition (the two blocks in the model).** The plain block and the quaternionic block act on the same image of the same matrix algebra and differ in the slot that carries the dagger.

| feature | plain block | quaternionic block |
|---|---|---|
| product | $\mathsf{M}_2(\tilde p\tilde q) = \mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q)$ | $\mathsf{M}_2(\tilde p \star \tilde q) = \mathsf{M}_2(\tilde p)^{\dagger}\mathsf{M}_2(\tilde q)$ |
| form | $\tfrac12\operatorname{tr}(\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q))$, Gram $D$, signature $(1,3)$ | $\tfrac12\operatorname{tr}(\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q)^{\dagger})$, Gram $\mathbb{1}_4$, signature $(4,0)$ |
| square | $\mathsf{M}_2(\tilde q^2)$ with $\det = N(\tilde q)^2$ | $\mathsf{M}_2(\tilde q \star \tilde q) = N(\tilde q)\mathbb{1}$ |
| shell | the unit sphere, the group of norm one | the same shell, read as $SU(2)$ |
| inner automorphisms | conjugation by $\mathsf{M}_2(\tilde q)$ | the same |

**Proposition (the biquaternion comparison).** Over the complex coefficient field the same matrix algebra is the biquaternion algebra, $\mathbb{B} \cong M_2(\mathbb{C})$ as a $\mathbb{C}$-algebra, with no dimension gap; the quaternionic form becomes a complex bilinear form with an isotropic cone, the dagger becomes one of the two conjugations, and the shell $N = 1$ becomes a non-compact complex quadric.

*Proof.* The isomorphism is the one of the biquaternion chapter; over $\mathbb{C}$ the quadratic form of four variables is isotropic and its level sets are quadrics rather than spheres.

## Summary

Under the embedding $\mathsf{M}_2(e_0) = \mathbb{1}$, $\mathsf{M}_2(e_k) = -i\sigma_k$, the quaternionic product of the block is the transposed product $\mathsf{M}_2(\tilde p \star \tilde q) = \mathsf{M}_2(\tilde p)^{\dagger}\mathsf{M}_2(\tilde q)$, the quaternionic form is half the trace pairing with the dagger in the second slot, $\tfrac12\operatorname{tr}(\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q)^{\dagger})$, with Gram matrix the identity of signature $(4,0)$, and the invariants are $\operatorname{tr}\mathsf{M}_2(\tilde q) = 2q_0$ and $\det\mathsf{M}_2(\tilde q) = N(\tilde q)$. The quaternionic square of an element is the positive scalar matrix $N(\tilde q)\mathbb{1}$; the units are the matrices of the image with positive determinant; the shell $N = 1$ is $SU(2)$, which is the pin and spin group of the form; the inner automorphisms are the conjugations by the image. The plain block uses the same embedding with the dagger removed, its form being half the trace pairing with the indefinite Gram matrix $D$; over $\mathbb{C}$ the same matrix algebra is the biquaternion algebra by an exact isomorphism.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathsf{M}_2$ | the matrix element representation $\mathbb{H} \to M_2(\mathbb{C})$ |
| $\dagger$ | the conjugate transpose, the image of the conjugation ${}^{\natural}$ |
| $\mathsf{M}_2(\tilde p \star \tilde q) = \mathsf{M}_2(\tilde p)^{\dagger}\mathsf{M}_2(\tilde q)$ | the quaternionic product in the model |
| $N(\tilde p,\tilde q) = \tfrac12\operatorname{tr}(\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q)^{\dagger})$ | the quaternionic form in the model |
| $\mathbb{1}_4$ | the Gram matrix of $N$, signature $(4,0)$ |
| $SU(2)$ | the image of the shell $\mathbb{H}^1$ |

## Further Reading

- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the Pauli-matrix representation of the quaternions and the unit sphere.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the embedding of the quaternions in $M_2(\mathbb{C})$, the real form and the special unitary group.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for representations of a division algebra and the trace pairing.
