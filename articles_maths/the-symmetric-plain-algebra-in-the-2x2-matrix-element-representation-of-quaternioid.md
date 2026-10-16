# __The Symmetric Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$__

## Introduction

The symmetric plain algebra of $\mathbb{H}$ carries the Jordan product $\tilde p\bullet\tilde q=\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$ of *Introduction to the Symmetric Plain Algebra*. This article reads the block on the $2\times2$ **matrix element representation**, the real-linear embedding $\mathsf{M}_2:\mathbb{H}\hookrightarrow M_2(\mathbb{C})$ that carries the plain product to the matrix product, so that the Jordan product becomes the half-sum of the two orders of the matrices.

**This is not the algebra $\mathbb{H}$.** The two algebras share the space, the addition, the real scalars and the unit, but $\bullet$ is a different multiplication and the projection onto the scalar line is not multiplicative. Throughout, the natural sign ${}^{\natural}$ is the quaternion conjugation, the bar is the identity because $\mathbb{R}$ has no nontrivial involution, and the star coincides with the natural sign and gives nothing new.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and $e_1^2=e_2^2=e_3^2=-e_0$. An element is $\tilde q=q_0e_0+\vec q$ with $\vec q=\sum_{k=1}^{3}q_ke_k$ and $q_\mu\in\mathbb{R}$; the norm is $\langle\tilde q\rangle_{\natural}=q_0^2+|\vec q|^2$, and the trace form is $\tau(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p\bullet\tilde q)$. The embedding $\mathsf{M}_2$, its multiplicativity and its invariants are *The General Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, whose conventions are held here.

## The Representation

### The Embedding and the Half-Sum

**Definition.** The **matrix element representation** of the block is the embedding $\mathsf{M}_2:\mathbb{H}\hookrightarrow M_2(\mathbb{C})$, $\mathsf{M}_2(\tilde q)=q_0\mathrm I+q_1\mathsf E_1+q_2\mathsf E_2+q_3\mathsf E_3$, with $\mathsf E_j$ the images of the units, $\mathsf E_j^2=-\mathrm I$.

**Theorem.** The embedding is multiplicative for the plain product and carries the Jordan product to the **half-sum of the two orders**:

$$
\mathsf{M}_2(\tilde p\tilde q)=\mathsf{M}_2(\tilde p)\,\mathsf{M}_2(\tilde q),\qquad
\mathsf{M}_2(\tilde p\bullet\tilde q)=\tfrac12\bigl(\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q)+\mathsf{M}_2(\tilde q)\mathsf{M}_2(\tilde p)\bigr).
$$

*Proof.* Multiplicativity is *The General Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*; the second identity is its linearity applied to the definition $\tilde p\bullet\tilde q=\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$.

**Remark (the block is the Jordan image of a matrix algebra).** Because $\mathsf{M}_2$ is multiplicative and injective, the block is the image of the **symmetrised matrix algebra** $\mathsf{M}_2(\mathbb{H})^{+}$: the Jordan product $\bullet$ is transported to the anticommutator of the matrices. The block is therefore a **special** Jordan algebra realised concretely, and the *half-sum* is the whole content of the representation.

### The Invariants

**Proposition.** The trace and the determinant of the representative are

$$
\operatorname{tr}\mathsf{M}_2(\tilde q)=2q_0=T(\tilde q),\qquad
\det\mathsf{M}_2(\tilde q)=\langle\tilde q\rangle_{\natural}=q_0^2+|\vec q|^2 .
$$

*Proof.* The trace is $2q_0$ on the embedding; the determinant is the multiplicativity of the norm, $\det\mathsf{M}_2(\tilde q)=\mathsf{M}_2(\tilde q)\mathsf{M}_2(\tilde q^{\natural})$ read as $\langle\tilde q\rangle_{\natural}$, by *The General Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*.

**Corollary.** The **Jordan inverse** is the normalised conjugate, $\mathsf{M}_2(\tilde q^{-1})=(2q_0\mathrm I-\mathsf{M}_2(\tilde q))/\langle\tilde q\rangle_{\natural}=\mathsf{M}_2(\tilde q^{\natural})/\langle\tilde q\rangle_{\natural}$; and the invertible elements are exactly those with $\det\neq0$, the nonzero elements.

## The Trace Form

**Theorem.** On the model the trace form is the **half of the matrix trace pairing**:

$$
\operatorname{tr}\bigl(\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q)\bigr)=2\,\tau(\tilde p,\tilde q)=2\bigl(p_0q_0-\vec p\cdot\vec q\bigr).
$$

*Proof.* $\operatorname{tr}\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q)=\operatorname{tr}\mathsf{M}_2(\tilde p\tilde q)=2\,\mathrm{Sc}(\tilde p\tilde q)=2\,\tau(\tilde p,\tilde q)$, using the multiplicativity of the embedding, the trace of the representative, and $\tau(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p\tilde q)$ of *The Trace Form and the Invariance of the Symmetric Plain Algebra*.

**Corollary (the Gram matrix and the signature).** The Gram matrix of the trace form in the basis of the representatives is $\operatorname{diag}(1,-1,-1,-1)$, so the signature is $(1,3)$; the form is the Lorentzian form of the block, read as the trace pairing of the matrix model.

**Remark (the definite form on the model).** The trace pairing of $M_2(\mathbb{C})$ is the Hermitian form $\operatorname{tr}(X^{\dagger}Y)$, positive definite; the **plain trace pairing** $\operatorname{tr}(XY)$ is indefinite, of the Lorentzian type. The block's trace form is the plain one, so it is the indefinite trace pairing, while the norm is the determinant, positive definite. **The two forms of the block are the two natural forms of the model**: the determinant and the indefinite trace pairing.

## The Comparison with the Plain Algebra on the Same Model

| | the plain algebra on $M_2(\mathbb{C})$ | the symmetric plain algebra on $M_2(\mathbb{C})$ |
|---|---|---|
| the product | the matrix product $\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q)$ | the half-sum (anticommutator) $\tfrac12(\;\cdot\;+\;\cdot\;)$ |
| the trace | $2q_0$ | $2q_0$ |
| the determinant | $\langle\tilde q\rangle_{\natural}$ | $\langle\tilde q\rangle_{\natural}$ |
| the trace form | $\tfrac12\operatorname{tr}(\;\cdot\;\cdot\;)$, signature $(1,3)$ | the same |
| the inverse | $\mathsf{M}_2(\tilde q)^{-1}=\mathsf{M}_2(\tilde q^{\natural})/\langle\tilde q\rangle_{\natural}$ | the same formula |

**Remark (what the change of product changes).** The trace, the determinant, the trace form and the inverse formula are **shared**: they depend on the plain product and the unit, which the embedding preserves. What the half-sum changes is the **product**: the associative matrix product becomes the commutative Jordan product, the brackets $[\mathsf{M}_2(\tilde p),\mathsf{M}_2(\tilde q)]$ are traded for the anticommutator, and the group $\mathsf{M}_2(\mathbb{H})^{\times}$ of the plain model is replaced by the multiplicatively unclosed invertible set of the block. The plain model is *The General Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*.

## Summary

The $2\times2$ matrix element representation $\mathsf{M}_2:\mathbb{H}\hookrightarrow M_2(\mathbb{C})$ is real-linear and multiplicative for the plain product, and it carries the Jordan product to the half-sum of the two orders of the matrices: $\mathsf{M}_2(\tilde p\bullet\tilde q)=\tfrac12(\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q)+\mathsf{M}_2(\tilde q)\mathsf{M}_2(\tilde p))$, so the block is the image of the symmetrised matrix algebra. The trace is $2q_0$ and the determinant is $\langle\tilde q\rangle_{\natural}=q_0^2+|\vec q|^2$, so the Jordan inverse is the normalised conjugate and the invertible elements are the nonzero ones. The trace form is the half of the plain matrix trace pairing, $\operatorname{tr}(\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q))=2\tau(\tilde p,\tilde q)$, of Gram matrix $\operatorname{diag}(1,-1,-1,-1)$ and signature $(1,3)$; it is the indefinite trace pairing, against the positive definite determinant. The trace, the determinant, the trace form and the inverse formula are shared with the plain algebra on the same model; the half-sum changes only the product.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2:\mathbb{H}\hookrightarrow M_2(\mathbb{C})$ | the embedding, multiplicative for the plain product |
| $\mathsf{M}_2(\tilde p\bullet\tilde q)=\tfrac12(\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q)+\mathsf{M}_2(\tilde q)\mathsf{M}_2(\tilde p))$ | the half-sum |
| $\operatorname{tr}\mathsf{M}_2(\tilde q)=2q_0$ | the trace |
| $\det\mathsf{M}_2(\tilde q)=\langle\tilde q\rangle_{\natural}$ | the determinant |
| $\operatorname{tr}(\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q))=2\tau(\tilde p,\tilde q)$ | the trace form as the half trace pairing |

## Further Reading

- *Introduction to the Symmetric Plain Algebra*, for the product.
- *The General Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, for the embedding, its multiplicativity and its invariants.
- *The Trace Form and the Invariance of the Symmetric Plain Algebra*, for the trace form.
- *Norm and Invertibility in the Symmetric Plain Algebra*, for the norm, the inverse and the invertibility criterion.
