# __The Symmetric Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$__

## Introduction

The symmetric plain algebra of $\mathbb{H}$ carries the Jordan product $\tilde p\bullet\tilde q=\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$ of *Introduction to the Symmetric Plain Algebra*. This article reads the block on the $4\times4$ **left regular representation** $\mathsf{M}_4:\mathbb{H}\hookrightarrow M_4(\mathbb{R})_L$, $\mathsf{M}_4(\tilde q)\tilde q_4=\tilde q\tilde q_4$, so that the Jordan product becomes the half-sum of the two orders of the regular matrices and the two commuting copies of the algebra become visible.

**This is not the algebra $\mathbb{H}$.** The two algebras share the space, the addition, the real scalars and the unit, but $\bullet$ is a different multiplication and the projection onto the scalar line is not multiplicative. Throughout, the natural sign ${}^{\natural}$ is the quaternion conjugation, the bar is the identity because $\mathbb{R}$ has no nontrivial involution, and the star coincides with the natural sign and gives nothing new.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$ and $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$. An element is $\tilde q=q_te_t+\vec q$ with $\vec q=\sum_{k=1}^{3}q_k\vec e_k$ and $q_\mu\in\mathbb{R}$; the norm is $\langle\tilde q\rangle_{\natural}=q_t^2+|\vec q|^2$, the trace form is $\tau(\tilde q_1,\tilde q_2)=\mathrm{Sc}(\tilde q_1\bullet\tilde q_2)$, and the left and right regular representations $\mathsf{M}_4$, $\mathsf{M}_4'$ are those of *The General Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$*.

## The Representation

### The Regular Matrices and the Half-Sum

**Definition.** The **left regular representation** of the block is $\mathsf{M}_4:\mathbb{H}\hookrightarrow M_4(\mathbb{R})_L$, $\mathsf{M}_4(\tilde q)\tilde q_4=\tilde q\tilde q_4$; the **right regular representation** is $\mathsf{M}_4'(\tilde q)\tilde q_4=\tilde q_4\tilde q$.

**Theorem.** The left representation is multiplicative for the plain product and carries the Jordan product to the **half-sum of the two orders**:

$$
\mathsf{M}_4(\tilde q_1\tilde q_2)=\mathsf{M}_4(\tilde q_1)\,\mathsf{M}_4(\tilde q_2),\qquad
\mathsf{M}_4(\tilde q_1\bullet\tilde q_2)=\tfrac12\bigl(\mathsf{M}_4(\tilde q_1)\mathsf{M}_4(\tilde q_2)+\mathsf{M}_4(\tilde q_2)\mathsf{M}_4(\tilde q_1)\bigr).
$$

*Proof.* Multiplicativity is the associativity of the plain product, $\mathsf{M}_4(\tilde q_1)\mathsf{M}_4(\tilde q_2)\tilde q_3=\tilde q_1(\tilde q_2\tilde q_3)=\tilde q_1\tilde q_2\,\tilde q_3$; the second identity is linearity applied to $\tilde q_1\bullet\tilde q_2=\tfrac12(\tilde q_1\tilde q_2+\tilde q_2\tilde q_1)$.

**Remark (the half-sum is not the product of the regular matrices).** The regular matrices are associative, so $\mathsf{M}_4(\tilde q_1)\mathsf{M}_4(\tilde q_2)=\mathsf{M}_4(\tilde q_1\tilde q_2)$; the block's product is the **symmetrised** one, and the failure of $\mathsf{M}_4(\tilde q_1\bullet\tilde q_2)$ to be $\mathsf{M}_4(\tilde q_1\tilde q_2)$ is exactly the failure of commutativity of the plain product, measured by the antisymmetric part at the matrix level.

### The Invariants

**Proposition.** The trace and the determinant of the regular matrix are

$$
\operatorname{tr}\mathsf{M}_4(\tilde q)=4q_t=2\,T(\tilde q),\qquad
\det\mathsf{M}_4(\tilde q)=\langle\tilde q\rangle_{\natural}^2 .
$$

*Proof.* The left multiplication by $\tilde q$ has the eigenvalues $q_t\pm|\vec q|\,i$ as a complex linear map, each with multiplicity two, so the trace is $4q_t$ and the determinant is $(q_t^2+|\vec q|^2)^2=\langle\tilde q\rangle_{\natural}^2$; both are quoted from *The General Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$*.

**Corollary.** The **Jordan inverse** is $\mathsf{M}_4(\tilde q^{-1})=(2q_t\mathrm I-\mathsf{M}_4(\tilde q))/\langle\tilde q\rangle_{\natural}$ for $\tilde q\neq0$; the invertibility criterion is $\det\neq0$, and the determinant being a square of the norm, it vanishes only at the origin.

## The Trace Form

**Theorem.** On the model the trace form is a **quarter of the matrix trace pairing**:

$$
\operatorname{tr}\bigl(\mathsf{M}_4(\tilde q_1)\mathsf{M}_4(\tilde q_2)\bigr)=4\,\tau(\tilde q_1,\tilde q_2)=4\bigl(q_{1t}q_{2t}-\vec q_1\cdot\vec q_2\bigr).
$$

*Proof.* $\operatorname{tr}\mathsf{M}_4(\tilde q_1)\mathsf{M}_4(\tilde q_2)=\operatorname{tr}\mathsf{M}_4(\tilde q_1\tilde q_2)=4\,\mathrm{Sc}(\tilde q_1\tilde q_2)=4\,\tau(\tilde q_1,\tilde q_2)$, using the multiplicativity, the trace of the regular matrix and $\tau(\tilde q_1,\tilde q_2)=\mathrm{Sc}(\tilde q_1\tilde q_2)$ of *The Trace Form and the Invariance of the Symmetric Plain Algebra*.

**Corollary.** The Gram matrix of the trace form has the same diagonal $\operatorname{diag}(1,-1,-1,-1)$ and the same signature $(1,3)$ as on the $2\times2$ model; the trace pairing of the regular matrices is the corresponding Lorentzian pairing, and the positive definite form of the model is the determinant, whose square root is the norm.

## The Commuting Copies

**Theorem.** The left and the right regular representations commute:

$$
\mathsf{M}_4(\tilde q_1)\,\mathsf{M}_4'(\tilde q_2)=\mathsf{M}_4'(\tilde q_2)\,\mathsf{M}_4(\tilde q_1)\qquad\text{for all }\tilde q_1,\tilde q_2,
$$

and the two together generate the **full** matrix algebra, $\mathrm{alg}\{\mathsf{M}_4,\mathsf{M}_4'\}=M_4(\mathbb{R})$.

*Proof.* Both sides applied to $\tilde q_3$ give $\tilde q_1\tilde q_3\tilde q_2$ by the associativity of the plain product, which is the commutativity; the fullness is the double centraliser statement of *The General Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$*.

**Remark (the commutant of the block's family).** The left multiplications alone generate every linear map of the space, as *The Multiplication Operators of the Symmetric Plain Algebra* records, so the block's family is irreducible and its commutant is the scalars; the commuting copy $\mathsf{M}_4'$ is the opposite algebra, and it is invisible to the Jordan product because the Jordan product is commutative. **The passage from the plain to the symmetric plain product forgets the right copy**, which is the matrix form of the one-operator statement $L^{\bullet}=R^{\bullet}$.

## The Comparison with the Plain Algebra on the Same Model

| | the plain algebra on $M_4(\mathbb{R})_L$ | the symmetric plain algebra on $M_4(\mathbb{R})_L$ |
|---|---|---|
| the product | the matrix product $\mathsf{M}_4(\tilde q_1)\mathsf{M}_4(\tilde q_2)$ | the half-sum (anticommutator) $\tfrac12(\;\cdot\;+\;\cdot\;)$ |
| the trace | $4q_t$ | $4q_t$ |
| the determinant | $\langle\tilde q\rangle_{\natural}^2$ | $\langle\tilde q\rangle_{\natural}^2$ |
| the trace form | $\tfrac14\operatorname{tr}(\;\cdot\;\cdot\;)$, signature $(1,3)$ | the same |
| the inverse | $\mathsf{M}_4(\tilde q)^{-1}=(2q_t\mathrm I-\mathsf{M}_4(\tilde q))/\langle\tilde q\rangle_{\natural}$ | the same formula |
| the commuting copy | $\mathsf{M}_4'$ genuinely present | $\mathsf{M}_4'$ invisible to the product |

**Remark (what the change of product changes).** As on the $2\times2$ model, the trace, the determinant, the trace form and the inverse formula are **shared**; the half-sum changes the product, replaces the associative product by the Jordan one, and **collapses the right copy into the left** because the product is commutative. The plain model is *The General Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$*; the two models of the block, the $2\times2$ complex and the $4\times4$ real, read the same trace form, the same determinant and the same inverse, differing only in the coefficient that relates the matrix trace to $\tau$.

## Summary

The left regular representation $\mathsf{M}_4:\mathbb{H}\hookrightarrow M_4(\mathbb{R})_L$, $\mathsf{M}_4(\tilde q)\tilde q_4=\tilde q\tilde q_4$, is multiplicative for the plain product and carries the Jordan product to the half-sum of the two orders of the regular matrices, $\mathsf{M}_4(\tilde q_1\bullet\tilde q_2)=\tfrac12(\mathsf{M}_4(\tilde q_1)\mathsf{M}_4(\tilde q_2)+\mathsf{M}_4(\tilde q_2)\mathsf{M}_4(\tilde q_1))$. The trace of the regular matrix is $4q_t=2T(\tilde q)$ and the determinant is $\langle\tilde q\rangle_{\natural}^2$, so the Jordan inverse is the normalised $2q_t\mathrm I-\mathsf{M}_4(\tilde q)$ and the invertible elements are the nonzero ones. The trace form is a quarter of the plain matrix trace pairing, $\operatorname{tr}(\mathsf{M}_4(\tilde q_1)\mathsf{M}_4(\tilde q_2))=4\tau(\tilde q_1,\tilde q_2)$, of Gram matrix $\operatorname{diag}(1,-1,-1,-1)$ and signature $(1,3)$, the same as on the $2\times2$ model. The left and the right regular representations commute and together generate the full matrix algebra, but the block's product is commutative, so the right copy is invisible to it; the trace, the determinant, the trace form and the inverse formula are shared with the plain algebra on the same model.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_4(\tilde q)\tilde q_4=\tilde q\tilde q_4$ | the left regular representation |
| $\mathsf{M}_4'(\tilde q)\tilde q_4=\tilde q_4\tilde q$ | the right regular representation, commuting with $\mathsf{M}_4$ |
| $\mathsf{M}_4(\tilde q_1\bullet\tilde q_2)=\tfrac12(\mathsf{M}_4(\tilde q_1)\mathsf{M}_4(\tilde q_2)+\mathsf{M}_4(\tilde q_2)\mathsf{M}_4(\tilde q_1))$ | the half-sum |
| $\operatorname{tr}\mathsf{M}_4(\tilde q)=4q_t$ | the trace |
| $\det\mathsf{M}_4(\tilde q)=\langle\tilde q\rangle_{\natural}^2$ | the determinant |
| $\operatorname{tr}(\mathsf{M}_4(\tilde q_1)\mathsf{M}_4(\tilde q_2))=4\tau(\tilde q_1,\tilde q_2)$ | the trace form as a quarter trace pairing |

## Further Reading

- *Introduction to the Symmetric Plain Algebra*, for the product.
- *The General Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$*, for the regular matrices, the commuting copies and the double centraliser.
- *The Multiplication Operators of the Symmetric Plain Algebra*, for the fullness of the family generated by the left multiplications.
- *The Trace Form and the Invariance of the Symmetric Plain Algebra*, for the trace form.
- *Introduction to the Symmetric Plain Algebra*, for the other model of the block.
- *Norm and Invertibility in the Symmetric Plain Algebra*, for the norm and the inverse.
