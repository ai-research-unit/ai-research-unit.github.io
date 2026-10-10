
# __The Trace Form of the Real Biquaternion Algebra__

## Introduction

The real biquaternion algebra carries a canonical symmetric bilinear form, its **trace form**, obtained from the regular representation: the left multiplication $L_{\tilde P}(\tilde X)=\tilde P\tilde X$ is a real endomorphism of the eight-dimensional algebra, and

$$
\tau(\tilde P,\tilde Q)=\operatorname{Tr}\!\left(L_{\tilde P}L_{\tilde Q}\right)
$$

is a real symmetric bilinear form on $\mathbb{B}$. This article develops it: the trace of a left multiplication, the Gram matrix in the real basis, the signature $(4,4)$, the identity with the realified general plain bilinear form up to the factor $8$, and the invariance under the automorphisms of the algebra.

The form is the one the real algebra possesses before any of the four complex forms is chosen: it uses only the regular representation and the trace, which are algebraic data of the ring, and it needs no conjugation. The result that organises the article is that this algebraic form is not a fifth form at all. It is **eight times the realification of the general plain bilinear form**,

$$
\tau(\tilde P,\tilde Q)=8\,\mathrm{Re}\langle\tilde P,\tilde Q\rangle,\qquad \langle\tilde P,\tilde Q\rangle=\sum_{\mu}\varepsilon_{\mu}P_{\mu}Q_{\mu},
$$

with the **sign vector** $\varepsilon=(1,-1,-1,-1)$ of the coefficient basis, so that the general plain bilinear form is the four terms $P_0Q_0-P_1Q_1-P_2Q_2-P_3Q_3$ and the Gram matrix of $\tau$ is the block matrix of *The Realification of the Four Forms* rescaled by $8$, its signature is the signature $(4,4)$ of that block matrix, and its null cone is the realified cone of the general plain bilinear form. The factor $8$ is the real dimension of the carrier of the regular representation, and the same form read on the complex four-dimensional module carries the factor $4$ instead. The trace form is therefore the regular-representation reading of the general plain bilinear form, and its interest is exactly that: it reaches the signature $(4,4)$ and the invariance under the algebra automorphisms from the ring structure alone.

**Boundary.** The four complex forms, their Gram matrices, their adjoints and their automorphism groups are *The Four Pairings of the Biquaternion Algebra* and the $2\times2$ and $4\times4$ representation articles of the four layers; their realified reading is *The Realification of the Four Forms*, whose signature table this article compares with. The Hilbert–Schmidt form of the matrix model, with the adjoint in the trace, is *The Matrix Element Representation and the Biquaternion Dynamics*, and the regular representation itself is *Modules over the General Plain Algebra of Biquaternions*.

## The Left Multiplication and the Trace

**Definition (the left multiplication).** For $\tilde P\in\mathbb{B}$ the **left multiplication** is $L_{\tilde P}:\mathbb{B}\to\mathbb{B}$, $L_{\tilde P}(\tilde X)=\tilde P\tilde X$. It is a real endomorphism of $\mathbb{B}\cong\mathbb{R}^{8}$, additive and $\mathbb{R}$-linear in the parameter, and injective.

**Proposition (the trace form is well defined).** The assignment $\tau(\tilde P,\tilde Q)=\operatorname{Tr}(L_{\tilde P}L_{\tilde Q})$ is a real symmetric bilinear form on $\mathbb{B}$.

*Proof.* Because $L_{\tilde P\tilde Q}=L_{\tilde P}L_{\tilde Q}$, the product $L_{\tilde P}L_{\tilde Q}=L_{\tilde P\tilde Q}$ is a left multiplication, and the trace is additive and $\mathbb{R}$-homogeneous, so $\tau$ is real-bilinear. Symmetry is the invariance of the trace under cyclic permutation, $\operatorname{Tr}(L_{\tilde P}L_{\tilde Q})=\operatorname{Tr}(L_{\tilde Q}L_{\tilde P})$.

**Lemma (the trace of a left multiplication).** For every $\tilde X=\sum_\mu X_\mu e_\mu$ with $X_\mu\in\mathbb{C}$,

$$
\operatorname{Tr}(L_{\tilde X}) = 8\,\mathrm{Re}\,\mathrm{Sc}(\tilde X) = 8\,\mathrm{Re}\,X_{0}.
$$

*Proof.* Evaluate the real $8\times8$ matrix of $L_{\tilde X}$ in the real basis $e_{0},e_{1},e_{2},e_{3},ie_{0},ie_{1},ie_{2},ie_{3}$ on each basis vector. On $e_{\nu}$ the product is $\tilde X e_{\nu}=\sum_\mu X_\mu e_\mu e_\nu$, whose $e_{\nu}$-component is $X_{0}$, contributing the real diagonal entry $\mathrm{Re}\,X_{0}$; on $ie_{\nu}$ the product is $\tilde X(ie_{\nu})=i\,\tilde X e_{\nu}$, whose $ie_{\nu}$-component is likewise $X_{0}$, again contributing $\mathrm{Re}\,X_{0}$. Summing the eight real diagonal entries gives $8\,\mathrm{Re}\,X_{0}$.

**Corollary (the trace of a product).** $\operatorname{Tr}(L_{\tilde P}L_{\tilde Q})=8\,\mathrm{Re}\,\mathrm{Sc}(\tilde P\tilde Q)$, and hence $\tau(\tilde P,\tilde Q)=\operatorname{Tr}(L_{\tilde P\tilde Q})$ depends on the pair through the product alone.

## The Gram Matrix and the Signature

**Theorem (the Gram matrix in the real basis).** With $\tilde Q=\sum_\mu q_\mu e_\mu+\sum_\mu q'_\mu ie_\mu$, the values of the trace form on the real basis are

$$
\tau(e_{\mu},e_{\nu})=8\,\varepsilon_{\mu}\delta_{\mu\nu},\qquad
\tau(e_{\mu},ie_{\nu})=0,\qquad
\tau(ie_{\mu},ie_{\nu})=-8\,\varepsilon_{\mu}\delta_{\mu\nu},
$$

so the Gram matrix is

$$
8\cdot\operatorname{diag}(1,-1,-1,-1,-1,1,1,1),
$$

of signature $(4,4)$. The four positive directions are $e_{0},ie_{1},ie_{2},ie_{3}$ and the four negative directions are $e_{1},e_{2},e_{3},ie_{0}$.

*Proof.* By the lemma, $\tau(e_\mu,e_\nu)=\operatorname{Tr}(L_{e_\mu e_\nu})=8\,\mathrm{Re}\,\mathrm{Sc}(e_\mu e_\nu)$. For $\mu\ne\nu$ the product $e_\mu e_\nu$ is a vector generator or its negative, of vanishing scalar part, so the entry is $0$; for $\mu=\nu$ it is $\varepsilon_\mu e_{0}$, with scalar part $\varepsilon_\mu$ and entry $8\varepsilon_\mu$. The mixed entries vanish for the same reason, since $e_\mu\,ie_\nu$ and $ie_\mu\,ie_\nu$ have real scalar part $0$ and $-\varepsilon_\mu\delta_{\mu\nu}$ respectively. The diagonal is $\operatorname{diag}(8\,\varepsilon,8\,(-\varepsilon))=8\cdot\operatorname{diag}(1,-1,-1,-1,-1,1,1,1)$; the four entries $+8$ and the four entries $-8$ give the signature $(4,4)$.

**Corollary (non-degeneracy).** The Gram matrix is invertible, of determinant $8^{8}$, so the trace form is non-degenerate.

## The Identity with the Realified General Plain Bilinear Form

**Theorem (the trace form is eight times the realified general plain bilinear form).** For all $\tilde P,\tilde Q$,

$$
\tau(\tilde P,\tilde Q)=8\,\mathrm{Re}\,\langle\tilde P,\tilde Q\rangle
=8\sum_{\mu}\varepsilon_{\mu}\bigl(p_{\mu}q_{\mu}-p'_{\mu}q'_{\mu}\bigr),
\qquad
\langle\tilde P,\tilde Q\rangle=\sum_{\mu}\varepsilon_{\mu}P_{\mu}Q_{\mu}.
$$

*Proof.* The corollary of the lemma gives $\tau(\tilde P,\tilde Q)=8\,\mathrm{Re}\,\mathrm{Sc}(\tilde P\tilde Q)$, and $\mathrm{Sc}(\tilde P\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu Q_\mu=\langle\tilde P,\tilde Q\rangle$ is the general plain bilinear form; taking real parts of $P_\mu Q_\mu=(p_\mu+ip'_\mu)(q_\mu+iq'_\mu)$ gives the second display.

**Remark (why the factor is eight).** The trace form is read on the regular representation, whose carrier is the algebra itself, of real dimension eight. The same construction on the complex four-dimensional module $\mathbb{B}\cong\mathbb{C}^{4}$ gives the complex trace $\operatorname{Tr}_{\mathbb{C}}(L_{\tilde P}L_{\tilde Q})=4\,\langle\tilde P,\tilde Q\rangle$, whose real part is $4\,\mathrm{Re}\langle\tilde P,\tilde Q\rangle$; the real trace is twice the real part of the complex trace, $8=2\cdot4$. The factor is the dimension of the carrier, and the form is the same.

**Corollary (the same null cone as the general plain bilinear realification).** The trace form has the null cone $\{\mathrm{Re}\sum_\mu\varepsilon_\mu Q_\mu^{2}=0\}$ of real dimension $7$, the maximal totally isotropic subspaces of real dimension $4$, and the same definite and indefinite rows on the remarkable subspaces, all rescaled by $8$ from the realified general plain bilinear form of *The Realification of the Four Forms*.

## The Invariance

**Theorem (invariance under the automorphism group, hence under the units).** For every algebra automorphism $\sigma$ of $\mathbb{B}$,

$$
\tau\bigl(\sigma\tilde P,\sigma\tilde Q\bigr)=\tau(\tilde P,\tilde Q),
$$

and in particular for every unit $\tilde U\in\mathbb{B}^{\times}$,

$$
\tau\bigl(\tilde U\tilde P\tilde U^{-1},\tilde U\tilde Q\tilde U^{-1}\bigr)=\tau(\tilde P,\tilde Q).
$$

*Proof.* An algebra automorphism satisfies $L_{\sigma\tilde P}=\sigma L_{\tilde P}\sigma^{-1}$, since both sides send $\tilde X$ to $\sigma(\tilde P)\tilde X$; hence $L_{\sigma\tilde P}L_{\sigma\tilde Q}=\sigma L_{\tilde P}L_{\tilde Q}\sigma^{-1}$, and the trace is invariant under conjugation. The unit statement is the inner automorphism $\sigma(\tilde X)=\tilde U\tilde X\tilde U^{-1}$. The complex conjugation of the coefficients acts nontrivially on the centre and is therefore outer, and it satisfies the identity as well, so the invariance is not merely inner.

**Corollary (invariance of the form, not only of the Gram matrix).** The conjugation identity states that each unit acts on $\mathbb{B}$ by an automorphism of the trace form, so the group of units has a representation in the orthogonal group $O(4,4)$ of the realified form. The trace form is the invariant symmetric bilinear form of the ring: it is built from the regular representation, which is the multiplication of the ring, and it is unchanged by every automorphism of the ring.

## The Place among the Four Forms

The trace form is the natural form of the **real** algebra, available before any complex product is singled out, and it is not an independent fifth form: it reproduces the realified general plain bilinear form with the normalisation $8$. Its relation to the four forms is the comparison of *The Realification of the Four Forms*: it has the Gram matrix $\operatorname{diag}(\mathrm{D},-\mathrm{D})$ of the general plain bilinear realification, and it is not the realified general quaternionic bilinear form, whose Gram matrix is $\operatorname{diag}(\mathrm{I}_{4},-\mathrm{I}_{4})$.

The contrast with the **Hilbert–Schmidt form** of the matrix model fixes the role of the trace. In the realization $\mathsf{M}_2:\mathbb{B}\to M_{2}(\mathbb{C})$ the Hilbert–Schmidt pairing is

$$
\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde P)^{\dagger}\mathsf{M}_2(\tilde Q)\bigr)=\langle\tilde P,\tilde Q\rangle_{*\mathbb{R}},
$$

the **positive definite** form of the realified Hermitian form; the trace form drops the adjoint and reads the plain trace product $\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q))$, of signature $(4,4)$. The difference is exactly the difference between the Hermitian realification $\mathrm{I}_{8}$ and the general plain bilinear realification $\operatorname{diag}(\mathrm{D},-\mathrm{D})$: the adjoint turns the indefinite split form into the Euclidean one. The two forms are compared form by form in *The Matrix Element Representation and the Biquaternion Dynamics*, and the matrix trace bridge $\mathrm{Sc}(\tilde P\tilde Q)=\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q))$ is the same identity at the level of elements.

## Worked Examples

**The generators.** $\tau(e_{0},e_{0})=8$ and $\operatorname{Tr}(L_{e_{0}})=8$; $\tau(e_{1},e_{1})=-8$ and $\tau(ie_{1},ie_{1})=+8$; the mixed value $\tau(e_{0},ie_{0})=0$. The element $e_{1}$ is anti-Hermitian and has vanishing trace, $\operatorname{Tr}(L_{e_{1}})=0$, in agreement with the lemma.

**A maximal totally isotropic subspace.** The four vectors $e_{0}+ie_{0}$, $e_{1}+ie_{1}$, $e_{2}+ie_{2}$, $e_{3}+ie_{3}$ span a totally isotropic real four-plane of the trace form: each has $\tau$-square $8(1-1)=0$, and distinct pairs are $\tau$-orthogonal. The span has rank four, and it is maximal because the signature is $(4,4)$.

**The null cone.** On the central line $\operatorname{span}\{e_{0},ie_{0}\}$ the trace form is $8(q_{0}^{2}-q_{0}'^{2})$, the hyperbolic plane of signature $(1,1)$; on the quaternion subspace $\mathbb{H}_{\mathbb{B}}=\operatorname{span}\{e_{0},e_{1},e_{2},e_{3}\}$ it is $8(q_{0}^{2}-q_{1}^{2}-q_{2}^{2}-q_{3}^{2})$, of signature $(1,3)$; and the full form is $8\bigl(q_{0}^{2}-q_{1}^{2}-q_{2}^{2}-q_{3}^{2}-q_{0}'^{2}+q_{1}'^{2}+q_{2}'^{2}+q_{3}'^{2}\bigr)$, of signature $(4,4)$. The null cone is the realified cone of the general plain bilinear form, of real dimension $7$.

**A value at a mixed pair.** For $\tilde P=e_{0}+ie_{1}$ and $\tilde Q=e_{1}+ie_{0}$ the general plain bilinear form is $\langle\tilde P,\tilde Q\rangle=\varepsilon_{0}P_{0}Q_{0}+\varepsilon_{1}P_{1}Q_{1}=i-i=0$, so $\tau(\tilde P,\tilde Q)=0$, while $\tau(\tilde P,\tilde P)=16$ and $\tau(\tilde Q,\tilde Q)=-16$. The pair is $\tau$-orthogonal with the two vectors of opposite sign, an explicit hyperbolic plane of the signature $(4,4)$.

## Summary

The trace form of the real biquaternion algebra is $\tau(\tilde P,\tilde Q)=\operatorname{Tr}(L_{\tilde P}L_{\tilde Q})$, the trace of the product of two left multiplications in the regular representation. It is real-bilinear, symmetric and non-degenerate, and the trace of a single left multiplication is $\operatorname{Tr}(L_{\tilde X})=8\,\mathrm{Re}\,\mathrm{Sc}(\tilde X)$. Its Gram matrix in the real basis is $8\cdot\operatorname{diag}(1,-1,-1,-1,-1,1,1,1)$, of signature $(4,4)$, with positive directions $e_{0},ie_{1},ie_{2},ie_{3}$ and negative directions $e_{1},e_{2},e_{3},ie_{0}$. It is exactly eight times the realification of the general plain bilinear form, $\tau=8\,\mathrm{Re}\langle\cdot,\cdot\rangle$; the factor is the real dimension of the carrier of the regular representation, and the complex trace gives $4\,\mathrm{Re}\langle\cdot,\cdot\rangle$ instead. Being built from the regular representation, it is invariant under every automorphism of the algebra and in particular under conjugation by the units, so the units act by automorphisms of the realified form. It is not a fifth form but the regular-representation reading of the general plain bilinear form, and its contrast with the positive definite Hilbert–Schmidt form of the matrix model is the contrast between the realified general plain bilinear form and the realified Hermitian form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{\tilde P}(\tilde X)=\tilde P\tilde X$ | the left multiplication; the regular representation |
| $\tau(\tilde P,\tilde Q)=\operatorname{Tr}(L_{\tilde P}L_{\tilde Q})$ | the trace form, read over $\mathbb{R}$ |
| $\operatorname{Tr}(L_{\tilde X})=8\,\mathrm{Re}\,\mathrm{Sc}(\tilde X)$ | the trace of a left multiplication |
| $8\cdot\operatorname{diag}(1,-1,-1,-1,-1,1,1,1)$ | its Gram matrix |
| $(4,4)$ | its signature |
| $\tau=8\,\mathrm{Re}\langle\cdot,\cdot\rangle$ | its identity with the realified general plain bilinear form |
| $\tau(\sigma\tilde P,\sigma\tilde Q)=\tau(\tilde P,\tilde Q)$ | invariance under the automorphisms, hence under the units |
| $\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde P)^{\dagger}\mathsf{M}_2(\tilde Q))$ | the Hilbert–Schmidt contrast, the realified Hermitian form |

## Further Reading

- *The Realification of the Four Forms* (`articles_maths/the-realification-of-the-four-forms.md`), for the four realified forms and the signature table the trace form is compared with
- *The Biquaternion Algebra over $\mathbb{R}$ in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* (`articles_maths/the-biquaternion-algebra-over-r-in-the-4x4-matrix-element-representation.md`), for the trace bridge and the Hilbert–Schmidt form
- *Modules over the General Plain Algebra of Biquaternions* (`articles_maths/modules-over-the-general-plain-algebra-of-biquaternions.md`), for the regular representation
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the general plain bilinear form the trace form reproduces and for the four Gram matrices of the complex forms compared with the realified ones
- *Bilinear Forms* (`articles_maths/bilinear-forms.md`) and *Quadratic Forms and Polarisation* (`articles_maths/quadratic-forms-and-polarisation.md`), for the general theory of bilinear forms, non-degeneracy and Sylvester's law
- *The Killing Form Operator* (`articles_maths/the-killing-form-operator.md`), for the invariant form of the operator algebra, of which the trace form is the ring-theoretic counterpart
- Werner Greub, *Linear Algebra*, 4th edition (Springer, 1981), for the trace of an endomorphism and the trace form of an algebra.
