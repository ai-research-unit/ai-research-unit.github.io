# __The Unit Group, the Cone and the Orders__

## Introduction

The multiplication of the biquaternion algebra is defined on the whole algebra, but it is a group operation only on the invertible elements. Those elements form the **group of units** $\mathbb{B}^{\times}$, the **$N$-regular set**; their complement is the **$N$-degenerate set**, the **zero-divisor cone** $\mathcal{N}$. The pair is the algebraic form of a distinction physics uses everywhere: the operations that can be undone and the operations that cannot. The cone is also the set on which a multiplication loses rank, and the orders are the discrete subsets of the real slice on which the group of units becomes finite.

The article reads three objects and their topology: the group, its boundary and the orders. Its thesis is that invertibility is the algebraic form of reversibility, that the cone is the wall at which a multiplication stops being reversible, and that the orders are the discrete skeletons on which the continuous group is replaced by a finite one. It proves nothing; the theorems are in the mathematics articles of the source table.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The invertibility criterion, the partition of the algebra and the inverse formula | [N-Regularity and N-Degeneracy in the Biquaternion Algebra, §The Group of Units](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html) |
| The group of units, the determinant sequence, the centre and the matrix model | [The Biquaternion Unit Group as a Topological Group](../articles_maths/the-biquaternion-unit-group-as-a-topological-group.html) |
| The compact real form, the polar retraction, the homotopy groups and the universal cover | [The Unitary Group of the Biquaternion Algebra](../articles_maths/the-unitary-group-of-the-biquaternion-algebra.html) |
| The zero-divisor cone: closedness, dimension, smoothness, contractibility and link | [The Topology of the Zero-Divisor Cone](../articles_maths/the-topology-of-the-zero-divisor-cone.html) |
| The Lipschitz and Hurwitz orders, their unit groups, the complex order and the McKay correspondence | [Quaternion Orders and Finite Groups of Units](../articles_maths/quaternion-orders-and-finite-groups-of-units.html) |
| The norm on the remarkable subspaces and the distribution of the units | [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html) |
| The parity-matched lattice and the kernel of the exponential | [Biquaternion Elementary Functions](../articles_maths/biquaternion-elementary-functions.html) |

## The Partition and the Wall

### The Criterion

The norm that decides invertibility is the general quaternionic bilinear algebraic norm
$$
\langle\tilde Q\rangle_{\natural}=\sum_{\mu\in\{t,x,y,z\}}Q_\mu^{2},
$$
An element is a unit exactly when $\langle\tilde Q\rangle_{\natural}\neq0$, and its inverse is then
$$
\tilde Q^{-1}=\frac{\tilde Q^{\natural}}{\langle\tilde Q\rangle_{\natural}} .
$$
The algebra is the disjoint union
$$
\boxed{\;\mathbb{B}=\mathbb{B}^{\times}\uplus\mathcal{N},
\qquad
\mathbb{B}^{\times}=\{\tilde Q:\langle\tilde Q\rangle_{\natural}\neq0\},
\qquad
\mathcal{N}=\{\tilde Q:\langle\tilde Q\rangle_{\natural}=0\}\;},
$$
and the zero-divisor set is the punctured cone $\mathcal{N}\setminus\{0\}$. The three classes are the units, the nonzero points of the cone and the origin.

| condition on $\langle\tilde Q\rangle_{\natural}$ | condition on $\tilde Q$ | class |
| --- | --- | --- |
| $\neq0$ | automatically $\neq0$ | $N$-regular; a unit, an element of $\mathbb{B}^{\times}$ |
| $=0$ | $\tilde Q=0$ | $N$-degenerate; the origin, neither a unit nor a zero divisor |
| $=0$ | $\tilde Q\neq0$ | $N$-degenerate; a zero divisor, a point of $\mathcal{N}\setminus\{0\}$ |

### The Reversible Operation

**The unit is a reversible operation.** Multiplication by a unit is a bijection of the algebra, and its inverse is multiplication by the inverse. The norm is the scale of the operation; the norm-one slice $\mathbb{B}^{\times}_{1}=\{\langle\tilde Q\rangle_{\natural}=1\}$ is its shape. A general unit is a complex scale times a norm-one element, the factorisation being two-to-one on the central line. Read on a map, a unit is a process with no loss: every output has exactly one input, and the map can be run backwards.

**The zero divisor is an operation that forgets.** A nonzero $\tilde Q$ with $\langle\tilde Q\rangle_{\natural}=0$ has a nonzero annihilator: there is a nonzero $\tilde Q_2$ with $\tilde Q\tilde Q_2=0$ or $\tilde Q_2\tilde Q=0$. In the matrix model its image has rank one, so it kills a direction and cannot be inverted. The cone is therefore the **wall of reversibility**: on one side the multiplication is a bijection, on the other it has a kernel.

**The apex is no operation.** The origin is the only element that is neither a unit nor a zero divisor. It is the zero map, which is not a process: it has no inverse, and it is excluded from the zero-divisor set by the convention that both factors of a zero product are nonzero. The apex is the one point of the wall that is not a wall.

| object | algebraic condition | operation | interpretation |
| --- | --- | --- | --- |
| a unit | $\langle\tilde Q\rangle_{\natural}\neq0$ | a bijection | reversible |
| a zero divisor | $\langle\tilde Q\rangle_{\natural}=0$, $\tilde Q\neq0$ | rank one | forgets a direction |
| the origin | $\tilde Q=0$ | the zero map | no operation |

**The boundary of the interpretation.** A zero divisor is not "irreversible in time"; it is non-invertible as a linear map. The algebra has no arrow and no dynamics, and the physical arrow requires a process and a law. The interpretation identifies the algebraic status of the map, not a thermodynamic direction.

### The Wall of the State Space

**The same cone bounds the pure states.** The zero-divisor cone has a second physical interpretation on the informational sector $\mathbb{M}_{+}$. There the trace-one slice of the positive cone is the Bloch ball, its boundary is the set of pure states, and every pure state is a zero divisor: the pure-state idempotents satisfy $\langle\tilde\Pi\rangle_{\natural}=0$ on the Bloch sphere. The cone is thus the wall of reversibility on $\mathbb{M}_{-}$, and on $\mathbb{M}_{+}$ it meets the positive cone in the cone over the pure states; its intersection with the trace-one slice is the Bloch sphere.

**The boundary of the interpretation.** The two interpretations are of one set and not of one physical object. On $\mathbb{M}_{-}$ the cone is the light cone; on $\mathbb{M}_{+}$ its trace-one slice is the boundary of the state space. The identification requires the cut by the sector, and the algebra alone does not say which interpretation applies.

### The Pairings and the Wall

The partition into units and cone is the domain of the **word**, not of every polar description. The four-factor word exists exactly when $\langle\tilde Q\rangle_{\natural}\neq0$, so its domain is the group of units. The three pairings have smaller construction domains, and none of them is the wall itself:

| pairing | construction needs | witness of failure |
| --- | --- | --- |
| quaternion | $\langle\tilde Q\rangle_{\natural}\neq0$ and $\tilde q_r\neq0$ | $i\vec e_x+i\vec e_y$: a unit with $\tilde q_r=0$ |
| Hamilton | $\langle\tilde Q\rangle_{\natural}\neq0$ and $\langle\vec Q,\vec Q\rangle_{\natural}\neq0$ | $e_t+\vec e_x+i\vec e_y$: a unit with a null vector part |
| Cartan | $\langle\tilde Q\rangle_{\natural}\neq0$; generalized: every element | $e_t+i\vec e_x$: a zero divisor |

The Cartan construction is the widest, and the generalized Cartan form extends it to the cone with a positive factor and a partial isometry. Every element is $\tilde H_{\mathrm{pos}}\tilde U_{\mathrm{p}}$ with $\tilde H_{\mathrm{pos}}\ge0$ and $\tilde U_{\mathrm{p}}\tilde U_{\mathrm{p}}^{*}\tilde U_{\mathrm{p}}=\tilde U_{\mathrm{p}}$. The word fails on the cone because the modulus vanishes; the physical image is a lightlike four-vector, which has no rest frame. The amplitude–phase split does not fail there.

**The boundary of the interpretation.** A unit is not "a reversible process" and a zero divisor is not "an irreversible process" without a dynamics; the partition is algebraic. What the domains add is the converse caution: invertibility is necessary for the word and for all three classical pairings, and it is not sufficient for the two smaller ones. A statement about units need not transport to a pairing.

### Divisibility

The partition has a divisibility form. In the multiplicative monoid, $a$ divides $b$ when $b=ac$ for some $c$. A unit divides every element, because $b=u\,(u^{-1}b)$; conversely an element that divides every element divides $e_t$, hence is a unit. A nonzero element is a zero divisor exactly when it divides $0$ with a nonzero cofactor. The partition therefore reads
$$
\text{units}=\{\text{divisors of every element}\},
\qquad
\mathcal{N}\setminus\{0\}=\{\text{divisors of }0\},
$$
and the apex is the element that divides only $0$ and is divided by everything. **The order structure is the divisibility preorder.** The units are its top equivalence class; the nonzero cone is the set of divisors of $0$ with a nonzero cofactor, and it splits into many divisibility classes.

**The boundary of the interpretation.** Divisibility is a preorder, not a total order, and it carries no cost. A physical resource theory would need a monotone and a composition law; the algebra supplies the preorder only.

### The Monoid of Processes

The partition is a partition of elements. Read on the maps they generate, it is a partition of processes. Left multiplication by $\tilde Q$ is a $\mathbb{C}$-linear map $L_{\tilde Q}$ of the algebra, and the assignment is injective. The maps compose by

$$
L_{\tilde A}\circ L_{\tilde B}=L_{\tilde A\tilde B},
$$

so the left multiplications form a **monoid** under composition, with identity $L_{e_t}$. The monoid is the element monoid seen through the regular representation, and it carries the same partition: its units are exactly the off-cone elements, and its non-units are the zero divisors together with zero.

A unit is a **reversible process**: the map is a bijection, and it can be run backwards. A zero divisor is a **process that forgets**: its map has a nonzero kernel, the annihilator, and the kernel is the direction it loses. The cone is the boundary between the two.

**The shape of a resource theory.** Read as a resource theory, the split is between free and costly operations: the units are the free, reversible operations, and the non-units are the operations that consume a resource. The states carry the algebraic invariant, the norm; the entropy functional is the informational reading, and the monoid is the setting for Landauer-type accounting. The reading is the shape and not the theory. The algebra supplies a preorder and a composition, not a complete set of monotones, and no resource theory in the strict sense is constructed. The physical content is in *Landauer's Principle and the Material–Informational Exchange in Biquaternionic Form* and *Coarse-Graining and the Biquaternion Entropy Functional*.

**The cone as a horizon.** The cone has three readings at once: its cut by the material sector is the light cone, its cut by the informational sector is the boundary of the state space, and in the whole algebra it is the locus of the non-invertible acting maps. Read as one object, it is where a process loses information: a map on the cone has a kernel, and what enters the kernel does not leave. The horizon reading is the identification of the three loci, and it is an interpretation. The algebra supplies the common set, not the thermodynamics; the area law, the temperature and the second law belong to *Black Hole Thermodynamics in Biquaternionic Form* and to the KMS articles. The cone is a horizon in the sense of a boundary at which the map stops being reversible, not in the sense of a metric horizon with a temperature.

**Which composition is physical.** The monoid composes by $L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B}$, so a sequence of two processes is a product. The product is associative, and associativity is order-blind: it says that the bracketing of three factors does not matter, not that the order of the two factors does. The two orders are the two products $\tilde A\tilde B$ and $\tilde B\tilde A$, and the algebra supplies both; their commutator $[\tilde A,\tilde B]$, the antisymmetric half of the product, measures the order sensitivity. **Which of the two orders is the physical composition is open.** The algebra supplies both and selects neither.

**The boundary.** The open question is not a defect of the algebra. It is the statement that a composition law is not a dynamics: a physical theory must say which product is the composition of its processes, and that choice is an input.

## The Shape of the Reversible Region

### The Group and Its Matrix Model

The group $\mathbb{B}^{\times}$ is open and dense in the algebra, connected, of real dimension eight. The cone is closed, of empty interior and of real codimension two, and the group and the cone share the boundary:
$$
\partial\mathbb{B}^{\times}=\partial\mathcal{N}=\mathcal{N}.
$$
Under the matrix model $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ the group is $GL_2(\mathbb{C})$ and the norm is the determinant, so the determinant is a surjective homomorphism
$$
1\longrightarrow \mathbb{B}^{\times}_{1}\cong SL_2(\mathbb{C})\longrightarrow \mathbb{B}^{\times}\cong GL_2(\mathbb{C})\xrightarrow{\ \det\ }\mathbb{C}^{\times}\longrightarrow 1,
$$
with kernel the norm-one group. The centre is $\mathbb{C}^{\times}e_t$, of real dimension two, and the determinant restricted to it is the squaring map.

### The Retraction to the Compact Form

The polar decomposition gives strong deformation retractions
$$
\mathbb{B}^{\times}\longrightarrow \mathrm{U}(\mathbb{B})\cong \mathrm{U}(2),
\qquad
\mathbb{B}^{\times}_{1}\longrightarrow S^{3},
$$
where $\mathrm{U}(\mathbb{B})=\{\tilde Q:\tilde Q^{*}\tilde Q=e_t\}$ and $S^{3}=Sp(1)$ is the unit quaternion sphere. Consequently
$$
\boxed{\;\mathbb{B}^{\times}\simeq \mathrm{U}(\mathbb{B})\simeq S^{1}\times S^{3},
\qquad
\mathbb{B}^{\times}_{1}\simeq S^{3}\;},
$$
and the homotopy groups are
$$
\pi_1(\mathbb{B}^{\times})\cong\mathbb{Z},
\qquad
\pi_2(\mathbb{B}^{\times})=0,
\qquad
\pi_3(\mathbb{B}^{\times})\cong\mathbb{Z},
$$
with $(\mathbb{B}^{\times})^{\mathrm{cov}}\simeq\mathbb{R}\times S^{3}$.

**The kernel is not discrete.** The exponential is onto the group. Its kernel meets the diagonal part in the parity-matched lattice $L=\pi i m\,e_t+\pi n\,\vec U$ with $m\equiv n\pmod2$ (*Biquaternion Elementary Functions*), but the full kernel also contains continuous families of logarithms. It is therefore not a discrete set and not a covering group, and its lattice part is not the fundamental group. The loops and the third homotopy group are those of the compact core, by the polar retraction of the preceding paragraph; the kernel is the fibre of the exponential over the identity, a gauge ambiguity of the logarithm rather than a set of components of the group. *The Exponential, the Logarithm and the Generator* reads it as such.

**The topology is carried by the compact form.** Every unit can be deformed to a $*$-unitary one, and every norm-one unit to a unit quaternion. The qualitative features of the group — its connectedness, its loops, its third homotopy — are therefore the features of $\mathrm{U}(2)$ and $S^{3}$; the non-compact directions are a contractible thickening. Interpreted physically, the reversible region has the topology of its compact core, and the boosts and dilations add no new loops or components.

**The boundary of the interpretation.** The retraction is a deformation, not a physical relaxation. The path supplied by the polar decomposition is a mathematical homotopy and is not a sequence of physical operations.

### The Norm-One Slice

**The norm-one slice is the shape of a frame.** The norm-one group $\mathbb{B}^{\times}_{1}$ has real dimension six, and its quotient by the central sign is
$$
\mathbb{B}^{\times}_{1}/\{\pm e_t\}\cong SO^{+}(1,3),
$$
the proper orthochronous Lorentz group. A norm-one unit is therefore a **spin frame**: a frame of the material sector together with the sign that the spinor carries. The centre supplies the complex scale and the phase, and the norm-one slice supplies the shape.

**The boundary of the interpretation.** The frame is an algebraic frame, not a laboratory. The identification of $\mathbb{B}^{\times}_{1}$ with the spin frame bundle is the statement that the group acts simply transitively on frames up to sign; it does not fix a reference frame, and it does not supply a metric beyond the norm.

### The Two Loops

**The fundamental group is the winding around the wall.** The complement of the null cone, a complex hypersurface of real codimension two in $\mathbb{C}^{4}$, has fundamental group $\mathbb{Z}$, and the generator is a loop that links the cone. In the matrix picture the generator is a loop along which the determinant winds once. The central phase circle $Ae_t$ with $|A|=1$ has determinant $A^{2}$ and is therefore twice the generator, not the generator itself. Interpreted physically, the one topological charge of the reversible region is the winding around the wall of non-invertibility; the overall phase is a double winding of it.

**The universal cover unwraps the phase.** The universal cover, which is homotopy equivalent to $\mathbb{R}\times S^{3}$, replaces the loop direction by a real line. The phase circle is the image of that line under the universal covering. A clock read on the cover has no intrinsic period, while a clock read on the group is periodic. The third homotopy group, $\pi_3(\mathbb{B}^{\times})\cong\mathbb{Z}$, is generated by the unit quaternions and is the winding of the compact factor.

**The fibre of the logarithm is a lattice coset.** The periodicity of the group is also the ambiguity of its logarithm. For a unit with $B\neq0$ the logarithms differ by the parity-matched lattice $\pi i m\,e_t+\pi n\,\vec U$ inside the diagonal part, with $\vec U=\vec Q/B$ the pure unit element (*Biquaternion Elementary Functions*, §*The Eigenvalue Formula*), and that lattice is not the fundamental group. The group $\pi_1$ is generated by a loop that links the cone, while the kernel is the fibre of the exponential over the identity. A loop is a map out of $S^1$. A kernel element is a period of the exponential. The two share the compact phase and answer different questions.

**The boundary of the interpretation.** The winding is a property of the group, not a quantisation of a physical charge. The algebra does not say that the phase is compact in nature, nor that the winding is observed. It supplies the homotopy class, and a gauge theory or a field configuration would have to supply the rest.

## The Cone and Its Link

### The Contractible Wall

The cone is the zero set of one polynomial, smooth away from its apex, and contractible:
$$
\mathcal{N}=\{\tilde Q:\langle\tilde Q\rangle_{\natural}=0\},
\qquad
\mathcal{N}\text{ is contractible}.
$$
Its link is
$$
\boxed{\;L=\mathcal{N}\cap S^{7}_{E}\;},
$$
the intersection with the Euclidean unit sphere. The link is a closed connected real five-manifold, an $S^{1}$-bundle over the projectivised cone $\mathbb{P}(\mathcal{N})\cong S^{2}\times S^{2}$. The bundle is nontrivial — its first Chern class is nonzero, the sum of the two hyperplane classes up to sign — but $L\cong S^{2}\times S^{3}$, with
$$
\pi_1(L)=0,
\qquad
\pi_2(L)\cong\mathbb{Z}.
$$
It is not $S^{5}$, so the apex is a genuine singularity of the cone.

**The wall has no topology of its own.** The cone is contractible, so its only topological invariant is the link. Interpreted physically, the radial extent of the light cone carries no topology; the directions carry it. The cone is a wall without holes, and the holes live in its link.

**The boundary of the interpretation.** The statement is about the full complex cone in the eight-dimensional real algebra. The light cone of the material sector is a real three-dimensional cone inside $\mathbb{M}_{-}$; it is also contractible, but its link is the ordinary $S^{2}$ of null directions, not the five-manifold $L$.

### The Link as Null Directions

The link is the space of complex null directions at fixed scale. A nonzero null element is a rank-one matrix, $\mathsf{M}_2(\tilde Q)=u v^{\mathsf T}$ with $u=(\alpha,\beta)$ and $v=(\gamma,\delta)$, the pair being determined up to $(u,v)\mapsto(\lambda u,\lambda^{-1}v)$. The link is therefore the quotient of $S^{3}\times S^{3}$ by the circle acting as $(u,v)\mapsto(\lambda u,\lambda^{-1}v)$, an $S^{1}$-bundle over $S^{2}\times S^{2}$: two projective spinors and a relative phase.

**The link is the space of complex null directions.** Interpreted physically, a complex null four-vector is a pair of chiral spinors together with a relative phase; the two $S^{2}$ factors are the two celestial spheres and the $S^{1}$ fibre is the little-group phase. On the real material sector the null four-vector is anti-Hermitian of rank one, the two spinors are conjugate, and the pair collapses to one projective spinor: the link becomes the $S^{2}$ of null directions, with the phase as the fibre of $S^{3}\to S^{2}$.

**The boundary of the interpretation.** The five-manifold $L$ is the complexified object. The physical null cone of $\mathbb{M}_{-}$ has the two-sphere link, and the two-sphere pair of $L$ is the complexification, not two physical directions.

### The Singular Apex

**The apex is not a direction.** The link of a manifold point is a sphere; the link of the apex is not, so the apex is not a manifold point. Interpreted physically, the zero four-vector is not a direction and not a state: the tip of the light cone is the one point with no celestial sphere. The singularity is topological; it is not a curvature singularity and it carries no metric.

## The Orders

### The Lattices

An **order** in the real quaternion algebra is a subring that is a free abelian group of rank four and whose $\mathbb{Q}$-span is the algebra. The **Lipschitz order** is
$$
\mathcal{L}=\mathbb{Z}e_t\oplus\mathbb{Z}\vec e_x\oplus\mathbb{Z}\vec e_y\oplus\mathbb{Z}\vec e_z,
$$
and the **Hurwitz order** is
$$
\mathcal{L}_{\mathrm{H}}=\mathcal{L}\oplus\mathbb{Z}\omega,
\qquad
\omega=\tfrac12(e_t+\vec e_x+\vec e_y+\vec e_z).
$$
The Hurwitz order contains the Lipschitz order with index two and is maximal; the Lipschitz order is not maximal.

### The Finite Unit Groups

The unit groups are
$$
\boxed{\;\mathcal{L}^{\times}\cong Q_8,
\qquad
(\mathcal{L}_{\mathrm{H}})^{\times}\cong 2T\;},
$$
the quaternion group of order eight and the binary tetrahedral group of order twenty-four. The unit-group index is three, although the lattice index is two. The finite subgroups of the unit sphere $Sp(1)=S^{3}$ are the cyclic groups, the binary dihedral groups and the binary polyhedral groups $2T$, $2O$, $2I$ of orders $24$, $48$ and $120$. The twenty-four Hurwitz units are the vertices of the regular $24$-cell in $\mathbb{H}_{\mathbb{B}}\cong\mathbb{R}^{4}$; its symmetry group is the Weyl group $F_4$ of order $1152$, containing $B_4$ of order $384$, and both are strictly larger than the unit group. The twenty-four units give twelve distinct rotations $\tilde Q_1\mapsto v\tilde Q_1v^{*}$ of the real slice, with $2T/\{\pm e_t\}\cong A_4$. The five families of finite subgroups are the five simply laced Dynkin types, the McKay correspondence.

**The order is the discrete skeleton.** An order is a lattice subring of the real sector: a discrete set of sites closed under addition and multiplication, the algebraic form of a lattice. Its unit group is the set of lattice operations that are reversible inside the lattice. The quaternion units are the rotations by $\pi$ of the lattice, and the binary groups are their lifts; read against the continuous groups, the orders are what survives when the frame is restricted to integral elements. Interpreted physically, the order is the discrete skeleton of the material sector, and the finite unit group is its discrete symmetry. Read on a lattice, the orders are the arithmetic counterpart of a lattice gauge theory and of a quantum simulation of the framework; the real slice is the Euclidean lattice and its imaginary translate the thermal direction, so the arithmetic of the orders is also the arithmetic of the thermal circle. The algebra supplies the arithmetic, not the gauge field or the temperature.

**The finite unit group has no phase.** A finite subgroup of $S^{3}$ is discrete and lies in the real slice; it carries no continuous phase. The phase of the framework comes from the centre $\mathbb{C}^{\times}e_t$, not from the units. Interpreted physically, a finite symmetry has no clock, and a continuous phase is a central, not a discrete, object.

**The Hurwitz units are the tetrahedral half of the Clifford lift.** The binary octahedral group $2O$ of order $48$ is the lift to the unit sphere of the one-qubit Clifford group, whose projective image is the octahedral rotation group of order $24$; the Hurwitz group $2T$ of order $24$ is its index-two tetrahedral half. Interpreted physically, the $24$-cell is not the Clifford group: it is the even half of it, and the identification of the Hurwitz units with the single-qubit Clifford group is wrong by the index two.

**The figure is larger than the group.** The $24$-cell has $1152$ symmetries, while the unit group has $24$ elements; its conjugation action on the real slice gives twelve rotations. Interpreted physically, the symmetry of the lattice is not the unit group; the figure can have more symmetries than the operations the units supply. The distinction is the one between a crystal's point group and the rotations of its lattice.

**The complex order sees the light cone.** The integral biquaternions $\mathbb{Z}[i]\otimes_{\mathbb{Z}}\mathcal{L}_{\mathrm{H}}$ have an infinite unit group. A pure null element with Gaussian-integer coefficients, for instance
$$
P=\vec e_x+i\vec e_y,
\qquad
P^{2}=0,
$$
generates the unipotent family
$$
(e_t+P)^{n}=e_t+nP,
\qquad
\langle e_t+P\rangle_{\natural}=1,
\qquad
n\in\mathbb{Z}.
$$
Interpreted physically, the real orders have finite unit groups because the real sector is definite and has no null direction; the complex order contains the null direction and its unit group is infinite. The finite unit groups are the symmetries of the massive, non-null sector; the infinite family is the algebraic trace of the light cone.

**The McKay classification is the ADE classification.** Through the McKay correspondence the finite subgroups of $S^{3}$ are the simply laced Dynkin types $A^{(1)}$, $D^{(1)}$, $E_6^{(1)}$, $E_7^{(1)}$, $E_8^{(1)}$, and the Kleinian singularities $\mathbb{C}^{2}/\Gamma$ are their orbifolds. Interpreted physically, the discrete symmetries of the framework are classified by the simply laced affine Dynkin diagrams rather than by a list of groups. The interpretation is a classification; it exhibits no orbifold of the algebra and no action of the finite groups on the fields.

**The boundary of the order interpretations.** The orders are arithmetic. They supply no lattice spacing, no dynamics and no spectrum; a physical lattice would require a scale and an action, and the algebra supplies neither. The identification of the infinite unit family with a translation is an algebraic analogy: $e_t+kP$ is a unit of the complex order and is not an element of the material sector, so it is not a spacetime translation.

## Limits

The topology of the unit group is not the dynamics of a physical system. The group is open, connected and homotopy equivalent to $S^{1}\times S^{3}$; the cone is closed, contractible and of codimension two; the orders are discrete subrings of the real slice. Each statement is a statement about the algebra, and each physical interpretation requires a sector, a scale and a law.

The group and the cone are one partition read twice. The group is the reversible region and the cone is its wall; on the informational sector the cone meets the positive cone in the cone over the pure states. The two interpretations are not unified by the algebra, and the article does not claim that they are. The cone is a light cone only after the material sector is cut out; it is a state boundary only after the trace-one slice is taken. Read on the acting maps, the same partition is a monoid of processes: the units are the reversible maps, the zero divisors are the maps with a kernel, and the cone is where a process loses information. Which of the product, its reverse and the bracket is the physical composition is open.

The orders are arithmetic, not dynamics. The finite unit groups are discrete symmetries, but the algebra does not say which of them a physical configuration realises, and the lattice spacing is external. The infinite unit group of the integral biquaternions is the algebraic trace of the null direction, not a derivation of a translation.

## Summary

The algebra is the disjoint union of its group of units $\mathbb{B}^{\times}=\{\langle\tilde Q\rangle_{\natural}\neq0\}$ and its zero-divisor cone $\mathcal{N}=\{\langle\tilde Q\rangle_{\natural}=0\}$; the zero-divisor set is the punctured cone. A unit is a reversible operation, a zero divisor is a rank-one operation that forgets a direction, and the origin is the one element that is neither. On the informational sector the cone meets the positive cone in the cone over the pure states; its trace-one slice is the Bloch sphere. In the divisibility preorder, the units are the divisors of every element and the nonzero cone is the set of divisors of zero.

The group is open, dense, connected and of real dimension eight, with $\mathbb{B}^{\times}\cong GL_2(\mathbb{C})$ and $\mathbb{B}^{\times}_{1}\cong SL_2(\mathbb{C})$; the polar decomposition retracts it onto $\mathrm{U}(2)$, and $\mathbb{B}^{\times}\simeq S^{1}\times S^{3}$, with $\pi_1\cong\mathbb{Z}$, $\pi_2=0$, $\pi_3\cong\mathbb{Z}$ and universal cover homotopy equivalent to $\mathbb{R}\times S^{3}$. The norm-one slice modulo the central sign is the frame space $SO^{+}(1,3)$. The cone is contractible, smooth off its apex, and its link is an $S^{1}$-bundle over $S^{2}\times S^{2}$ with $\pi_1=0$ and $\pi_2\cong\mathbb{Z}$; the apex is a genuine singularity.

The orders are the Lipschitz and Hurwitz lattices, with unit groups $Q_8$ and $2T$, the finite subgroups of $S^{3}$, the $24$-cell, the McKay correspondence and the infinite unit group of the integral biquaternions. They are the discrete skeleton of the real sector. The algebra supplies the structures; the physical interpretations are reversible operations, a wall of reversibility, a state boundary, a monoid of processes, a frame space and a discrete symmetry, each with its boundary.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}^{\times}=\{\langle\tilde Q\rangle_{\natural}\neq0\}$ | the group of units; the complement of the cone |
| $\mathcal{N}=\{\langle\tilde Q\rangle_{\natural}=0\}$ | the zero-divisor cone; the wall of reversibility |
| $\langle\tilde Q\rangle_{\natural}$ | the general quaternionic algebraic norm; the invertibility criterion |
| $\mathbb{B}^{\times}_{1}=\{\langle\tilde Q\rangle_{\natural}=1\}$ | the norm-one group; the spin frame slice |
| $\mathrm{U}(\mathbb{B})=\{\tilde Q:\tilde Q^{*}\tilde Q=e_t\}$ | the $*$-unitary group; maximal compact subgroup, $\cong U(2)$ |
| $L=\mathcal{N}\cap S^{7}_{E}$ | the link of the cone; $L\cong S^{2}\times S^{3}$, an $S^{1}$-bundle over $S^{2}\times S^{2}$ |
| $\mathcal{L}$, $\mathcal{L}_{\mathrm{H}}$ | the Lipschitz and Hurwitz orders |
| $Q_8$, $2T$ | the unit groups of $\mathcal{L}$ and $\mathcal{L}_{\mathrm{H}}$ |
| $24$-cell | the regular polytope with the Hurwitz units as vertices |
| $B_4$, $F_4$ | the Weyl groups of orders $384$ and $1152$ |
| $P=\vec e_x+i\vec e_y$ | the integral null element, $P^{2}=0$ |
| $e_t+nP$ | the unipotent family of norm-one units of the complex order |

## Further Reading

- [N-Regularity and N-Degeneracy in the Biquaternion Algebra, §The Group of Units](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the criterion and the partition.
- [The Biquaternion Unit Group as a Topological Group](../articles_maths/the-biquaternion-unit-group-as-a-topological-group.html), for the determinant sequence and the matrix model.
- [The Unitary Group of the Biquaternion Algebra](../articles_maths/the-unitary-group-of-the-biquaternion-algebra.html), for the polar retraction and the homotopy groups.
- [The Topology of the Zero-Divisor Cone](../articles_maths/the-topology-of-the-zero-divisor-cone.html), for the link and the contractibility.
- [Biquaternion Elementary Functions](../articles_maths/biquaternion-elementary-functions.html), for the parity-matched lattice and the kernel of the exponential.
- [Quaternion Orders and Finite Groups of Units](../articles_maths/quaternion-orders-and-finite-groups-of-units.html), for the lattices, the finite unit groups and the complex order.
- [The Polar Decomposition and Its Three Pairings](the-polar-decomposition-and-its-three-pairings.html), §*The Domain*, for the three construction domains and the witnesses in one table.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A. K. Peters, 2003), for the Lipschitz and Hurwitz orders and the $24$-cell.
