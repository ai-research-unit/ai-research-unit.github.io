# __$M_2(\mathbb{C})$ Remaining Ideas__

## Scope

This file is an **inventory**, not a list of defects. It takes the nineteen titles of the legacy $M_2(\mathbb{C})$ series and records, for each, which of its ideas the two articles that exist contain, and which they do not.

The two articles are

| article | lines | what it owns |
|---|---|---|
| [$M_2(\mathbb{C})$ Standard Peirce Representation](../articles_maths/m2c-standard-peirce-representation-the-matrix-product-the-trace-and-the-determinant.html) | 839 | the root and the idempotents, the Peirce frame and its two orders, the coordinates, the left matrix $A$ and the right matrix $A^{\mathsf T}$, the stitch, the compression, the product, the trace, the determinant, the spectral projectors, the eigenbasis and the diagonalising matrix, the adjugate and the inverse, the four norms, the six subspaces, the three splits |
| [$M_2(\mathbb{C})$ Standard Peirce Representation : Operators](../articles_maths/m2c-standard-peirce-representation-operators.html) | 470 | the one-sided operators on the two planes, the two copies and the mutual centralisers, the pair, the scaling, the table of levels, the vectorisation and the Kronecker display, the coefficient matrix, the rank, trace and determinant of the operator, the three rank examples, the pair as a semigroup, the matrix-unit systems, the four-pair bound, the transpose as four pairs, the pair set as a cone |

The verdicts are three: **implemented**, the idea is in one of the two articles; **partial**, part of the idea is there and part is not; **absent**, the idea is in neither.

Five are implemented, six are partial, eight are absent. The absent ones are the substance of this file.

## The Verdict on the Nineteen Titles

| # | legacy title | verdict | where the idea is, if not here |
|---|---|---|---|
| 1 | The Product, the Trace and the Determinant | implemented | — |
| 2 | The Six Subspaces as Matrix Conditions | implemented | — |
| 3 | Peirce Coordinates, Matrix Units and the Spinor Planes | partial | §1.1 |
| 4 | The Spectral Projectors | implemented | — |
| 5 | The Centraliser and the Double Centraliser | partial | §1.2 |
| 6 | The Eigenbasis and the Diagonalising Matrix | implemented | — |
| 7 | The Jordan Basis and the Jordanising Matrix | absent | §2.1, *The Jordan Basis of a Spectrally Degenerate Biquaternion* |
| 8 | Worked Examples | partial | §2.6 |
| 9 | The Four Words and the Four Traces | partial | §1.3 |
| 10 | Trace, Determinant and the Biquaternion Norm | implemented | — |
| 11 | The Polar Decomposition of a Matrix | absent | §2.2, the polar articles of the algebra |
| 12 | Rank-One Matrices and the Determinantal Variety | partial | §1.4 |
| 13 | Spin, Qubits and the Bloch Vector | absent | §3.1, no owner |
| 14 | The Conjugations and the Adjoints | partial | §1.5 |
| 15 | $\mathrm{GL}_2(\mathbb{C})$, $\mathrm{SL}_2(\mathbb{C})$ and the Determinant | absent | §3.2, *The Lie Algebra $\mathfrak{gl}_4$ and $\mathfrak{sl}_4$* for $n=4$ only |
| 16 | The Projective Line and the Möbius Action | absent | §3.3, the generic Möbius articles |
| 17 | The Hermitian Sandwich | absent | §2.3, Part V |
| 18 | The Killing Form | absent | §2.4, *The Killing Form Operator* |
| 19 | The Functional Calculus | absent | §2.5, the generic calculus articles |

## 1. Partial: What Is There and What Is Not

### 1.1 Peirce Coordinates, Matrix Units and the Spinor Planes

**There.** The frame $\mathcal{P}=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$, its multiplication table, the coordinates $P_\pm,X_\pm$ with
$$
A=\begin{pmatrix}P_+&X_-\\X_+&P_-\end{pmatrix},\qquad P_\pm=Q_t\mp iQ_z,\quad X_\pm=-iQ_x\pm Q_y,
$$
the four matrix units $\mathsf M_2(\tilde\Pi_+)=E_{11}$, $\mathsf M_2(\vec\Upsilon_-)=E_{12}$, $\mathsf M_2(\vec\Upsilon_+)=E_{21}$, $\mathsf M_2(\tilde\Pi_-)=E_{22}$, the two orders and the swap of the nilpotents, and the ideal bases $S_\pm=\mathbb{B}\tilde\Pi_\pm$, $T_\pm=\tilde\Pi_\pm\mathbb{B}$.

**Not there.**

- **The element as two spinors.** The matrix is its two columns, $A=(\psi,\chi)$ with $\psi=(P_+,X_+)^{\mathsf T}$ in $S_+$ and $\chi=(X_-,P_-)^{\mathsf T}$ in $S_-$; the left action of the algebra is the action on the columns, and the right action is the action on the rows. The two planes are written as ideals in the introduction and are never used as carriers with the algebra acting on them.
- **The Plücker form of the determinant.** $\det A=P_+P_--X_+X_-$ is the Plücker relation of the two columns, so the singular element is exactly the element whose two spinors are proportional. This is one line and it joins the determinant to the planes.
- **Rank one as a spinor product.** $A=\psi\varphi^{\mathsf T}$ of two nonzero vectors, the cone over $\mathbb{P}^1\times\mathbb{P}^1$, with the two rulings the lines of the two left ideals and the lines of the two right ideals.
- **The action of a single matrix unit.** $E_{ij}\psi=\psi_j e_i$ on a column and $\varphi^{\mathsf T}E_{ij}=\varphi_i e_j^{\mathsf T}$ on a row, which is the sense in which a matrix unit is a rank-one operator of the plane.
- **The two planes as projective lines.** $S_+$ and $S_-$ are two copies of $\mathbb{C}^2$ and each has a projective line; the two lines are the two rulings of §1.4 and the sphere of §3.1.

### 1.2 The Centraliser and the Double Centraliser

**There.** One sentence in the operators article, §*The Two Copies*: "The two copies are mutual centralisers; the proof is in the $4\times4$ operators article." And one sentence in the representation article, in §*The Spectral Projectors*: "the centraliser of a spectrally regular element is two-dimensional, as in *The Centraliser*."

**Not there.**

- **The element-level theorem at this size.** For $A$ non-scalar, $C(A)=\{B:AB=BA\}=\mathbb{C}[A]$, of complex dimension two, spanned by $\mathrm I_2$ and $A$; for $A$ scalar, $C(A)=M_2(\mathbb{C})$, of dimension four. The proof by the eigenbasis of §*The Eigenbasis*, with the two cases of the degenerate element, is not written.
- **The eigenline reading.** The centraliser of a regular element is the set of matrices preserving its two eigenlines, so $C(A)$ is the stabiliser of the pair of lines, of dimension two; the scalar case is the stabiliser of nothing. This is the geometric content of the dimension table and it is missing.
- **The double centraliser at this size.** The commutant of the left copy is the right copy and conversely, with intersection the scalars; the algebra of all two-sided operators is the double centraliser of either copy, and the pair family spans it. The statement is cited and never proved here.
- **The degenerate case.** For a nonzero nilpotent $N$, $C(N)=\mathbb{C}[N]$, of dimension two, and the two-dimensional centraliser consists of matrices of the form $\alpha\mathrm I+\beta N$: the same dimension as the regular case, with a different structure.
- **The commutant of a single two-sided operator.** $T_{A,B}$ commutes with $T_{C,D}$ on the pair level when the pairs commute and on the operator level when the coefficient matrices commute; the two are different conditions, and the article does not separate them.

### 1.3 The Four Words and the Four Traces

**There.** The four norms of the representation article, each as the trace of a word: the plain $P=Q_t^2-B^2=\tfrac12\operatorname{Tr}(A^2)$, the quaternionic $N=Q_t^2+B^2=\det A$, the Hermitian $H=\sum_\mu\lvert Q_\mu\rvert^2=\tfrac12\operatorname{Tr}(A^{\dagger}A)$, the Krein $K=\lvert Q_t\rvert^2-\sum_k\lvert Q_k\rvert^2=\tfrac12\operatorname{Tr}(\operatorname{adj}(A)A^{\dagger})$.

**Not there.**

- **The traces of the powers.** $\operatorname{Tr}A=2Q_t$, $\operatorname{Tr}A^2=2(Q_t^2-B^2)$, and the two determine the determinant by Newton's identity,
$$
\det A=\tfrac12\bigl((\operatorname{Tr}A)^2-\operatorname{Tr}A^2\bigr),
$$
which is the trace form of $\operatorname{Tr}A^2-(\operatorname{Tr}A)A+(\det A)\mathrm I_2=0$. The higher traces $\operatorname{Tr}A^k$ and the power sums $Q_t\pm iB$ are absent.
- **The traces of the four words.** $\operatorname{Tr}(A\operatorname{adj}A)=2\det A$, $\operatorname{Tr}(\operatorname{adj}A)=2Q_t$, $\operatorname{Tr}(A^{\dagger}A)=2H$; the four traces as a table, and the fact that these are the four quadratic words the frame allows.
- **The mixed trace of the regular size.** The $4\times4$ articles carry the trace $4Q_{1t}Q_{2t}$ of the mixed pair, and the representation article states explicitly that it does not compress. The statement is a negative one, and the positive companion — what the mixed trace becomes at size two — is missing.
- **The four traces of the operator.** $\operatorname{Tr}T_{A,B}=4Q_tP_t$ is in the operators article; the other three trace-words $\operatorname{Tr}(T_{A,B}T_{C,D})$, $\operatorname{Tr}(T_{A,B}^{\dagger}T_{A,B})$ and $\operatorname{Tr}(\operatorname{adj}T_{A,B}\cdot T_{A,B}^{\dagger})$ are not.

### 1.4 Rank-One Matrices and the Determinantal Variety

**There.** In the operators article: the rank formula $\operatorname{rank}T_{A,B}=\operatorname{rank}A\cdot\operatorname{rank}B$, the three examples of ranks $1,2,4$, the coefficient matrix of rank one, and the pair set as the cone over $\mathbb{P}^3\times\mathbb{P}^3$.

**Not there.**

- **The rank-one matrices of the algebra itself.** $\{A:\operatorname{rank}A\le1\}=\{A:\det A=0\}=\{uv^{\mathsf T}\}$, the cone over $\mathbb{P}^1\times\mathbb{P}^1$, of complex dimension three, with the two rulings. The article treats the rank of the *operator* and never the determinantal variety of the *element*.
- **The Plücker reading.** $\det A=P_+P_--X_+X_-$, so the singular set is the quadric of the two columns, and its two rulings are the lines of the four ideals.
- **The stratification.** $\{0\}$, the rank-one cone of dimension three, the open set of units of dimension four; and the comparison with the operator ranks $0,1,2,4$ of the pair.
- **The determinant as a quadratic form.** On the four-dimensional space, $\det$ is a nondegenerate quadratic form of rank four with a null cone; the signature of its real part is $(2,2)$. The four norms name the forms but the null quadric of $\det$ is not drawn.

### 1.5 The Conjugations and the Adjoints

**There.** The adjugate as the matrix of the natural conjugation $\natural$, $\operatorname{adj}A=(\operatorname{Tr}A)\mathrm I_2-A=\mathsf M_2(\tilde Q^{\natural})$; the transpose as the matrix of $\varrho$, the reflection fixing $e_t,\vec e_x,\vec e_z$; the dagger $A^{\dagger}$ used in the six-subspace table and in the Hermitian and Krein norms; the identity $\operatorname{adj}(A_1A_2)=\operatorname{adj}A_2\operatorname{adj}A_1$.

**Not there.**

- **The four conjugations as four matrix maps.** Only two are named: $\natural\mapsto\operatorname{adj}A$ and the transpose. The entrywise conjugation $\bar A$, the fifth operation of the table, and the fourth conjugation $\flat$, identified only by its fixed space $\mathbb{M}_-=\{A=-A^{\dagger}\}$, are not given as matrix formulas, and the composition table of the four is not written.
- **The adjoints of the operators.** The dagger of the one-sided and two-sided operators, $(L_A)^{\dagger}=L_{A^{\dagger}}$, $(R_B)^{\dagger}=R_{B^{\dagger}}$, $(T_{A,B})^{\dagger}=T_{A^{\dagger},B^{\dagger}}$, and the plain adjoint of the same three, are not stated at this size; the operators article cites the abstract article for "the adjoint", and the adjoint there is the slot exchange of the plain form and not the dagger.
- **Which conjugation closes which norm.** Each of the four norms is a word closed by one conjugation; the correspondence $\natural\leftrightarrow N$, $\dagger\leftrightarrow H$, $\text{adj}\cdot\dagger\leftrightarrow K$, none $\leftrightarrow P$ is the organising table of the section and is not written.

## 2. Absent, With an Owner Elsewhere

### 2.1 The Jordan Basis and the Jordanising Matrix

**There.** One clause: in the degenerate case $B^2=0$ the element is "either scalar, with minimal polynomial $t-Q_t$, or non-scalar with a single eigenvalue and a nontrivial Jordan block, and the two projectors do not exist."

**Remaining ideas.**

- The two degenerate types as matrices: $A=Q_t\mathrm I_2$ and $A=Q_t\mathrm I_2+N$ with $N\neq0$, $N^2=0$; the second is the image of the elements of the form $Q_t e_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ with $B^2=0$.
- The Jordan basis: the chain $(\vec\Upsilon_+,\tilde\Pi_+)$ or $(\tilde\Pi_+,\vec\Upsilon_-)$ in which the element is $\begin{pmatrix}Q_t&1\\0&Q_t\end{pmatrix}$, and the Jordanising matrix that carries the Peirce frame to it.
- The eigenline and the generalised eigenline: the first is one of the two mixed lines, the second the whole plane; the reason no second projector exists is that the two lines coincide in the limit.
- The minimal polynomial $t^2-2Q_tt+Q_t^2=(t-Q_t)^2$, in contrast with the regular case; the diagonalising matrix of §*The Diagonalising Matrix* diverges as $B\to0$, and the Jordanising matrix is its limit in a different normalisation.
- The conjugation orbits: the scalar line, the nilpotent orbit (the null cone minus the origin, of real dimension six) and the regular orbit, with the Jordan type as the complete invariant of the closure.

**Owner.** *The Jordan Basis of a Spectrally Degenerate Biquaternion* for the algebra; no $2\times2$ matrix statement exists.

### 2.2 The Polar Decomposition of a Matrix

**There.** Nothing. The Hermitian norm is defined, and the polar decomposition is never formed.

**Remaining ideas.**

- $A=UP=PU$ with $U$ unitary and $P$ positive semidefinite; the modulus $P=\sqrt{A^{\dagger}A}$ and the unitary factor $U=A P^{-1}$ on the range.
- The spectral form: with $A=\mathsf C_Q\operatorname{diag}(\lambda_+,\lambda_-)\mathsf C_Q^{-1}$, the polar factors are $\mathsf C_Q\operatorname{diag}(e^{i\theta_\pm})\mathsf C_Q^{*}$ and $\mathsf C_Q\operatorname{diag}(\lvert\lambda_\pm\rvert)\mathsf C_Q^{*}$ for a unitary $\mathsf C_Q$, and the singular values are $\lvert\lambda_\pm\rvert$.
- The degenerate case: the polar factor is not unique when $A$ is singular, and the set of unitary factors is parametrised by the arbitrary action on the kernel.
- The trace and determinant of the polar factors: $\det P=\lvert\det A\rvert$, $\lvert\det U\rvert=1$, and the four norms read on $P$ and $U$.
- The contrast with the quaternionic polar decomposition, where the modulus is taken in the algebra and the unit is a versor: the two differ because the dagger is a different adjoint.

**Owner.** *The Polar Decomposition of a Biquaternion*, *The Polar Decomposition of $M_4(\mathbb{C})$* and the exponential-polar articles; no $2\times2$ statement.

### 2.3 The Hermitian Sandwich

**There.** A single sentence of the operators article: "The Hermitian sandwich is Part V and is not treated here."

**Remaining ideas.**

- $H\mapsto HXH$ for $H$ Hermitian, and $A\mapsto S A S^{\dagger}$ as the $\ast$-congruence of the element.
- Sylvester's law of inertia at size two: the signature $(2,0)$, $(1,1)$, $(0,2)$ of a Hermitian form, the classification of the Hermitian forms up to congruence, and the normal forms $\mathrm I_2$, $\operatorname{diag}(1,-1)$, $-\mathrm I_2$.
- The positivity: $HXH$ is positive semidefinite for $X$ positive, of rank $(\operatorname{rank}H)^2$, and it preserves $\mathbb{M}_+$.
- The sandwich of the *pair*, $T_{A,B}^{\dagger}T_{A,B}=T_{A^{\dagger}A,BB^{\dagger}}$, as the Gram operator of the pair.

**Owner.** Part V, *The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint*, and the sandwich articles of the algebra.

### 2.4 The Killing Form

**There.** Nothing.

**Remaining ideas.**

- $\kappa(X,Y)=4\operatorname{tr}(XY)-2\operatorname{tr}X\operatorname{tr}Y$ on $\mathfrak{gl}_2(\mathbb{C})$, verified on the matrix units; the radical is the scalar line, so the form is degenerate on $\mathfrak{gl}_2$ and the trace is the only null direction.
- $\kappa(X,Y)=4\operatorname{tr}(XY)$ on $\mathfrak{sl}_2(\mathbb{C})$, non-degenerate, with $\kappa(H,H)=8$, $\kappa(E,F)=4$ and $\kappa(E,E)=\kappa(F,F)=0$ in the order $(H,E,F)$; the isotropy of $E$ and $F$, and the degeneracy of the form on $\mathfrak{gl}_2$ in the scalar direction.
- The link with the plain norm: on the traceless part $\kappa(A,A)=4\operatorname{Tr}(A^2)=-8B^2$, so the Killing form is $-8$ times the vector-part quadratic form of the four norms.
- The real forms: on $\mathfrak{su}(2)$ the form is negative definite, on the split real form of signature $(2,1)$; the compact form read as a negative definite form is the reason the group is compact.

**Owner.** *The Killing Form Operator* for the general theory; *The Lie Algebra $\mathfrak{gl}_4$ and $\mathfrak{sl}_4$* for $n=4$. No $2\times2$ computation exists anywhere in the corpus.

### 2.5 The Functional Calculus

**There.** The Cayley–Hamilton remark: every polynomial in $A$ of degree at least two is a linear combination of $\mathrm I_2$ and $A$, and the minimal polynomial is $t^2-2Q_tt+\langle\tilde Q\rangle_{\natural}$.

**Remaining ideas.**

- The two-point formula: for a regular element with spectral projectors $\rho_\pm$,
$$
f(A)=f(\lambda_+)\rho_++f(\lambda_-)\rho_-,
$$
and its polynomial form $f(A)=\alpha\mathrm I_2+\beta A$ with $\alpha,\beta$ the Lagrange coefficients of $f$ at the two eigenvalues.
- The resolvent: $(z\mathrm I_2-A)^{-1}=\operatorname{adj}(z\mathrm I_2-A)/\det(z\mathrm I_2-A)$ with two simple poles at $\lambda_\pm$, and the Cauchy–Dunford integral around the two poles.
- The degenerate limit: for $A=Q_t\mathrm I_2+N$ with $N^2=0$, the calculus is $f(A)=f(Q_t)\mathrm I_2+f'(Q_t)N$, the two-term Taylor form, and it is not the limit of the two-point formula unless $f$ is differentiable at the double eigenvalue.
- The named functions: the square root $\sqrt{A}$ (two branches, and none at the degenerate element unless the eigenvalue is nonzero and a branch is chosen), the logarithm (existence exactly for invertible $A$, and the multivaluedness from the two eigenvalues), the Cayley transform $(A-\mathrm I_2)(A+\mathrm I_2)^{-1}$, the exponential $e^{A}=e^{Q_t}(\cos B\,\mathrm I_2+\tfrac{\sin B}{B}\mathsf M_2(\vec Q))$.
- The functional calculus as the source of the four norms: $H=\tfrac12\operatorname{Tr}(\sqrt{A^{\dagger}A}^{\,2})$, the modulus of §2.2.

**Owner.** *Holomorphic Functional Calculus* and *The Functional Calculus of a Self-Adjoint Element* for the general theory; the exponential-polar articles for the specific functions. No $2\times2$ statement.

### 2.6 Worked Examples

**There.** Three rank examples in the operators article: $A=B=E_{11}$ (rank one), $A=\mathrm I_2$, $B=E_{11}$ (rank two), $A=B=\mathrm I_2$ (rank four). Nothing else: one "example" in the representation article.

**Remaining ideas.** A collected set of elements, each carried through the whole dictionary, with the six columns $A$, $\det A$, the eigenvalues, $\rho_\pm$, $\mathsf C_Q$, $C(A)$, the pair decomposition and the rank of the coefficient matrix:

- the unit $e_t$ and the identity;
- a rank-one element, $\tilde\Pi_+$ and a general $uv^{\mathsf T}$;
- a mixed nilpotent, $\vec\Upsilon_+$;
- a real quaternion, $e_t+\vec e_x$, and a pure vector, $\vec e_z$;
- a Hermitian element off the axis;
- a skew-Hermitian element, $i\mathrm I_2$ and $i\vec e_x$;
- a degenerate non-scalar element, $e_t+\vec\Upsilon_+$ and $e_t+\vec e_x+i\vec e_y$ with $B^2=0$;
- a non-diagonalisable singular element of rank one;
- the transpose as the canonical example of an operator that is not a pair.

**Owner.** None. The two articles scatter three examples and collect none.

## 3. Absent, With No Owner

### 3.1 Spin, Qubits and the Bloch Vector

Nothing in the corpus treats the qubit reading of $M_2(\mathbb{C})$.

**The ideas.**

- The Hermitian trace-one elements: $H=\tfrac12(\mathrm I_2+\vec n\cdot\vec\sigma)$ with $\vec n\in\mathbb{R}^3$, the eigenvalues $\tfrac12(1\pm\lvert\vec n\rvert)$, and $\det H=\tfrac14(1-\lvert\vec n\rvert^2)$. The set is the **Bloch ball**, and the six-subspace table of the representation article already names its ambient space $\mathbb{M}_+$ of real dimension four.
- The pure elements: $\det H=0$ with $\operatorname{Tr}H=1$, that is $\lvert\vec n\rvert=1$, that is $\operatorname{rank}H=1$, that is $H=vv^{\dagger}$: the **Bloch sphere**, which is the projective line of §3.3 and the union of the two rulings of §1.4.
- The action: $H\mapsto UHU^{\dagger}$ for $U\in\mathrm{U}(2)$ is the rotation of $\vec n$, the map $\mathrm{SU}(2)\to\mathrm{SO}(3)$ is two-to-one with kernel $\pm\mathrm I_2$, and the sandwich of §2.3 is the operator form of the action.
- The positivity: the ball is the positive cone of $\mathbb{M}_+$ cut by the trace; the boundary is the pure set; the interior is the mixed set. The four norms give the radius: $\lvert\vec n\rvert^2=4H-1$ on the trace-one slice.
- The dictionary with the algebra: $\mathsf M_2(\vec e_k)=-i\sigma_k$, $\mathsf M_2(i\vec e_k)=\sigma_k$, so the Pauli matrices are the images of the anti-Hermitian basis and the quaternion units are $-i$ times them.
- The entropy: $S(H)=-\operatorname{Tr}(H\log H)$ by the functional calculus of §2.5, $S=0$ on the sphere and $S=\log2$ at the centre; the monotonicity under the sandwich.

### 3.2 $\mathrm{GL}_2(\mathbb{C})$, $\mathrm{SL}_2(\mathbb{C})$ and the Determinant

Nothing in the corpus treats these groups at this size.

**The ideas.**

- $\det:\mathrm{GL}_2(\mathbb{C})\to\mathbb{C}^{\times}$ is surjective and multiplicative, $\mathrm{SL}_2(\mathbb{C})=\ker\det$ is normal, and the quotient is $\mathbb{C}^{\times}$; the centre of $\mathrm{GL}_2$ is the scalar line, the centre of $\mathrm{SL}_2$ is $\pm\mathrm I_2$, and $\mathrm{PSL}_2=\mathrm{PGL}_2$.
- $\mathrm{SL}_2$ is generated by the transvections $\begin{pmatrix}1&t\\0&1\end{pmatrix}$ and $\begin{pmatrix}1&0\\t&1\end{pmatrix}$; the commutator subgroup of $\mathrm{GL}_2$ is $\mathrm{SL}_2$; $\mathrm{SL}_2$ is perfect.
- The Lie algebra: $\mathfrak{gl}_2$ with the commutator, $\mathfrak{sl}_2$ traceless of dimension three, the basis $(H,E,F)$ with $[H,E]=2E$, $[H,F]=-2F$, $[E,F]=H$; the Killing form of §2.4; $\mathfrak{su}(2)$ as the compact real form and $\mathfrak{sl}_2=\mathfrak{su}(2)\oplus i\mathfrak{su}(2)$ as the Cartan decomposition.
- The adjoint action: conjugation on the traceless part is the map $\mathrm{SL}_2\to\mathrm{SO}(3,\mathbb{C})$, the double cover, with the same kernel $\pm\mathrm I_2$ as in §3.1.
- The action on the Hermitian forms: $H\mapsto SHS^{\dagger}$, preserving $\det H$ up to $\lvert\det S\rvert^2$; on the trace-one slice this is the action of $\mathrm{SU}(2)$ on the sphere, and the Lorentz group of the algebra is $\mathrm{SL}_2(\mathbb{C})$ read on $\mathbb{M}_+$.
- The determinant of the elementary matrices and the multiplicativity on the Peirce frame: $\det E_{ij}=0$, $\det(\mathrm I_2+tE_{12})=1$, which is the transvection with unit determinant.

**Owner.** *The Lie Algebra $\mathfrak{gl}_4$ and $\mathfrak{sl}_4$* covers $n=4$; the $n=2$ case has no article.

### 3.3 The Projective Line and the Möbius Action

Nothing in the corpus treats the projective line of $M_2(\mathbb{C})$ or the induced Möbius action, although the generic Möbius articles treat the group abstractly.

**The ideas.**

- $\mathbb{P}^1$ as the set of lines of $\mathbb{C}^2$, as the set of rank-one projections $\tfrac12(\mathrm I_2+\vec n\cdot\vec\sigma)$, as the Bloch sphere, and as the projective space of each minimal left ideal $S_\pm$: four descriptions of one object, and the article that identifies them does not exist.
- The action $[v]\mapsto[Av]$ of $\mathrm{GL}_2(\mathbb{C})$, with kernel the scalars, hence the effective group $\mathrm{PGL}_2(\mathbb{C})$; the action is transitive, the stabiliser of a point is the parabolic subgroup of matrices fixing a line.
- The cross-ratio as a ratio of $2\times2$ determinants,
$$
(z_1,z_2;z_3,z_4)=\frac{\det(v_1,v_3)\det(v_2,v_4)}{\det(v_1,v_4)\det(v_2,v_3)},
$$
which is the invariant of four points, and it is the only invariant of the diagonal action on $(\mathbb{P}^1)^4$; at this size it is the quotient of two minors, and the minors are the Plücker coordinates of §1.4.
- The classification by the discriminant: with $\operatorname{Tr}A=t$ and $\det A=d$, the fixed points are the eigenvectors and the type is read on $t^2-4d$: two distinct fixed points ($t^2\neq4d$), one double fixed point ($t^2=4d$, $A$ not scalar, the parabolic case), no fixed point on the line over $\mathbb{R}$ but two conjugate ones (the elliptic case). The classification is the spectral trichotomy of §*The Spectral Projectors* read on the projective line.
- The three real forms: $\mathrm{PSU}(2)$ acting on the sphere by rotations, $\mathrm{PSL}_2(\mathbb{R})$ acting on the upper half-plane, $\mathrm{PSL}_2(\mathbb{C})$ acting on the sphere by conformal maps; the elliptic, parabolic and hyperbolic words are the same three words as the three orbits of the classification.
- The Möbius action as a two-sided operator: the element $A$ acts on the line by $[v]\mapsto[Av]$, and the operator on functions is the sandwich of §2.3 with the Jacobian factor $\det(A^{\dagger}A)/\lvert cv+d\rvert^4$; this is the point where the operator language and the Möbius language meet, and it is nowhere written for this algebra.

**Owner.** *The Möbius Transformation as an Operator* and *Operators on a Projective Space* for the general theory; *Split-Biquaternion Null Quadric and Projective Geometry* for the split-quaternion analogue. No $M_2(\mathbb{C})$ statement.

## What the Five Implemented Titles Own

Recorded so that the planner does not re-propose them.

- **The Product, the Trace and the Determinant.** The product $AB$, the anti-multiplicativity of the right matrix, $\operatorname{Tr}=2Q_t$, $\det=\langle\tilde Q\rangle_{\natural}$, the eigenvalues $Q_t\pm iB$, and the doubling of each invariant at the regular size.
- **The Six Subspaces as Matrix Conditions.** The table of the six conditions ($A=\lambda\mathrm I_2$, $\operatorname{Tr}A=0$, $A=A_{\mathbb{H}}$, $A=A_{i\mathbb{H}}$, $A=A^{\dagger}$, $A=-A^{\dagger}$), their real dimensions $2,6,4,4,4,4$, their traces and their determinants, and the three splits.
- **The Spectral Projectors.** $\rho_\pm=\tfrac12(\mathrm I_2\pm\mathsf M_2(\vec\Xi))$ with $\vec\Xi=-i\vec Q/B$, of rank one, complementary, orthogonal, commuting with $A$; the degenerate case excluded and named.
- **The Eigenbasis and the Diagonalising Matrix.** One column of each projector, the matrix $\mathsf C_Q$, and $\mathsf C_Q^{-1}A\mathsf C_Q=\operatorname{diag}(\lambda_+,\lambda_-)$.
- **Trace, Determinant and the Biquaternion Norm.** The four norms as the four quadratic invariants, their word formulas, their value rings and their definiteness, and the two pairings that produce them.

## Counts

- Nineteen legacy titles: five implemented, six partial, eight absent.
- Partial with the largest residue: *Peirce Coordinates, Matrix Units and the Spinor Planes* (the spinor reading, the Plücker form, the rank-one cone) and *The Four Words and the Four Traces* (the powers, Newton, the four operator traces).
- Absent with no owner at all: *Spin, Qubits and the Bloch Vector*, *$\mathrm{GL}_2(\mathbb{C})$, $\mathrm{SL}_2(\mathbb{C})$ and the Determinant*, *The Projective Line and the Möbius Action*, *Worked Examples*.
- Absent with an owner elsewhere: *The Jordan Basis and the Jordanising Matrix*, *The Polar Decomposition of a Matrix*, *The Hermitian Sandwich*, *The Killing Form*, *The Functional Calculus*.
- The three absent-with-no-owner articles of §§3.1–3.3 are one subject seen from three sides: the Hilbert space, the group, the projective line. The Plücker form $\det A=P_+P_--X_+X_-$ and the spinor columns of §1.1 are the common technical core.
