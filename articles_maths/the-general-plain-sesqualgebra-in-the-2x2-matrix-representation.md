
# __The General Plain Sesqualgebra in the $2\times2$ Matrix Representation__

## Introduction

The reading group *Topology on the Introduction to the General Plain Sesqualgebra of Biquaternions* reads the algebra through the **general plain sesquilinear form** $\langle\tilde{P},\tilde{Q}\rangle_{*}=\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})=\sum_\mu P_\mu\overline{Q_\mu}$ and through the **sesquilinear product** $\tilde{P}\star\tilde{Q}=\tilde{P}\tilde{Q}^{*}$ that it polarises, whose algebra is *Introduction to the General Plain Sesqualgebra of Biquaternions*. This article reads that group through the $2\times2$ matrix realization $\mathsf{M}_2$ of *Introduction to the $2\times2$ Matrix Representation of Biquaternions*, and it is the first of the two representation articles of the group; the companion *The General Plain Sesqualgebra in the $4\times4$ Matrix Representation* repeats the reading on the left regular representation.

The Hermitian conjugation is the characteristic operation of the group, and in the model it is the **conjugate transpose**: $\mathsf{M}_2(\tilde{Q}^{*})=\mathsf{M}_2(\tilde{Q})^{\dagger}$. The sesquilinear product is therefore the matrix product with the conjugate transpose of the second factor, $\mathsf{M}_2(\tilde{P}\star\tilde{Q})=\mathsf{M}_2(\tilde{P})\mathsf{M}_2(\tilde{Q})^{\dagger}$, and the general plain sesquilinear form is the **Hilbert–Schmidt pairing** of the matrices. The form is positive definite, so its matrix reading is the one of the five that is definite rather than indefinite, and the Frobenius norm is its carrier.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the identity and $e_k^2=-e_0$; $\tilde{Q}=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; scalar part $\mathrm{Sc}$; natural conjugation ${}^{\natural}$ negating $e_1,e_2,e_3$, Hermitian conjugation ${}^{*}={}^{\natural}\circ\bar{\cdot}$; sesquilinear product $\tilde{P}\star\tilde{Q}=\tilde{P}\tilde{Q}^{*}$. All matrix claims of this article are recomputed in the verification script of the pass.

## The Representation

**Definition.** The **matrix realization** is the isomorphism written $\mathsf{M}_2$. It converts a biquaternion into a $2 \times 2$ complex matrix,

$$
\mathsf{M}_2:\mathbb{B}\longrightarrow M_2(\mathbb{C}),
$$

and it is fixed by its values on the basis, the rest following by $\mathbb{C}$-linearity: $\mathsf{M}_2(e_0)=I$ on the identity and $\mathsf{M}_2(e_k)=-i\sigma_k$ on the three vector units.

The invariants and the two conjugations are

$$
\operatorname{Tr}\mathsf{M}_2(\tilde{Q})=2Q_0,\qquad \det \mathsf{M}_2(\tilde{Q})=\sum_\mu Q_\mu^2,\qquad \mathsf{M}_2(\tilde{Q}^{\natural})=\operatorname{adj}\mathsf{M}_2(\tilde{Q}),\qquad \mathsf{M}_2(\tilde{Q}^{*})=\mathsf{M}_2(\tilde{Q})^{\dagger} .
$$

The realization is a $*$-isomorphism: it is multiplicative and it carries the Hermitian conjugation of the algebra to the conjugate transpose of the matrices.

## The Sesquilinear Product in the Model

**Theorem (the product is the conjugate-transposed matrix product).** For all biquaternions,

$$
\mathsf{M}_2(\tilde{P}\star\tilde{Q})=\mathsf{M}_2(\tilde{P})\,\mathsf{M}_2(\tilde{Q})^{\dagger} ,
$$

the ordinary matrix product with the conjugate transpose in the second slot.

*Proof.* $\tilde{P}\star\tilde{Q}=\tilde{P}\tilde{Q}^{*}$, $\mathsf{M}_2$ is multiplicative and $\mathsf{M}_2(\tilde{Q}^{*})=\mathsf{M}_2(\tilde{Q})^{\dagger}$.

**The two actions of the unit.** The identity matrix acts by

$$
I\star Y=IY^{\dagger}=Y^{\dagger},\qquad Y\star I=YI^{\dagger}=Y,
$$

so $e_0$ is a **right unit and not a left unit** of the product: the right action of the unit is the identity while the left action is the conjugate transpose. In the notation of the two multiplication operators, $\mathsf{M}_2(L_{\tilde{A}}(\tilde{X}))=\mathsf{M}_2(\tilde{A})\mathsf{M}_2(\tilde{X})^{\dagger}$ and $\mathsf{M}_2(R_{\tilde{A}}(\tilde{X}))=\mathsf{M}_2(\tilde{X})\mathsf{M}_2(\tilde{A})^{\dagger}$. The absence of a two-sided unit is the failure of the conjugate transpose to be the identity, and every asymmetry of the group has this origin. The involution ${}^{*}$ is the conjugate transpose, so an element is self-adjoint exactly when its matrix is Hermitian and the Hermitian subspace $\mathbb{M}_+$ is the set of Hermitian matrices of $M_2(\mathbb{C})$.

**The units and the zero divisors.** An element is a unit of the algebra exactly when its matrix is invertible, so the units are $GL_2(\mathbb{C})$ and the zero divisors are the singular matrices; the norm-one group $\{\tilde{A}:\langle\tilde{A},\tilde{A}\rangle_{\natural}=1\}$ is $SL_2(\mathbb{C})$.

## The Sesquilinear Objects in the Model

**The ternary product and the quadratic representation.** The ternary product is the matrix product

$$
\mathsf{M}_2\bigl(\{\tilde{P},\tilde{Q},\tilde{R}\}\bigr)=\mathsf{M}_2(\tilde{P})\,\mathsf{M}_2(\tilde{Q})^{\dagger}\,\mathsf{M}_2(\tilde{R}),\qquad\text{so}\qquad \{X,Y,Z\}=XY^{\dagger}Z ,
$$

the **middle model** of the matrix algebra, and its quadratic representation is $Z\mapsto ZY^{\dagger}Z$.

**The associator.** The associator is

$$
[X,Y,Z]=X\bigl(Y^{\dagger}Z^{\dagger}-ZY^{\dagger}\bigr),
$$

the two groupings of the product being $(X\star Y)\star Z=XY^{\dagger}Z^{\dagger}$ and $X\star(Y\star Z)=XZY^{\dagger}$.

**The sandwich, the commutator and the symmetrised product.** The sandwich operator $S_{\tilde{P},\tilde{Q}}$ is $X\mapsto PX^{\dagger}Q^{\dagger}$, the commutator is the antisymmetric part $X\mapsto XY^{\dagger}-YX^{\dagger}$, and the symmetrised product is $\tfrac12(XY^{\dagger}+YX^{\dagger})$, whose diagonal is the Hermitian part of $XY^{\dagger}$. The rank of an element is the rank of its matrix, and the rank of a sandwich is at most the smaller of the ranks of its two parameters.

**The idempotents.** The idempotents of the multiplication are the **Hermitian projections**: $\Pi\star\Pi=\Pi$ is $\Pi\Pi^{\dagger}=\Pi$, that is $\Pi^{\dagger}=\Pi=\Pi^{2}$. They are $0$, $I$ and the orthogonal projections onto the lines of $\mathbb{C}^{2}$; the rank-one ones form the complex projective line $\mathbb{CP}^{1}\cong S^{2}$.

**Simplicity.** The multiplication has exactly the two two-sided ideals of $M_2(\mathbb{C})$, because a nonzero two-sided ideal of a full matrix algebra contains a matrix unit and hence the identity; the centre is $\mathbb{C}I=\mathbb{C}e_0$, and the only central idempotents are $0$ and $I$.

**The square and its invariants.** At $\tilde{P}=\tilde{Q}$ the value is $\tilde{Q}\star\tilde{Q}=\tilde{Q}\tilde{Q}^{*}$, of matrix $\mathsf{M}_2(\tilde{Q})\mathsf{M}_2(\tilde{Q})^{\dagger}$, and

$$
\operatorname{Tr}\mathsf{M}_2(\tilde{Q}\star\tilde{Q})=2\sum_\mu|Q_\mu|^{2},\qquad \det \mathsf{M}_2(\tilde{Q}\star\tilde{Q})=\bigl|\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\bigr|^{2},
$$

both real and nonnegative; the trace vanishes exactly at $\tilde{Q}=0$ and the determinant exactly at the zero divisors. This is the matrix form of the positivity of the square: the trace of the square is twice the squared definite norm of the eight real coordinates, and the determinant of the square is the squared modulus of the norm.

## The Batch in the Model

The model collects the objects of the group in one dictionary.

| object of the group | matrix model |
|---|---|
| element $\tilde{Q}=Q_0e_0+\mathbf{Q}$ | $\mathsf{M}_2(\tilde{Q})=\begin{pmatrix}Q_0-iQ_3&-iQ_1-Q_2\\-iQ_1+Q_2&Q_0+iQ_3\end{pmatrix}$ |
| involution $\tilde{Q}^{*}$ | the conjugate transpose $\mathsf{M}_2(\tilde{Q})^{\dagger}$ |
| multiplication $\tilde{P}\star\tilde{Q}$ | $XY^{\dagger}$ |
| ternary product $\{\tilde{P},\tilde{Q},\tilde{R}\}$ | $XY^{\dagger}Z$ |
| associator $[\tilde{P},\tilde{Q},\tilde{R}]$ | $X(Y^{\dagger}Z^{\dagger}-ZY^{\dagger})$ |
| idempotents of the multiplication | the Hermitian projections; the rank-one ones the projective line $\mathbb{CP}^{1}$ |
| simplicity | $M_2(\mathbb{C})$ simple, centre $\mathbb{C}I$ |
| left and right multiplications | $Y\mapsto AY^{\dagger}$, $Y\mapsto YA^{\dagger}$ |
| sandwich $S_{\tilde{P},\tilde{Q}}$ | $X\mapsto PX^{\dagger}Q^{\dagger}$ |
| commutator $[\tilde{P},\tilde{Q}]_\varsigma$ | $XY^{\dagger}-YX^{\dagger}$ |
| symmetrised product $\tilde{P}\circ\tilde{Q}$ | $\tfrac12(XY^{\dagger}+YX^{\dagger})$ |
| norm $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$ | $\det \mathsf{M}_2(\tilde{Q})$ |
| scalar part $\mathrm{Sc}(\tilde{Q})$ | $\tfrac12\operatorname{Tr}\mathsf{M}_2(\tilde{Q})$ |
| Hermitian form $\langle\tilde{P},\tilde{Q}\rangle_{*}$ | $\tfrac12\operatorname{Tr}(XY^{\dagger})$ |
| rank of an element | the rank of the matrix |

The ordinary matrix algebra, with no transpose, is the bilinear reading of the algebra; the table is the sesquilinear reading, and the transpose is the whole difference between the two columns.

## The General Plain Sesquilinear Form in the Model

**Theorem (the Hilbert–Schmidt pairing).** For all biquaternions,

$$
\langle\tilde{Q},\tilde{P}\rangle_{*} = \tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde{P})^{\dagger}\mathsf{M}_2(\tilde{Q})\bigr),
$$

the **Hilbert–Schmidt pairing** of the matrices; since $\mathsf{M}_2(\tilde{P})^{\dagger}=\mathsf{M}_2(\tilde{P}^{*})$, the right-hand side is $\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde{P}^{*}\tilde{Q}))=\mathrm{Sc}(\tilde{P}^{*}\tilde{Q})$ by the trace identity $\mathrm{Sc}(\tilde{R}\tilde{S})=\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde{R})\mathsf{M}_2(\tilde{S}))$.

**Theorem (the Frobenius norm).** On the diagonal,

$$
\langle\tilde{Q},\tilde{Q}\rangle_{*} = \tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde{Q})^{\dagger}\mathsf{M}_2(\tilde{Q})\bigr) = \tfrac12\bigl\lVert \mathsf{M}_2(\tilde{Q})\bigr\rVert_F^2 = \sum_\mu|Q_\mu|^2 = \lVert\tilde{Q}\rVert_E^2 ,
$$

so that $\lVert \mathsf{M}_2(\tilde{Q})\rVert_F=\sqrt2\,\lVert\tilde{Q}\rVert_E$, and the Hilbert–Schmidt inner product of the matrix algebra is one half of the squared Frobenius norm.

**Theorem (the trace and the determinant of a value).** For all biquaternions,

$$
\operatorname{Tr}\mathsf{M}_2(\tilde{P}\star\tilde{Q})=2\langle\tilde{P},\tilde{Q}\rangle_{*},\qquad \det \mathsf{M}_2(\tilde{P}\star\tilde{Q})=\langle\tilde{P},\tilde{P}\rangle_{\natural}\overline{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}},
$$

the trace of a value twice its Hermitian form and the determinant of a value the norm of the first factor times the conjugate of the norm of the second. The determinant is multiplicative and $\det \mathsf{M}_2(\tilde{Q})^{\dagger}=\overline{\det \mathsf{M}_2(\tilde{Q})}$, so the value of two norm-one elements again has determinant one and the product of two units is a unit.

**The signature and the null set.** The form is positive definite of signature $(8,0)$ on the eight real coordinates, so its null set is $\{0\}$ alone: no non-zero biquaternion is isotropic. The definite form is the companion of the four indefinite ones of the algebra.

**The automorphism group and the unit groups.** The form lives on the four complex coordinates, so its automorphism group is the unitary group $U(4)$, of real dimension $16$; among these, the maps $X\mapsto UXV^{\dagger}$ form the subgroup $U(2)\times U(2)$ modulo the common centre, which is the part that also preserves the algebra structure of $M_2(\mathbb{C})$. Under $\mathsf{M}_2$ the group of units of the algebra is $GL_2(\mathbb{C})$, the norm-one group is $SL_2(\mathbb{C})$, and the unitary slice is $U(2)$, whose special part is $SU(2)\cong\mathrm{Spin}(3)$.

## The Frobenius Norm of the Realization

**Proposition (the scale of the realization).** For every biquaternion,

$$
\bigl\|\mathsf{M}_2(\tilde{Q})\bigr\|_F=\sqrt{2}\,\bigl\|\tilde{Q}\bigr\|_E ,
$$

so $\mathsf{M}_2$, regarded as a real-linear map $\mathbb{B}_{\mathbb{R}}\to M_2(\mathbb{C})_{\mathbb{R}}\cong\mathbb{R}^{8}$, is bijective and multiplies all lengths by the fixed constant $\sqrt2$. The scale $\sqrt2$ is the trace normalisation $\operatorname{Tr}\mathsf{M}_2(\tilde{Q})=2Q_0$, and with the normalised map $\mathsf{M}_2/\sqrt2$ the two norms agree, $\lVert \mathsf{M}_2(\tilde{Q})/\sqrt2\rVert_F=\lVert\tilde{Q}\rVert_E$.

## The Unit Group in Matrix Form

**Proposition (the unit groups in matrix form).** Under $\mathsf{M}_2$,

$$
\mathbb{B}^{\times}\cong GL_2(\mathbb{C}),\qquad \{\tilde{Q}:\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=1\}\cong SL_2(\mathbb{C}),
$$

and their unitary slices are $U(2)$ and $SU(2)$, with $SU(2)\cong\mathrm{Spin}(3)$ and $SU(2)/\{\pm I\}\cong SO(3)$. The unit-norm group is the group that acts on the Hermitian subspace by $*$-congruence, $\tilde{Q}\mapsto\tilde{A}\tilde{Q}\tilde{A}^{*}$, which in the model is $X\mapsto AXA^{\dagger}$ on the Hermitian matrices.

## Worked Examples

**A definite element.** Let $\tilde{Q}=e_0+ie_1$. Then $\langle\tilde{Q},\tilde{Q}\rangle_{*}=|1|^2+|i|^2=2$ and $\lVert \mathsf{M}_2(\tilde{Q})\rVert_F=2=\sqrt2\cdot\sqrt2$; the element is a zero divisor of the plain product, yet it is not isotropic for the general plain sesquilinear form, and its matrix is singular.

**A Hermitian element.** Let $\tilde{Q}=e_0+ie_3$, so $Q_0=1$, $Q_3=i$. Then the coefficients of $\tilde{Q}^{*}$ are $\varepsilon_\mu\overline{Q_\mu}=(1,0,0,(-1)(-i))=Q_\mu$, so $\tilde{Q}^{*}=\tilde{Q}$ and the element is Hermitian; in the model $\mathsf{M}_2(\tilde{Q})=I+\sigma_3=\operatorname{diag}(2,0)$, a Hermitian matrix, and $\langle\tilde{Q},\tilde{Q}\rangle_{*}=2=\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde{Q})^{\dagger}\mathsf{M}_2(\tilde{Q}))$.

**A product read in matrices.** Let $\tilde{P}=e_1$ and $\tilde{Q}=e_2$. Then $\tilde{P}\star\tilde{Q}=e_1e_2^{*}=-e_3$, and in the model $\mathsf{M}_2(e_1)\mathsf{M}_2(e_2)^{\dagger}=(-i\sigma_1)(i\sigma_2)=\sigma_1\sigma_2=i\sigma_3=-\mathsf{M}_2(e_3)$, as the theorem requires.

## Summary

The $2\times2$ realization turns the Hermitian conjugation into the conjugate transpose, so the sesquilinear product is the matrix product with the conjugate transpose in the second slot, $\mathsf{M}_2(\tilde{P}\star\tilde{Q})=\mathsf{M}_2(\tilde{P})\mathsf{M}_2(\tilde{Q})^{\dagger}$, with the identity matrix as a right unit alone (the left action of the unit is the conjugate transpose) and the Hermitian subspace the Hermitian matrices. The ternary product is the middle model $XY^{\dagger}Z$, the associator is $X(Y^{\dagger}Z^{\dagger}-ZY^{\dagger})$, the sandwich is $X\mapsto PX^{\dagger}Q^{\dagger}$, and the idempotents are the Hermitian projections, $0$, $I$ and the orthogonal projections onto the lines of $\mathbb{C}^{2}$, of which the rank-one ones form $\mathbb{CP}^{1}$; the multiplication is simple with centre $\mathbb{C}I$, and the rank of an element is the rank of its matrix. The general plain sesquilinear form of the group is the Hilbert–Schmidt pairing $\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde{P})^{\dagger}\mathsf{M}_2(\tilde{Q}))=\langle\tilde{Q},\tilde{P}\rangle_{*}$, whose diagonal is the definite norm, $\tfrac12\lVert \mathsf{M}_2(\tilde{Q})\rVert_F^2=\sum_\mu|Q_\mu|^2$, with $\lVert \mathsf{M}_2(\tilde{Q})\rVert_F=\sqrt2\lVert\tilde{Q}\rVert_E$; it is positive definite of signature $(8,0)$, of null set $\{0\}$. Its automorphism group is $U(4)$, whose algebra-preserving part is $U(2)\times U(2)$ modulo the centre; the units are $GL_2(\mathbb{C})$, the norm-one group is $SL_2(\mathbb{C})$, and the unitary slice is $U(2)$ with special part $SU(2)\cong\mathrm{Spin}(3)$. The determinant of a value is $\langle\tilde{P},\tilde{P}\rangle_{\natural}\overline{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$ and its trace is $2\langle\tilde{P},\tilde{Q}\rangle_{*}$; the realization has scale $\sqrt2$, $\lVert \mathsf{M}_2(\tilde{Q})\rVert_F=\sqrt2\,\lVert\tilde{Q}\rVert_E$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2(\tilde{Q})$ | the $2\times2$ matrix of the realization, $\operatorname{Tr}\mathsf{M}_2(\tilde{Q})=2Q_0$ |
| $\mathsf{M}_2(\tilde{Q}^{*})=\mathsf{M}_2(\tilde{Q})^{\dagger}$ | the Hermitian conjugation is the conjugate transpose |
| $\mathsf{M}_2(\tilde{P}\star\tilde{Q})=\mathsf{M}_2(\tilde{P})\mathsf{M}_2(\tilde{Q})^{\dagger}$ | the sesquilinear product is the conjugate-transposed matrix product |
| $I\star Y=Y^{\dagger}$, $Y\star I=Y$ | the identity is a right unit alone |
| $\{X,Y,Z\}=XY^{\dagger}Z$, $[X,Y,Z]=X(Y^{\dagger}Z^{\dagger}-ZY^{\dagger})$ | the ternary product and the associator |
| $\Pi^{\dagger}=\Pi=\Pi^{2}$ | the idempotents are the Hermitian projections |
| $\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde{P})^{\dagger}\mathsf{M}_2(\tilde{Q}))=\langle\tilde{Q},\tilde{P}\rangle_{*}$ | the general plain sesquilinear form as the Hilbert–Schmidt pairing |
| $\operatorname{Tr}\mathsf{M}_2(\tilde{P}\star\tilde{Q})=2\langle\tilde{P},\tilde{Q}\rangle_{*}$, $\det \mathsf{M}_2(\tilde{P}\star\tilde{Q})=\langle\tilde{P},\tilde{P}\rangle_{\natural}\overline{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$ | the trace and the determinant of a value |
| $\lVert \mathsf{M}_2(\tilde{Q})\rVert_F=\sqrt2\,\lVert\tilde{Q}\rVert_E$ | the scale of the realization |
| $U(4)$, $U(2)\times U(2)$ modulo the centre | the automorphism group and the algebra-preserving part |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Graduate Texts in Mathematics 88, Springer, 1982), for the algebra $M_2(\mathbb{C})$, its idempotents, its one-sided ideals and the rank identity.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the matrix algebras with an involution and the Hermitian transpose as the standard example.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society Colloquium Publications 37, 1956), for the simplicity of a full matrix ring, the centre and the trace.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, second edition, 2013), for the trace, the determinant, the rank identity and the Hermitian forms of a matrix algebra.
- Irving Kaplansky, *Rings of Operators* (Benjamin, 1968), for the middle model $XY^{\dagger}Z$, its quadratic representation and the associated triple systems.
- *Introduction to the 2×2 Matrix Representation of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-representation-of-biquaternions.md`), for the realization and its first properties
- *Biquaternion 2×2 Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/biquaternion-2x2-matrix-element-representation-m2c.md`), for the further reading of the isomorphism
- *Introduction to the General Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-general-plain-sesqualgebra-of-biquaternions.md`), for the sesquilinear product on the algebra
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the form on the algebra
- *The Euclidean Topology of the Biquaternion Algebra* (`articles_maths/the-euclidean-topology-of-the-biquaternion-algebra.md`), for the topology the form induces
- *The General Plain Sesqualgebra in the $4\times4$ Matrix Representation* (`articles_maths/the-general-plain-sesqualgebra-in-the-4x4-matrix-representation.md`), for the companion reading of the group
- *The Six Subspaces under the General Plain Sesqualgebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-plain-sesqualgebra-of-biquaternions.md`), for the restriction theory of the form
