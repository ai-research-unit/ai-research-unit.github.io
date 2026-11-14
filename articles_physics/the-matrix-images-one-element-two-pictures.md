# __The Matrix Images: One Element, Two Pictures__

## Introduction

**This entry reads the second section of the mathematical category: the matrix representations.** Four mathematics articles build them — the two families in a general frame, the axis-free form and the Peirce form in $M_4(\mathbb{C})$, and the compressed form in $M_2(\mathbb{C})$.

**A matrix image is a choice of picture, not a new object.** The element is one; the array depends on the frame and on the size. The entry states what each picture makes visible, what each one loses, and where the conversions between them are linear and where they are not.

**The one idea that governs the section is the doubling.** The $4\times4$ picture is the $2\times2$ picture written twice, and every quantity of the smaller picture changes at the larger size by a definite rule: additive quantities double, multiplicative ones square, the spectrum repeats, and the minimal polynomial does not change. A computation that does not say which size it is in produces factors of two and four that look like physics and are not.

## The Source Table

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| the left and the right families, their three composition laws, the switch between the sides, the frame-changing matrix, the $2\times2$ family and why it has no second side | [Families of Matrix Representations of the Biquaternion Algebra](../articles_maths/families-of-matrix-representations.html) |
| the axis-free basis, the two families, the product, the trace, the determinant, the four norms, the six subspaces in the image, the three splits | [$M_4(\mathbb{C})$ Axis-Free Representation](../articles_maths/m4c-axis-free-representation.html) |
| the root and the Peirce frame, the two families, the stitch, the switch to the axis-free display, the sixteen products, the comparison table, which roots give a Peirce frame | [$M_4(\mathbb{C})$ Pauli Representation](../articles_maths/m4c-pauli-representation.html) |
| the root and the two idempotents, the Peirce basis, the compression, the product, the trace, the determinant, the spectral projectors, the diagonalising matrix, the adjugate and the inverse, the four norms, the six subspaces | [$M_2(\mathbb{C})$ Pauli Representation](../articles_maths/m2c-pauli-representation.html) |

**The rows are the entry's own order.** The general frame comes first, then the regular size, then the compressed size, and the reading goes with them.

## The Results in Brief

### The Two Families

**Fix a frame and read the columns.** For a frame $\mathcal{F}=(f_1,f_2,f_3,f_4)$ of $\mathbb{B}$,

$$
L(\tilde Q)_{\mu\nu}=\bigl[\tilde Qf_\nu\bigr]_\mu,\qquad R(\tilde Q)_{\mu\nu}=\bigl[f_\nu\tilde Q\bigr]_\mu .
$$

**Three laws hold, and they need no coordinates.**

$$
L(\tilde Q_2\tilde Q)=L(\tilde Q_2)L(\tilde Q),\qquad R(\tilde Q_2\tilde Q)=R(\tilde Q)R(\tilde Q_2),\qquad L(\tilde Q_2)R(\tilde Q)=R(\tilde Q)L(\tilde Q_2) .
$$

**The left family is the algebra and the right family is its opposite.** The second law carries the product backwards. Both images are faithful and four-complex-dimensional inside the sixteen of $M_4(\mathbb{C})$.

**The two families meet in the scalars and nowhere else.**

$$
L(\tilde Q)=R(\tilde Q)\iff\tilde Q\in\mathbb{C}e_t,\qquad \mathbb{B}_L\cap\mathbb{B}_R=\mathbb{C}\,\mathrm I_4 .
$$

Two four-dimensional spaces with a line in common span seven dimensions, not eight.

### The Invariants at the Two Sizes

$$
\operatorname{Tr}L(\tilde Q)=\operatorname{Tr}R(\tilde Q)=4Q_t,\qquad \det L(\tilde Q)=\det R(\tilde Q)=\langle\tilde Q\rangle_{\natural}^{2}=N^2 ,
$$

$$
\chi(\lambda)=\bigl((\lambda-Q_t)^2+B^2\bigr)^2,\qquad \operatorname{spec}=\{Q_t+iB,\ Q_t-iB\}\ \text{each twice} .
$$

**At size two the same data appear at half the size.**

$$
\operatorname{Tr}\mathsf M_2(\tilde Q)=2Q_t,\qquad \det\mathsf M_2(\tilde Q)=N,\qquad \operatorname{spec}=\{Q_t+iB,\ Q_t-iB\},\qquad \operatorname{rank}\in\{0,1,2\} .
$$

**At size four the rank is even.** It is twice the rank of the $2\times2$ image, hence $0$, $2$ or $4$, and never $1$ or $3$.

### The Doubling Rule

| quantity | size two | size four | rule |
| --- | --- | --- | --- |
| trace | $2Q_t$ | $4Q_t$ | double |
| determinant | $N$ | $N^2$ | square |
| characteristic polynomial | degree $2$ | its square | square |
| spectrum | $\lambda_\pm$ once each | each twice | repeat |
| rank | $r$ | $2r$ | double |
| minimal polynomial | degree $2$ | degree $2$ | unchanged |

**The last row is the exception.** The characteristic polynomial squares and the minimal polynomial does not, because the square of a minimal polynomial is not minimal.

### The Pauli Correspondence

| unit | matrix | Hermitian |
| --- | --- | --- |
| $e_t$ | $\mathrm I_2$ | yes |
| $\vec e_\eta$ | $-i\sigma_\eta$ | no |
| $i\vec e_\eta$ | $\sigma_\eta$ | yes |

$$
\boxed{\;\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i\bigl(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3\bigr)\;}
$$

**Hermitian conjugation becomes the conjugate transpose,** $\mathsf M_2(\tilde Q^{*})=\mathsf M_2(\tilde Q)^{\dagger}$, so the fixed space of ${}^{*}$ is carried onto the Hermitian matrices.

**There is no second side at size two.** The right action there is the ordinary matrix product $\mathsf A\mapsto\mathsf A\,\mathsf M_2(\tilde Q)$, which is not left multiplication by a matrix unless $\mathsf M_2(\tilde Q)$ is scalar. At size two the transpose is a conjugation and returns the conjugate element; the second side appears only when the element is read as acting on a carrier.

### The Peirce Frame

**A root of the unit fixes a frame.** For $\vec Z=\sum_ka_k\vec e_k$ with

$$
\vec Z^2=-\bigl(a_x^2+a_y^2+a_z^2\bigr)e_t=e_t ,
$$

the condition is $a_x^2+a_y^2+a_z^2=-1$, one complex equation in three unknowns: a family of real dimension four. The root gives the idempotent pair, and the pair gives a frame.

**In that frame the sixteen matrices are monomial, unitary, of determinant one, with entries in $\mathbb{Z}[i]$.** The display is a tensor product,

$$
L(\tilde Q)=\mathrm I_2\otimes\mathsf M_2(\tilde Q),\qquad R(\tilde Q)=\mathsf M_2(\tilde Q)^{\mathsf T}\otimes\mathrm I_2 ,
$$

the idempotents are the first and fourth frame vectors, and the stitch is a pure swap, $R=\mathsf P L^{\mathsf T}\mathsf P$.

**Only the six coordinate roots keep the sparsity.** The roots $\pm i\vec e_x,\pm i\vec e_y,\pm i\vec e_z$ give one frame up to cyclic relabelling and the exchange of the two idempotents. A root with two nonzero coordinates densifies every array.

**Every frame that contains two orthogonal idempotents summing to $e_t$ is a root frame.** Their difference is $\vec Z=2\tilde\Pi_+-e_t$, a vector of square $e_t$.

### The Six Subspaces in the Image

| subspace | condition on $L(\tilde Q)$ | $\operatorname{Tr}$ | $\det\mathsf M_2$ |
| --- | --- | --- | --- |
| $\mathbb{B}_{C}$ | $M=\lambda\mathrm I_4$ | $4Q_t$ | $Q_t^2$ |
| $\mathbb{B}_{V}$ | $\operatorname{Tr}M=0$ | $0$ | $B^2$ |
| $\mathbb{B}_{H}$ | $M=\overline M$ | $4q_t$ | $\sum q_\mu^2$ |
| $\mathbb{B}_{iH}$ | $M=-\overline M$ | $4iq'_t$ | $-\sum(q'_\mu)^2$ |
| $\mathbb{B}_{\Psi}$ | $M=M^{\dagger}$ | $4q_t$ | $q_t^2-\lvert\vec q'\rvert^2$ |
| $\mathbb{B}_{\Phi}$ | $M=-M^{\dagger}$ | $4iq'_t$ | $-(q'_t)^2+\lvert\vec q\rvert^2$ |

**The four conjugations become the four matrix involutions.** Complex conjugation is the entrywise bar, quaternion conjugation is the transpose in the axis-free basis, Hermitian conjugation is the dagger, and the anti-Hermitian one is minus the dagger.

**The conditions are necessary and not sufficient in the ambient $M_4(\mathbb{C})$.** The real matrices, the Hermitian matrices and the anti-Hermitian matrices each form a real space of dimension sixteen; the image is a four-dimensional subspace of each. A condition stated on the image is a statement about the image and not about matrix theory.

**Two of the six are closed under the product and the others are not.** The centre and the quaternion subspace are subalgebras; the vector subspace is a Lie subalgebra under the commutator; the anti-quaternion and the two sector images are neither.

### The Spectral Projectors

**A general element carries its own root and its own idempotent pair.** With $B^2\neq0$ and $B$ a square root, $\vec Z=-i\vec Q/B$ is a root, and the two projectors $\rho_\pm$ are the spectral projectors of the element. A diagonalising matrix is

$$
\mathsf C_Q=\begin{pmatrix}B-Q_z&Q_x-iQ_y\\-Q_x-iQ_y&B-Q_z\end{pmatrix},\qquad \det\mathsf C_Q=2B(B-Q_z) ,
$$

with a second chart for $B=Q_z$ of determinant $-2B(B+Q_z)$. The two determinants cannot both vanish, so the pair of charts covers every element with $B\neq0$.

**The freedom left is the two diagonal rescalings.** $\mathsf C_Q\mapsto\lambda\mathsf C_QD$ with $D$ invertible diagonal, and $\lambda$ cancels from the similarity.

### The Adjugate and the Inverse

$$
\mathsf M^{-1}=\frac{\mathsf M^{\mathsf T}}{N},\qquad \operatorname{adj}\mathsf M=N\mathsf M^{\mathsf T},\qquad \operatorname{adj}\bigl(\operatorname{adj}\mathsf M\bigr)=N^{4}\mathsf M .
$$

**At size four the adjugate is not an involution and not linear.** At size two it is both. The inverse formula is the $2\times2$ one with the determinant replaced by $N$ and the transpose standing for the conjugate.

## The Interpretations

### I.2.a — One Element, Two Pictures, and the Doubling Is Not a Second Particle

**Read:** the $4\times4$ regular image is the $2\times2$ image written twice, and the two copies are the two dimensions of the module.

**The tensor display makes the doubling visible as a block structure.** $L=\mathrm I_2\otimes\mathsf M_2$ and $R=\mathsf M_2^{\mathsf T}\otimes\mathrm I_2$: the first factor of each tensor is the copy index, the second is the element. The matrix is a two-by-two array of blocks, each block a copy of $\mathsf M_2(\tilde Q)$.

**The consequences are bookkeeping and they are not optional.** The trace doubles because there are two blocks. The determinant squares because it is multiplicative over the blocks. The spectrum repeats because each block has the same two eigenvalues. The rank doubles because both blocks have the same rank. None of these is a physical multiplicity.

**The boundary.** The copy index is not a chirality, not a generation and not a particle label. The two copies are the two columns of the module, and the two minimal left ideals they correspond to are isomorphic, so nothing in the algebra distinguishes them. A reading that treats the two copies as two species is reading the display and not the algebra.

### I.2.b — The Qubit Is the $2\times2$ Image, and It Has One Side

**Read:** the compressed image is the state space of a two-level system, and the regular image is the same object with its copy index exposed.

**At size two the picture is complete and it has one side.** The carrier is $M_2(\mathbb{C})$ itself: the element acts on a two-component column, and the column is a spinor. The right action there is an ordinary matrix product, and it is not the left multiplication by a second matrix. So the element yields one matrix, and the "before" and "after" pictures collapse into one.

**The transposition and the conjugation are the same operation at this size.** The conjugating matrix is $\varepsilon=i\sigma_2$, with $\varepsilon^{\mathsf T}=-\varepsilon$ and $\varepsilon^{2}=-\mathrm I_2$, and

$$
\mathsf M_2(\tilde Q^{\natural})=\varepsilon\,\mathsf M_2(\tilde Q)^{\mathsf T}\varepsilon^{-1} .
$$

The transpose returns the conjugate element, not a second side. At size four the two operations separate, and that separation is what the regular picture buys.

**The boundary.** The $2\times2$ image is a model of the module and not of the algebra's action on itself. Anything that needs the algebra as a carrier — a commutator of two multiplications, a two-sided operator, the Peirce corners — has no home at this size.

### I.2.c — Left Multiplication Carries, Right Multiplication Couples: the Mass Is a Right Action

**Read:** the two families are the two things an element can do to another element. A left multiplication carries what it acts on; a right multiplication changes its internal index.

**The reason is one line of the composition laws.** $L(\tilde Q_2\tilde Q)=L(\tilde Q_2)L(\tilde Q)$ is associativity read on the left, so left multiplication composes forward. $R(\tilde Q_2\tilde Q)=R(\tilde Q)R(\tilde Q_2)$ carries the product backwards, so right multiplication is a map on the other side of the argument.

**The mass is a right multiplication, and the algebra says why.** Left multiplication preserves the copy index, so a term that couples the two copies cannot be a left action. The coupling is the right multiplication by the column swap

$$
J=i\vec e_x,\qquad J^{2}=e_t,\qquad \mathsf M_2(J)=\sigma_1,\qquad R_J(\tilde Q)=\tilde QJ ,
$$

and $R_J$ exchanges the two columns with $R_J^{2}=\mathrm I$. The coupling element has to be a unit, because the mass is a bijection between the copies: one coefficient in each direction. A nilpotent cannot serve. For $\vec\Upsilon_x$ the matrix is $E_{12}$, the right multiplication carries the first column into the second and annihilates the second, and the map has rank two and no inverse. That is a one-way copy flip, not a mass.

**The boundary.** The statement is structural: it says which kind of action can couple the two copies, and it says that the coupling element must be off the cone. It does not give the coupling a value, and it does not produce a mass spectrum. The magnitude of the mass is an input, and the algebra is scale-free.

### I.2.d — The Factor $i$ Separates the Generators from the Observables

**Read:** the algebra's own basis maps to minus $i$ times the Pauli matrices, and the Hermitian basis maps to the Pauli matrices. The two rows differ by one factor and by nothing else.

$$
\vec e_\eta\longmapsto-i\sigma_\eta\ \ (\text{anti-Hermitian, generates}),\qquad i\vec e_\eta\longmapsto\sigma_\eta\ \ (\text{Hermitian, is measured}) .
$$

**The factor is forced, and the sign is forced.** A real $2\times2$ matrix of square $-\mathrm I_2$ is a complex structure on $\mathbb{R}^2$; three of them, anticommuting, are the quaternionic structure. The algebra whose vectors square to $-e_t$ needs the coefficient field to supply the $i$ that turns $\sigma_\eta$ into $-i\sigma_\eta$. The alternative assignment $\vec e_\eta\mapsto-\mathsf M_2(\vec e_\eta)$ keeps the squares and fails the products.

**So $i$ is not bookkeeping.** It is the statement that the three directions of the algebra are generators of rotations and not observables, and that the same three directions multiplied by $i$ are observables and not generators. The complexification is what allows one algebra to hold both.

**The boundary.** The argument explains why the factor is present in the model. It does not derive the complex numbers from anything physical, and it does not say that a measured quantity must be Hermitian; that is a separate postulate which the image makes convenient.

### I.2.e — The Trace Is the Clock and the Traceless Part Is the Motion

**Read:** the matrix trace sees the scalar part only, and the traceless part of the image is the vector part.

$$
\operatorname{Tr}L(\tilde Q)=4Q_t,\qquad \operatorname{Tr}M=0\iff\tilde Q\in\mathbb{B}_{V} .
$$

**The split is exact, and it is the scalar–vector split in the image.** The trace is additive, bilinear and blind to everything except $Q_t$; the traceless remainder carries the three directions. In the axis-free display the vector image is skew-symmetric, $M^{\mathsf T}=-M$, so the traceless condition and the antisymmetry coincide inside the image.

**The physical reading is the one from the previous entry, in matrix form.** The scalar part is the complex time, so the trace is the clock; the vector part is the three directions, so the traceless part is the motion. A matrix statement about a biquaternion that uses only the trace is a statement about time, and it cannot see a direction.

**The boundary.** The factor four is the dimension of the regular module and the factor two at size two is the dimension of the spinor module. Neither is a physical factor, and both are the origin of the factor-of-two errors that occur in computations that change size without saying so.

### I.2.f — The Determinant Is One Function with Three Readings

**Read:** the determinant is the norm, and the norm is read differently on three real slices.

| slice | determinant | reading |
| --- | --- | --- |
| material $\mathbb{B}_{\Phi}$ | $-(r'_t)^2+\lvert\vec r\rvert^2$ | the interval |
| informational $\mathbb{B}_{\Psi}$ | $h_t^2-\lvert\vec h'\rvert^2$ | the causal type |
| trace-one state | $\tfrac14(1-\lvert\vec r\rvert^2)$ | the mixedness |

**One zero set, three meanings.** The determinant vanishes on the light cone, on the boundary of the state space, and on the set of pure states, and these are three descriptions of one locus in three slices. Purity is affine in the determinant on the trace-one slice.

**The image makes invertibility a determinant.** A unit is an element with $N\neq0$, so in the matrix image a unit is a matrix with non-zero determinant. The algebraic criterion of the previous entry and the matrix criterion are the same criterion, and the zero-divisor cone is the determinant's vanishing set.

**The boundary.** These are three restrictions of one function to three real slices, not three quantities. A statement about the determinant must say which slice it is on, or it will read an interval as a probability weight.

### I.2.g — The Determinant Is a Volume, and an Interval Is Not

**Read:** multiplication by $\mathsf M$ is a real-linear map of $\mathbb{C}^2\cong\mathbb{R}^4$, and its real determinant is $\lvert\det\mathsf M\rvert^2$.

**On the unit-norm slice the map is volume preserving.** There $\det\mathsf M=1$, so the real determinant is one and the group is $SL_2(\mathbb{C})$. Volume preservation is a property of the transformation, and it holds for every element of the group.

**The two readings agree only in the zero set.** The volume is the volume of the realification of the module; the interval is the interval of the material sector. They vanish together, because both are built from the same determinant, and elsewhere they are different functions of the same four numbers.

**The boundary.** A "volume" in the module and a "volume" in spacetime are different objects with one algebraic ancestor. An argument that transfers a volume-preservation statement to a spacetime volume is transferring a statement between two different realifications.

### I.2.h — The Doubling Rule Is Where the Factors of Two Live

**Read:** every quantity of the smaller picture changes in one of three ways at the larger size, and the three ways are fixed by the block structure.

**Additive quantities double, multiplicative ones square, the spectrum repeats, the minimal polynomial does not change.** The first four follow from the block form. The last does not, and it is the one that catches errors: the characteristic polynomial squares and the minimal polynomial stays at degree two, because the square of a minimal polynomial is not minimal. An element therefore has two eigenmodes and not four, and the four entries of the regular spectrum are two modes counted twice.

**The trace, the determinant and the rank are three different rules on one object.** $4Q_t$ against $2Q_t$; $N^2$ against $N$; $2r$ against $r$. A number read at the wrong size is wrong by a definite factor, and the factor is always a power of two.

**The operator picture is worse.** The two-sided operator $X\mapsto\tilde QX\tilde Q^{*}$ is quadratic in the element, so it double-counts the parameters: its trace is $4\lvert Q_t\rvert^2$ and its determinant is $\lvert N\rvert^4$. Only the zero sets of the three determinants agree.

**The boundary.** The rule is bookkeeping and not physics. Its role in this category is diagnostic: when a factor of two appears in an argument, the first question is which picture the argument is in.

### I.2.i — The Element Stores Half the Rapidity

**Read:** a boost rotor of rapidity $\eta$ has a matrix with eigenvalues $e^{\pm\eta/2}$, and its two-sided operator has eigenvalues $e^{\eta},1,1,e^{-\eta}$.

$$
\tilde B_\eta=\cosh\tfrac{\eta}{2}\,e_t+\sinh\tfrac{\eta}{2}\,i\vec e_z,\qquad \mathsf M_2(\tilde B_\eta)=\operatorname{diag}\bigl(e^{\eta/2},e^{-\eta/2}\bigr) .
$$

**The half is the double cover, read on the spectrum.** The element acts on the spinor, so it carries half of the rapidity; the congruence acts on the four-vector, so it carries the whole of it. The two middle eigenvalues of the operator are the transverse directions, which the boost fixes.

**The same factor appears for a rotation, with a sign that is observable.** For a rotation of angle $\theta$ the element has eigenvalues $e^{\pm i\theta/2}$ and the operator has $e^{\pm i\theta}$ beside two ones. At $\theta=2\pi$ the element eigenvalues are $-1$ and the operator eigenvalues are $1$: the spinor returns with a sign and the vector returns unchanged.

**The boundary.** The reading needs a diagonalisable element and a pure boost or rotation. On the cone one eigenvalue vanishes, on its trace-zero part the two collide at zero, and the reading stops. For a general Lorentz element no single rapidity exists, and the polar decomposition separates the boost from the rotation.

### I.2.j — The Central Phase Is the Fibre, and the Operator Cannot See It

**Read:** the central element $e^{i\theta}e_t$ maps to the scalar matrix $e^{i\theta}\mathrm I_2$, which multiplies the element, multiplies the determinant by $e^{2i\theta}$, multiplies a state by $e^{i\theta}$, and acts trivially in the two-sided operator.

**A state is a ray and not a vector.** The scalar matrix does not preserve the trace-one slice, because it multiplies it by a phase; so the phase is not a property of the state and the state is an equivalence class. The map $\varsigma\mapsto\varsigma\varsigma^{\dagger}$ from unit spinors to rank-one Hermitian matrices of trace one has the phase circle as its fibre, and the bundle

$$
U(1)\hookrightarrow S^{3}\longrightarrow S^{2}
$$

is the Hopf bundle.

**The element picture sees the phase and the operator picture does not.** This is why the polar word carries a phase and the two-sided operator does not, and it is why a phase cannot be an observable: no operator of the algebra's own action records it.

**The boundary.** The fibre of the ray map and the stabiliser of an axis are different circles of $U(2)$ that meet only in $\{\pm\mathrm I_2\}$. They must not be identified fibre by fibre. And the holonomy of the Hopf connection is not derived here; it belongs to the entry on the gauge bundle.

### I.2.k — The Peirce Frame Is a Choice of Axis, and the Algebra Does Not Make It

**Read:** a frame with the monomial properties exists for every root of the unit, and there is a four-real-parameter family of roots.

**The root is a pair of projectors, and the pair is a measurement axis.** A root $\vec Z$ gives the idempotents $\tfrac12(e_t\pm\vec Z)$, and the idempotents are the first and fourth frame vectors. So the frame is a measurement axis together with the two nilpotent directions that complete it. Conversely every frame containing two orthogonal idempotents that sum to $e_t$ arises this way, so there is nothing else a frame can be.

**Sparsity belongs to six roots and not to the algebra.** Only $\pm i\vec e_x,\pm i\vec e_y,\pm i\vec e_z$ keep the sixteen arrays monomial with entries in $\mathbb{Z}[i]$, and those six give one frame up to a cyclic relabelling and the exchange of the two idempotents. A root with two nonzero coordinates has an idempotent with three nonzero coordinates, so the change matrix is not monomial, and the sixteen arrays lose the monomial form: the coefficients of the change and of its inverse are carried into every product.

**The consequence is a rule of method.** The standard form of the display is a convention about the axis, and the axis is chosen by the algebra's convention article and not by the algebra. Any result that changes when the root changes is a result about the frame.

**The boundary.** The sparsity is a property of the display, not a symmetry of the algebra. All Peirce frames are conjugate, so no physics can depend on the choice, and the appearance of a dense array in an unusual frame is not a signal of anything.

### I.2.l — The Six Subspaces Are Four Matrix Involutions

**Read:** the dagger, the entrywise bar, the transpose and minus the dagger carry the four conjugations onto the matrix side, and each subspace is a fixed or anti-fixed space of one of them.

**The dictionary is exact on the image and only on the image.** $\mathbb{B}_{\Psi}$ is the Hermitian part, $\mathbb{B}_{\Phi}$ the anti-Hermitian part, $\mathbb{B}_{H}$ the entrywise real part, $\mathbb{B}_{iH}$ the entrywise imaginary part, $\mathbb{B}_{C}$ the scalar matrices, $\mathbb{B}_{V}$ the traceless ones. Each condition defines a real sixteen-dimensional space in the ambient $M_4(\mathbb{C})$, and the image selects four dimensions inside it.

**The closure pattern is visible at a glance and it is not uniform.** The centre and the quaternion subspace are subalgebras. The vector subspace is closed under the commutator and not under the product. The anti-Hermitian image is the same: a Lie algebra under the bracket, not a subalgebra under the product.

**That last fact is why a Lorentz transformation is an exponential.** The boost and rotation generators lie in the anti-Hermitian image, where the bracket closes and the product does not. A finite transformation is therefore an exponential of a bracket element and not a product of two elements of the sector, which is the matrix statement of the fact that the material sector holds the generators and not the finite elements.

**The boundary.** The four matrix involutions are four *words in the matrix*, and which word a conjugation becomes depends on the frame. In the axis-free basis the transpose is quaternion conjugation; in another frame the same conjugation is a transpose conjugated by a fixed matrix. A formula that uses the transpose silently assumes the basis.

### I.2.m — Every Element Carries Its Own Frame, and the Chart Is Singular on the Axis

**Read:** a general element produces its own root, its own projectors and its own diagonalising matrix.

$$
\vec Z=-\frac{i}{B}\vec Q,\qquad \mathsf C_Q=\begin{pmatrix}B-Q_z&Q_x-iQ_y\\-Q_x-iQ_y&B-Q_z\end{pmatrix},\qquad \det\mathsf C_Q=2B(B-Q_z) .
$$

**The frame is not the frame of the last reading.** The Peirce frame is fixed once for the whole algebra; $\mathsf C_Q$ moves inside the element and depends on it. The first is a change of basis of the algebra, the second a change of basis adapted to one element.

**The singularity is a coordinate artefact.** The chart degenerates exactly when $B=Q_z$, which is one point of the sphere of directions. The second chart degenerates at $B=-Q_z$, and the two cannot degenerate together because $B\neq0$. So every element off the cone is covered.

**The physical reading is that a generic element has a frame of its own and a degenerate one does not.** An element with $B=0$ has coincident eigenvalues, and both charts degenerate with it, since both determinants carry the factor $B$. Its two projectors merge, no eigenbasis follows from the spectrum, and the diagonalisation carries nothing that the element did not already carry.

**The boundary.** The frame of an element is a statement about that element's spectrum and not about a measurement performed on it. Two elements with the same spectrum are not thereby in the same frame, and the diagonalising matrix is defined up to two rescalings that no measurement fixes.

## The Limits

**The entry reads the representations and not the operators.** It states what the images are worth and what each one loses. The operator pictures — the congruence, the two-sided operator, the adjoint and the swap, the monoid of acting maps — belong to the entries on the forms and on the modules, and the Peirce corners belong to the entry on the idempotents.

**The entry does not read the spectrum.** The eigenvalue pair is named because the matrix invariants carry it, and the spectral theory is the subject of its own entry. What this entry establishes is only that the pair is the same pair at both sizes and that the multiplicity is the module's dimension.

**Two readings are labelled and not proved.** The identification of the four matrix involutions with the physical conjugations, and the identification of the copy index with an internal index that a mass couples, are conventions of the corpus with a stated reason. The algebra supplies the two sides and the two involutions; which physical name goes with which is a naming.

**No factor in this entry is physical.** The factors two and four are the dimensions of the spinor and the regular modules. They are exact, they are unavoidable, and they are not measurements.

## Summary

- A matrix image depends on the frame and on the size; the element does not.
- The left family is the algebra and the right family is its opposite. They meet exactly in the scalar matrices and span seven dimensions.
- The $4\times4$ image is the $2\times2$ image written twice, with the copy index as the first tensor factor.
- Additive quantities double, multiplicative ones square, the spectrum repeats, and the minimal polynomial is unchanged. The element has two eigenmodes, not four.
- The determinant is the norm at size two and its square at size four; only the zero sets agree, and the zero set is the light cone, the state-space boundary and the set of pure states in three slices.
- The $2\times2$ image is the qubit and it has one side. The second side appears only when the element acts on a carrier.
- Left multiplication preserves the copy index, so a mass term is a right multiplication, and the element that carries it must be a unit because the mass is a bijection.
- The factor $i$ in the Pauli correspondence separates the anti-Hermitian generators from the Hermitian observables.
- A boost stores half its rapidity in the element and the whole of it in the congruence; that factor is the double cover.
- The central phase is the fibre of the ray map and it acts trivially in the two-sided operator, so it is not an observable.
- The Peirce frame is a choice of root, the roots form a four-parameter family, and only six of them keep the display sparse.
- The anti-Hermitian image is a Lie algebra under the commutator and not a subalgebra under the product, which is why a finite transformation is an exponential.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $L(\tilde Q)$, $R(\tilde Q)$ | the left and right matrices in a frame, in $M_4(\mathbb{C})$ |
| $\mathsf M_2(\tilde Q)$ | the compressed image in $M_2(\mathbb{C})$ |
| $\mathbb{B}_L$, $\mathbb{B}_R$ | the two four-dimensional families inside $M_4(\mathbb{C})$ |
| $N=\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ | the quaternionic norm |
| $\sigma_1,\sigma_2,\sigma_3$ | the Pauli matrices |
| $\varepsilon=i\sigma_2$ | the conjugating matrix of the transpose at size two |
| $\vec Z$ | a root of the unit, $\vec Z^2=e_t$ |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec Z)$ | the idempotent pair of the root |
| $\mathsf P$ | the swap matrix of the stitch, $\mathsf P^2=\mathrm I_4$ |
| $\mathsf C_Q$ | the diagonalising matrix of the element $\tilde Q$ |
| $\rho_\pm$ | the spectral projectors of the element |

## Further Reading

**In the mathematics corpus.** The four articles of the source table, and *Matrix Representations Conventions* for the choice of root that the standard display fixes.

**In this category.** The next entry, *Idempotents, Ideals and Observables*, reads the roots of $+e_t$ and $-e_t$ and the Peirce corners that this entry only names. *The Modules: What the Algebra Acts On* reads the carrier that the copy index belongs to. *The Four Forms and the Four Norms* reads the quarter-traces that this entry quotes as norms.

**In the archive, until they are rewritten.** The two longer treatments of the same material are [The Pauli Correspondence and the Matrix Image](../articles_physics/the-pauli-correspondence-and-the-matrix-image.html), which carries the observables, the states, the phase fibre and the double cover in full, and [Element and Operator Representations: The Three Actions](../articles_physics/element-and-operator-representations-the-three-actions.html), which carries the five pictures, the three actions and the mass coupling at operator level.
