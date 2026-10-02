# __One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with the Hermitian conjugation ${}^{*}$ of the physics corpus, carries two one-sided operators for each element:

$$
L_{\tilde A}(\tilde V)=\tilde A\,\tilde V ,\qquad R_{\tilde B}(\tilde V)=\tilde V\,\tilde B .
$$

Physically the pair is already in use everywhere without being named. The **left multiplication by a generator** is the Clifford multiplication that the corpus writes with the $\gamma$'s, and the products of the left multiplications are the Dirac matrices of the framework; the **right multiplication** is the commuting shadow action that fixes the chirality and the reality conditions; and the **Dirac operator** is a sum of left multiplications with derivatives, $D=\sum_{\mu}e_{\mu}\partial_{\mu}$ (*Biquaternion Spin Geometry*, *The Dirac Equation in Biquaternionic Form*).

This article is the physics companion of *One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* of the mathematical series, where the operator, the composition laws, the adjoint theorem, the type criteria and the double centraliser theorem are proved. What is added here is the physical reading: which generator acts skew-adjointly, why that is what makes the Clifford relations and the Dirac operator work, why the right multiplications are the commutant, which group acts isometrically, and what the one-sided operators see that the two-sided sandwich of the companion article does not.

## The Left Multiplication as the Clifford Action

**Proposition (linearity and composition).** The assignment $\tilde A\mapsto L_{\tilde A}$ is $\mathbb{C}$-linear and injective, and $L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B}$; the assignment $\tilde B\mapsto R_{\tilde B}$ is $\mathbb{C}$-linear and injective too, with $R_{\tilde A}R_{\tilde B}=R_{\tilde B\tilde A}$, and the two families commute: $L_{\tilde A}R_{\tilde B}=R_{\tilde B}L_{\tilde A}$.

**Physical reading.** $L$ is a faithful representation of the algebra on a four-complex-dimensional space with the positive definite form $(\tilde T,\tilde V)=\mathrm{Sc}(\tilde T^{*}\tilde V)$, that is, on **two copies of the spinor module** (*The 2×2 Matrix Element Representation of Biquaternions* (`articles_physics/the-2x2-matrix-element-representation-of-biquaternions.md`), *The Spinor Module in Biquaternionic Form and Its Lorentz Action*). Writing the elements of the algebra as matrices, $L_{\tilde A}$ is the matrix multiplication on the left, which is the standard way the corpus writes the Clifford action and the Dirac matrices; the right multiplications $R_{\tilde B}$ act on the second factor and are the shadow algebra.

**Proposition (the generator relations).** With the basis $e_{0},e_{1},e_{2},e_{3}$ of the algebra, $e_{0}=1$,

$$
L_{e_{0}}=\mathrm{id},\qquad
L_{e_{k}}^{2}=-L_{e_{0}}=-\mathrm{id},\qquad
L_{e_{j}}L_{e_{k}}+L_{e_{k}}L_{e_{j}}=-2\delta_{jk}\,\mathrm{id}\quad(j,k\geq1),
$$

and the commutator closes on the generators, $[L_{e_{1}},L_{e_{2}}]=2L_{e_{3}}$ and its cyclic permutations.

*Proof.* The composition law gives $L_{e_{j}}L_{e_{k}}=L_{e_{j}e_{k}}$ and the quaternion relations give $e_{k}^{2}=-1$, $e_{j}e_{k}+e_{k}e_{j}=0$ for $j\neq k$, $e_{1}e_{2}=e_{3}$. In particular $L_{e_{1}}L_{e_{2}}-L_{e_{2}}L_{e_{1}}=L_{2e_{3}}=2L_{e_{3}}$.

**Physical reading.** The three operators $L_{e_{1}},L_{e_{2}},L_{e_{3}}$ are three complex structures on the spinor space, mutually anticommuting, of squares minus the identity: they are the Clifford generators of the internal space, and their commutators close the Lie algebra of the internal rotations on themselves, $[L_{e_{j}},L_{e_{k}}]=2\sum_{l}\epsilon_{jkl}L_{e_{l}}$. This is the operator form of the structure that *The Clifford Structure of the Biquaternion Algebra* states algebraically, and it is what makes the algebra the even Clifford algebra of the framework.

## The Adjoint of the Action and the Spinor Form

**Theorem (the adjoints).** For all $\tilde A,\tilde B$,

$$
(L_{\tilde A})^{*}=L_{\tilde A^{*}},\qquad (R_{\tilde B})^{*}=R_{\tilde B^{*}} .
$$

**Corollary (the module axiom).** The form is invariant in the sense of a Hermitian module,

$$
(\tilde A\cdot s,\ t) = (s,\ \tilde A^{*}\cdot t) ,
$$

and $L$ is a faithful $*$-representation of the algebra on the positive definite spinor form. This is the biquaternion instance of the module axiom of *Hermitian Modules over a Hilbert Algebra with Hermitian Adjoint* and of *The Adjoint of the One-Sided Action with Hermitian Adjoint*.

**The physical point.** The adjoint of the action is the action of the adjoint element, and **not** the other family: $(L_{\tilde A}s,t)\neq(s,R_{\tilde A^{*}}t)$ in general. It is this asymmetry that makes the positive definite form the right spinor form for the framework: the infinitesimal generators — the material sector elements, which are anti-Hermitian — act by **skew-adjoint** operators, so the exponentials act by unitary ones, and the internal group is compact.

## Skew-Adjoint Generators and the Internal Group

**Theorem (the type criteria).** For $\tilde A\in\mathbb{B}$,

$$
L_{\tilde A}\ \text{self-adjoint}\iff \tilde A\in\mathbb{M}_+,\qquad
L_{\tilde A}\ \text{skew-adjoint}\iff \tilde A\in\mathbb{M}_-,\qquad
L_{\tilde A}\ \text{unitary and isometric}\iff \tilde A\in U ,
$$

and $L_{\tilde A}$ is invertible iff $\tilde A$ is. Here $\mathbb{M}_+$ is the informational sector, $\mathbb{M}_-$ the material sector, and $U=U(2)$ the unitary slice.

**Corollary (where the generators live).** In the basis of the algebra, $e_{0}\in\mathbb{M}_+$ and $e_{k}\in\mathbb{M}_-$: the identity generator is **self-adjoint** and the three vector generators are **skew-adjoint**. This is the operator statement of the relation of the dagger to the Clifford structure, and it is why the internal rotations, whose generators are the $L_{e_{k}}$, are unitary while the mass and the boosts, whose generators are in the informational sector, are self-adjoint.

**Corollary (the exponential and the internal group).** The image of the slice is a compact group of unitary operators isomorphic to $U(2)$, the image of the material sector is its Lie algebra of skew-adjoint operators, and the exponential stays inside the one-sided family:

$$
\tilde A\in\mathbb{M}_-\ \Longrightarrow\ e^{L_{\tilde A}}=L_{e^{\tilde A}}\ \text{is unitary} .
$$

The internal symmetry group of the framework is therefore one-sided, and its compact part is $U(2)$, with determinant-one part $\mathrm{SU}(2)\cong\mathrm{Spin}(3)$ (*The Biquaternion Unit Group as a Topological Group*, *Biquaternion Versors and the Orthogonal Group*).

**Corollary (the phase is visible, unlike the two-sided case).** $L_{\omega \tilde A}=\omega L_{\tilde A}$ for a central phase $\omega$, so the phase is **not** erased: $L_{\omega e_{0}}$ is the scalar operator $\omega\,\mathrm{id}$, which is the identity only for $\omega=1$. The contrast with the two-sided operator is exact and physical: the two-sided sandwich is phase-blind, $\Theta_{\omega\tilde{Q}}=\Theta_{\tilde{Q}}$, because it acts on states and returns the quadratic combination $\tilde{Q}\tilde{Q}^{*}$; the one-sided operator sees the phase because it acts on the amplitude. This is the operator form of the double cover, of $SU(2)$ against $SO(3)$, and of the phase freedom that is a redundancy of the description of a state and not of a state vector.

## The Dirac Operator as a One-Sided Operator

The corpus's Dirac operator is the composition of the covariant derivative with the Clifford multiplication by the basis vectors,

$$
D=\sum_{\mu=0}^{3}e_{\mu}\partial_{\mu} = \sum_{\mu}L_{e_{\mu}}\,\partial_{\mu},
$$

with $D^{2}$ the d'Alembertian on the flat algebra and with the kernel the space of the regular functions (*Biquaternion Spin Geometry*, *The Dirac Equation in Biquaternionic Form*).

**Physical reading.** The operator is a sum of one-sided operators, and its formal properties are the one-sided ones: each $L_{e_{\mu}}$ acts on the spinor variable, each $\partial_{\mu}$ acts on the spacetime variable, and the two commute. The self-adjointness of $D$ for the spinor form is the statement $(L_{e_{\mu}})^{*}=L_{e_{\mu}^{*}}$ composed with the formal skew-adjointness of the derivative; the details, including the sign fixing and the role of the timelike basis element, are the subject of the Dirac adjoint, which is *Spinor Adjoints and the Dirac Adjoint with Hermitian Adjoint* in the mathematical series and the adjoint conventions of *The Spinor Module in Biquaternionic Form and Its Lorentz Action* in this one. What matters here is that **no two-sided operator enters the Dirac operator**: the dynamics is one-sided, and the two-sided operator is reserved for the transformations of the sectors.

## The Right Multiplication, the Commutant and the Absence of Invariants

**Theorem (the double centraliser).** An operator commuting with every left multiplication is a right multiplication, and conversely; an operator commuting with both families is a scalar.

**Physical reading.** The right multiplications form the **commutant** of the Clifford action, hence the shadow algebra that the corpus meets whenever it separates the left and the right structure of a spinor: the chirality projectors, the reality condition and the conjugation of the Dirac equation are written with the right action. The bicommutant theorem has a physical consequence that is easy to state: since the commutant of the Clifford action is generated by the right action and the bicommutant is the scalars, the spinor module is irreducible up to the shadow algebra, so the algebra admits **no invariant operator except the scalars**. Physically this is the statement that the internal space of this algebra has no coarse-grained label that survives the action: every internal observable is a scalar multiple of the identity unless it is written with the shadow algebra, which is the algebraic reason for the framework's absence of superselection sectors, and the algebraic form of the simplicity of the Clifford algebra (see *The Clifford Structure of the Biquaternion Algebra* and the commutant statements of *The 2×2 Matrix Element Representation of Biquaternions* (`articles_physics/the-2x2-matrix-element-representation-of-biquaternions.md`)).

**Corollary (the mixed operators).** The general product $L_{\tilde A}R_{\tilde B}$ has two independent parameters and commutes with nothing in general; it is a two-sided operator only for $\tilde B=\lambda \tilde A^{*}$. Physically, the two-sided operators are the one-parameter specialisations of the mixed family, and the extra parameter of the mixed family is a **relative phase between the left and the right structure**, which the sandwich cannot carry.

## The Isometry Group, and the Lorentz Action Again

**Proposition (which action preserves the spinor form).** $L_{\tilde A}$ is an isometry of $(\cdot,\cdot)$ exactly for $\tilde A\in U$, and $R_{\tilde B}$ exactly for $\tilde B\in U$.

**Physical reading.** The group of the one-sided isometries is $U(2)$, the internal group; the Lorentz action is **not** among them. A Lorentz transformation is produced by an element of unit quaternion norm, and the unit-norm slice is $SL(2,\mathbb{C})$ up to phase, not the slice of the dagger; so the Lorentz action preserves the **interval** $N$ and the internal form $(\cdot,\cdot)$ is not preserved by it except on the compact part. The corpus states the contrast group-theoretically, $U(2)$ for the automorphisms and the similarities of $N$ for the Lorentz action (*Biquaternion Versors and the Orthogonal Group*, *Biquaternion Rotations and Lorentz Transformations*); the operator version is that the isometries of the spinor form and the similarities of the interval are different groups, of different generators, and that the second contains the first exactly when the transformation is compact.

## Worked Examples

**The internal rotation generators.** For the material-sector elements $e_{1},e_{2},e_{3}$ the operators $L_{e_{k}}$ are skew-adjoint, of square $-\mathrm{id}$, and $[L_{e_{1}},L_{e_{2}}]=2L_{e_{3}}$. The exponential of $L_{\theta e_{1}/2}$ is the unitary operator of the internal rotation by the angle $\theta$ about the first internal axis, and the factor one-half of the exponent is the double cover: the one-sided operator exponentiates half of what the two-sided sandwich of the companion article produces.

**The informational generator.** For $\tilde A=e_{0}$ the operator is the identity, self-adjoint; for $\tilde A=ie_{1}$, which is Hermitian and of vector part imaginary, $L_{ie_{1}}=iL_{e_{1}}$ is self-adjoint as $i$ times a skew-adjoint operator, and of square $-\mathrm{id}\cdot i^{2}=$ positive: the informational generators act by self-adjoint operators, and the mass term of the framework, which lives in that sector, is therefore a self-adjoint one-sided operator.

**A mixed operator.** $\tilde V\mapsto e_{1}\tilde Ve_{2}$ is neither a two-sided operator nor a symmetry: $L_{e_{1}}R_{e_{2}}(e_{0})=e_{1}e_{2}=e_{3}$, which is anti-Hermitian, while a two-sided operator always sends the identity into the informational sector, $\Theta_{\tilde{Q}}(e_{0})=\tilde{Q}\tilde{Q}^{*}\in\mathbb{M}_+$. The mixed family is the one that changes the relative phase of the two structures.

**A plane-wave spinor.** For a plane-wave solution $\psi$ of the Dirac equation the one-sided action is what the equation uses: the Clifford generators act on the spinor index and the derivative brings down the momentum, $D\psi = i\not{p}\psi$ in the corpus's conventions, and the two-sided operator then acts on the resulting state as the sandwich of the companion article. The two articles together therefore split the physics cleanly: **one-sided for the amplitudes and the dynamics, two-sided for the states and the frames.**

## Summary

The left and the right multiplications $L_{\tilde A}(\tilde V)=\tilde A\tilde V$ and $R_{\tilde B}(\tilde V)=\tilde V\tilde B$ are the one-sided operators of the biquaternion algebra, and in the physics they are the Clifford action and its shadow. $L$ is a faithful $*$-representation of the algebra on the positive definite spinor form of complex dimension four, that is, on two copies of the spinor module, with the composition law $L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B}$ and the module axiom $(\tilde A\cdot s,t)=(s,\tilde A^{*}\cdot t)$. The type criteria are the ones of the sectors: $L_{\tilde A}$ is self-adjoint exactly on the informational sector, skew-adjoint exactly on the material sector, and unitary and isometric exactly on the slice $U(2)$; consequently the three vector generators are skew-adjoint complex structures with $L_{e_{j}}L_{e_{k}}+L_{e_{k}}L_{e_{j}}=-2\delta_{jk}\mathrm{id}$ and commutators $[L_{e_{j}},L_{e_{k}}]=2\epsilon_{jkl}L_{e_{l}}$, the internal group is compact and one-sided, the exponential stays inside the family, $e^{L_{\tilde A}}=L_{e^{\tilde A}}$, and the phase is **visible** here, $L_{\omega \tilde A}=\omega L_{\tilde A}$, in exact contrast with the phase-blind two-sided sandwich. The Dirac operator is a sum of one-sided operators, $D=\sum_{\mu}L_{e_{\mu}}\partial_{\mu}$, so the dynamics is one-sided and the two-sided operators are reserved for the states and the frames. The double centraliser theorem makes the right multiplications the commutant of the Clifford action and the scalars the bicommutant, so the spinor module is irreducible up to the shadow algebra and the internal space has no coarse-grained invariant. The isometries of the spinor form are $U(2)$ and the Lorentz action is not among them: it is the similarity of the interval, and $U(2)$ is contained in it exactly on the compact part. The pair of articles separates in this way what the physics uses one-sidedly from what it uses two-sidedly, and shows that the doubling of the parameter in the sandwich is exactly what erases the phase and merges the two sectors.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | The biquaternion algebra; basis $e_{0},e_{1},e_{2},e_{3}$ |
| ${}^{*}$ | Hermitian conjugation; $Q_{0}^{*}e_{0}-Q_{1}^{*}e_{1}-Q_{2}^{*}e_{2}-Q_{3}^{*}e_{3}$ |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Informational sector and material sector |
| $(\tilde T,\tilde V)=\mathrm{Sc}(\tilde T^{*}\tilde V)$ | The positive definite spinor form |
| $L_{\tilde A}(\tilde V)=\tilde A\tilde V$ | Left multiplication; the Clifford action on the spinor variable |
| $R_{\tilde B}(\tilde V)=\tilde V\tilde B$ | Right multiplication; the shadow algebra, the commutant |
| $L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B}$, $L_{\tilde A}R_{\tilde B}=R_{\tilde B}L_{\tilde A}$ | Composition law and commutation |
| $(L_{\tilde A})^{*}=L_{\tilde A^{*}}$ | The adjoint; the module axiom of the spinor form |
| $L_{e_{k}}$, $e_{k}\in\mathbb{M}_-$ | Skew-adjoint generators, $L_{e_{k}}^{2}=-\mathrm{id}$, $[L_{e_{j}},L_{e_{k}}]=2\epsilon_{jkl}L_{e_{l}}$ |
| $L_{e_{0}}=\mathrm{id}$, $e_{0}\in\mathbb{M}_+$ | The self-adjoint identity generator |
| $U=U(2)$ | The slice: unitary and isometric one-sided operators |
| $e^{L_{\tilde A}}=L_{e^{\tilde A}}$ | The exponential stays one-sided; the internal group |
| $D=\sum_{\mu}L_{e_{\mu}}\partial_{\mu}$ | The Dirac operator as a one-sided operator |
| $\{S:SL_{\tilde A}=L_{\tilde A}S\}=R(\mathbb{B})$ | The commutant of the Clifford action |

## Further Reading

- *One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/one-sided-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), the mathematical companion, for the proofs of the composition laws, the adjoint theorem, the type criteria and the double centraliser.
- *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_physics/two-sided-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), the companion of this article on the other side.
- *Biquaternion Spin Geometry* (`articles_physics/biquaternion-spin-geometry.md`), for the Clifford structure, the spinor module and the Dirac operator.
- *The Clifford Structure of the Biquaternion Algebra* (`articles_physics/biquaternion-clifford-structure.md`), for the algebra as a Clifford algebra and the relations of the generators.
- *The Spinor Module in Biquaternionic Form and Its Lorentz Action* (`articles_physics/the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.md`), for the module structure, the Lorentz action and the adjoint conventions.
- *The Dirac Equation in Biquaternionic Form* (`articles_physics/the-dirac-equation-in-biquaternionic-form.md`), for the dynamics written with the one-sided action.
- *Biquaternion Rotations and Lorentz Transformations* (`articles_physics/biquaternion-rotations-and-lorentz-transformations.md`), for the Lorentz action and the unit-norm slice.
- *Biquaternion Versors and the Orthogonal Group* (`articles_physics/biquaternion-versors-and-the-orthogonal-group.md`), for $U(2)$ as the automorphisms against $SL(2,\mathbb{C})$ as the similarities.
- *The Biquaternion Unit Group as a Topological Group* (`articles_physics/the-biquaternion-unit-group-as-a-topological-group.md`), for the topology of $U(2)$ and of the group of units.
- *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/two-sided-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the theorem that no nonzero two-sided operator is skew, which is why the generators are one-sided.
- *One-Sided Operators on a Hilbert Algebra with Hermitian Adjoint* (`articles_maths/one-sided-operators-on-a-hilbert-algebra-with-hermitian-adjoint.md`), for the general one-sided theory and the double centraliser.
