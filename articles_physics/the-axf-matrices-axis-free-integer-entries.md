# __The AXF Matrices: Axis-Free, Integer Entries__

## Introduction

**This entry reads the AXF matrices of the biquaternion algebra.** The label $\mathrm{axf}$ is short for *axis-free*: it names the family built in the coefficient basis, whose four vectors are the four units themselves, and it names the one thing the display does not do, which is to choose a direction. The label is a name in lowercase roman letters and not an exponent.

**Two claims, and the second is the strong one.** The first is that in this basis the sixteen arrays of the four units are signed permutations with entries in $\{0,+1,-1\}$, and that ten properties hold at once. The second is that this basis is the only one, up to a relabelling of the three directions and a sign on each vector, with that sparsity, so the array names its frame instead of the frame naming the array.

**The entry also states what an array is not.** The operator is unique and frame-free; its matrix is one representative of a conjugacy class. Every invariant is read from the operator, and the array is a service to the reader and a diagnostic of the frame.

**Boundaries.** The basis, the two families, the stitch, the ten properties, the uniqueness among sparse frames, the product, the trace, the determinant and the four norms are *$M_4(\mathbb{C})$ Axis-Free Representation*; the general theory of the two families and of the change of frame is *Families of Matrix Representations*; the six subspaces and the three decompositions are *Subspaces and Decompositions of the Biquaternion Algebra*. The Peirce display — the root, the idempotents, the tensor product and the compression at size two — is *The Pauli and Gamma Matrices: the Direction in the Display*, and why the corpus displays in this basis rather than in that one is *Why AXF Matrices instead of Pauli and Gamma Matrices*. The spectrum is named here because the matrix invariants carry it, and it is read in *The Spectrum and the Two Modes*. No dynamics, no Clifford algebra and no gamma matrix appears below.

## The Source Table

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| the axis-free basis and the structure constants, the left family, the right family, the stitch, the conjugacy class, the ten properties, realness and the subring, the uniqueness among signed-permutation frames, the product, the trace, the determinant, the four norms, the six subspaces | [$M_4(\mathbb{C})$ Axis-Free Representation](../articles_maths/m4c-axis-free-representation.html) |
| the definition of the two families in a general frame, the three composition laws, the switch and its transformation law, the change of frame, the $2\times2$ family | [Families of Matrix Representations](../articles_maths/families-of-matrix-representations.html) |
| the six remarkable subspaces, the three decompositions, the closure of each subspace | [Subspaces and Decompositions of the Biquaternion Algebra](../articles_maths/subspaces-and-decompositions-of-the-biquaternion-algebra.html) |

**The rows are the entry's own order.** The frame comes first, then the general theory it is an instance of, then the subspaces the image makes visible.

## The Results in Brief

### The Basis

**The four units are the basis.** With $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ and

$$
e_t=1\otimes1,\qquad \vec e_x=1\otimes\vec e_x,\qquad \vec e_y=1\otimes\vec e_y,\qquad \vec e_z=1\otimes\vec e_z,
$$

the element is $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ with $Q_\mu=q_\mu+iq'_\mu$. The two names for this basis are *coefficient basis*, which names the coordinates, and *axis-free*, which names what the frame does not do.

**The product is the table, and the table is the algebra.**

$$
e_\mu e_\nu=\sum_\rho\varepsilon_{\mu\nu}^{\ \ \rho}\,e_\rho,\qquad \varepsilon_{\mu\nu}^{\ \ \rho}\in\{0,+1,-1\} .
$$

No complex number appears in it: $i$ is central and is carried by the coefficients.

### The Array

**The $\nu$-th column is the product with the $\nu$-th unit.**

$$
L_{\mathrm{axf}}(\tilde Q)_{\mu\nu}=\bigl[\tilde Qe_\nu\bigr]_\mu,
\qquad
L_{\mathrm{axf}}(\tilde Q)=
\begin{pmatrix}
Q_t&-Q_x&-Q_y&-Q_z\\
Q_x&Q_t&-Q_z&Q_y\\
Q_y&Q_z&Q_t&-Q_x\\
Q_z&-Q_y&Q_x&Q_t
\end{pmatrix}.
$$

**The first column recovers the element,** because $\tilde Qe_t=\tilde Q$, so the assignment is injective and multiplicative, and its image is a four-complex-dimensional subalgebra $\mathbb{B}_L$ with unit $\mathrm I_4$.

**The right family is the same rule on the other side,** $R_{\mathrm{axf}}(\tilde Q)_{\mu\nu}=[\vec e_\nu\tilde Q]_\mu$, it is anti-multiplicative, and it commutes with the left family.

### The Ten Properties

**In this basis the sixteen matrices have all of the following at once.**

| | property |
| --- | --- |
| (a) | every entry lies in $\{0,+1,-1\}$; no imaginary unit appears |
| (b) | each is a signed permutation matrix |
| (c) | each is orthogonal over $\mathbb{R}$, hence also unitary |
| (d) | the entries are the structure constants, read by columns |
| (e) | the transpose is the quaternion conjugation, $L(\tilde Q)^{\mathsf T}=L(\tilde Q^{\natural})$ |
| (f) | the stitch is real and diagonal, $R=DL^{\mathsf T}D$ with $D=\operatorname{diag}(1,-1,-1,-1)$ |
| (g) | the eight matrices $\pm L_{\mathrm{axf},e_\mu}$ are the quaternion group $Q_8$ |
| (h) | a cyclic relabelling of the three directions conjugates every matrix by a permutation matrix |
| (i) | the real slice is preserved: $\mathbb{H}\subset\mathbb{B}$ lands in $M_4(\mathbb{R})$ |
| (j) | $\det L_{\mathrm{axf},e_\mu}=1$ and $2\,\mathrm{Sc}L_{\mathrm{axf},e_\mu}=4\delta_{\mu t}$ |

**Ten readings of one fact.** Properties (b) and (d) are the root: the basis is multiplicative, so each column of a matrix is a signed basis vector. The rest follow, and each of them is a property of this frame and not of the algebra.

### The Stitch

**The right matrix is the transposed left one between $D$ and its inverse.**

$$
R_{\mathrm{axf}}(\tilde Q)=D\,L_{\mathrm{axf}}(\tilde Q)^{\mathsf T}D,
\qquad
R_{\mathrm{axf}}(\tilde Q)_{\mu\nu}=s_\mu s_\nu\,L_{\mathrm{axf}}(\tilde Q)_{\nu\mu},
\qquad s_t=1,\quad s_x=s_y=s_z=-1 .
$$

**$D$ is three objects in one.** It is the switch, it is the Gram matrix of the symmetric form $\beta(\tilde X,\tilde Y)=\operatorname{Sc}(\tilde X\tilde Y)$, and it is the matrix of the quaternion conjugation in this basis.

**Two identities follow and they are the reason the frame is used.** The transpose is the quaternion conjugation and the dagger is the Hermitian conjugation,

$$
L_{\mathrm{axf}}(\tilde Q)^{\mathsf T}=L_{\mathrm{axf}}(\tilde Q^{\natural}),\qquad
L_{\mathrm{axf}}(\tilde Q)^{\dagger}=L_{\mathrm{axf}}(\tilde Q^{*}).
$$

In a general frame the transpose of a left matrix is a conjugate of a right matrix, $L^{\mathsf T}=\mathsf W R\mathsf W^{-1}$, so both identities are properties of this basis and not of the algebra.

### The Invariants

$$
2\,\mathrm{Sc}L_{\mathrm{axf}}(\tilde Q)=4Q_t,\qquad
\det L_{\mathrm{axf}}(\tilde Q)=\langle\tilde Q\rangle_{\natural}^{2}=N^{2},
$$

$$
\chi(\lambda)=\bigl((\lambda-Q_t)^2+B^2\bigr)^{2},\qquad
\operatorname{spec}=\{Q_t+iB,\ Q_t-iB\}\ \text{each twice},\qquad B^2=Q_x^2+Q_y^2+Q_z^2 .
$$

**The rank is even.** It is twice the rank of the $2\times2$ image, hence $0$, $2$ or $4$; a matrix of rank one or three is a general matrix of the ambient and not the left matrix of any element.

### The Four Norms

**Each is the quarter-trace of one word in the array.** The quarter is the price of the block: a quadratic word in the $4\times4$ matrix carries four times its $2\times2$ value.

| norm | algebra value | matrix formula | value ring | definite |
| --- | --- | --- | --- | --- |
| plain $P$ | $Q_t^2-B^2$ | $\tfrac142\,\mathrm{Sc}(M^2)$ | $\mathbb{C}$ | no |
| quaternionic $N$ | $Q_t^2+B^2$ | $\tfrac14\operatorname{Tr}(M^{\mathsf T}M)$ | $\mathbb{C}$ | no |
| Hermitian $H$ | $\sum_\mu\lvert Q_\mu\rvert^2$ | $\tfrac142\,\mathrm{Sc}(M^{\dagger}M)$ | $\mathbb{R}$ | yes |
| Krein $K$ | $\lvert Q_t\rvert^2-\sum_k\lvert Q_k\rvert^2$ | $\tfrac14\operatorname{Tr}(M^{\mathsf T}M^{\dagger})$ | $\mathbb{R}$ | no |

**The second and the fourth rows use the transpose identity,** $M^{\mathsf T}=M^{\natural}$, and that identity is a property of this basis. In another frame the words have to be written with the conjugation, and $\tfrac14\operatorname{Tr}(M^{\mathsf T}M)$ is then none of the four norms.

### The Six Subspaces

**The four conjugations become four entrywise conditions.**

| subspace | condition on $\tilde Q$ | condition on $M$ | real dim. |
| --- | --- | --- | --- |
| $\mathbb{B}_{C}$ | $\tilde Q^{\natural}=\tilde Q$ | $M=\lambda\mathrm I_4$ | $2$ |
| $\mathbb{B}_{V}$ | $\tilde Q^{\natural}=-\tilde Q$ | $\operatorname{Tr}M=0$, equivalently $M^{\mathsf T}=-M$ | $6$ |
| $\mathbb{B}_{H}$ | $\overline{\tilde Q}=\tilde Q$ | $M=\overline M$ | $4$ |
| $\mathbb{B}_{iH}$ | $\overline{\tilde Q}=-\tilde Q$ | $M=-\overline M$ | $4$ |
| $\mathbb{B}_{\Psi}$ | $\tilde Q^{*}=\tilde Q$ | $M=M^{\dagger}$ | $4$ |
| $\mathbb{B}_{\Phi}$ | $\tilde Q^{\flat}=\tilde Q$ | $M=-M^{\dagger}$ | $4$ |

**The vector condition is one condition here and two in the ambient.** Inside the image the trace condition and the antisymmetry coincide, because the transpose is the quaternion conjugation and $\tilde Q^{\natural}=-\tilde Q$ exactly when $Q_t=0$.

**The closure is not uniform.** The centre and the quaternion subspace are subalgebras; the vector subspace is a Lie subalgebra under the commutator; the anti-quaternion subspace and the two Hermitian subspaces are neither.

### The Uniqueness

**No other basis keeps the sparsity.** Let $\mathcal{F}$ be a basis in which all sixteen matrices of the four units are signed permutations. Then, after relabelling the indices,

$$
f_t=\pm e_t,\qquad f_k=\pm e_{\sigma(k)}\ (k=x,y,z),\qquad \sigma\in S_3 .
$$

**The count is $3!\cdot2^{4}=96$** with the scalar unit in the first slot, $3!\cdot2^{3}=48$ if the scalar unit is also fixed at $+e_t$, and $4!\cdot2^{4}=384$ if the four slots are free. So the sparse frames are the axis-free basis up to a permutation of the three directions and a sign on each vector, and the sparsity is a name for the frame rather than a coincidence of it.

## The Operator Behind the Array

### The Operator Is Frame-Free

**Left multiplication is defined by the product alone.**

$$
\rho_L(\tilde Q)(\tilde X)=\tilde Q\tilde X .
$$

No basis enters the definition, no array appears in it, and the map is the same linear map of $\mathbb{B}$ in every frame. The same holds for $\rho_R$ and for every two-sided operator $L_aR_b$.

### The Array Is a Class

**A change of frame conjugates the array.**

$$
L_{\mathcal{F}'}(\tilde Q)=\mathsf C^{-1}L_{\mathrm{axf}}(\tilde Q)\,\mathsf C,\qquad
R_{\mathcal{F}'}(\tilde Q)=\mathsf C^{-1}R_{\mathrm{axf}}(\tilde Q)\,\mathsf C,\qquad
\mathsf W_{\mathcal{F}'}=\mathsf C^{\mathsf T}D\,\mathsf C .
$$

So the matrices of one element over all frames are one conjugacy class and not one matrix. The trace, the determinant, the characteristic polynomial, the spectrum and the rank are class functions; the entries, the sparsity, the subring and the two identities of §*The Stitch* are not.

### The Canonical Representative

**Inside the class this frame is the representative that adds nothing.** The operator is unique, the matrix is a class, and the axis-free family is the member of the class in which the structure constants are read off the display.

**The trade is a trade in the subring.** A real change of frame whose matrix leaves $\mathbb{Z}$ costs the integers first, and with them the sparsity, the orthogonality, the real diagonal stitch, and the transpose identity that goes with it. What survives every frame is the operator.

## The Interpretations

### I.2.a — No Spatial Direction Is Chosen, and Time Is Distinguished by a Sign

**Read:** the display carries the asymmetry the algebra has and invents no other.

**The three vector units enter by one rule.** The $\nu$-th column is the product with the $\nu$-th unit, and the three vector columns are produced from the same table by the same substitution. No coefficient is singled out by its position: $Q_x$, $Q_y$ and $Q_z$ appear with one sign each and no sum, in the same shape.

**The symmetry of the display is the cyclic one.** The relabelling $x\mapsto y\mapsto z\mapsto x$ is an algebra automorphism, and its permutation matrix conjugates every array into itself. A transposition reverses the orientation and flips the sign of the table, because $\vec e_x\vec e_y=\vec e_z$ becomes $\vec e_y\vec e_x=-\vec e_z$. That sign belongs to the quaternion product and not to a preference of the basis.

**Time is different, and the difference is in the object.** The signs are carried by the squares, $e_t^2=+e_t$ and $\vec e_\eta^2=-e_t$, and the display inherits it without a sentence: the scalar unit occupies the first slot and the trace is $4\delta_{\mu t}$. Physical space is isotropic and spacetime is not, and the array shows the first as a symmetry of the entries and the second as a sign.

**The boundary.** This is a statement about a frame and not about a canonical basis. The axis-free family is one representative of a conjugacy class, and nothing in the physics selects it; what it does is decline to add a direction the algebra does not contain.

### I.2.b — The Entries Are the Multiplication Table Read Aloud

**Read:** the display of the algebra is the multiplication of the algebra, written as an array, and a check of an identity is an integer check.

**The columns are products.** $L_{\mathrm{axf}}(\tilde Q)$ has the coordinate column of $\tilde Q$ in its first place and the coordinate columns of $\tilde Q\vec e_x$, $\tilde Q\vec e_y$, $\tilde Q\vec e_z$ after it. Each of the three is the same table read from another column. Nothing is rescaled, nothing is rotated and no change of basis intervenes.

**The consequence is that a sign error is visible.** An identity between elements becomes an identity between integer arrays of the four units, and a wrong sign shows as a wrong entry in a place where the table says $\pm1$. In a display whose entries are in $\mathbb{Z}[i]$ and are the table conjugated by a dense matrix, the same error is a wrong complex number inside a sum, and the table has to be reconstructed before it can be checked.

**The boundary.** The entries are the table for the units and the coefficients for a general element. The reading is about legibility, not about content: the product is the same product in every frame.

### I.2.c — The Trace Is the Clock and the Traceless Part Is the Motion

**Read:** the trace sees the scalar part only, and the scalar-free part of the image is the vector part.

$$
2\,\mathrm{Sc}L_{\mathrm{axf}}(\tilde Q)=4Q_t,\qquad 2\,\mathrm{Sc}M=0\iff\tilde Q\in\mathbb{B}_{V} .
$$

**The split is exact and it is the scalar–vector split in the image.** The trace is additive, bilinear and blind to everything except $Q_t$; the traceless remainder carries the three directions. In this basis the traceless image is also the antisymmetric one, $M^{\mathsf T}=-M$, so inside the image the trace condition and the antisymmetry are one condition.

**The physical reading is the scalar–vector reading in matrix form.** The scalar part is the complex time, so the trace is the clock; the vector part is the three directions, so the traceless part is the motion. A matrix statement about a biquaternion that uses only the trace is a statement about time, and it cannot see a direction.

**The boundary.** The factor four is the dimension of the regular module, and the factor two at size two is the dimension of the spinor module. Neither is a physical factor, and both are the origin of the factor-of-two errors that occur in computations which change size without saying so.

### I.2.d — The Determinant Is One Function with Three Readings

**Read:** the determinant is the norm, and the norm is read differently on three real slices.

| slice | determinant at size two | reading |
| --- | --- | --- |
| material $\mathbb{B}_{\Phi}$ | $-(q'_t)^2+\lvert\vec q\rvert^2$ | the interval |
| informational $\mathbb{B}_{\Psi}$ | $q_t^2-\lvert\vec q'\rvert^2$ | the causal type |
| unit-weight state | $\tfrac14(1-\lvert\vec r\rvert^2)$ | the mixedness |

**One zero set, three meanings.** The determinant vanishes on the light cone, on the boundary of the state space and on the set of pure states, and these are three descriptions of one locus in three slices. Purity is affine in the determinant on the unit-weight slice.

**Invertibility becomes a determinant.** An element is invertible exactly when $N\neq0$, so in the image an invertible element is a matrix of non-zero determinant and the cone of zero divisors is the vanishing set of the determinant. At size four the determinant is $N^2$ and the zero set is unchanged.

**The boundary.** These are three restrictions of one function to three real slices, not three quantities. A statement about the determinant must say which slice it is on, or it will read an interval as a probability weight.

### I.2.e — The Determinant Is a Volume, and an Interval Is Not

**Read:** multiplication by $\mathsf M$ is a real-linear map of $\mathbb{C}^2\cong\mathbb{R}^4$, and its real determinant is $\lvert\det\mathsf M\rvert^2$.

**On the unit-norm slice the map is volume preserving.** There $\det\mathsf M=1$, the real determinant is one, and the group is $SL_2(\mathbb{C})$. Volume preservation is a property of the transformation and it holds for every element of the group.

**The two readings agree only in the zero set.** The volume is the volume of the realification of the module; the interval is the interval of the material sector. They vanish together because both are built from the same determinant, and elsewhere they are different functions of the same four numbers.

**The boundary.** A volume in the module and a volume in spacetime are different objects with one algebraic ancestor. An argument that transfers a volume-preservation statement to a spacetime volume transfers a statement between two different realifications.

### I.2.f — The Six Subspaces Are Four Entrywise Conditions

**Read:** the four conjugations of the algebra are the entrywise bar, the transpose, the dagger and minus the dagger of one array, and each of the six subspaces is a fixed or anti-fixed space of one of them.

**The dictionary is exact on the image and only on the image.** The real matrices, the Hermitian matrices and the anti-Hermitian matrices each form a real space of dimension sixteen in the ambient; the image selects four dimensions inside each. A condition stated on the image is a statement about the image and not about matrix theory.

**That the transpose is the quaternion conjugation is what makes the list short.** In another frame the same conjugation is a transpose conjugated by a fixed matrix, and the entrywise condition becomes a condition with a matrix in the middle. Here the four words of the algebra are four words of the array, and a reader can see which subspace he is in by looking at the entries.

**The boundary.** The four conditions are four words in the matrix, and which word a conjugation becomes depends on the frame. A formula that uses the transpose silently assumes the basis.

### I.2.g — The Transpose Is the Conjugation, So Two Adjoints Need No Frame

**Read:** the two conjugations the physics uses — the quaternionic and the Hermitian — are the transpose and the dagger of the same array, and neither needs a matrix to declare it.

$$
L_{\mathrm{axf}}(\tilde Q)^{\mathsf T}=L_{\mathrm{axf}}(\tilde Q^{\natural}),\qquad
L_{\mathrm{axf}}(\tilde Q)^{\dagger}=L_{\mathrm{axf}}(\tilde Q^{*}).
$$

**The gain is that a pairing is visible.** The quaternionic conjugation is the pairing the norm $N$ uses, and the Hermitian one is the pairing the norm $H$ uses; both are operations on the array itself, of one letter each, with no conjugating matrix between them. In a display where the transpose of the array is a conjugate of the right family, the same two operations have to be assembled from three matrices, and the assembly is where a sign goes missing.

**The boundary.** The identities are properties of this frame, not of the algebra, and the pairings themselves are extra data. The Dirac adjoint is not an operator on the element at all but a pairing of two elements, so no frame supplies it and no array displays it.

### I.2.h — The Array Is a Class, and Its Frame Is Visible in It

**Read:** an element has one operator and many matrices, and the frame of a printed matrix can be recovered from the matrix itself.

**A change of frame is a conjugation, and it leaves the invariants alone.** The trace, the determinant, the spectrum and the rank are the same in all frames; the entries, the sparsity and the transpose identity are not. A quantity that moves with the frame is a fact about the display.

**The uniqueness statement is what makes the frame readable.** Among all bases the signed-permutation ones are the $96$ relatives of this one, so a reader who sees integer entries and a $Q_8$ of units knows the frame without being told. That is the diagnostic value of the display: the frame is not declared in a sentence that can be lost, it is visible in the entries.

**The boundary.** The frame is canonical in this precise sense only. It is not the frame the algebra prefers, and it does not make a computation right that would otherwise be wrong; it makes the frame of a computation legible.

## The Limits

**The entry reads one family and not the algebra.** It states what the axis-free display is worth and what it costs. The Peirce display, the root, the idempotents and the compression at size two belong to *The Pauli and Gamma Matrices: the Direction in the Display*, and the argument that the corpus should display in this basis belongs to *Why AXF Matrices instead of Pauli and Gamma Matrices*.

**The entry does not read the spectrum.** The eigenvalue pair is named because the matrix invariants carry it, and the spectral theory is the subject of its own entry. What is established here is only that the pair is the same at both sizes and that the multiplicity is the module's dimension.

**The ten properties are properties of the frame.** Every one of them changes under a general change of basis, and none is a symmetry of the algebra. Their content is that one representative of the class has all ten at once.

**No factor in this entry is physical.** The factors two, four and the quarter are the dimensions of the spinor and the regular modules and the price of the block. They are exact, they are unavoidable, and they are not measurements.

## Summary

- The AXF matrices are the family of left and right matrices in the coefficient basis, whose vectors are the four units.
- Its columns are products: the $\nu$-th column of the left matrix is the coordinate column of $\tilde Qe_\nu$, so the array is the multiplication table read aloud.
- Ten properties hold at once: integer entries, signed permutations, orthogonality, entries equal to the structure constants, the transpose as the quaternion conjugation, a real diagonal stitch, the quaternion group on $\mathbb{R}^4$, cyclic symmetry, the real slice preserved, determinant one and trace $4\delta_{\mu t}$.
- The stitch is $R=DL^{\mathsf T}D$ with $D=\operatorname{diag}(1,-1,-1,-1)$, which is at once the switch, the Gram matrix of $\beta$ and the matrix of the quaternion conjugation.
- The invariants are $4Q_t$, $N^2$, the squared characteristic polynomial and a spectrum of two modes counted twice; the rank is even.
- The four norms are the four quarter-traces, and two of them use the transpose identity, which is a property of this basis.
- The six subspaces are four entrywise conditions, and the vector subspace is traceless and antisymmetric by one condition.
- No other basis keeps the sparsity: the signed-permutation frames are the $96$ relabellings and sign changes of this one.
- The operator is unique and the array is a conjugacy class; this frame is the representative that adds nothing, and the frame of a printed matrix can be read off its entries.
- The display chooses no spatial direction, and it carries the sign pattern as a sign rather than as a sentence.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)$ | the coefficient basis, called AXF in this entry |
| $\mathrm{axf}$ | the label of the family, $L_{\mathrm{axf}}$ and $R_{\mathrm{axf}}$ |
| $L_{\mathrm{axf}}(\tilde Q)$, $R_{\mathrm{axf}}(\tilde Q)$ | the left and right matrices of $\tilde Q$ |
| $L_{\mathrm{axf},e_\mu}$, $R_{\mathrm{axf},e_\mu}$ | the left and right matrices of the four units |
| $\mathbb{B}_L$, $\mathbb{B}_R$ | the two four-dimensional families inside $M_4(\mathbb{C})$ |
| $\varepsilon_{\mu\nu}^{\ \ \rho}$ | the structure constants, the multiplication table of the units |
| $D=\operatorname{diag}(1,-1,-1,-1)$ | the stitch, the Gram matrix of $\beta$, the matrix of $\natural$ |
| $s_\mu$ | the sign of $e_\mu^{\natural}=s_\mu e_\mu$ |
| $\mathsf C$ | the matrix of a change of frame |
| $\mathsf W$ | the switch of a general frame, $\mathsf W'=\mathsf C^{\mathsf T}D\mathsf C$ |
| $N=\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ | the quaternionic norm |
| $B^2$ | $Q_x^2+Q_y^2+Q_z^2$ |
| $q_\mu$, $q'_\mu$ | the real and imaginary parts of $Q_\mu$ |
| $P$, $N$, $H$, $K$ | the four norms, as quarter-traces of the four words |

## Further Reading

- [$M_4(\mathbb{C})$ Axis-Free Representation](../articles_maths/m4c-axis-free-representation.html), for the basis, the two families, the ten properties and the uniqueness.
- [Families of Matrix Representations](../articles_maths/families-of-matrix-representations.html), for the two families in a general frame and the change of frame.
- [Subspaces and Decompositions of the Biquaternion Algebra](../articles_maths/subspaces-and-decompositions-of-the-biquaternion-algebra.html), for the six subspaces and the three decompositions.
- [Matrix Representations Conventions](../articles_maths/matrix-representations-conventions.html), for the naming of the basis and of the family.
- [The Pauli and Gamma Matrices: the Direction in the Display](the-pauli-and-gamma-matrices-the-direction-in-the-display.html), for the Peirce display, the gamma frame and what those displays print.
- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the argument that this basis is the one to display in.
- [The Operators of the Algebra](the-operators-of-the-algebra.html), for the two-sided operators, the five pictures and the mass coupling at operator level.
- [The Four Forms and the Four Norms](the-four-forms-and-the-four-norms.html), for the four norms in the algebra rather than in the array.
