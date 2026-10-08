
# __The Biquaternion Sesqualgebra in the $2\times2$ Matrix Representation__

## Introduction

The reading group *Topology on the Biquaternions as a General Plain Sesqualgebra (GPS) over $\mathbb{C}$* reads the algebra through the **complex sesquilinear form** $\langle\tilde{P},\tilde{Q}\rangle_{*}=\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})=\sum_\mu P_\mu\overline{Q_\mu}$ and through the **sesquilinear product** $\tilde{P}\star\tilde{Q}=\tilde{P}\tilde{Q}^{*}$ that it polarises, whose algebra is *Biquaternions as a General Plain Sesqualgebra (GPS) over $\mathbb{C}$*. This article reads that group through the $2\times2$ matrix realization $\Phi$ of *Introduction to the $2\times2$ Matrix Representation of Biquaternions*, and it is the first of the two representation articles of the group; the companion *The Biquaternion Sesqualgebra in the $4\times4$ Regular Matrix Representation* repeats the reading on the left regular representation.

The Hermitian conjugation is the characteristic operation of the group, and in the model it is the **conjugate transpose**: $\Phi(\tilde{Q}^{*})=\Phi(\tilde{Q})^{\dagger}$. The sesquilinear product is therefore the matrix product with the conjugate transpose of the second factor, $\Phi(\tilde{P}\star\tilde{Q})=\Phi(\tilde{P})\Phi(\tilde{Q})^{\dagger}$, and the complex sesquilinear form is the **Hilbert–Schmidt pairing** of the matrices. The form is positive definite, so this is the one group of the five whose matrix reading carries a Euclidean and not an indefinite topology, and the Frobenius norm is its carrier.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the identity and $e_k^2=-e_0$; $\tilde{Q}=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; scalar part $\mathrm{Sc}$; natural conjugation ${}^{\natural}$ negating $e_1,e_2,e_3$, Hermitian conjugation ${}^{*}={}^{\natural}\circ\bar{\cdot}$; sesquilinear product $\tilde{P}\star\tilde{Q}=\tilde{P}\tilde{Q}^{*}$. All matrix claims of this article are recomputed in the verification script of the pass.

## The Representation

**Definition.** The **matrix realization** is the $\mathbb{C}$-linear isomorphism

$$
\Phi:\mathbb{B}\longrightarrow M_2(\mathbb{C}),\qquad \Phi(e_0)=I,\qquad \Phi(e_k)=-i\sigma_k ,
$$

with the invariants and the two conjugations

$$
\operatorname{Tr}\Phi(\tilde{Q})=2Q_0,\qquad \det\Phi(\tilde{Q})=\sum_\mu Q_\mu^2,\qquad \Phi(\tilde{Q}^{\natural})=\operatorname{adj}\Phi(\tilde{Q}),\qquad \Phi(\tilde{Q}^{*})=\Phi(\tilde{Q})^{\dagger} .
$$

The realization is a $*$-isomorphism: it is multiplicative and it carries the Hermitian conjugation of the algebra to the conjugate transpose of the matrices.

## The Sesquilinear Product in the Model

**Theorem (the product is the conjugate-transposed matrix product).** For all biquaternions,

$$
\Phi(\tilde{P}\star\tilde{Q})=\Phi(\tilde{P})\,\Phi(\tilde{Q})^{\dagger} ,
$$

the ordinary matrix product with the conjugate transpose in the second slot.

*Proof.* $\tilde{P}\star\tilde{Q}=\tilde{P}\tilde{Q}^{*}$, $\Phi$ is multiplicative and $\Phi(\tilde{Q}^{*})=\Phi(\tilde{Q})^{\dagger}$.

**The two actions of the unit.** The identity matrix acts by

$$
I\star Y=IY^{\dagger}=Y^{\dagger},\qquad Y\star I=YI^{\dagger}=Y,
$$

so $e_0$ is a **right unit and not a left unit** of the product: the right action of the unit is the identity while the left action is the conjugate transpose. In the notation of the two multiplication operators, $\Phi(L_{\tilde{A}}(\tilde{X}))=\Phi(\tilde{A})\Phi(\tilde{X})^{\dagger}$ and $\Phi(R_{\tilde{A}}(\tilde{X}))=\Phi(\tilde{X})\Phi(\tilde{A})^{\dagger}$. The absence of a two-sided unit is the failure of the conjugate transpose to be the identity, and every asymmetry of the group has this origin. The involution ${}^{*}$ is the conjugate transpose, so an element is self-adjoint exactly when its matrix is Hermitian and the Hermitian subspace $\mathbb{M}_+$ is the set of Hermitian matrices of $M_2(\mathbb{C})$.

**The units and the zero divisors.** An element is a unit of the algebra exactly when its matrix is invertible, so the units are $GL_2(\mathbb{C})$ and the zero divisors are the singular matrices; the norm-one group $\{\tilde{A}:\langle\tilde{A},\tilde{A}\rangle_{\natural}=1\}$ is $SL_2(\mathbb{C})$.

## The Sesquilinear Objects in the Model

**The ternary product and the quadratic representation.** The ternary product is the matrix product

$$
\Phi\bigl(\{\tilde{P},\tilde{Q},\tilde{R}\}\bigr)=\Phi(\tilde{P})\,\Phi(\tilde{Q})^{\dagger}\,\Phi(\tilde{R}),\qquad\text{so}\qquad \{X,Y,Z\}=XY^{\dagger}Z ,
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

**The square and its invariants.** At $\tilde{P}=\tilde{Q}$ the value is $\tilde{Q}\star\tilde{Q}=\tilde{Q}\tilde{Q}^{*}$, of matrix $\Phi(\tilde{Q})\Phi(\tilde{Q})^{\dagger}$, and

$$
\operatorname{Tr}\Phi(\tilde{Q}\star\tilde{Q})=2\sum_\mu|Q_\mu|^{2},\qquad \det\Phi(\tilde{Q}\star\tilde{Q})=\bigl|\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\bigr|^{2},
$$

both real and nonnegative; the trace vanishes exactly at $\tilde{Q}=0$ and the determinant exactly at the zero divisors. This is the matrix form of the positivity of the square: the trace of the square is twice the squared Euclidean norm of the eight real coordinates, and the determinant of the square is the squared modulus of the norm.

## The Batch in the Model

The model collects the objects of the group in one dictionary.

| object of the group | matrix model |
|---|---|
| element $\tilde{Q}=Q_0e_0+\mathbf{Q}$ | $\Phi(\tilde{Q})=\begin{pmatrix}Q_0-iQ_3&-iQ_1-Q_2\\-iQ_1+Q_2&Q_0+iQ_3\end{pmatrix}$ |
| involution $\tilde{Q}^{*}$ | the conjugate transpose $\Phi(\tilde{Q})^{\dagger}$ |
| multiplication $\tilde{P}\star\tilde{Q}$ | $XY^{\dagger}$ |
| ternary product $\{\tilde{P},\tilde{Q},\tilde{R}\}$ | $XY^{\dagger}Z$ |
| associator $[\tilde{P},\tilde{Q},\tilde{R}]$ | $X(Y^{\dagger}Z^{\dagger}-ZY^{\dagger})$ |
| idempotents of the multiplication | the Hermitian projections; the rank-one ones the sphere $\mathbb{CP}^{1}$ |
| simplicity | $M_2(\mathbb{C})$ simple, centre $\mathbb{C}I$ |
| left and right multiplications | $Y\mapsto AY^{\dagger}$, $Y\mapsto YA^{\dagger}$ |
| sandwich $S_{\tilde{P},\tilde{Q}}$ | $X\mapsto PX^{\dagger}Q^{\dagger}$ |
| commutator $[\tilde{P},\tilde{Q}]_\varsigma$ | $XY^{\dagger}-YX^{\dagger}$ |
| symmetrised product $\tilde{P}\circ\tilde{Q}$ | $\tfrac12(XY^{\dagger}+YX^{\dagger})$ |
| norm $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$ | $\det\Phi(\tilde{Q})$ |
| scalar part $\mathrm{Sc}(\tilde{Q})$ | $\tfrac12\operatorname{Tr}\Phi(\tilde{Q})$ |
| Hermitian form $\langle\tilde{P},\tilde{Q}\rangle_{*}$ | $\tfrac12\operatorname{Tr}(XY^{\dagger})$ |
| rank of an element | the rank of the matrix |

The ordinary matrix algebra, with no transpose, is the bilinear reading of the algebra; the table is the sesquilinear reading, and the transpose is the whole difference between the two columns.

## The Complex Sesquilinear Form in the Model

**Theorem (the Hilbert–Schmidt pairing).** For all biquaternions,

$$
\langle\tilde{Q},\tilde{P}\rangle_{*} = \tfrac12\operatorname{Tr}\bigl(\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q})\bigr),
$$

the **Hilbert–Schmidt pairing** of the matrices; since $\Phi(\tilde{P})^{\dagger}=\Phi(\tilde{P}^{*})$, the right-hand side is $\tfrac12\operatorname{Tr}(\Phi(\tilde{P}^{*}\tilde{Q}))=\mathrm{Sc}(\tilde{P}^{*}\tilde{Q})$ by the trace identity $\mathrm{Sc}(\tilde{R}\tilde{S})=\tfrac12\operatorname{Tr}(\Phi(\tilde{R})\Phi(\tilde{S}))$.

**Theorem (the Frobenius norm).** On the diagonal,

$$
\langle\tilde{Q},\tilde{Q}\rangle_{*} = \tfrac12\operatorname{Tr}\bigl(\Phi(\tilde{Q})^{\dagger}\Phi(\tilde{Q})\bigr) = \tfrac12\bigl\lVert\Phi(\tilde{Q})\bigr\rVert_F^2 = \sum_\mu|Q_\mu|^2 = \lVert\tilde{Q}\rVert_E^2 ,
$$

so that $\lVert\Phi(\tilde{Q})\rVert_F=\sqrt2\,\lVert\tilde{Q}\rVert_E$, and the Hilbert–Schmidt inner product of the matrix algebra is one half of the squared Frobenius norm.

**Theorem (the trace and the determinant of a value).** For all biquaternions,

$$
\operatorname{Tr}\Phi(\tilde{P}\star\tilde{Q})=2\langle\tilde{P},\tilde{Q}\rangle_{*},\qquad \det\Phi(\tilde{P}\star\tilde{Q})=\langle\tilde{P},\tilde{P}\rangle_{\natural}\overline{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}},
$$

the trace of a value twice its Hermitian form and the determinant of a value the norm of the first factor times the conjugate of the norm of the second. The determinant is multiplicative and $\det\Phi(\tilde{Q})^{\dagger}=\overline{\det\Phi(\tilde{Q})}$, so the value of two norm-one elements again has determinant one and the product of two units is a unit.

**The signature and the null set.** The form is positive definite of signature $(8,0)$ on the eight real coordinates, so its null set is $\{0\}$ alone: no non-zero biquaternion is isotropic, and the topology that the form induces is the Euclidean topology of $\mathbb{B}$, which *The Euclidean Topology of the Biquaternion Algebra* reads on the algebra itself.

**The isometry group and the unit groups.** The form lives on the four complex coordinates, so its isometry group is the unitary group $U(4)$, of real dimension $16$; among these, the maps $X\mapsto UXV^{\dagger}$ form the subgroup $U(2)\times U(2)$ modulo the common centre, which is the part that also preserves the algebra structure of $M_2(\mathbb{C})$. Under $\Phi$ the group of units of the algebra is $GL_2(\mathbb{C})$, the norm-one group is $SL_2(\mathbb{C})$, and the maximal compact subgroup is $U(2)$, whose special part is $SU(2)\cong\mathrm{Spin}(3)$.

## The Frobenius Norm and the Underlying Topology

**Proposition (the realization is a similarity of Euclidean spaces).** For every biquaternion,

$$
\bigl\|\Phi(\tilde{Q})\bigr\|_F=\sqrt{2}\,\bigl\|\tilde{Q}\bigr\|_E ,
$$

so $\Phi$, regarded as a real-linear map $\mathbb{B}_{\mathbb{R}}\to M_2(\mathbb{C})_{\mathbb{R}}\cong\mathbb{R}^{8}$, is a **similarity of Euclidean spaces**: it is bijective and multiplies all lengths by the fixed constant $\sqrt2$. The underlying topology of the algebra is therefore the Euclidean topology of $\mathbb{R}^{8}$ transported along $\Phi$; the algebra is complete and contractible, and its Euclidean unit sphere is the $7$-sphere $S^{7}$. The scale $\sqrt2$ is the trace normalisation $\operatorname{Tr}\Phi(\tilde{Q})=2Q_0$, and with the normalised map $\Phi/\sqrt2$ the realization is an exact isometry onto $M_2(\mathbb{C})$ with the Frobenius norm.

## The Unit Group and the Unit Spheres

**Proposition (the unit groups in matrix form).** Under $\Phi$,

$$
\mathbb{B}^{\times}\cong GL_2(\mathbb{C}),\qquad \{\tilde{Q}:\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=1\}\cong SL_2(\mathbb{C}),
$$

and their maximal compact subgroups are $U(2)$ and $SU(2)$, with $SU(2)\cong\mathrm{Spin}(3)$ and $SU(2)/\{\pm I\}\cong SO(3)$. The unit-norm group is the group that acts on the Hermitian subspace by $*$-congruence, $\tilde{Q}\mapsto\tilde{A}\tilde{Q}\tilde{A}^{*}$, which in the model is $X\mapsto AXA^{\dagger}$ on the Hermitian matrices.

The Euclidean unit spheres of the algebra and of its distinguished subspaces have a direct matrix reading.

| object | Euclidean description | matrix description |
|---|---|---|
| the algebra $\mathbb{B}$ | unit sphere $S^{7}$ | the Frobenius sphere $\|\Phi(\tilde{Q})\|_F^2=2$ |
| the quaternion subspace | unit sphere $S^{3}$ | the Frobenius sphere on the matrices with real entries |
| the roots of $-1$ in the quaternion subspace | $S^{2}$ | the traceless anti-Hermitian matrices of Frobenius norm $\sqrt2$ |
| the Hermitian subspace $\mathbb{M}_+$ | its null cone and its link | the Hermitian matrices, of signature $(1,3)$ |

## Worked Examples

**A definite element.** Let $\tilde{Q}=e_0+ie_1$. Then $\langle\tilde{Q},\tilde{Q}\rangle_{*}=|1|^2+|i|^2=2$ and $\lVert\Phi(\tilde{Q})\rVert_F=2=\sqrt2\cdot\sqrt2$; the element is a zero divisor of the plain product, yet it is not isotropic for the sesquilinear form, and its matrix is singular.

**A Hermitian element.** Let $\tilde{Q}=e_0+ie_3$, so $Q_0=1$, $Q_3=i$. Then the coefficients of $\tilde{Q}^{*}$ are $\varepsilon_\mu\overline{Q_\mu}=(1,0,0,(-1)(-i))=Q_\mu$, so $\tilde{Q}^{*}=\tilde{Q}$ and the element is Hermitian; in the model $\Phi(\tilde{Q})=I+\sigma_3=\operatorname{diag}(2,0)$, a Hermitian matrix, and $\langle\tilde{Q},\tilde{Q}\rangle_{*}=2=\tfrac12\operatorname{Tr}(\Phi(\tilde{Q})^{\dagger}\Phi(\tilde{Q}))$.

**A product read in matrices.** Let $\tilde{P}=e_1$ and $\tilde{Q}=e_2$. Then $\tilde{P}\star\tilde{Q}=e_1e_2^{*}=-e_3$, and in the model $\Phi(e_1)\Phi(e_2)^{\dagger}=(-i\sigma_1)(i\sigma_2)=\sigma_1\sigma_2=i\sigma_3=-\Phi(e_3)$, as the theorem requires.

## Summary

The $2\times2$ realization turns the Hermitian conjugation into the conjugate transpose, so the sesquilinear product is the matrix product with the conjugate transpose in the second slot, $\Phi(\tilde{P}\star\tilde{Q})=\Phi(\tilde{P})\Phi(\tilde{Q})^{\dagger}$, with the identity matrix as a right unit alone (the left action of the unit is the conjugate transpose) and the Hermitian subspace the Hermitian matrices. The ternary product is the middle model $XY^{\dagger}Z$, the associator is $X(Y^{\dagger}Z^{\dagger}-ZY^{\dagger})$, the sandwich is $X\mapsto PX^{\dagger}Q^{\dagger}$, and the idempotents are the Hermitian projections, $0$, $I$ and the orthogonal projections onto the lines of $\mathbb{C}^{2}$, of which the rank-one ones form $\mathbb{CP}^{1}$; the multiplication is simple with centre $\mathbb{C}I$, and the rank of an element is the rank of its matrix. The complex sesquilinear form of the group is the Hilbert–Schmidt pairing $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q}))=\langle\tilde{Q},\tilde{P}\rangle_{*}$, whose diagonal is the Euclidean norm, $\tfrac12\lVert\Phi(\tilde{Q})\rVert_F^2=\sum_\mu|Q_\mu|^2$, with $\lVert\Phi(\tilde{Q})\rVert_F=\sqrt2\lVert\tilde{Q}\rVert_E$; it is positive definite of signature $(8,0)$, of null set $\{0\}$, and it induces the Euclidean topology of the algebra. Its isometry group is $U(4)$, whose algebra-preserving part is $U(2)\times U(2)$ modulo the centre; the units are $GL_2(\mathbb{C})$, the norm-one group is $SL_2(\mathbb{C})$, and the maximal compact subgroup is $U(2)$ with special part $SU(2)\cong\mathrm{Spin}(3)$. The determinant of a value is $\langle\tilde{P},\tilde{P}\rangle_{\natural}\overline{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$ and its trace is $2\langle\tilde{P},\tilde{Q}\rangle_{*}$; the realization is a similarity of Euclidean spaces of scale $\sqrt2$, so the underlying space is $\mathbb{R}^{8}$ with unit sphere $S^{7}$, the quaternion subspace carrying $S^{3}$ and its root set $S^{2}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Phi(\tilde{Q})$ | the $2\times2$ matrix of the realization, $\operatorname{Tr}\Phi(\tilde{Q})=2Q_0$ |
| $\Phi(\tilde{Q}^{*})=\Phi(\tilde{Q})^{\dagger}$ | the Hermitian conjugation is the conjugate transpose |
| $\Phi(\tilde{P}\star\tilde{Q})=\Phi(\tilde{P})\Phi(\tilde{Q})^{\dagger}$ | the sesquilinear product is the conjugate-transposed matrix product |
| $I\star Y=Y^{\dagger}$, $Y\star I=Y$ | the identity is a right unit alone |
| $\{X,Y,Z\}=XY^{\dagger}Z$, $[X,Y,Z]=X(Y^{\dagger}Z^{\dagger}-ZY^{\dagger})$ | the ternary product and the associator |
| $\Pi^{\dagger}=\Pi=\Pi^{2}$ | the idempotents are the Hermitian projections |
| $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q}))=\langle\tilde{Q},\tilde{P}\rangle_{*}$ | the complex sesquilinear form as the Hilbert–Schmidt pairing |
| $\operatorname{Tr}\Phi(\tilde{P}\star\tilde{Q})=2\langle\tilde{P},\tilde{Q}\rangle_{*}$, $\det\Phi(\tilde{P}\star\tilde{Q})=\langle\tilde{P},\tilde{P}\rangle_{\natural}\overline{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$ | the trace and the determinant of a value |
| $\lVert\Phi(\tilde{Q})\rVert_F=\sqrt2\,\lVert\tilde{Q}\rVert_E$ | the realization is a similarity of Euclidean spaces |
| $U(4)$, $U(2)\times U(2)$ modulo the centre | the isometry group and the algebra-preserving part |
| $S^{7}$, $S^{3}$, $S^{2}$ | the unit spheres of the algebra, of the quaternion subspace and of its roots of $-1$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Graduate Texts in Mathematics 88, Springer, 1982), for the algebra $M_2(\mathbb{C})$, its idempotents, its one-sided ideals and the rank identity.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the matrix algebras with an involution and the Hermitian transpose as the standard example.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society Colloquium Publications 37, 1956), for the simplicity of a full matrix ring, the centre and the trace.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, second edition, 2013), for the trace, the determinant, the rank identity and the Hermitian forms of a matrix algebra.
- Irving Kaplansky, *Rings of Operators* (Benjamin, 1968), for the middle model $XY^{\dagger}Z$, its quadratic representation and the associated triple systems.
- *Introduction to the $2\times2$ Matrix Representation of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-representation-of-biquaternions.md`), for the realization and its first properties
- *Biquaternion 2×2 Matrix Element Representation* (`articles_maths/biquaternion-2x2-matrix-element-representation.md`), for the further reading of the isomorphism
- *Biquaternions as a General Plain Sesqualgebra (GPS) over $\mathbb{C}$* (`articles_maths/biquaternions-as-a-general-plain-sesqualgebra-gps-over-c.md`), for the sesquilinear product on the algebra
- *The Hermitian Form on the Biquaternion Algebra* (`articles_maths/the-hermitian-form-on-the-biquaternion-algebra.md`), for the form on the algebra
- *The Euclidean Topology of the Biquaternion Algebra* (`articles_maths/the-euclidean-topology-of-the-biquaternion-algebra.md`), for the topology the form induces
- *The Biquaternion Sesqualgebra in the $4\times4$ Regular Matrix Representation* (`articles_maths/the-biquaternion-sesqualgebra-in-the-4x4-regular-matrix-representation.md`), for the companion reading of the group
- *The Six Subspaces under the Complex Sesquilinear Form* (`articles_maths/the-six-subspaces-under-the-complex-sesquilinear-form.md`), for the restriction theory of the form
