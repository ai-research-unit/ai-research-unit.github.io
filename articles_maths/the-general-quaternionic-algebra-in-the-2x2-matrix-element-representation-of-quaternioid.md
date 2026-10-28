# __The General Quaternionic Algebra in the 2×2 Matrix Element Representation $M_2(\mathbb{C})$__

## Introduction

The quaternion algebra is embedded in the $2\times2$ complex matrices by the assignment that sends $e_t$ to the identity and $\vec e_x,\vec e_y,\vec e_z$ to the negative imaginary multiples of the Pauli matrices (*The General Plain Algebra in the 2×2 Matrix Element Representation $M_2(\mathbb{C})$*, the companion reading of the plain algebra of quaternions). On that image the **quaternionic product** of the block is the matrix product with the conjugate transpose in the first slot, the **quaternionic form** is half the trace pairing with the conjugate transpose in the second slot, and the invariants of the element are the trace and the determinant of its image.

## The Embedding

**Definition.** The **matrix element representation** is the map $\mathsf{M}_2 : \mathbb{H} \to M_2(\mathbb{C})$ with $\mathsf{M}_2(e_t) = \mathbb{1}$, $\mathsf{M}_2(\vec e_k) = -i\sigma_k$ for $k = 1,2,3$. In coordinates, $\mathsf{M}_2(\tilde q) = \begin{pmatrix}\alpha&\beta\\-\overline{\beta}&\overline{\alpha}\end{pmatrix}$ with $\alpha = q_t - iq_3$ and $\beta = -iq_1 - q_y$.

**Theorem.** $\mathsf{M}_2$ is an injective real-algebra homomorphism, $\mathsf{M}_2(\tilde q_1\tilde q_2) = \mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2)$, with image the four-dimensional real subspace of matrices of the displayed shape; the plain product is the matrix product, and the conjugation is the conjugate transpose, $\mathsf{M}_2(\tilde q^{\natural}) = \mathsf{M}_2(\tilde q)^{\dagger}$.

*Proof.* The Pauli matrices satisfy $\sigma_k^2 = \mathbb{1}$ and $\sigma_1\sigma_2 = i\sigma_3$ with the cyclic companions, so the defining relations of $\mathbb{H}$ are respected; injectivity is read from the coordinates $q_t = \mathrm{Re}\,\alpha$, $q_z = -\mathrm{Im}\,\alpha$, $q_x = -\mathrm{Im}\,\beta$, $q_y = -\mathrm{Re}\,\beta$. The conjugate transpose of the displayed matrix has entries $\overline{\alpha}, -\beta$ and their companions, which is $\mathsf{M}_2(\tilde q^{\natural})$.

## The Quaternionic Product

**Theorem (the product in the model).** On the image the quaternionic product is the **transposed product**

$$
\boxed{\;\mathsf{M}_2(\tilde q_1 \star \tilde q_2) = \mathsf{M}_2(\tilde q_1^{\natural}\tilde q_2) = \mathsf{M}_2(\tilde q_1)^{\dagger}\,\mathsf{M}_2(\tilde q_2)\;},
$$

the matrix product with the conjugate transpose taken in the first factor.

*Proof.* By multiplicativity of $\mathsf{M}_2$ and the correspondence of the conjugation with the dagger: $\mathsf{M}_2(\tilde q_1^{\natural}\tilde q_2) = \mathsf{M}_2(\tilde q_1^{\natural})\mathsf{M}_2(\tilde q_2) = \mathsf{M}_2(\tilde q_1)^{\dagger}\mathsf{M}_2(\tilde q_2)$.

**Corollary (the two slots and the two transposes).** The plain product inserts the identity in the first slot, $\mathsf{M}_2(\tilde q_1\tilde q_2) = \mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2)$, and the quaternionic product inserts the dagger there; consequently the quaternionic product is the plain product of the conjugated first factor, and the two products agree exactly on the Hermitian parameters, that is on the scalar line $S$.

*Proof.* The first statement is the plain sibling; the second is the definition; the third is $\mathsf{M}_2(\tilde q_1)^{\dagger} = \mathsf{M}_2(\tilde q_1)$, which is $\tilde q_1^{\natural} = \tilde q_1$, that is $\tilde q_1 \in S$.

**Corollary (the square and the norm).** For every element,

$$
\mathsf{M}_2(\tilde q \star \tilde q) = \mathsf{M}_2(\tilde q)^{\dagger}\mathsf{M}_2(\tilde q) = \langle\tilde q\rangle_{\natural}\,\mathbb{1} ,
$$

a positive scalar matrix; the quaternionic square of an element is the scalar of its norm, and it vanishes exactly on the isotropic cone, which over the real quaternions is the single point $0$.

*Proof.* $\mathsf{M}_2(\tilde q^{\natural}\tilde q) = \mathsf{M}_2(\langle\tilde q\rangle_{\natural}e_t) = \langle\tilde q\rangle_{\natural}\mathbb{1}$, and $A^{\dagger}A$ is positive semidefinite with $\det = |\det A|^2 = \langle\tilde q\rangle_{\natural}^2 > 0$ for $\tilde q \neq 0$.

## The Form

**Theorem (the form in the model).** The quaternionic form is half the trace pairing with the dagger,

$$
\boxed{\;\langle\tilde q_1,\tilde q_2\rangle_{\natural} = \mathrm{Sc}(\tilde q_1\tilde q_2^{\natural}) = \tfrac12\operatorname{tr}\bigl(\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2)^{\dagger}\bigr)\;}.
$$

*Proof.* $\operatorname{tr}(\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2)^{\dagger}) = \operatorname{tr}(\mathsf{M}_2(\tilde q_1\tilde q_2^{\natural})) = 2\,\mathrm{Sc}(\tilde q_1\tilde q_2^{\natural}) = 2\langle\tilde q_1,\tilde q_2\rangle_{\natural}$, because the trace of a quaternion image is twice its scalar part.

**Theorem (the coefficient Gram matrix).** In the basis $e_t,\vec e_x,\vec e_y,\vec e_z$,

$$
G_{\mu\nu} = \tfrac12\operatorname{tr}\bigl(\mathsf{M}_2(e_\mu)\mathsf{M}_2(e_\nu)^{\dagger}\bigr) = \mathbb{1}_4 ,
$$

of signature $(4,0)$; the Gram matrix is the identity and not the diagonal $D$ of the plain block.

*Proof.* $\mathsf{M}_2(e_t) = \mathbb{1}$ is self-adjoint of trace $2$, so the first entry is $1$. For a vector basis element, $\mathsf{M}_2(\vec e_k)^{\dagger} = i\sigma_k = -\mathsf{M}_2(\vec e_k)$, so $\operatorname{tr}(\mathsf{M}_2(\vec e_k)\mathsf{M}_2(\vec e_k)^{\dagger}) = \operatorname{tr}(\sigma_k^2) = 2$; distinct Pauli matrices have product of trace zero, so the off-diagonal entries vanish.

**Corollary (the comparison of the two forms).** The plain form is half the trace pairing without the dagger, $\langle\tilde q_1,\tilde q_2\rangle = \tfrac12\operatorname{tr}(\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2))$, with Gram matrix $D = \operatorname{diag}(1,-1,-1,-1)$ of signature $(1,3)$; the quaternionic form is the same pairing with the dagger in the second slot, with Gram matrix $\mathbb{1}_4$ of signature $(4,0)$. The dagger is the matrix form of the conjugation that the quaternionic product takes in its first slot, and it is the whole difference of the two forms.

*Proof.* The plain statement is the companion reading; the identification of the quaternionic one is the theorem above, and $D$ versus $\mathbb{1}_4$ is read off the two computations.

## The Units, the Shell and the Invariants

**Theorem (trace and determinant).** For every $\tilde q$,

$$
\boxed{\;\operatorname{tr}\mathsf{M}_2(\tilde q) = 2q_t , \qquad \det\mathsf{M}_2(\tilde q) = \langle\tilde q\rangle_{\natural}\;},
$$

so that the quaternionic form is the determinant of the image, read positively.

*Proof.* The trace is $\alpha + \overline{\alpha} = 2q_t$; the determinant is $\alpha\overline{\alpha} + \beta\overline{\beta} = (q_t^2+q_z^2) + (q_x^2+q_y^2) = \langle\tilde q\rangle_{\natural}$.

**Corollary (the units).** $\tilde q$ is a unit exactly when $\det\mathsf{M}_2(\tilde q) \neq 0$, that is exactly when $\mathsf{M}_2(\tilde q) \in GL_2(\mathbb{C})$; the image of the unit group is the group of matrices of the displayed shape with positive determinant, isomorphic to $\mathbb{H}^{\times}$.

*Proof.* $\det\mathsf{M}_2(\tilde q) = \langle\tilde q\rangle_{\natural} > 0$ for $\tilde q \neq 0$, and the image is closed under products and inverses.

**Theorem (the shell).** The shell $N = 1$ corresponds to the matrices of the image with $\det = 1$ and $A^{\dagger}A = \mathbb{1}$; it is the special $*$-unitary group,

$$
\boxed{\;\mathsf{M}_2(\mathbb{H}^1) = SU(2)\;},
$$

a compact group of real dimension three.

*Proof.* $A^{\dagger}A = \mathsf{M}_2(\tilde q)^{\dagger}\mathsf{M}_2(\tilde q) = \mathsf{M}_2(\tilde q^{\natural}\tilde q) = \langle\tilde q\rangle_{\natural}\mathbb{1}$, so on the shell $A$ is $*$-unitary; and $\det A = \langle\tilde q\rangle_{\natural} = 1$, so $A \in SU(2)$. Conversely a $*$-unitary matrix of the image has $N = \det = 1$.

**Corollary.** The pin and spin groups of the quaternionic form are the shell $\mathbb{H}^1$, by *The Pin and Spin Groups of the General Quaternionic Algebra*, above this article in this category, and the matrix model identifies them with $SU(2)$; the identification is the standard one of the unit quaternions with the special $*$-unitary group.

## The Inner Automorphisms

**Theorem (conjugation).** For a unit $\tilde q_1$ the inner automorphism corresponds to the conjugation by the matrix:

$$
\mathsf{M}_2(\operatorname{Ad}_{\tilde q_1}\tilde q_2) = \mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2)\mathsf{M}_2(\tilde q_1)^{-1} .
$$

*Proof.* Multiplicativity of $\mathsf{M}_2$ and $\mathsf{M}_2(\tilde q_1^{-1}) = \mathsf{M}_2(\tilde q_1)^{-1}$.

**Corollary.** The inner automorphisms of the block are the conjugations of $M_2(\mathbb{C})$ that leave the real form $\mathsf{M}_2(\mathbb{H})$ stable; they use the plain product of the model, and their effect on the quaternionic form is the identity, since conjugation preserves the determinant and hence $\langle\cdot,\cdot\rangle_{\natural}$.

## Summary

Under the embedding $\mathsf{M}_2(e_t) = \mathbb{1}$, $\mathsf{M}_2(\vec e_k) = -i\sigma_k$, the quaternionic product of the block is the transposed product $\mathsf{M}_2(\tilde q_1 \star \tilde q_2) = \mathsf{M}_2(\tilde q_1)^{\dagger}\mathsf{M}_2(\tilde q_2)$, the quaternionic form is half the trace pairing with the dagger in the second slot, $\tfrac12\operatorname{tr}(\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2)^{\dagger})$, with Gram matrix the identity of signature $(4,0)$, and the invariants are $\operatorname{tr}\mathsf{M}_2(\tilde q) = 2q_t$ and $\det\mathsf{M}_2(\tilde q) = \langle\tilde q\rangle_{\natural}$. The quaternionic square of an element is the positive scalar matrix $\langle\tilde q\rangle_{\natural}\mathbb{1}$; the units are the matrices of the image with positive determinant; the shell $N = 1$ is $SU(2)$, which is the pin and spin group of the form; the inner automorphisms are the conjugations by the image.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathsf{M}_2$ | the matrix element representation $\mathbb{H} \to M_2(\mathbb{C})$ |
| $\dagger$ | the conjugate transpose, the image of the conjugation ${}^{\natural}$ |
| $\mathsf{M}_2(\tilde q_1 \star \tilde q_2) = \mathsf{M}_2(\tilde q_1)^{\dagger}\mathsf{M}_2(\tilde q_2)$ | the quaternionic product in the model |
| $\langle\tilde q_1,\tilde q_2\rangle_{\natural} = \tfrac12\operatorname{tr}(\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2)^{\dagger})$ | the quaternionic form in the model |
| $\mathbb{1}_4$ | the Gram matrix of $\langle\cdot,\cdot\rangle_{\natural}$, signature $(4,0)$ |
| $SU(2)$ | the image of the shell $\mathbb{H}^1$ |

## Further Reading

- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the Pauli-matrix representation of the quaternions and the unit sphere.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the embedding of the quaternions in $M_2(\mathbb{C})$, the real form and the special $*$-unitary group.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for representations of a division algebra and the trace pairing.
