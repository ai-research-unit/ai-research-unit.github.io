
# __The Biquaternion Algebra over $\mathbb{R}$ in the $2\times2$ Matrix Representation__

## Introduction

The reading group *Topology on the Biquaternions as an Algebra over $\mathbb{R}$* forgets the complex structure of the algebra and reads it as a real algebra of dimension eight. Its form is the **trace form** $\tau(\tilde{P},\tilde{Q})=\operatorname{Tr}(L_{\tilde{P}}L_{\tilde{Q}})$, the canonical symmetric bilinear form of *The Trace Form of the Real Biquaternion Algebra*, which is eight times the realification of the general plain bilinear form, $\tau=8\,\mathrm{Re}\langle\cdot,\cdot\rangle$, and its grammar is the realification of the four complex forms of *The Realification of the Four Forms*, of signatures $(4,4)$, $(4,4)$, $(8,0)$ and $(2,6)$. This article reads that group through the $2\times2$ matrix realization $\Phi$ of *Introduction to the $2\times2$ Matrix Representation of Biquaternions*, and it is the first of the two representation articles of the group; the companion *The Biquaternion Algebra over $\mathbb{R}$ in the $4\times4$ Regular Matrix Representation* repeats the reading on the real regular representation.

The real reading of the model is the realification $M_2(\mathbb{C})\cong\mathbb{R}^8$, in which the complex structure is the multiplication by the scalar matrix $iI$ and the eight real coordinates are the real and imaginary parts of the four matrix entries. The trace form is the real trace pairing $\tau(\tilde{P},\tilde{Q})=4\,\mathrm{Re}\operatorname{Tr}(\Phi(\tilde{P})\Phi(\tilde{Q}))$, and the four realified forms are the real parts of the four pairings of the model, whose signatures are the four rows of the signature table.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the identity and $e_k^2=-e_0$; $\tilde{Q}=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; scalar part $\mathrm{Sc}$, sign vector $\varepsilon=(1,-1,-1,-1)$; natural conjugation ${}^{\natural}$ negating $e_1,e_2,e_3$, Hermitian conjugation ${}^{*}={}^{\natural}\circ\bar{\cdot}$; the real basis is $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$. All matrix claims of this article are recomputed in the verification script of the pass.

## The Realification of the Model

**The real structure.** $\Phi$ is $\mathbb{C}$-linear, hence $\mathbb{R}$-linear, and it is an isomorphism of real algebras

$$
\Phi:\mathbb{B}\longrightarrow M_2(\mathbb{C})\cong\mathbb{R}^8 ,
$$

the real dimension being eight on both sides. The complex structure of the algebra is the operator $J:\tilde{Q}\mapsto i\tilde{Q}$, and in the model it is the multiplication by the scalar matrix $iI$; the coefficient conjugation is the complex conjugation of the matrix, $\Phi(\bar{\tilde{Q}})=\overline{\Phi(\tilde{Q})}$.

**The real basis.** The eight elements $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ form a real basis of the algebra, and their images under $\Phi$ form a real basis of the model; in this basis the product is real bilinear and the complex structure $i$ acts on the last four coordinates alone.

## The Trace Form in the Model

**Theorem (the trace form as a real trace pairing).** For all biquaternions,

$$
\tau(\tilde{P},\tilde{Q})=\operatorname{Tr}(L_{\tilde{P}}L_{\tilde{Q}})=8\,\mathrm{Re}\langle\tilde{P},\tilde{Q}\rangle = 4\,\mathrm{Re}\operatorname{Tr}\bigl(\Phi(\tilde{P})\Phi(\tilde{Q})\bigr),
$$

the real trace pairing of the matrices, with the factor $4$ in place of the factor $8$ because the complex trace identity carries the factor $2$.

*Proof.* $\tau(\tilde{P},\tilde{Q})=8\,\mathrm{Re}\,\mathrm{Sc}(\tilde{P}\tilde{Q})$ by the trace-form theorem, and $\mathrm{Re}\operatorname{Tr}(\Phi(\tilde{P})\Phi(\tilde{Q}))=2\,\mathrm{Re}\,\mathrm{Sc}(\tilde{P}\tilde{Q})$ by the complex trace identity; the two factors $8$ and $4$ differ by the factor $2$ of that identity.

**Theorem (the diagonal and the signature).** With $\tilde{Q}=\sum_\mu(q_\mu+iq'_\mu)e_\mu$,

$$
\tau(\tilde{Q},\tilde{Q}) = 8\sum_\mu\varepsilon_\mu\bigl(q_\mu^2-q'_\mu{}^2\bigr) ,
$$

so the form has signature $(4,4)$ on the eight real coordinates: the four real parts of the coefficients $q_\mu$ carry the sign $\varepsilon_\mu$ and the four imaginary parts carry the opposite sign. The form is the realified general plain bilinear form rescaled by $8$, so its Gram matrix is the block matrix of *The Realification of the Four Forms* rescaled by $8$, and its null cone is the realified cone of the general plain bilinear form.

**Invariance.** The trace form is invariant under the automorphisms of the algebra: for every unit $\tilde{A}$ and all biquaternions, $\tau(\tilde{A}\tilde{P}\tilde{A}^{-1},\tilde{A}\tilde{Q}\tilde{A}^{-1})=\tau(\tilde{P},\tilde{Q})$, which in the model is the invariance of the real trace pairing under simultaneous conjugation by $\Phi(\tilde{A})$.

## The Four Realified Forms in the Model

The four complex forms of the matrix model have real parts, and the four real quadratic forms on the eight real coordinates are

$$
\mathrm{Re}\operatorname{Tr}\bigl(\Phi(\tilde{P})\Phi(\tilde{Q})\bigr),\quad \mathrm{Re}\operatorname{Tr}\bigl(\Phi(\tilde{P})\operatorname{adj}\Phi(\tilde{Q})\bigr),\quad \mathrm{Re}\operatorname{Tr}\bigl(\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q})\bigr),\quad \mathrm{Re}\operatorname{Tr}\bigl(\operatorname{adj}\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q})\bigr),
$$

the trace pairings of the plain, adjugated, conjugate-transposed and adjugated conjugate-transposed products. Their signatures are the four signatures of the group: $(4,4)$ for the general plain bilinear form, $(4,4)$ split for the general quaternionic bilinear form, $(8,0)$ for the general plain sesquilinear form, and $(2,6)$ for the general quaternionic sesquilinear form. The first of the four is the trace form of this group up to the factor $4$, and the others are the realified readings recorded in *The Realification of the Four Forms*.

**The Minkowski form.** The second real $4\times4$ realization of *Biquaternion 4×4 Regular Matrix Element Representation* lives on the real span of $e_0,ie_1,ie_2,ie_3$, and its Minkowski form, of signature $(1,3)$, is recorded in *Biquaternion 4×4 Regular Matrix Element Representation*, §*A Second $4 \times 4$ Realization, and the Multiplicative Map*; it is the form of the Lorentzian slice of the algebra, not a form of the eight-dimensional realification.

## Worked Examples

**The identity.** Let $\tilde{Q}=e_0$. Then $\tau(e_0,e_0)=8$, and $4\operatorname{Re}\operatorname{Tr}(I_2\cdot I_2)=4\cdot2=8$; the trace of the left multiplication is $8\operatorname{Re}Q_0=8$.

**A real and an imaginary basis element.** Let $\tilde{Q}=e_1$ and $\tilde{P}=ie_1$. Then $\tau(e_1,e_1)=8\varepsilon_1=-8$ and $\tau(ie_1,ie_1)=8\varepsilon_1(0-1)=+8$, so the real and the imaginary copy of the same basis vector carry opposite signs: this is the signature $(4,4)$ of the trace form in one line.

**An automorphism-invariant value.** Let $\tilde{A}=e_1$ and $\tilde{P}=\tilde{Q}=e_2$. Then $\tilde{A}^{-1}=-e_1$ and $\tilde{A}e_2\tilde{A}^{-1}=e_1e_2(-e_1)=-e_1e_2e_1=-e_2$, so both arguments change sign and $\tau(-e_2,-e_2)=\tau(e_2,e_2)=-8$, as the invariance requires.

## Summary

The real reading of the $2\times2$ model is the realification $M_2(\mathbb{C})\cong\mathbb{R}^8$, in which the complex structure is multiplication by $iI$ and the coefficient conjugation is the conjugation of the matrix. The group's trace form is the real trace pairing $\tau(\tilde{P},\tilde{Q})=4\operatorname{Re}\operatorname{Tr}(\Phi(\tilde{P})\Phi(\tilde{Q}))=8\operatorname{Re}\langle\tilde{P},\tilde{Q}\rangle$, the realified general plain bilinear form rescaled by $8$, of signature $(4,4)$ and invariant under the automorphisms of the algebra. The four realified forms of the group are the real parts of the four pairings of the model, with the signatures $(4,4)$, $(4,4)$, $(8,0)$ and $(2,6)$ of *The Realification of the Four Forms*, and the Minkowski form of signature $(1,3)$ is the form of the Lorentzian slice of the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M_2(\mathbb{C})\cong\mathbb{R}^8$ | the realification of the model, complex structure $iI$ |
| $\tau(\tilde{P},\tilde{Q})=4\operatorname{Re}\operatorname{Tr}(\Phi(\tilde{P})\Phi(\tilde{Q}))$ | the trace form of the group |
| $\tau=8\operatorname{Re}\langle\cdot,\cdot\rangle$ | the trace form as the realified general plain bilinear form rescaled |
| $\tau(\tilde{Q},\tilde{Q})=8\sum_\mu\varepsilon_\mu(q_\mu^2-q'_\mu{}^2)$ | the diagonal, signature $(4,4)$ |
| $(4,4),(4,4),(8,0),(2,6)$ | the signatures of the four realified forms |
| $(1,3)$ | the signature of the Minkowski form of the Lorentzian slice |

## Further Reading

- *Introduction to the $2\times2$ Matrix Representation of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-representation-of-biquaternions.md`), for the realization and its first properties
- *The Trace Form of the Real Biquaternion Algebra* (`articles_maths/the-trace-form-of-the-real-biquaternion-algebra.md`), for the trace form on the algebra
- *The Realification of the Four Forms* (`articles_maths/the-realification-of-the-four-forms.md`), for the signature table of the realified forms
- *Operators of the Real Biquaternion Algebra* (`articles_maths/operators-of-the-real-biquaternion-algebra.md`), for the operators of the real reading
- *The Biquaternion Algebra over $\mathbb{R}$ in the $4\times4$ Regular Matrix Representation* (`articles_maths/the-biquaternion-algebra-over-r-in-the-4x4-regular-matrix-representation.md`), for the companion reading of the group
- *The Six Subspaces under the Real Biquaternion Algebra* (`articles_maths/the-six-subspaces-under-the-real-biquaternion-algebra.md`), for the restriction theory of the trace form
