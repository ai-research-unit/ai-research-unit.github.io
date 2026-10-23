# __The Quaternion Algebra in the 2×2 Matrix Element Representation $M_2(\mathbb{C})$__

## Introduction

The quaternion algebra is embedded in the $2\times2$ complex matrices by the assignment that sends $e_t$ to the identity and $\vec e_x,\vec e_y,\vec e_z$ to the negative imaginary multiples of the Pauli matrices. On that image the quaternion product is the matrix product, the plain form is half the trace pairing, and the invariants of the quaternion are the trace and the determinant of its image. The norm and the invertibility criterion are *Norm and Invertibility in the Quaternion Algebra*, above this article in this category; the form and the transpose are *Association and the Transpose on the Quaternion Algebra*, above this article in this category; the operators are *Two-Sided Operators on the Quaternion Algebra*, above this article in this category; the left regular model is *The Quaternion Algebra in the 4×4 Matrix Element Representation $M_4(\mathbb{R})_L$*, below this article in this category.

## The Embedding

**Definition.** The **matrix element representation** is the map

$$
\mathsf{M}_2:\mathbb{H}\to M_2(\mathbb{C}),\qquad \mathsf{M}_2(e_t)=\mathbb{1},\quad \mathsf{M}_2(\vec e_\mu)=-i\sigma_\mu\ (k=1,2,3),
$$

with $\sigma_1,\sigma_2,\sigma_3$ the Pauli matrices. In coordinates,

$$
\mathsf{M}_2(\tilde q)=\begin{pmatrix}\alpha&\beta\\-\overline{\beta}&\overline{\alpha}\end{pmatrix},\qquad \alpha=q_t-iq_z,\quad \beta=-iq_x-q_y.
$$

**Theorem.** $\mathsf{M}_2$ is an injective $\mathbb{R}$-algebra homomorphism, $\mathsf{M}_2(\tilde q_1\tilde q_2)=\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2)$; its image is the real four-dimensional subspace

$$ \boxed{\; \mathsf{M}_2(\mathbb{H})=\Bigl\{\begin{pmatrix}\alpha&\beta\\-\overline{\beta}&\overline{\alpha}\end{pmatrix}:\alpha,\beta\in\mathbb{C}\Bigr\} \;} .$$

*Proof.* The Pauli matrices satisfy $\sigma_\mu^2=\mathbb{1}$ and $\sigma_1\sigma_2=i\sigma_3$ with the cyclic companions, so $\mathsf{M}_2(\vec e_\mu)^2=-\mathbb{1}$ and $\mathsf{M}_2(\vec e_x)\mathsf{M}_2(\vec e_y)=\mathsf{M}_2(\vec e_z)=-\mathsf{M}_2(\vec e_y)\mathsf{M}_2(\vec e_x)$; the defining relations of $\mathbb{H}$ are respected, and a bilinear map respecting them is a homomorphism. The image is as displayed by expanding, and $\alpha,\beta$ are free complex parameters, so the real dimension is $4$; injectivity is read from the coordinates: $q_t=\mathrm{Re}\,\alpha$, $q_z=-\mathrm{Im}\,\alpha$, $q_x=-\mathrm{Im}\,\beta$, $q_y=-\mathrm{Re}\,\beta$, so $\mathsf{M}_2(\tilde q)=0$ forces $\tilde q=0$.

**Corollary (the dimensions).** The image has real dimension $4$; it is a real form inside the complex four-dimensional algebra $M_2(\mathbb{C})$, so its complex span is all of $M_2(\mathbb{C})$, and the entries $\alpha,\beta$ are two complex coordinates while the quaternion has four real ones.

*Proof.* The image is closed under no multiplication by $i$ in general: $i\,\mathsf{M}_2(\vec e_x)$ is not of the displayed shape; hence the complex span is larger, and it contains $\mathbb{1}$, $\sigma_\mu$, so it is $M_2(\mathbb{C})$.

## The Product

**Theorem.** The quaternion product corresponds to the matrix product: $\mathsf{M}_2(\tilde q_1\tilde q_2)=\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2)$. In particular $\mathsf{M}_2$ is multiplicative, carries the unit $e_t$ to the identity matrix, and the conjugate corresponds to the conjugate transpose, $\mathsf{M}_2(\tilde q^{\natural})=\mathsf{M}_2(\tilde q)^{\dagger}$.

*Proof.* The multiplicativity is the theorem above; for the conjugate, $\mathsf{M}_2(\tilde q^{\natural})$ has entries $\overline{\alpha},-\beta$ and their companions, which is $\mathsf{M}_2(\tilde q)^{\dagger}$.

## The Form

**Theorem.** The plain form is half the trace pairing:

$$ \boxed{\; \langle\tilde q_1,\tilde q_2\rangle=\mathrm{Sc}(\tilde q_1\tilde q_2)=\tfrac12\operatorname{tr}\bigl(\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2)\bigr) \;} .$$

*Proof.* $\operatorname{tr}(\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2))=\operatorname{tr}(\mathsf{M}_2(\tilde q_1\tilde q_2))=2(\tilde q_1\tilde q_2)_t=2\,\mathrm{Sc}(\tilde q_1\tilde q_2)$, because the trace of a quaternion image is twice its scalar part, as the diagonal entries $\alpha,\overline{\alpha}$ show.

**Theorem (the coefficient Gram matrix).** In the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ the Gram matrix of $\mathrm B$ is

$$
G_{\mu\nu}=\tfrac12\operatorname{tr}\bigl(\mathsf{M}_2(e_\mu)\mathsf{M}_2(e_\nu)\bigr)=\operatorname{diag}(1,-1,-1,-1)=D,
$$

of signature $(1,3)$.

*Proof.* $\mathsf{M}_2(e_t)=\mathbb{1}$ has trace $2$; $\mathsf{M}_2(\vec e_\mu)=-i\sigma_\mu$ is traceless with square $-\mathbb{1}$, so $\operatorname{tr}(\mathsf{M}_2(\vec e_\mu)^2)=-2$ and $\operatorname{tr}(\mathsf{M}_2(\vec e_\mu)\mathsf{M}_2(\vec e_\nu))=0$ for $\mu\neq\nu$ because distinct Pauli matrices have vanishing trace of their product.

**Corollary.** The form is indefinite; the trace pairing is the complex-linear extension of the same form, and its restriction to the image is $\mathrm B$ up to the factor two.

## The Units and the Invariants

**Theorem (trace and determinant).** For every $\tilde q$,

$$ \boxed{\; \operatorname{tr}\mathsf{M}_2(\tilde q)=2q_t,\qquad \det\mathsf{M}_2(\tilde q)=\langle\tilde q\rangle_{\natural}=q_t^2+q_x^2+q_y^2+q_z^2 \;} .$$

*Proof.* The trace is $\alpha+\overline{\alpha}=2\mathrm{Re}\,\alpha=2q_t$. The determinant is $\alpha\overline{\alpha}+\beta\overline{\beta}=|\alpha|^2+|\beta|^2=(q_t^2+q_z^2)+(q_x^2+q_y^2)=\langle\tilde q\rangle_{\natural}$, the second term because $-\overline{\beta}$ is the companion of $\beta$.

**Corollary.** $\tilde q$ is a unit exactly when $\det\mathsf{M}_2(\tilde q)\neq0$, that is exactly when $\mathsf{M}_2(\tilde q)\in GL_2(\mathbb{C})$; the determinant is positive, so the image of the group of units is the subgroup of $GL_2(\mathbb{C})$ of matrices of the displayed shape with positive determinant, isomorphic to $\mathbb{H}^{\times}$.

*Proof.* $\det\mathsf{M}_2(\tilde q)=\langle\tilde q\rangle_{\natural}>0$ for $\tilde q\neq0$; the determinant is multiplicative and the image is closed under products and inverses.

## The Inner Automorphisms and the Transpose as Form-Preserving Maps

**Theorem (conjugation).** For a unit $\tilde q$ the inner automorphism $\operatorname{Ad}_{\tilde q}$ corresponds to conjugation by the matrix $\mathsf{M}_2(\tilde q)$:

$$ \boxed{\; \mathsf{M}_2(\operatorname{Ad}_{\tilde q}\tilde p)=\mathsf{M}_2(\tilde q)\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q)^{-1} \;} .$$

*Proof.* Multiplicativity and $\mathsf{M}_2(\tilde q^{-1})=\mathsf{M}_2(\tilde q)^{-1}$.

**Theorem.** Conjugation by $\mathsf{M}_2(\tilde q)$ and the transpose preserve the trace pairing on $M_2(\mathbb{C})$; the conjugate transpose corresponds to the natural sign.

*Proof.* $\operatorname{tr}(\mathsf{M}_2(\tilde q)X\mathsf{M}_2(\tilde q)^{-1}\,\mathsf{M}_2(\tilde q)Y\mathsf{M}_2(\tilde q)^{-1})=\operatorname{tr}(\mathsf{M}_2(\tilde q)XY\mathsf{M}_2(\tilde q)^{-1})=\operatorname{tr}(XY)$; and $\operatorname{tr}(X^{\mathsf T}Y^{\mathsf T})=\operatorname{tr}((YX)^{\mathsf T})=\operatorname{tr}(YX)=\operatorname{tr}(XY)$. The last statement is the correspondence $\mathsf{M}_2(\tilde q^{\natural})=\mathsf{M}_2(\tilde q)^{\dagger}$ above.

**Corollary.** The inner automorphisms of $\mathbb{H}$ are the inner automorphisms of $M_2(\mathbb{C})$ that leave the real form $\mathsf{M}_2(\mathbb{H})$ stable, and they preserve the form $\mathrm B$; the transpose and the conjugate transpose likewise preserve the trace pairing.

## Summary

The embedding $\mathsf{M}_2$ with $\mathsf{M}_2(e_t)=\mathbb{1}$ and $\mathsf{M}_2(\vec e_\mu)=-i\sigma_\mu$ is an injective real-algebra homomorphism of $\mathbb{H}$ into $M_2(\mathbb{C})$, with image the matrices $\begin{pmatrix}\alpha&\beta\\-\overline{\beta}&\overline{\alpha}\end{pmatrix}$ of real dimension four whose complex span is the whole matrix algebra. On the image the quaternion product is the matrix product, the plain form is $\langle\tilde q_1,\tilde q_2\rangle=\tfrac12\operatorname{tr}(\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2))$ with Gram matrix $D=\operatorname{diag}(1,-1,-1,-1)$ of signature $(1,3)$, and the invariants are $\operatorname{tr}\mathsf{M}_2(\tilde q)=2q_t$ and $\det\mathsf{M}_2(\tilde q)=\langle\tilde q\rangle_{\natural}$. The unit group maps onto the matrices of the image with positive determinant; the inner automorphisms become conjugations by those matrices; and conjugation and the transpose preserve the trace pairing, with the conjugate transpose corresponding to the natural sign.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2$ | The matrix element representation $\mathbb{H}\to M_2(\mathbb{C})$ |
| $\sigma_\mu$ | Pauli matrices, $\mathsf{M}_2(\vec e_\mu)=-i\sigma_\mu$ |
| $\dagger$ | Conjugate transpose of a matrix |
| $D=\operatorname{diag}(1,-1,-1,-1)$ | Gram matrix of the plain form |
| $\operatorname{tr},\det$ | Trace and determinant of the matrix image |

## Further Reading

- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the Pauli-matrix representation of the quaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the embedding of the quaternions in $M_2(\mathbb{C})$ and its real form.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for representations of a division algebra and the trace pairing.
