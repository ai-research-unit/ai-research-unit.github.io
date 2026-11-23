# __The Pauli Pair and the Gamma Frame: Which Statements Survive Conjugation__

## Introduction

The Pauli pair is the $2\times2$ image and its $4\times4$ tensor lift, built in the Peirce frame of a root; the gamma frame is the five generators of the complexified Dirac algebra, written inside $M_4(\mathbb{C})$.

Both are frames, and both print a direction. The entry states what each display shows, what each one costs, and how the cost is measured. The measurement is a test and not an opinion: conjugate the statement and re-read it. What returns itself is a fact about the algebra; what does not is a fact about the page.

The one idea that governs the entry is that the element is one and the pictures are many. The doubling of the size, the block structure, the diagonal member and the gamma list are all consequences of one choice of frame, and none of them is a second object.

Boundaries. The root, the Peirce frame, the tensor product, the six roots that keep the sparsity, the compression at size two, the Pauli correspondence, the spectral projectors and the adjugate are *$M_4(\mathbb{C})$ Pauli Representation* and *$M_2(\mathbb{C})$ Pauli Representation*; the two families in a general frame and the change of frame are *Families of Matrix Representations*; the gamma frame, its non-canonicity, the Clifford and pin groups and the legacy dictionary are *The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$* and *The Pin Group of the Gamma Frame*. The display that chooses no direction is *The AXF Matrices: Axis-Free, Integer Entries*, and the argument for preferring it is *The AXF Matrices: Axis-Free, Integer Entries*, §*Why the Pauli and the Gamma Displays Are Refused*. No dynamics, no mass value and no quantum postulate appears below.

## The Source Table

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| the root $\vec\Xi=i\vec e_z$, the idempotents and the Peirce basis, the left and right families, the stitch as a pure swap, the switch to the axis-free display, the sixteen products, which roots give a Peirce frame | [$M_4(\mathbb{C})$ Pauli Representation](../articles_maths/m4c-pauli-representation.html) |
| the compression to size two, the two orders, the images of the four units, the Pauli correspondence, the spectral projectors, the diagonalising matrix, the adjugate and the inverse | [$M_2(\mathbb{C})$ Pauli Representation](../articles_maths/m2c-pauli-representation.html) |
| the two families in a general frame, the three composition laws, the $2\times2$ family and why it has no second side | [Families of Matrix Representations](../articles_maths/families-of-matrix-representations.html) |
| the five frame operators, their identity with five of the sixteen basis operators, the non-canonicity of the frame, the Clifford group and the legacy gamma formulation | [The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$](../articles_maths/the-gamma-frame-and-the-complexified-dirac-algebra-of-m4c.html) |
| the unit vectors of the frame, the finite group, the lift and the double cover | [The Pin Group of the Gamma Frame](../articles_maths/the-pin-group-of-the-gamma-frame.html) |

The Peirce frame comes first, then its compression, then the general theory, then the gamma frame built on the same sixteen operators.

## The Results in Brief

### The Root and the Peirce Frame

A root of the unit fixes a frame. For $\vec Z=\sum_{\imath\in\{x,y,z\}}a_{\imath}\vec e_{\imath}$ with

$$
\vec Z^{2}=-\bigl(a_x^2+a_y^2+a_z^2\bigr)e_t=e_t ,
$$

the condition is $a_x^2+a_y^2+a_z^2=-1$, one complex equation in three unknowns: a family of real dimension four. The root gives the idempotent pair, and the pair gives a frame.

The standard root is $\vec\Xi=i\vec e_z$, with

$$
\tilde\Pi_{\mathrm{id},\pm}=\tfrac12\bigl(e_t\pm i\vec e_z\bigr),\qquad
\vec\Pi_{\mathrm{nil},\pm}=\tfrac12\bigl(i\vec e_x\pm\vec e_y\bigr),
$$

and the order $\mathcal{P}=(\tilde\Pi_{\mathrm{id},+},\vec\Pi_{\mathrm{nil},+},\vec\Pi_{\mathrm{nil},-},\tilde\Pi_{\mathrm{id},-})$.

In that frame the sixteen matrices are monomial, unitary, of determinant one, with entries in $\mathbb{Z}[i]$. The display is a tensor product,

$$
L(\tilde Q)=\mathrm I_2\otimes\mathsf M_2(\tilde Q),\qquad R(\tilde Q)=\mathsf M_2(\tilde Q)^{\mathsf T}\otimes\mathrm I_2 ,
$$

the idempotents are the first and fourth frame vectors, and the stitch is a pure swap, $R=\mathsf P L^{\mathsf T}\mathsf P$.

**Only the six coordinate roots keep the sparsity.** The roots $\pm i\vec e_x,\pm i\vec e_y,\pm i\vec e_z$ give one frame up to cyclic relabelling and the exchange of the two idempotents; a root with two nonzero coordinates densifies every array.

### The Doubling Rule

At size two the same data appear at half the size.

$$
\operatorname{Tr}\mathsf M_2(\tilde Q)=2Q_t,\qquad \det\mathsf M_2(\tilde Q)=N,\qquad \operatorname{spec}=\{Q_t+iB,\ Q_t-iB\},\qquad \operatorname{rank}\in\{0,1,2\} .
$$

The larger size is the smaller one written twice.

| quantity | size two | size four | rule |
| --- | --- | --- | --- |
| trace | $2Q_t$ | $4Q_t$ | double |
| the determinant of the image | $N$ | $N^2$ | square |
| characteristic polynomial | degree $2$ | its square | square |
| spectrum | $\eta_{\pm}$ once each | each twice | repeat |
| rank | $r$ | $2r$ | double |
| minimal polynomial | degree $2$ | degree $2$ | unchanged |

**The last row is the exception.** The characteristic polynomial squares and the minimal polynomial does not, because the square of a minimal polynomial is not minimal. The element has two eigenmodes and not four.

### The Pauli Correspondence

| unit | matrix | Hermitian |
| --- | --- | --- |
| $e_t$ | $\mathrm I_2$ | yes |
| $\vec e_{\imath}$ | $-i\sigma_{\imath}$ | no |
| $i\vec e_{\imath}$ | $\sigma_{\imath}$ | yes |

$$
\boxed{\;\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i\bigl(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3\bigr)\;}
$$

Hermitian conjugation becomes the conjugate transpose, $\mathsf M_2(\tilde Q^{*})=\mathsf M_2(\tilde Q)^{\dagger}$, so the fixed space of ${}^{*}$ is carried onto the Hermitian matrices.

**There is no second side at size two.** The right action there is the ordinary matrix product $\mathsf A\mapsto\mathsf A\,\mathsf M_2(\tilde Q)$, which is not left multiplication by a matrix unless $\mathsf M_2(\tilde Q)$ is scalar.

### The Gamma Frame

The five operators are five of the sixteen basis operators. In the coefficient frame of the method article,

$$
\gamma_0=iL_{e_t}R_{\vec e_x},\quad \gamma_1=iL_{\vec e_x}R_{\vec e_y},\quad \gamma_2=iL_{\vec e_y}R_{\vec e_y},\quad \gamma_3=iL_{\vec e_z}R_{\vec e_y},\quad \gamma_5=-iL_{e_t}R_{\vec e_z} .
$$

They satisfy the Clifford relations, with the sign vector $\varepsilon=(1,-1,-1,-1)$.

$$
\{\gamma_{\imath},\gamma_{\jmath}\}=2\varepsilon_{\imath}\delta_{\imath\jmath}\mathrm I_4,\qquad
(\gamma_{\imath})^2=-\mathrm I_4,\qquad
\gamma_5^2=\mathrm I_4,\qquad
\{\gamma_{\imath},\gamma_5\}=0,
$$

$$
\operatorname{tr}(\gamma_{\imath}\gamma_{\jmath})=4\varepsilon_{\imath}\delta_{\imath\jmath},\qquad
\operatorname{tr}(\gamma_5\gamma_{\imath}\gamma_{\jmath}\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\imath\jmath\rho\sigma} .
$$

**The frame is not canonical.** If the generators satisfy the anticommutation relations and $S\in GL_4(\mathbb{C})$, then $S\gamma_{\imath} S^{-1}$ satisfy the same relations, so the frames form a homogeneous space under $GL_4(\mathbb{C})$, and the subgroup that preserves the span of the generators is the Clifford group, which acts on the frame by Lorentz transformations. The gamma set is one frame among a bundle of them.

### The Switch Between the Two Displays

One matrix carries the Peirce frame onto the axis-free one.

$$
C_{\Pi}=\bigl(\tilde\Pi_{\mathrm{id},+}\ \ \vec\Pi_{\mathrm{nil},+}\ \ \vec\Pi_{\mathrm{nil},-}\ \ \tilde\Pi_{\mathrm{id},-}\bigr)
=\frac12
\begin{pmatrix}
1&0&0&1\\
0&i&i&0\\
0&1&-1&0\\
i&0&0&-i
\end{pmatrix},
\qquad
L_{\mathrm{pau}}(\tilde Q)=C_{\Pi}^{-1}L_{\mathrm{axf}}(\tilde Q)\,C_{\Pi},
$$

with $\det C_{\Pi}=-\tfrac14$ and $C_{\Pi}^{-1}=2C_{\Pi}^{\dagger}$. The switch is two independent $2\times2$ Hadamard blocks and it mixes no direction: one block joins $\{e_t,\vec e_z\}$ to $\{\tilde\Pi_{\mathrm{id},+},\tilde\Pi_{\mathrm{id},-}\}$, the other joins $\{\vec e_x,\vec e_y\}$ to $\{\vec\Pi_{\mathrm{nil},+},\vec\Pi_{\mathrm{nil},-}\}$.

Every invariant survives the change. Products, anticommutators, traces, determinants, spectra, ranks and the eigenvalue count are the same on both sides, which is why the correspondence between two articles written in different displays is a sentence and not a computation.

## What the Two Displays Show

### Why the Third Matrix Is the Diagonal One

The Pauli matrices are

$$
\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
\sigma_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\qquad
\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$

**Two of them carry $i$ or carry zeros on the diagonal; the third is real and diagonal.** That difference is not a difference between three operators. It is a difference between three positions in a list, produced by the order in which the list was built: the root is $\vec\Xi=i\vec e_z$, the idempotents are built from $\vec e_z$, and $\sigma_3$ is the matrix of the unit the root was made from. The direction is in the frame, and the array reports it.

### The Three Spatial Units Have Three Different Jobs

In the gamma set the three spatial units appear in three shapes. $\vec e_x$ sits in the left slot of $\gamma_0$, $\vec e_z$ in the right slot of $\gamma_3$ and $\gamma_5$, and $\vec e_y$ in the right slot of three of them, while $\gamma_1$ and $\gamma_2$ carry two of them at once. The three are one orbit under the rotations of the algebra, and the display shows them as three unrelated objects.

The orbit is a statement of physics; the page shows one member of it and two others, and a reader who wants to use the symmetry must first discover that the symmetry exists. The display is what conceals it.

### The Relabelling Test

Apply the automorphism that exchanges two spatial units, re-read the statement, and compare.

$$
\vec e_{\imath}^{2}=-e_t
$$

returns itself, with the index renamed: it is a fact about $\mathbb{B}$.

$$
\sigma_3=\operatorname{diag}(1,-1)
$$

does not return itself: under the exchange of $\vec e_z$ with $\vec e_x$ the diagonal member becomes the first one, and the array is not the array that was printed. It is a fact about the page.

**Both are printed as equalities, in the same font, with no marker.** A reader who wants to know which kind of statement is in front of him has nothing to consult, and a writer who copies the second into a rotated context produces a formula that is wrong without being detectable as wrong.

### The Defect Is the Unmarked Direction

The defect is not that the display has a direction. A frame is legitimate whenever the physics supplies one: a Stern–Gerlach apparatus has an axis, a beam has an axis, a background field breaks isotropy, and in each case the frame is a datum and the correct practice is to name it and use it.

**The defect is that the direction is unmarked.** A sentence $\sigma_3[\vec u]$, with $\vec u$ the axis, would be complete and could be rotated. The sentence $\sigma_3$, with no axis, is incomplete and cannot be rotated, and the notation supplies no place to put the missing name. A formula of general physics is then printed with a datum it does not contain, and the reader has no way to subtract the datum.

The signs are the model of the other case. Time is distinguished from space by the squares, $e_t^2=+e_t$ and $\vec e_{\imath}^2=-e_t$, and that asymmetry is carried by an object of the algebra, where it cannot be lost and needs no declaration. An asymmetry that the physics has belongs in an object; a direction that the physics does not have belongs nowhere.

### What Is Not Claimed

**No computation done in the Pauli or gamma display is wrong.** The Clifford relations hold in every display, every trace and every determinant is invariant, and an amplitude computed with gammas is correct. The Dirac equation written with the five gammas is a correct equation, and it is the equation of the literature.

The claim is about the page. A fundamental equation should not be written in a form that privileges a direction the physical reality does not contain, because the privilege then travels with the formula and cannot be distinguished from the physics. The remedy is not a correction of any result; it is a rule of writing, and the display that obeys it is *The AXF Matrices: Axis-Free, Integer Entries*.

## The Interpretations

### I.2.i — One Element, Two Pictures, and the Doubling Is Not a Second Particle

Read: the $4\times4$ regular image is the $2\times2$ image written twice, and the two copies are the two dimensions of the module.

The tensor display makes the doubling visible as a block structure. $L=\mathrm I_2\otimes\mathsf M_2$ and $R=\mathsf M_2^{\mathsf T}\otimes\mathrm I_2$: the first factor of each tensor is the copy index, the second is the element. The matrix is a two-by-two array of blocks, each block a copy of $\mathsf M_2(\tilde Q)$.

The consequences are bookkeeping and they are not optional. The trace doubles because there are two blocks. The determinant squares because it is multiplicative over the blocks. The spectrum repeats because each block has the same two eigenvalues. The rank doubles because both blocks have the same rank. None of these is a physical multiplicity.

The boundary. The copy index is not a chirality, not a generation and not a particle label. The two copies are the two columns of the module, and the two minimal left ideals they correspond to are isomorphic, so nothing in the algebra distinguishes them. A reading that treats the two copies as two species is reading the display and not the algebra.

### I.2.j — The Qubit Is the $2\times2$ Image, and It Has One Side

Read: the compressed image is the state space of a two-level system, and the regular image is the same object with its copy index exposed.

At size two the picture is complete and it has one side. The carrier is $M_2(\mathbb{C})$ itself: the element acts on a two-component column, and the column is a spinor. The right action there is an ordinary matrix product, and it is not the left multiplication by a second matrix. So the element yields one matrix, and the "before" and "after" pictures collapse into one.

The transposition and the conjugation are the same operation at this size. The conjugating matrix is $\varepsilon=i\sigma_2$, with $\varepsilon^{\mathsf T}=-\varepsilon$ and $\varepsilon^{2}=-\mathrm I_2$, and

$$
\mathsf M_2(\tilde Q^{\natural})=\varepsilon\,\mathsf M_2(\tilde Q)^{\mathsf T}\varepsilon^{-1} .
$$

The transpose returns the conjugate element, not a second side. At size four the two operations separate, and that separation is what the regular picture buys.

The boundary. The $2\times2$ image is a model of the module and not of the algebra's action on itself. Anything that needs the algebra as a carrier — a commutator of two multiplications, a two-sided operator, the Peirce corners — has no home at this size.

### I.2.k — Left Multiplication Carries, Right Multiplication Couples: the Mass Is a Right Action

Read: the two families are the two things an element can do to another element. A left multiplication carries what it acts on; a right multiplication changes its internal index.

The reason is one line of the composition laws. $L(\tilde Q_2\tilde Q)=L(\tilde Q_2)L(\tilde Q)$ is associativity read on the left, so left multiplication composes forward. $R(\tilde Q_2\tilde Q)=R(\tilde Q)R(\tilde Q_2)$ carries the product backwards, so right multiplication is a map on the other side of the argument.

**The mass is a right multiplication, and the algebra says why.** Left multiplication preserves the copy index, so a term that couples the two copies cannot be a left action. The coupling is the right multiplication by the column swap

$$
J=i\vec e_x,\qquad J^{2}=e_t,\qquad \mathsf M_2(J)=\sigma_1,\qquad R_J(\tilde Q)=\tilde QJ ,
$$

and $R_J$ exchanges the two columns with $R_J^{2}=\mathrm I$. The coupling element has to be invertible, because the mass is a bijection between the copies: one coefficient in each direction. A nilpotent cannot serve. For $\vec\Pi_{\mathrm{nil},x}$ the matrix is $E_{21}$, the right multiplication carries the first column into the second and annihilates the second, and the map has rank two and no inverse. That is a one-way copy flip, not a mass.

The boundary. The statement is structural: it says which kind of action can couple the two copies, and it says that the coupling element must be off the cone. It does not give the coupling a value, and it does not produce a mass spectrum. The magnitude of the mass is an input, and the algebra is scale-free.

### I.2.l — The Factor $i$ Separates the Generators from the Observables

Read: the algebra's own basis maps to minus $i$ times the Pauli matrices, and the Hermitian basis maps to the Pauli matrices. The two rows differ by one factor and by nothing else.

$$
\vec e_{\imath}\longmapsto-i\sigma_{\imath}\ \ (\text{anti-Hermitian, generates}),\qquad i\vec e_{\imath}\longmapsto\sigma_{\imath}\ \ (\text{Hermitian, is measured}) .
$$

The factor is forced, and the sign is forced. A real $2\times2$ matrix of square $-\mathrm I_2$ is a complex structure on $\mathbb{R}^2$; three of them, anticommuting, are the quaternionic structure. The algebra whose vectors square to $-e_t$ needs the coefficient field to supply the $i$ that turns $\sigma_{\imath}$ into $-i\sigma_{\imath}$. The alternative assignment $\vec e_{\imath}\mapsto-\mathsf M_2(\vec e_{\imath})$ keeps the squares and fails the products.

So $i$ is not bookkeeping. It is the statement that the three directions of the algebra are generators of rotations and not observables, and that the same three directions multiplied by $i$ are observables and not generators. The complexification is what allows one algebra to hold both.

The boundary. The argument explains why the factor is present in the model. It does not derive the complex numbers from anything physical, and it does not say that a measured quantity must be Hermitian; that is a separate postulate which the image makes convenient.

### I.2.m — The Doubling Is Where the Factors of Two Live

Read: every quantity of the smaller picture changes in one of three ways at the larger size, and the three ways are fixed by the block structure.

**Additive quantities double, multiplicative ones square, the spectrum repeats, the minimal polynomial does not change.** The first four follow from the block form. The last does not, and it is the one that catches errors: the characteristic polynomial squares and the minimal polynomial stays at degree two, because the square of a minimal polynomial is not minimal.

The operator picture makes it worse. The two-sided operator $X\mapsto\tilde QX\tilde Q^{*}$ is quadratic in the element, so it double-counts the parameters: its trace is $4\lvert Q_t\rvert^2$ and its determinant is $\lvert N\rvert^4$. Only the zero sets of the three determinants agree.

The boundary. The rule is bookkeeping and not physics. Its role is diagnostic: when a factor of two appears in an argument, the first question is which picture the argument is in.

### I.2.n — The Element Stores Half the Rapidity

Read: a boost rotor of rapidity $\upsilon_{\mathrm{rnd}}$ has a matrix with eigenvalues $e^{\pm k/2}$, and its two-sided operator has eigenvalues $e^k,1,1,e^{-k}$.

$$
\tilde B_{\imath}=\cosh\tfrac{\upsilon_{\mathrm{rnd}}}{2}\,e_t+\sinh\tfrac{\upsilon_{\mathrm{rnd}}}{2}\,i\vec e_z,\qquad \mathsf M_2(\tilde B_{\imath})=\operatorname{diag}\bigl(e^{k/2},e^{-k/2}\bigr) .
$$

The half is the double cover, read on the spectrum. The element acts on the spinor, so it carries half of the rapidity; the congruence acts on the four-vector, so it carries the whole of it. The two middle eigenvalues of the operator are the transverse directions, which the boost fixes.

The same factor appears for a rotation, with a sign that is observable. For a rotation of angle $\theta$ the element has eigenvalues $e^{\pm i\theta/2}$ and the operator has $e^{\pm i\theta}$ beside two ones. At $\theta=2\pi$ the element eigenvalues are $-1$ and the operator eigenvalues are $1$: the spinor returns with a sign and the vector returns unchanged.

The boundary. The reading needs a diagonalisable element and a pure boost or rotation. On the cone one eigenvalue vanishes, on its trace-zero part the two collide at zero, and the reading stops. For a general Lorentz element no single rapidity exists, and the polar decomposition separates the boost from the rotation.

### I.2.o — The Central Phase Is the Fibre, and the Operator Cannot See It

Read: the central element $e^{i\theta}e_t$ maps to the scalar matrix $e^{i\theta}\mathrm I_2$, which multiplies the element, multiplies the determinant by $e^{2i\theta}$, multiplies a state by $e^{i\theta}$, and acts trivially in the two-sided operator.

A state is a ray and not a vector. The scalar matrix does not preserve the unit-weight slice, because it multiplies it by a phase; so the phase is not a property of the state and the state is an equivalence class. The map $\varsigma\mapsto\varsigma\varsigma^{\dagger}$ from unit spinors to rank-one Hermitian matrices of trace one has the phase circle as its fibre, and the bundle

$$
U(1)\hookrightarrow S^{3}\longrightarrow S^{2}
$$

is the Hopf bundle.

**The element picture sees the phase and the operator picture does not.** This is why the polar word carries a phase and the two-sided operator does not, and it is why a phase cannot be an observable: no operator of the algebra's own action records it.

The boundary. The fibre of the ray map and the stabiliser of an axis are different circles of $U(2)$ that meet only in $\{\pm\mathrm I_2\}$. They must not be identified fibre by fibre. And the holonomy of the Hopf connection is not derived here; it belongs to the entry on the gauge bundle.

### I.2.p — The Peirce Frame Is a Choice of Axis, and the Algebra Does Not Make It

Read: a frame with the monomial properties exists for every root of the unit, and there is a four-real-parameter family of roots.

The root is a pair of projectors, and the pair is a measurement axis. A root $\vec Z$ gives the idempotents $\tfrac12(e_t\pm\vec Z)$, and the idempotents are the first and fourth frame vectors. So the frame is a measurement axis together with the two nilpotent directions that complete it. Conversely every frame containing two orthogonal idempotents that sum to $e_t$ arises this way, so there is nothing else a Peirce frame can be.

Sparsity belongs to six roots and not to the algebra. Only $\pm i\vec e_x,\pm i\vec e_y,\pm i\vec e_z$ keep the sixteen arrays monomial with entries in $\mathbb{Z}[i]$, and those six give one frame up to a cyclic relabelling and the exchange of the two idempotents. A root with two nonzero coordinates has an idempotent with three nonzero coordinates, so the change matrix is not monomial and the sixteen arrays lose the monomial form.

The consequence is a rule of method. The standard form of the display is a convention about the axis, and the axis is chosen by the conventions article and not by the algebra. Any result that changes when the root changes is a result about the frame.

The boundary. The sparsity is a property of the display, not a symmetry of the algebra. All Peirce frames are conjugate, so no physics can depend on the choice, and the appearance of a dense array in an unusual frame is not a signal of anything.

### I.2.q — Every Element Carries Its Own Frame, and the Chart Is Singular on the Axis

Read: a general element produces its own root, its own projectors and its own diagonalising matrix.

$$
\vec Z=-\frac{i}{B}\vec Q,\qquad \mathsf C_Q=\begin{pmatrix}B-Q_z&Q_x-iQ_y\\-Q_x-iQ_y&B-Q_z\end{pmatrix},\qquad \det\mathsf C_Q=2B(B-Q_z) .
$$

The frame is not the frame of the previous reading. The Peirce frame is fixed once for the whole algebra; $\mathsf C_Q$ moves inside the element and depends on it. The first is a change of basis of the algebra, the second a change of basis adapted to one element.

The singularity is a coordinate artefact. The chart degenerates exactly when $B=Q_z$, which is one point of the sphere of directions. The second chart degenerates at $B=-Q_z$, and the two cannot degenerate together because $B\neq0$. So every element off the cone is covered.

The physical reading is that a generic element has a frame of its own and a degenerate one does not. An element with $B=0$ has coincident eigenvalues, and both charts degenerate with it, since both determinants carry the factor $B$. Its two projectors merge, no eigenbasis follows from the spectrum, and the diagonalisation carries nothing that the element did not already carry.

The boundary. The frame of an element is a statement about that element's spectrum and not about a measurement performed on it. Two elements with the same spectrum are not thereby in the same frame, and the diagonalising matrix is defined up to two rescalings that no measurement fixes.

## The Limits

The entry reads displays and not the algebra. It states what each picture makes visible and what each one loses. The axis-free display, its ten properties and its uniqueness belong to *The AXF Matrices: Axis-Free, Integer Entries*, and the argument that the corpus should display in that basis belongs to *The AXF Matrices: Axis-Free, Integer Entries*, §*Why the Pauli and the Gamma Displays Are Refused*.

The entry does not read the spectrum. The eigenvalue pair is named because the matrix invariants carry it, and the spectral theory is the subject of its own entry.

Three readings are labelled and not proved. The identification of the four matrix involutions with the physical conjugations, the identification of the copy index with an internal index that a mass couples, and the naming of the phase as a fibre are conventions of the corpus with a stated reason. The algebra supplies the two sides, the two involutions and the circle; which physical name goes with which is a naming.

The gamma section is a dictionary and not a derivation. The five operators are identified with five of the sixteen basis operators in a particular coefficient frame, and a different normalisation of the basis operators changes the identification. Nothing in the physics depends on which five are chosen, because the frame is not canonical.

**No factor in this entry is physical.** The factors two and four are the dimensions of the spinor and the regular modules. They are exact, they are unavoidable, and they are not measurements.

## Summary

- The Peirce frame is built from a root of the unit; the standard root is $i\vec e_z$, and the frame gives the tensor display $L=\mathrm I_2\otimes\mathsf M_2$, $R=\mathsf M_2^{\mathsf T}\otimes\mathrm I_2$ with a pure-swap stitch.
- The $4\times4$ image is the $2\times2$ image written twice: additive quantities double, multiplicative ones square, the spectrum repeats, the minimal polynomial is unchanged.
- The $2\times2$ image is the qubit and it has one side; the second side appears only when the element acts on a carrier.
- Left multiplication preserves the copy index, so a mass term is a right multiplication, and the element that carries it must be invertible because the mass is a bijection.
- The factor $i$ in the Pauli correspondence separates the anti-Hermitian generators from the Hermitian observables.
- A boost stores half its rapidity in the element and the whole of it in the congruence; that factor is the double cover.
- The central phase is the fibre of the ray map and it acts trivially in the two-sided operator, so it is not an observable.
- The Peirce frame is a choice of axis; the roots form a four-parameter family and only six of them keep the sparsity.
- The gamma set is five of the sixteen basis operators, it satisfies the Clifford relations with the sign vector $(1,-1,-1,-1)$, and the frame is not canonical.
- The display prints a direction the algebra does not contain, and the relabelling test measures it: a statement that does not return itself under the exchange of two spatial units is a statement about the page.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathsf M_2(\tilde Q)$ | the compressed image in $M_2(\mathbb{C})$ |
| $L(\tilde Q)$, $R(\tilde Q)$ | the left and right matrices in the Peirce frame, in $M_4(\mathbb{C})$ |
| $\vec Z$, $\vec\Xi$ | a root of the unit, $\vec Z^2=e_t$; and the standard root $i\vec e_z$ |
| $\tilde\Pi_{\mathrm{id},\pm}$, $\vec\Pi_{\mathrm{nil},\pm}$ | the idempotents and the nilpotents of the root |
| $\mathcal{P}$ | the Peirce order $(\tilde\Pi_{\mathrm{id},+},\vec\Pi_{\mathrm{nil},+},\vec\Pi_{\mathrm{nil},-},\tilde\Pi_{\mathrm{id},-})$ |
| $\mathsf P$ | the swap matrix of the stitch, $\mathsf P^2=\mathrm I_4$ |
| $\sigma_1,\sigma_2,\sigma_3$ | the Pauli matrices |
| $\varepsilon=i\sigma_2$ | the conjugating matrix of the transpose at size two |
| $C_{\Pi}$ | the switch to the axis-free frame, $\det C_{\Pi}=-\tfrac14$ |
| $\gamma_0,\gamma_1,\gamma_2,\gamma_3,\gamma_5$ | the five frame operators of the gamma set |
| $\varepsilon_{\imath}$ | the sign vector $(1,-1,-1,-1)$ of the frame operators |
| $N=\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ | the quaternionic norm |
| $\mathsf C_Q$ | the diagonalising matrix of the element $\tilde Q$ |
| $\rho_\pm$ | the spectral projectors of the element |

## Further Reading

- [$M_4(\mathbb{C})$ Pauli Representation](../articles_maths/m4c-pauli-representation.html), for the root, the Peirce frame, the stitch and the switch.
- [$M_2(\mathbb{C})$ Pauli Representation](../articles_maths/m2c-pauli-representation.html), for the compression, the Pauli correspondence and the diagonalising matrix.
- [Families of Matrix Representations](../articles_maths/families-of-matrix-representations.html), for the two families in a general frame.
- [The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$](../articles_maths/the-gamma-frame-and-the-complexified-dirac-algebra-of-m4c.html), for the five frame operators and the legacy dictionary.
- [The Pin Group of the Gamma Frame](../articles_maths/the-pin-group-of-the-gamma-frame.html), for the finite group and the double cover.
- [The AXF Matrices: Axis-Free, Integer Entries](the-axf-matrices-axis-free-integer-entries.html), for the display that chooses no direction.
- [The AXF Matrices: Axis-Free, Integer Entries](the-axf-matrices-axis-free-integer-entries.html#why-the-pauli-and-the-gamma-displays-are-refused), for the argument and the migration rules.
- [Idempotents, Ideals and Observables](idempotents-ideals-and-observables.html), for the roots of $+e_t$ and $-e_t$ and the Peirce corners named here.
- [The Modules: What the Algebra Acts On](the-modules-what-the-algebra-acts-on.html), for the carrier the copy index belongs to.
