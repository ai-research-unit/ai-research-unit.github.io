# __The Symmetric Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$__

## Introduction

The symmetric plain algebra of $\mathbb{H}$ carries the Jordan product $\tilde q_1\bullet\tilde q_2=\tfrac12(\tilde q_1\tilde q_2+\tilde q_2\tilde q_1)$ of *Introduction to the Symmetric Plain Algebra*. This article reads the block on the $2\times2$ **matrix element representation**, the real-linear embedding $\mathsf{M}_2:\mathbb{H}\hookrightarrow M_2(\mathbb{C})$ that carries the plain product to the matrix product, so that the Jordan product becomes the half-sum of the two orders of the matrices.

**This is not the algebra $\mathbb{H}$.** The two algebras share the space, the addition, the real scalars and the unit, but $\bullet$ is a different multiplication and the projection onto the scalar line is not multiplicative. Throughout, the natural sign ${}^{\natural}$ is the quaternion conjugation, the bar is the identity because $\mathbb{R}$ has no nontrivial involution, and the star coincides with the natural sign and gives nothing new.

## The Representation

### The Embedding and the Half-Sum

**Definition.** The **matrix element representation** of the block is the embedding $\mathsf{M}_2:\mathbb{H}\hookrightarrow M_2(\mathbb{C})$, $\mathsf{M}_2(\tilde q)=q_t\mathrm I+q_x\mathsf E_1+q_y\mathsf E_2+q_z\mathsf E_3$, with $\mathsf E_j$ the images of the units, $\mathsf E_j^2=-\mathrm I$.

**Theorem.** The embedding is multiplicative for the plain product and carries the Jordan product to the **half-sum of the two orders**:

$$
\boxed{\;\mathsf{M}_2(\tilde q_1\tilde q_2)=\mathsf{M}_2(\tilde q_1)\,\mathsf{M}_2(\tilde q_2),\qquad
\mathsf{M}_2(\tilde q_1\bullet\tilde q_2)=\tfrac12\bigl(\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2)+\mathsf{M}_2(\tilde q_2)\mathsf{M}_2(\tilde q_1)\bigr)\;}.
$$

*Proof.* Multiplicativity is *The General Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*; the second identity is its linearity applied to the definition $\tilde q_1\bullet\tilde q_2=\tfrac12(\tilde q_1\tilde q_2+\tilde q_2\tilde q_1)$.

**Remark (the block is the Jordan image of a matrix algebra).** Because $\mathsf{M}_2$ is multiplicative and injective, the block is the image of the **symmetrised matrix algebra** $\mathsf{M}_2(\mathbb{H})^{+}$: the Jordan product $\bullet$ is transported to the anticommutator of the matrices. The block is therefore a **special** Jordan algebra realised concretely, and the *half-sum* is the whole content of the representation.

### The Invariants

**Proposition.** The trace and the determinant of the representative are

$$
\boxed{\;\operatorname{tr}\mathsf{M}_2(\tilde q)=2q_t=T(\tilde q),\qquad
\det\mathsf{M}_2(\tilde q)=\langle\tilde q\rangle_{\natural}=q_t^2+|\vec q|^2\;}.
$$

*Proof.* The trace is $2q_t$ on the embedding; the determinant is the multiplicativity of the norm, $\det\mathsf{M}_2(\tilde q)=\mathsf{M}_2(\tilde q)\mathsf{M}_2(\tilde q^{\natural})$ read as $\langle\tilde q\rangle_{\natural}$, by *The General Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*.

**Corollary.** The **Jordan inverse** is the normalised conjugate, $\mathsf{M}_2(\tilde q^{-1})=(2q_t\mathrm I-\mathsf{M}_2(\tilde q))/\langle\tilde q\rangle_{\natural}=\mathsf{M}_2(\tilde q^{\natural})/\langle\tilde q\rangle_{\natural}$; and the invertible elements are exactly those with $\det\neq0$, the nonzero elements.

## The Trace Form

**Theorem.** On the model the trace form is the **half of the matrix trace pairing**:

$$
\boxed{\;\operatorname{tr}\bigl(\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2)\bigr)=2\,\tau(\tilde q_1,\tilde q_2)=2\bigl(q_{1t}q_{2t}-\vec q_1\cdot\vec q_2\bigr)\;}.
$$

*Proof.* $\operatorname{tr}\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2)=\operatorname{tr}\mathsf{M}_2(\tilde q_1\tilde q_2)=2\,\mathrm{Sc}(\tilde q_1\tilde q_2)=2\,\tau(\tilde q_1,\tilde q_2)$, using the multiplicativity of the embedding, the trace of the representative, and $\tau(\tilde q_1,\tilde q_2)=\mathrm{Sc}(\tilde q_1\tilde q_2)$ of *The Trace Form and the Invariance of the Symmetric Plain Algebra*.

**Corollary (the Gram matrix and the signature).** The Gram matrix of the trace form in the basis of the representatives is $\operatorname{diag}(1,-1,-1,-1)$, so the signature is $(1,3)$; the form is the Lorentzian form of the block, read as the trace pairing of the matrix model.

**Remark (the definite form on the model).** The trace pairing of $M_2(\mathbb{C})$ is the Hermitian form $\operatorname{tr}(X^{\dagger}Y)$, positive definite; the **plain trace pairing** $\operatorname{tr}(XY)$ is indefinite, of the Lorentzian type. The block's trace form is the plain one, so it is the indefinite trace pairing, while the norm is the determinant, positive definite. **The two forms of the block are the two natural forms of the model**: the determinant and the indefinite trace pairing.

## The Comparison with the Plain Algebra on the Same Model

| | the plain algebra on $M_2(\mathbb{C})$ | the symmetric plain algebra on $M_2(\mathbb{C})$ |
|---|---|---|
| the product | the matrix product $\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2)$ | the half-sum (anticommutator) $\tfrac12(\;\cdot\;+\;\cdot\;)$ |
| the trace | $2q_t$ | $2q_t$ |
| the determinant | $\langle\tilde q\rangle_{\natural}$ | $\langle\tilde q\rangle_{\natural}$ |
| the trace form | $\tfrac12\operatorname{tr}(\;\cdot\;\cdot\;)$, signature $(1,3)$ | the same |
| the inverse | $\mathsf{M}_2(\tilde q)^{-1}=\mathsf{M}_2(\tilde q^{\natural})/\langle\tilde q\rangle_{\natural}$ | the same formula |

**Remark (what the change of product changes).** The trace, the determinant, the trace form and the inverse formula are **shared**: they depend on the plain product and the unit, which the embedding preserves. What the half-sum changes is the **product**: the associative matrix product becomes the commutative Jordan product, the brackets $[\mathsf{M}_2(\tilde q_1),\mathsf{M}_2(\tilde q_2)]$ are traded for the anticommutator, and the group $\mathsf{M}_2(\mathbb{H})^{\times}$ of the plain model is replaced by the multiplicatively unclosed invertible set of the block. The plain model is *The General Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*.

## Summary

The $2\times2$ matrix element representation $\mathsf{M}_2:\mathbb{H}\hookrightarrow M_2(\mathbb{C})$ is real-linear and multiplicative for the plain product, and it carries the Jordan product to the half-sum of the two orders of the matrices: $\mathsf{M}_2(\tilde q_1\bullet\tilde q_2)=\tfrac12(\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2)+\mathsf{M}_2(\tilde q_2)\mathsf{M}_2(\tilde q_1))$, so the block is the image of the symmetrised matrix algebra. The trace is $2q_t$ and the determinant is $\langle\tilde q\rangle_{\natural}=q_t^2+|\vec q|^2$, so the Jordan inverse is the normalised conjugate and the invertible elements are the nonzero ones. The trace form is the half of the plain matrix trace pairing, $\operatorname{tr}(\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2))=2\tau(\tilde q_1,\tilde q_2)$, of Gram matrix $\operatorname{diag}(1,-1,-1,-1)$ and signature $(1,3)$; it is the indefinite trace pairing, against the positive definite determinant. The trace, the determinant, the trace form and the inverse formula are shared with the plain algebra on the same model; the half-sum changes only the product.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2:\mathbb{H}\hookrightarrow M_2(\mathbb{C})$ | the embedding, multiplicative for the plain product |
| $\mathsf{M}_2(\tilde q_1\bullet\tilde q_2)=\tfrac12(\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2)+\mathsf{M}_2(\tilde q_2)\mathsf{M}_2(\tilde q_1))$ | the half-sum |
| $\operatorname{tr}\mathsf{M}_2(\tilde q)=2q_t$ | the trace |
| $\det\mathsf{M}_2(\tilde q)=\langle\tilde q\rangle_{\natural}$ | the determinant |
| $\operatorname{tr}(\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2))=2\tau(\tilde q_1,\tilde q_2)$ | the trace form as the half trace pairing |

## Further Reading

- [Introduction to the Symmetric Plain Algebra](introduction-to-the-symmetric-plain-algebra-of-quaternioid.html), for the product.
- [Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Quaternions](introduction-to-the-2x2-matrix-element-representation-of-quaternions.html), for the embedding, its multiplicativity and its invariants.
- [The Trace Form and the Invariance of the Symmetric Plain Algebra](the-trace-form-and-the-invariance-of-the-symmetric-plain-algebra-of-quaternioid.html), for the trace form.
- [Norm and Invertibility in the Symmetric Plain Algebra](norm-and-invertibility-in-the-symmetric-plain-algebra.html), for the norm, the inverse and the invertibility criterion.
