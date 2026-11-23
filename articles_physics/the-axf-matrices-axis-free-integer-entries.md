# __The AXF Matrices: Axis-Free, Integer Entries__

## Introduction

**This entry reads the AXF matrices of the biquaternion algebra.** The label $\mathrm{axf}$ is short for *axis-free*: it names the family built in the coefficient basis, whose four vectors are the four units themselves, and it names the one thing the display does not do, which is to choose a direction. The label is a name in lowercase roman letters and not an exponent.

**Two claims, and the second is the strong one.** The first is that in this basis the sixteen arrays of the four units are signed permutations with entries in $\{0,+1,-1\}$, and that ten properties hold at once. The second is that this basis is the only one, up to a relabelling of the three directions and a sign on each vector, with that sparsity, so the array names its frame instead of the frame naming the array.

**The entry also states what an array is not.** The operator is unique and frame-free; its matrix is one representative of a conjugacy class. Every invariant is read from the operator, and the array is a service to the reader and a diagnostic of the frame.

**Boundaries.** The basis, the two families, the stitch, the ten properties, the uniqueness among sparse frames, the product, the trace, the determinant and the four norms are *$M_4(\mathbb{C})$ Axis-Free Representation*; the general theory of the two families and of the change of frame is *Families of Matrix Representations*; the six subspaces and the three decompositions are *Subspaces and Decompositions of the Biquaternion Algebra*. The Peirce display — the root, the idempotents, the tensor product and the compression at size two — is *The Pauli Pair and the Gamma Frame: Which Statements Survive Conjugation*, and why the corpus displays in this basis rather than in one of those is §*Why the Pauli and the Gamma Displays Are Refused* below, which absorbs the entry formerly titled *The AXF Matrices: Axis-Free, Integer Entries*, §*Why the Pauli and the Gamma Displays Are Refused*. The spectrum is named here because the matrix invariants carry it, and it is read in *The Spectrum and the Two Modes*. No dynamics, no Clifford algebra and no gamma matrix appears below.

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
| unit-weight state | $\tfrac14(1-\lvert\vec s_{\Psi}\rvert^2)$ | the mixedness |

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

## Why the Pauli and the Gamma Displays Are Refused

**The array is one choice among many, and the corpus refuses two of the others on a stated ground.** The Pauli display and the gamma display both carry a spatial direction inside the notation: one entry of one matrix is diagonal by privilege, and every construction that reads a root from the display inherits that direction. The section below states the defect, checks that no relabelling removes it, and records what survives a change of display. It is the argument for the frame used above; the construction itself is §*The Operator Behind the Array* and §*The Interpretations*.

### The Direction Inside the Pauli Matrices

#### The Three Matrices

The Pauli matrices are

$$
\sigma_1=\begin{pmatrix}0&1\ 1&0\end{pmatrix},\qquad
\sigma_2=\begin{pmatrix}0&-i\ i&0\end{pmatrix},\qquad
\sigma_3=\begin{pmatrix}1&0\ 0&-1\end{pmatrix}.
$$

Two of them carry $i$ or carry zeros on the diagonal. The third is real and diagonal. That difference is the subject of this section, and it is not a difference between three operators. It is a difference between three positions in a list, produced by the order in which the list was built.

The same asymmetry appears in the two-dimensional image of a general element. The image of $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ is

$$
\mathsf M_2(\tilde Q)=Q_t\,\mathrm I_2-i\bigl(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3\bigr)
=\begin{pmatrix}Q_t-iQ_z&-iQ_x-Q_y\ -iQ_x+Q_y&Q_t+iQ_z\end{pmatrix}.
$$

The diagonal of this matrix carries $Q_t$ and $Q_z$. The off-diagonal carries $Q_x$ and $Q_y$. The trace and the determinant are unaffected — the trace is $2Q_t$ and the determinant is $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ in every display — but the shape of the array is not neutral. It puts one spatial coefficient in the diagonal slots and the other two in the off-diagonal slots, and a reader has no way to learn from the array that this was a decision.

#### Why the Third Matrix Is the Diagonal One

The reason is the construction, not the algebra. The two-dimensional image is left multiplication read on a minimal left ideal, and the ideal is built from an idempotent. The idempotents used are the Peirce idempotents of the root $\vec{Ζ}=i\vec e_z$,

$$
\tilde\Pi_{\mathrm{id},\pm}=\tfrac12\bigl(e_t\pm i\vec e_z\bigr),
$$

with $\tilde\Pi_{\mathrm{id},+}\tilde\Pi_{\mathrm{id},-}=0$ and $\tilde\Pi_{\mathrm{id},++}\tilde\Pi_{\mathrm{id},-}=e_t$. The carrier of the image is $\mathbb{B}\tilde\Pi_{\mathrm{id},+}$, of complex dimension two, and the matrix of $\vec e_z$ on that carrier is diagonal because $\vec e_z$ built the carrier.

The computation is one line. Multiply the idempotent by the unit:

$$
\tilde\Pi_{\mathrm{id},+}\vec e_z=\tfrac12\bigl(\vec e_z+i\vec e_z^2\bigr)=\tfrac12\bigl(\vec e_z-i e_t\bigr)=-i\,\tfrac12\bigl(e_t+i\vec e_z\bigr)=-i\tilde\Pi_{\mathrm{id},+}.
$$

So $\vec e_z$ acts on the ideal as the scalar $-i$, and its array is $-i\sigma_3$: diagonal, with the two eigenvalues $-i$ and $+i$ in the two slots. The other two units permute the two slots, so their arrays are off-diagonal. The root $i\vec e_z$ is the datum the display consumes, and the diagonal of $\sigma_3$ is its footprint.

Nothing forced $\vec e_z$. The same construction runs on $\vec e_x$ or on $\vec e_y$, with the idempotents $\tfrac12(e_t\pm i\vec e_x)$ and $\tfrac12(e_t\pm i\vec e_y)$, and produces a triplet whose diagonal member is the unit used. The algebra has three interchangeable spatial units, and the display needs exactly one of them.

#### The Direction in the Four-Dimensional Array

The four-dimensional Pauli array of the same element is the two-dimensional image in both slots, because left multiplication does not mix the two Peirce components:

$$
L_{\mathrm{pau}}(\tilde Q)=\mathrm I_2\otimes\mathsf M_2(\tilde Q).
$$

The arrays of the four units show the direction twice. The time unit is the identity, the $\vec e_z$ array is diagonal, and the other two are off-diagonal inside each of the two identical blocks:

$$
L_{\mathrm{pau},e_t}=\mathrm I_4,\qquad
L_{\mathrm{pau},\vec e_z}=\begin{pmatrix}-i&0&0&0\ 0&i&0&0\ 0&0&-i&0\ 0&0&0&i\end{pmatrix},
$$

$$
L_{\mathrm{pau},\vec e_x}=\begin{pmatrix}0&-i&0&0\ -i&0&0&0\ 0&0&0&-i\ 0&0&-i&0\end{pmatrix},\qquad
L_{\mathrm{pau},\vec e_y}=\begin{pmatrix}0&-1&0&0\ 1&0&0&0\ 0&0&0&-1\ 0&0&1&0\end{pmatrix}.
$$

Three statements follow, and each is a statement about the page and not about the algebra.

Exactly one of the three spatial units is diagonal. A triplet with this shape cannot be written without deciding which unit it is, because the shape of the list — one diagonal member, two off-diagonal members — is what a triplet of this kind is. The decision is made at the moment the arrays are written, and it is made silently.

The diagonal unit appears twice, once in each block. The repetition is not an accident of the layout; it is $\mathrm I_2\otimes\cdot$, the statement that the frame was built from a root and that the root appears in both slots.

The two remaining spatial units carry the same weight. No entry distinguishes $\vec e_x$ from $\vec e_y$, which is correct, because no entry should. The asymmetry is therefore exactly one-against-two, and it sits in the diagonal.

#### The Diagonal Operators Tell the Same Story
The same fact can be stated without writing a single array, and the statement is the one used later.

A basis operator is diagonal in a basis when it sends each basis vector to a multiple of itself. In the coefficient basis the diagonal basis operators are the four squares, $e_te_t$, $\vec e_x\vec e_x$, $\vec e_y\vec e_y$ and $\vec e_z\vec e_z$: the square of an invertible element is a scalar, so it multiplies every basis vector by that scalar. No other basis operator is diagonal, because a basis operator with two different slots multiplies an invertible element by a different unit.

In the Pauli display the diagonal basis operators are four others. They are $e_te_t$, $e_t\vec e_z$, $\vec e_ze_t$ and $\vec e_z\vec e_z$: both slots take their value from the pair $\{e_t,\vec e_z\}$. The declared unit appears twice, and the two other spatial units appear in no diagonal basis operator at all.

| basis | basis operators that are diagonal |
|---|---|
| the four units, in any order of the three spatial units | $e_te_t$, $\vec e_x\vec e_x$, $\vec e_y\vec e_y$, $\vec e_z\vec e_z$ |
| a frame built on the unit $u$ | $e_te_t$, $e_tu$, $ue_t$, $uu$ |

The second row was verified for $u=\vec e_x$, $u=\vec e_y$ and $u=\vec e_z$: in each case the diagonal set is the four basis operators named, and no other. The pattern is therefore not a property of $\vec e_z$. It is the mark of a frame built on any declared unit, and it moves when the declared unit moves.

A reader who can see which basis operators are diagonal can read the hidden unit off the page. That is the compensation the Pauli display offers, and it is a real one. The information is present; it is simply never stated, and it is carried by a list of four products rather than by a sentence.

#### What the Direction Carries

The direction does not stay in the triplet. It is inherited by every construction built from the root, and the inheritance is mechanical: whatever is built from $\vec e_z$ carries $\vec e_z$. Each item below is a place where a reader meets the choice without being told.

The root. The Peirce frame is the frame of the root $\vec{Ζ}=i\vec e_z$, of square $e_t$. The root is the choice, named or not.

The idempotents. $\tilde\Pi_{\mathrm{id},\pm}=\tfrac12(e_t\pm i\vec e_z)$. The unit appears inside both, with opposite signs.

The mixed units. $\vec\Pi_{\mathrm{nil},\pm}=\tfrac12(i\vec e_x\pm\vec e_y)$. The two remaining spatial units are consumed here, and consumed in an order: $\vec e_x$ multiplied by $i$ comes first, $\vec e_y$ second. The pair $(\vec e_x,\vec e_y)$ is no longer a set; it is an ordered pair, and its orientation is part of the frame.

The Peirce decomposition. The four components are read in the order $(\tilde\Pi_{\mathrm{id},+},\vec\Pi_{\mathrm{nil},+},\vec\Pi_{\mathrm{nil},-},\tilde\Pi_{\mathrm{id},-})$, which is a second choice, independent of the first: the two middle slots can be exchanged.

The adapted basis and its scale. The mixed units are defined only up to $\vec\Pi_{\mathrm{nil},+}\mapsto\lambda\vec\Pi_{\mathrm{nil},+}$ and $\vec\Pi_{\mathrm{nil},-}\mapsto\lambda^{-1}\vec\Pi_{\mathrm{nil},-}$, so the frame carries a free nonzero scalar as well. The scale is harmless for the algebra and fatal for a display that pretends to be unique.

The minimal left ideal. $\mathbb{B}\tilde\Pi_{\mathrm{id},+}$ is the two-dimensional carrier of the older literature. It is built from the unit, and it is the idempotent of the unit that selects it.

The projector and the block split. The projector $\tfrac12(\mathrm I-\gamma_5[\mathbb{B}_{\Phi}])$ has rank two and its range is the ideal $\mathbb{B}\tilde\Pi_{\mathrm{id},+}$. The four-dimensional array is $\mathrm I_2\otimes\mathsf M_2(\tilde Q)$: two identical blocks, and the split of the array is the split of the ideal, written twice.

The two-component column, and the spinor. A column of two components is an element of the ideal written in the basis $(\tilde\Pi_{\mathrm{id},+},i\tilde\Pi_{\mathrm{id},+})$, and the spinor of the older literature is that column. This is a consequence of the frame and not of the algebra: a state is an element of $\mathbb{B}$, which needs no ideal, no column and no frame, and it becomes a column only after the ideal has been chosen. The column is the most consequential item of the list, because a whole literature is written in it.

The gamma frame. In the five gammas the unit $\vec e_y$ is the common right multiplier of the spatial three, and $\vec e_z$ is the axis of the fifth basis operator. Neither fact is stated anywhere on a page that prints the five matrices.

The Dirac adjoint. The adjoint $\tilde{Ξ}^{\dagger}\gamma_0[\mathbb{B}_{\Phi}]$ needs a chosen time generator. It is a statement about a pairing, and the pairing imports the frame.

The charge conjugation. The basis operator $C=L_{e_t}R_{\vec e_x}$ serves as the charge conjugation of the reference frame, with $C^2=-1$. That this one basis operator serves is a fact of the frame; which basis operator it is, is a choice.

The third component of spin. A triplet whose third member is diagonal makes $\sigma_3$ the distinguished one, and every later sentence that measures "the third component" inherits the distinction.

The sentences. "The third member is the diagonal one." "The upper half of the column is the left part." "The diagonal member is the energy." Each is true in the frame that produced it, false in a rotated one, and printed in the same font as the identities that hold everywhere.

| object | the direction it carries | what happens on a relabelling of the spatial units |
|---|---|---|
| the root $i\vec e_z$ | the unit $\vec e_z$ | the root becomes another root |
| the idempotents $\tilde\Pi_{\mathrm{id},\pm}$ | the unit $\vec e_z$, twice, with opposite signs | the idempotents change |
| the mixed units $\vec\Pi_{\mathrm{nil},\pm}$ | the ordered pair $(\vec e_x,\vec e_y)$ | the pair changes, and the orientation with it |
| the Peirce decomposition | the order of the four components | the two middle slots exchange |
| the minimal left ideal | the idempotent of the unit | a different ideal |
| the two-component column, and the spinor | the basis of that ideal | a different column |
| the block split | the split of the ideal, twice | a different block split |
| the gamma set | $\vec e_y$ as the common right multiplier, $\vec e_z$ as the axis of the fifth basis operator | a different five-element set |
| the Dirac adjoint | the chosen time generator $\gamma_0[\mathbb{B}_{\Phi}]$ | a different $\gamma_0[\mathbb{B}_{\Phi}]$ |
| the charge conjugation | the basis operator $L_{e_t}R_{\vec e_x}$ | a different basis operator |
| the third component of spin | the diagonal member of the triplet | the diagonal moves |

### The Direction Inside the Gamma Matrices

#### The Five Basis Operators
The gamma set is five basis operators of the operator algebra:

$$
\gamma_0[\mathbb{B}_{\Phi}]=iR_{\vec e_x},\qquad
\gamma_1[\mathbb{B}_{\Phi}]=iL_{\vec e_x}R_{\vec e_y},\qquad
\gamma_2[\mathbb{B}_{\Phi}]=iL_{\vec e_y}R_{\vec e_y},\qquad
\gamma_3[\mathbb{B}_{\Phi}]=iL_{\vec e_z}R_{\vec e_y},\qquad
\gamma_5[\mathbb{B}_{\Phi}]=-iR_{\vec e_z}.
$$

The frame is named in brackets and it is $\mathbb{B}_{\Phi}$ throughout this article; below the label is dropped, and every $\gamma_\mu[\mathbb{B}_{\Phi}]$ is $\gamma_\mu[\mathbb{B}_{\Phi}]$. Two of the five are single multipliers, because $L_{e_t}$ is the identity of the operator algebra: $e_t$ is the unit of $\mathbb{B}$. The five satisfy the basis operator relation of that frame, with $\delta_{\mu\nu}=(1,1,1,1)$ the unit metric,

$$
\{\gamma_\mu[\mathbb{B}_{\Phi}],\gamma_\nu[\mathbb{B}_{\Phi}]\}=2\varepsilon_\mu\delta_{\mu\nu}\,\mathrm I_4,\qquad
\varepsilon=(1,-1,-1,-1),$$

so that $\gamma_0[\mathbb{B}_{\Phi}]^2=+\mathrm I_4$ and $\gamma_\eta[\mathbb{B}_{\Phi}]^2=-\mathrm I_4$; their product is the fifth, $\gamma_5[\mathbb{B}_{\Phi}]=i\gamma_0[\mathbb{B}_{\Phi}]\gamma_1[\mathbb{B}_{\Phi}]\gamma_2[\mathbb{B}_{\Phi}]\gamma_3[\mathbb{B}_{\Phi}]$, with $\gamma_5[\mathbb{B}_{\Phi}]^2=\mathrm I_4$. All of this was verified on the arrays.

In the Pauli display of the previous section the five become

$$
\gamma_0[\mathbb{B}_{\Phi}]=\begin{pmatrix}0&\mathrm I_2\ \mathrm I_2&0\end{pmatrix},\qquad
\gamma_\eta[\mathbb{B}_{\Phi}]=\begin{pmatrix}0&\sigma_\eta\ -\sigma_\eta&0\end{pmatrix},\qquad
\gamma_5[\mathbb{B}_{\Phi}]=\begin{pmatrix}-\mathrm I_2&0\ 0&\mathrm I_2\end{pmatrix}.
$$

This is the block form that the Peirce frame produces. It is not a form chosen afterwards, and that is the point of the section.

#### The Three Spatial Units Have Three Different Jobs

In the five basis operators the three spatial units are not interchangeable, and the asymmetry is visible in the definitions.

The unit $\vec e_x$ is the right multiplier of the time gamma, and it is also the left multiplier of the first spatial gamma.

The unit $\vec e_y$ is the common right multiplier of all three spatial gammas. That is what makes the three spatial terms of the Dirac operator combine into one term, as shown below.

The unit $\vec e_z$ is never the right multiplier of a spatial gamma. It appears once, as the axis of the fifth basis operator, and it is the only unit that does.

#### The Relabelling Test

The test is a relabelling. Take the five definitions and permute the names $x,y,z$ among the units. For the permutation that sends $\vec e_x\to\vec e_y$, $\vec e_y\to\vec e_z$ and $\vec e_z\to\vec e_x$, the five basis operators become

$$
iR_{\vec e_y},\qquad iL_{\vec e_y}R_{\vec e_z},\qquad iL_{\vec e_z}R_{\vec e_z},\qquad iL_{\vec e_x}R_{\vec e_z},\qquad -iR_{\vec e_x},
$$

which is not the original set. The same failure occurs for all five non-trivial permutations, as checked on the basis operators. So the gamma set is tied to a labelling of the spatial units, and a relabelling produces a different frame, related to the first by a conjugation.

The distinction is worth stating exactly, because it is easy to overstate. The Clifford relations are invariant: the relabelled basis operators satisfy the same relations with the same metric, because a permutation of the three spatial units is an automorphism of the algebra and leaves the metric alone. What is not invariant is the set of five. The metric cannot tell the three units apart, and the five-basis operator list can.

#### Every Gamma Display Writes One Direction

The choice cannot be removed by choosing a better gamma basis, and the reason is a one-line argument.

Suppose a display made both $\gamma_0[\mathbb{B}_{\Phi}]$ and $\gamma_5[\mathbb{B}_{\Phi}]$ diagonal. Both are invertible, so their diagonal entries are nonzero. They anticommute, and two diagonal matrices anticommute only if the entrywise product of their diagonals vanishes in every slot. That product vanishes, so $\gamma_0[\mathbb{B}_{\Phi}]\gamma_5[\mathbb{B}_{\Phi}]=0$, which contradicts invertibility. Hence at most one of the two is diagonal.

The two standard displays are the two ways of spending that one allowance. The Dirac display makes $\gamma_0[\mathbb{B}_{\Phi}]$ diagonal and $\gamma_5[\mathbb{B}_{\Phi}]$ off-diagonal: it writes the time direction, which the plain weight does distinguish, into the array. The block display, and the Pauli display of this corpus, makes $\gamma_5[\mathbb{B}_{\Phi}]$ diagonal and $\gamma_0[\mathbb{B}_{\Phi}]$ off-diagonal: it writes a spatial direction, which the plain weight does not distinguish, into the array. A page that prints gammas has made the choice before it prints anything, and the notation gives the reader no way to tell which choice was made.

#### The Split the Pauli Display Shows

The fifth basis operator is $i$ times a real signed permutation with zeros on the whole diagonal in $\mathrm{axf}$, and it is $\operatorname{diag}(-1,-1,1,1)$ in the Pauli display. Its eigenvalues are $\pm1$ in both, its square is the identity in both, and its trace is zero in both. What changes is whether the array splits into two blocks, and the split is the Peirce split of the same unit.

The projector $\tfrac12(\mathrm I-\gamma_5[\mathbb{B}_{\Phi}])$ is $\operatorname{diag}(1,1,0,0)$ and the projector $\tfrac12(\mathrm I+\gamma_5[\mathbb{B}_{\Phi}])$ is $\operatorname{diag}(0,0,1,1)$, both of rank two. Their ranges are the two left ideals of the frame: the eigenvalue $-1$ holds on $\mathbb{B}\tilde\Pi_{\mathrm{id},+}$ and the eigenvalue $+1$ on $\mathbb{B}\tilde\Pi_{\mathrm{id},-}$, as verified on both ideals. So the block, the left ideal, the two-component column and the projector are one object seen four times, and one choice of unit produces all four.

The three basis operators $-iR_{\vec e_x}$, $-iR_{\vec e_y}$ and $-iR_{\vec e_z}$ are conjugate to one another, and the conjugation is implemented by an operator of the algebra. For $s$ the quarter-turn versor about $\vec e_y$, the conjugation $L_sR_{s^{-1}}$ carries $\vec e_z$ to $\vec e_x$ and carries $-iR_{\vec e_z}$ to $-iR_{\vec e_x}$ exactly. So the choice of which spatial unit carries the fifth basis operator is a labelling, and every labelling gives a split of the same kind. Only one of the three is diagonal in the display, and it is the one the frame was built on.

### Why a Direction in the Notation Is a Defect

#### Physical Space Has No Preferred Spatial Direction

Take any two spatial directions. A rotation of the algebra carries one to the other, and the rotation is an automorphism: it preserves the product, the metric, the trace and the determinant. For $s$ a nonzero versor, the operator $L_sR_{s^{-1}}$ is such an automorphism, and it acts on the invertibles by $u\mapsto sus^{-1}$. The three spatial units are one orbit.

No experiment distinguishes them. A laboratory that is turned by ninety degrees measures the same physics, and the transformation that relates the two descriptions is a symmetry of the theory and not a relabelling of a measurement error. Isotropy is not a convenience of notation; it is a property of space, and it is the reason angular momentum is conserved.

An equation of general physics therefore does not contain a spatial direction. If it did, the direction would have to be supplied by something outside the equation, and the equation would be about a situation rather than about a law. The Dirac operator of a free field, the wave equation, the Maxwell equations and the Klein–Gordon equation all have this property: each is form-invariant under the rotation, and none of them names a direction.

#### The Display Adds a Direction the Equation Does Not Have

A display is a function of a basis. Written in a basis, an operator becomes numbers, and a rotation of the basis becomes a conjugation of the array. The pair (operator, array) is therefore covariant: the operator is fixed and the array moves.

The standard Pauli display breaks the covariance of the page. The array $L_{\mathrm{pau}}(\tilde Q)$ is written in a basis fixed by a root, and the rotation that exchanges $\vec e_z$ with $\vec e_x$ does not produce another array of the same shape: it produces an array in another frame. So the sentence "$\sigma_3$ is diagonal" is not a statement that survives the symmetry. It is a statement about the frame, printed in the grammar of a statement about the algebra.

The defect is not that the display has a direction. The defect is that the direction is unmarked. A sentence $\sigma_3[u]$, with $u$ the axis, would be complete and could be rotated. The sentence $\sigma_3$, with no axis, is incomplete and cannot be rotated, and the notation supplies no place to put the missing name. A formula of general physics is then printed with a datum it does not contain, and the reader has no way to subtract the datum.

#### The Defect Hides Structures, Properties and Correspondences

An unmarked direction does not only add a datum. It also removes one, because whatever depends on the direction is absorbed into the frame and stops being visible. Three examples from the material of this article show the damage.

A physical structure disappears. The three spatial basis operators of the gamma set are one orbit: a conjugation of the algebra carries any one of them to any other, so the statement "these three are one object" is a statement of physics. In the Pauli display the third of them is $\operatorname{diag}(1,-1)$ inside its block and the other two are off-diagonal, so the page shows one member and two others, and the orbit is not on the page. A reader who wants to use the symmetry must first discover that it exists, and the display is what conceals it.

A property of an equation disappears. The axis-free array satisfies $L(\tilde Q)^{\mathsf T}=L(\tilde Q^{\natural})$, so the transpose of the array is again the array of an element, and the adjoint operation is basis-free. In the Pauli display no such rule holds: the transpose of the array is not the array of any conjugation of the element, and the property is not available to a reader who works in that display. It is not that the property is false. It is that the display cannot state it.

A correspondence disappears. The Dirac operator written in the block form and the same operator written in the Dirac form are one operator in two frames, and the matrix that carries one to the other is $C_{\Pi}$. On a page that prints both, the correspondence has to be supplied by a sentence. On a page that prints only one, the other is not visible at all, and two articles that use different conventions look like two different theories.

The pattern is general. A frame that is declared nowhere is a frame nobody can undo, and an object written in it carries the frame in place of the information it displaced.

#### Not Every Frame Is a Defect

The argument would be worthless if it condemned every frame, and it does not. A frame is legitimate whenever the physics supplies one.

A measurement supplies one. A Stern–Gerlach apparatus has an axis, and the axis is in the laboratory, not in the notation. An experiment on a beam has a beam axis. A scattering process has a plane, and the plane has a normal. A background field breaks isotropy, and its direction is part of the solution. In each of these cases a frame is a physical datum, and the correct practice is to name it, use it, and say that the result is about that frame.

The squares of the units supply one, and it is a different kind of direction. Time is distinguished from space by the sign, $e_t^2=e_t$ and $\vec e_\eta^2=-e_t$, and that asymmetry is carried by the units themselves. Every formula inherits it automatically and correctly, with no sentence and no declaration, because it lives in an object and not in a layout. That is the model: an asymmetry that the physics has should be carried by an object of the algebra, where a reader can see it and where it cannot be lost.

The defect is the third case, which is neither of these: a direction that the problem does not supply, that the notation supplies anyway, that is used in every formula of the article, and that is never named.

#### The Test Is Covariance

The test of a displayed statement is mechanical. Apply the automorphism, re-read the statement, and compare.

The statement
$$
\vec e_\eta^2=-e_t
$$
returns itself, with $k$ renamed. It is a fact about $\mathbb{B}$.

The statement
$$
\sigma_3=\operatorname{diag}(1,-1)
$$
does not return itself. Under the exchange of $\vec e_z$ with $\vec e_x$ the diagonal member becomes the first one, and the array is not the array that was printed. It is a fact about the page.

Both are printed as equalities, in the same font, with no marker. The first is true of every direction. The second is true of one direction and false of the other two. A reader who wants to know which kind of statement is in front of him has nothing to consult, and a writer who copies the second into a rotated context produces a formula that is wrong without being detectable as wrong.

#### The Four Things the Reader Loses

The loss is practical, and it can be listed.

He cannot sort. Two statements with the same grammar and different status stand side by side, and nothing in the notation separates the invariant from the frame-dependent one.

He cannot check. Verifying that an equation is rotation-invariant requires seeing how it transforms. In the standard display the transformation is invisible, so the check cannot be done on the page and must be redone from the algebra every time.

He cannot copy. A declaration is local. It is dropped when the formula moves into the next article, into a program as a literal array, or into a comparison with a paper that uses another convention. What travels is the array, and the array carries the direction while the sentence that named it stays behind.

He cannot reuse a proof. A theorem proved for one split of the three units must be reproved for the other two, or shown to be covariant, and the second task is the harder one precisely because the statement was written in a form that hides the transformation.

#### What Is Not Claimed

No computation done in the Pauli or gamma display is wrong. The Clifford relations hold in every display, every trace and every determinant is invariant, and an amplitude computed with gammas is correct. The Dirac equation written with the five gammas is a correct equation, and it is the equation of the literature.

The claim is narrower and it is about the page. A fundamental equation should not be written in a form that privileges a direction the physical reality does not contain, because the privilege then travels with the formula and cannot be distinguished from the physics. The remedy is not a correction of any result. It is a rule of writing: the direction is an object of the sentence, with a name, and it appears only where the construction is the subject.

### The Intrinsic Form

#### The Operator Is a Pair

A matrix display is already a compromise. The object an equation of the corpus names is not an array but an action on an element:

$$
\tilde{Ξ}\longmapsto a\,\tilde{Ξ}\,b.
$$

The pair $(a,b)$ is the operator, written $L_aR_b$ when a name is needed. It carries seven effective parameters rather than eight, because $(a,b)$ and $(\lambda a,\lambda^{-1}b)$ give the same action for any nonzero scalar $\lambda$. No basis appears in the definition, and none appears in the result.

This is the form the physics equations of the corpus take when the equation is the subject and no array is required. Each factor is named, so a reader sees which factor carries the mass, which the momentum and which the grading, and no factor is an entry of a display.

#### Composition and Invariants

Composition is one line, with the second slot reversed because right multiplications compose in the opposite order:

$$
\bigl(L_aR_b\bigr)\bigl(L_cR_d\bigr)=L_{ac}R_{db}.
$$

Powers, inverses and the adjoint follow without a display:

$$
\bigl(L_aR_b\bigr)^n=L_{a^n}R_{b^n},\qquad
\bigl(L_aR_b\bigr)^{-1}=L_{a^{-1}}R_{b^{-1}},\qquad
\bigl(L_aR_b\bigr)^{\approx}=L_bR_a.
$$

The trace and the determinant are read from the multipliers:

$$
2\,\mathrm{Sc}L_aR_b=4\,a_tb_t,\qquad
\det L_aR_b=\bigl\langle a\bigr\rangle_\natural^{2}\bigl\langle b\bigr\rangle_\natural^{2}.
$$

The signs are the squares of the units, and no separate metric is needed:

$$
e_t^2=e_t,\qquad \vec e_\eta^2=-e_t,\qquad
\mathrm{Sc}\bigl(\tilde Q^2\bigr)=Q_t^2-Q_x^2-Q_y^2-Q_z^2.
$$

#### The Carrier Is the Algebra

The intrinsic form takes the carrier to be $\mathbb{B}$ itself, with its own multiplication, so the objects of an equation are elements and their products. Nothing else is introduced: no ideal, no column, no projector, no frame.

Two consequences follow, and both are properties of the algebra rather than of a display.

The split of the algebra into its two sectors is the conjugation $\natural$, and it is carried by the algebra. A column of $\mathbb{C}^4$ carries no conjugation of its own, and a display in columns must import the split as extra structure.

The five gammas belong to a frame and not to the algebra. In the intrinsic form they are written out as the basis operators they are, $iR_{\vec e_x}$, $iL_{\vec e_\eta}R_{\vec e_y}$ and $-iR_{\vec e_z}$, and a reader sees the three spatial units in three different jobs on the same line. That is the defect of §*The Three Spatial Units Have Three Different Jobs* made visible at the place where it enters, which is the most a notation can do about it.

#### When a Matrix Is Still Needed

Some statements are about an array: a comparison of two displays, the census of the sixteen basis operators, a sentence that makes the direction visible, a program that multiplies numbers. For those, the array is the object of the sentence and must be written.

The natural array is the $\mathrm{axf}$ one, because it is the only one that adds nothing. A reader who sees an $\mathrm{axf}$ array can be sure that any direction in the surrounding paragraph came from the physics and not from the layout.

The order of preference is therefore four-level: the action first, a basis operator when the operator must be one symbol, an $\mathrm{axf}$ array when an array is unavoidable, and a Pauli or gamma array only where the array itself is the subject, as in a comparison or a dictionary.

| level | object | needs a basis | used when |
|---|---|---|---|
| the action | the pair $(a,b)$ | no | the operator is the subject |
| the basis operator | $L_aR_b$ as one element of a basis of operators | no | the operator must be one symbol |
| the array | $L_{\mathrm{axf}}(\tilde Q)$ | yes, the coefficient basis | an array is the object of the sentence |
| the Pauli array | $L_{\mathrm{pau}}(\tilde Q)$ | yes, the Peirce frame | a block, an ideal or a gamma is the subject |

### Migrating from the Pauli Framework

An article written in the Pauli framework does not have to be rewritten at once. The move has three passes, and each pass is mechanical enough to be checked.

#### The First Pass: From Arrays to Operators
Replace every array by the basis operator it displays. A basis operator is written $L_{e_\mu}R_{e_\nu}$, and its array is read in whichever frame the sentence needs. The pass removes the frame from the algebra and leaves it in the notation, where it can be seen.

A basis operator with a time slot collapses, because $e_t$ is the unit of the algebra: $L_{e_t}$ and $R_{e_t}$ are the identity operator, and a basis operator with two time slots is the identity. Two of the five gammas are single multipliers for exactly this reason.

During this pass an array may stay only where the array is the object: a comparison of two displays, the table of the sixteen basis operators, a sentence whose content is which entry is nonzero. Everything else becomes a basis operator.

#### The Second Pass: From Operators to Actions
Replace every basis operator by what it does. The rule is one line, and it is the whole pass:

$$
\tilde{Ξ}\longmapsto a\,\tilde{Ξ}\,b.
$$

The pass removes the operator symbol as well. A mass term is $k_m\tilde{Ξ}$; a derivative term is a term of the Dirac operator written out; a product is a product of elements. The composition law of §*Composition and Invariants* replaces every matrix multiplication. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

An article that reaches this pass has no arrays and no ideals in its body, and reads its operators off the formula itself.

#### The Third Pass: Keep the Axis-Free Array Where an Array Is Required

The remaining arrays are the ones the sentence is about. Write them in $\mathrm{axf}$, and put the frame label low: $L_{\mathrm{axf}}(\tilde Q)$ and $L_{\mathrm{pau}}(\tilde Q)$. The label is a name and not an exponent, and no label stands in the caret.

A section that survives all three passes has no Pauli object in its body, and any Pauli object it keeps is inside a closing block whose subject is the dictionary.

#### The Dictionary

The three passes need a table, and one table serves all three. Each row gives the name in the old notation, the object behind it, and the action.

| Pauli or gamma name | object | $\mathrm{axf}$ array | action |
|---|---|---|---|
| the identity $\mathrm I_4$ | $L_{e_t}R_{e_t}$ | $\mathrm I_4$ | $\tilde{Ξ}\mapsto\tilde{Ξ}$ |
| the image $\mathsf M_2(\tilde Q)$ | the left action on $\mathbb{B}\tilde\Pi_{\mathrm{id},+}$ | $\mathrm I_2\otimes\mathsf M_2(\tilde Q)$ | the action read on one ideal |
| $\gamma_0[\mathbb{B}_{\Phi}]$ | $iR_{\vec e_x}$ | $iR_{\mathrm{axf},\vec e_x}$ | $\tilde{Ξ}\mapsto i\tilde{Ξ}\vec e_x$ |
| $\gamma_\eta[\mathbb{B}_{\Phi}]$ | $iL_{\vec e_\eta}R_{\vec e_y}$ | $iL_{\mathrm{axf},\vec e_\eta}R_{\mathrm{axf},\vec e_y}$ | $\tilde{Ξ}\mapsto i\vec e_\eta\tilde{Ξ}\vec e_y$ |
| $\gamma_5[\mathbb{B}_{\Phi}]$ | $-iR_{\vec e_z}$ | $-iR_{\mathrm{axf},\vec e_z}$ | $\tilde{Ξ}\mapsto-i\tilde{Ξ}\vec e_z$ |
| the mass term | $k_mL_{e_t}R_{e_t}$ | $k_m\mathrm I_4$ | $\tilde{Ξ}\mapsto k_m\tilde{Ξ}$ |
| the Peirce projector $\tfrac12(\mathrm I-\gamma_5[\mathbb{B}_{\Phi}])$ | $\tfrac12\bigl(L_{e_t}R_{e_t}+iR_{\vec e_z}\bigr)$ | $\tfrac12\bigl(\mathrm I_4-iR_{\mathrm{axf},\vec e_z}\bigr)$ | $\tilde{Ξ}\mapsto\tfrac12\bigl(\tilde{Ξ}-i\tilde{Ξ}\vec e_z\bigr)$ |
| the Dirac adjoint | a pairing, not an action | — | needs the frame that declares the pairing |

The last row is the one that has no action, and that is the honest answer: the adjoint is not an operator on the element but a pairing of two elements.

#### The Conjugation and What It Preserves

The two displays are related by one matrix. With the Peirce vectors as columns,

$$
C_{\Pi}=\bigl(\tilde\Pi_{\mathrm{id},+}\ \ \vec\Pi_{\mathrm{nil},+}\ \ \vec\Pi_{\mathrm{nil},-}\ \ \tilde\Pi_{\mathrm{id},-}\bigr),\qquad
L_{\mathrm{pau}}(\tilde Q)=C_{\Pi}^{-1}L_{\mathrm{axf}}(\tilde Q)\,C_{\Pi},
$$

and $\det C_{\Pi}=-\tfrac14$. Every invariant survives the change: products, anticommutators, traces, determinants, spectra, ranks and the eigenvalue count. This is why the migration cannot change a result, and why it must be checked on invariants rather than on entries.

The conjugation is the check. Take an identity, conjugate both sides, and verify that the two sides remain equal. If a statement survives the conjugation, it was a statement about the operator. If it does not, it was a statement about the display.

#### The Four Traps

A migration that has been done once already leaves a record of what went wrong, and the record is four statements that looked like algebra and were notation.

The transpose rule. It holds in $\mathrm{axf}$, $L(\tilde Q)^{\mathsf T}=L(\tilde Q^{\natural})$, and it does not hold in the Pauli display. A proof that uses it is a proof about the axis-free frame, and it must be stated as such or re-proved.

The blocks. The two identical blocks of the Pauli array are the statement that left multiplication preserves the two Peirce components. In $\mathrm{axf}$ there are no blocks, and the same content is the statement that the right slot of the basis operator $L_{\vec e_\eta}R_{\vec e_y}$ does not move. A sentence about "the blocks" has to be rewritten as a sentence about the ideal.

The diagonal member. In the Pauli display one spatial unit sits on the diagonal, and a sentence about "the diagonal entry" is a sentence about that unit. In $\mathrm{axf}$ every diagonal basis operator is a square, and the entry says nothing about any unit. A sentence of that kind must be rewritten with the unit named.

The swap. The right family is the transpose of the left one between $\mathsf D$ and its own inverse in $\mathrm{axf}$, and the Pauli display has no such rule. A symmetry argument that uses the swap is a symmetry of the coefficient basis.

#### The Checklist

Five checks catch a migration that has gone wrong, and all five are mechanical.

The glyph census. Count the occurrences of the array delimiters and of the symbols $\sigma$, $\gamma$ and $\Pi$ in the body, everything before the closing block. A body with no array, no $\sigma$ and no $\gamma$ has passed the first two passes.

The operator census. Count the occurrences of the letters $L$ and $R$ carrying a subscript, section by section. A section that has reached the third pass has none, except a basis operator the section is about.

The invariant test. Evaluate both sides of every identity on a hundred random elements and compare. A mismatch is a conjugation error, not a typo.

The permutation test. Rename the three spatial units by a cycle and re-read the section. Every sentence that becomes false was a sentence about the display. This test is the reason the article exists, and it is the one a migration usually skips.

The link test. Every cited title must resolve, and a rewritten section must not cite a section that no longer exists.

#### The Rules of Use

Write the action first, $\tilde{Ξ}\mapsto a\tilde{Ξ} b$, and name the operator only when the operator is the subject.

Write one term per line. A sum is a sum of terms, and each term is a pair.

Never compress a sum into one symbol unless its coefficient matrix has rank one.

Keep the coefficient matrix out of the page. It is a diagnostic of the dictionary, not a datum of the physics.

Use no arrays, columns or Kronecker products in a physical formula.

Name the basis once, where it is used, and state a change of pair of spatial units where it occurs.

Enter the Pauli chain only where it is the subject: a Pauli array, a root, an idempotent, a Peirce basis, an ideal or a block.

Put the gamma form in one closing section, with the dictionary and no derivation, except in an article whose subject is the comparison, as in this one.

## The Limits

**The entry reads one family and not the algebra.** It states what the axis-free display is worth and what it costs. The Peirce display, the root, the idempotents and the compression at size two belong to *The Pauli Pair and the Gamma Frame: Which Statements Survive Conjugation*, and the argument that the corpus should display in this basis belongs to *The AXF Matrices: Axis-Free, Integer Entries*, §*Why the Pauli and the Gamma Displays Are Refused*.

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
- [The Pauli Pair and the Gamma Frame: Which Statements Survive Conjugation](the-pauli-pair-and-the-gamma-frame-which-statements-survive-conjugation.html), for the Peirce display, the gamma frame and what those displays print.
- [The AXF Matrices: Axis-Free, Integer Entries](the-axf-matrices-axis-free-integer-entries.html#why-the-pauli-and-the-gamma-displays-are-refused), for the argument that this basis is the one to display in.
- [The Operators of the Algebra](the-operators-of-the-algebra.html), for the two-sided operators, the five pictures and the mass coupling at operator level.
- [The Four Forms and the Four Norms](the-four-forms-and-the-four-norms.html), for the four norms in the algebra rather than in the array.
