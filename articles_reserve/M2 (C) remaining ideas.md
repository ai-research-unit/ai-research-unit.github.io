# M2 (C) Remaining Ideas

## What this note is

The $M_2(\mathbb{C})$ block once held twenty-one drafts: the nineteen topics of the request, plus the columns/rows article and the umbrella draft. All of them were deleted when the block was compressed into two articles, *$M_2(\mathbb{C})$ Standard Peirce Representation* (the model, 839 lines) and *$M_2(\mathbb{C})$ Standard Peirce Representation : Operators* (470 lines). This note records, topic by topic, **the ideas that were in the drafts and are not in the two survivors**.

**Method.** The legacy files were read from git history: twenty-one drafts, 5827 lines. Each was reduced to its section headings and its bold lead-ins, and each claim was looked for in the two surviving articles, by keyword and then by reading. The verdict is per idea and not per topic, because most topics are mixed.

**The three verdicts.**

- **Implemented** — the topic is in the pair, with at most a residue of one or two ideas.
- **Partly implemented** — the object is present but the legacy gave it a structure the pair does not.
- **Not implemented** — nothing of the topic is in the pair.

**Two cautions.** First, several of these ideas exist elsewhere in the corpus, in the $M_4(\mathbb{C})$ articles, in the biquaternion articles or in the general articles on operators and forms. Where I know of such a home I name it, because the question there is whether to write the idea at the $2\times2$ size or to cross-reference it. Second, a few formulas below are quoted from the legacy drafts without independent re-derivation; they are marked *check*.

## Verdict table

| # | legacy topic | verdict | where it is today |
|---|---|---|---|
| 1 | The Product, the Trace and the Determinant | implemented | model, §*The Product*, §*The Trace*, §*The Determinant* |
| 2 | The Six Subspaces as Matrix Conditions | implemented | model, §*The Six Subspaces* |
| 3 | Peirce Coordinates, Matrix Units and the Spinor Planes | partly | model, §*The Peirce Basis and the Two Orders*; operators, §*The Pair as a Semigroup* |
| 4 | The Spectral Projectors | implemented | model, §*The Spectral Projectors* |
| 5 | The Centraliser and the Double Centraliser | **not** | one sentence in the operators article |
| 6 | The Eigenbasis and the Diagonalising Matrix | implemented | model, §*The Spectral Projectors* and its subsection *The Diagonalising Matrix* |
| 7 | The Jordan Basis and the Jordanising Matrix | **not** | one sentence in the degenerate case |
| 8 | Worked Examples | **not** | absent |
| 9 | The Four Words and the Four Traces | partly | model, §*The Four Norms* |
| 10 | Trace, Determinant and the Biquaternion Norm | implemented | model, §*The Trace*, §*The Determinant*, §*The Four Norms* |
| 11 | The Polar Decomposition of a Matrix | **not** | absent |
| 12 | Rank-One Matrices and the Determinantal Variety | **not** | a fragment in the operators article |
| 13 | Spin, Qubits and the Bloch Vector | **not** | absent |
| 14 | The Conjugations and the Adjoints | partly | model, §*The Stitch Between the Left and the Right*, §*The Adjugate and the Inverse* |
| 15 | $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ and the Determinant | **not** | one sentence |
| 16 | The Projective Line and the Möbius Action | **not** | absent |
| 17 | The Hermitian Sandwich | **not** | absent |
| 18 | The Killing Form | **not** | absent |
| 19 | The Functional Calculus | **not** | absent |

**The count.** Five topics are implemented, three are partly there, and eleven are missing. The missing eleven are not a residue of the block: they are its two thirds, and they are the half of the subject that is not the Peirce frame.

---

## Part A — Implemented, and what did not travel

### 1. The Product, the Trace and the Determinant

**In the pair.** The isomorphism, the four unit images, the factor $i$ and the forced signs, $M_QM_P=M_{QP}$, the trace $2Q_t$, the determinant $Q_t^2+B^2$, multiplicativity, invertibility, Cayley–Hamilton, the rank criterion.

**The residue.**

- **The structure map and the presentation.** The scalars act through $\mathbb{C}\to\mathbb{B}$, $\lambda\mapsto\lambda e_t$, and the algebra is presented by two generators $X=\mathsf M_2(\vec e_x)$, $Y=\mathsf M_2(\vec e_y)$ with the relations of the pair. The pair names the isomorphism but never writes the presentation, and the presentation is what makes "the model is a quotient" a statement rather than a slogan.
- **The real form.** Read over $\mathbb{R}$, $M_2(\mathbb{C})$ is eight-dimensional, and the real form $\mathbb{B}$ is cut out by an antilinear involution. The pair works over $\mathbb{C}$ throughout and never states which real structure the model carries, so the reader cannot see why the same complex algebra carries several real forms.
- **Simple, and therefore not a division algebra.** A nonzero two-sided ideal contains a matrix with a nonzero entry, hence a matrix unit, hence everything. The legacy proved it in three lines; the pair asserts simplicity once, in passing.
- **Any two models differ by conjugation.** If $\mathsf M_2'$ is another $\mathbb{C}$-algebra isomorphism $\mathbb{B}\to M_2(\mathbb{C})$, then $\mathsf M_2'=\operatorname{Ad}_C\circ\mathsf M_2$ for some $C\in GL_2(\mathbb{C})$. This is the moduli statement of the block — the model is unique up to conjugation, so every "choice of model" is a choice of basis of $\mathbb{C}^2$ — and it is the sentence that justifies the whole idea of a standard frame.
- **The null-cone basis, as a second model.** The isotropic basis of the null cone gives a second family of models, in which the idempotents are the coordinate points and the nilpotents are the off-diagonal units. The pair has the Peirce frame but not the *contrast* between the two frames.

### 2. The Six Subspaces as Matrix Conditions

**In the pair.** All six, with their dimensions, the three splits, the intersections and the closure table. This is the most completely absorbed topic of the block.

**The residue.**

- **The mirror.** Multiplication by the central $i$ exchanges $\mathbb{M}_+$ and $\mathbb{M}_-$, reverses the sign of the determinant and preserves the null cone. The pair tabulates the two subspaces side by side but never names the operator that exchanges them.
- **The two blocks of the vector subspace.** Writing $Q_k=q_k+iq_k'$, the real and the imaginary parts of the traceless subspace are the blocks of real and imaginary coefficients; the pair gives the trace condition only.
- **The conjugate-linear pattern.** On the quaternion subspace the entries follow $w\mapsto-\bar w$, and this is the unique conjugate-linear pattern compatible with the multiplication. It is the reason the quaternion subspace is a subalgebra and the anti-quaternion one is not, and the pair does not say it.

### 4. The Spectral Projectors

**In the pair.** The two projectors, the spectral decomposition, the rank-one proposition, the non-Hermitian remark, the eigenvector columns, the diagonalising matrix, the two charts, the degenerate case.

**The residue.**

- **The projectors as contour residues.** $\rho_\pm=\frac{1}{2\pi i}\oint_{\gamma_\pm}(z-M)^{-1}\,dz$ around a small circle enclosing $\lambda_\pm$ alone; the resolvent $(z-M)^{-1}$, and its expansion in the two projectors. The pair has no resolvent and no contour, so the projectors appear as an algebraic formula rather than as a residue. This is the bridge to the functional calculus of topic 19.
- **The signed projector.** $\rho_+-\rho_-$ is the image of the spectral direction $\vec\Xi/B$; it is the matrix form of "which way the element points", and the pair computes the projectors but not their difference.
- **The nilpotents as conjugates of the off-diagonal units.** $\mathsf C_QE_{12}\mathsf C_Q^{-1}$ and $\mathsf C_QE_{21}\mathsf C_Q^{-1}$ are the two nilpotents of the element, of rank one and square zero. The pair mentions nilpotents only in the degenerate sentence.
- **The directional limit at the degenerate cone.** As $\vec Q\to0$ along a fixed direction, $\rho_\pm$ tends to a pair of rank-one projectors that depends on the direction. The pair says "the formula has no limit" and stops, which is true of the pair and false of the limit.

### 6. The Eigenbasis and the Diagonalising Matrix

**In the pair.** The eigenbasis, the diagonalising matrix, its inverse, the two charts, the freedom, the warning that $\mathsf C_Q$ is not the frame change.

**The residue.**

- **The normal case, in full.** $M$ normal $\iff$ $M$ is $*$-unitary diagonalisable $\iff$ there is a $*$-unitary $U$ with $U^{\dagger}MU$ diagonal; the Hermitian decomposition $M=\frac{M+M^\dagger}{2}+\frac{M-M^\dagger}{2}$; the three normal types; the normal form $U\operatorname{diag}(\lambda_+,\lambda_-)U^{\dagger}$. The pair's only "normal" is the phrase "normal forms", and its only "spectral theorem" is a rhetorical flourish about trace and determinant; the theorem itself, about normal matrices, is absent. It is the one place where the matrix model meets the spectral theorem of quantum mechanics.
- **The transition matrix and its cocycle.** For two spectrally regular elements, $\mathsf C_Q^{-1}\mathsf C_{Q'}$ changes $Q'$-coordinates to $Q$-coordinates, and the three matrices satisfy the cocycle identity. The pair computes the diagonalisation of one element and never relates two.
- **The Gram matrix in the eigenbasis order.** The trace pairing read in the eigenbasis order $(\Pi_+,\Upsilon_-,\Upsilon_+,\Pi_-)$ has a Gram matrix whose entries are the four pairings, and it is what makes the coordinates computable by duality. The pair gives the coordinates but not their Gram matrix.

### 10. Trace, Determinant and the Biquaternion Norm

**In the pair.** The trace, the trace pairing, "the trace is not the norm", the determinant as the quaternionic norm, invertibility, the zero divisors as the singular matrices, the four norms, the characteristic polynomial, Cayley–Hamilton, the spectrum.

**The residue.**

- **The determinant as a volume.** Over $\mathbb{C}$ the determinant is a complex volume; $|\det M|^2$ is the real area of the image of the unit square. It is the geometric reading that justifies the word "unimodular" for $SL_2$, and the pair has no "volume" at all.
- **The biquadratic.** $p_M(t)=t^2-2Q_tt+N$ with $N=Q_t^2+B^2$, and its two roots $Q_t\pm iB$ exchanged by $B\mapsto-B$. The pair has the polynomial; it does not make the exchange of the roots a symmetry of the statement, which is what makes the eigenvalue pair a *pair*.

---

## Part B — Partly implemented

### 3. Peirce Coordinates, Matrix Units and the Spinor Planes

**In the pair.** The Peirce table (the four basis elements multiply as the four matrix units), the coordinate isomorphism, the corner coordinates by trace pairing, the two orders, and in the operators article the systems of matrix units, the reciprocal scaling and the conjugation theorem.

**Remaining ideas.**

- **The two spinor planes as carriers.** $S_\pm=\mathbb{B}\tilde\Pi_\pm$ are minimal left ideals of complex dimension two, each with an adapted basis $\mathcal{C}_\pm=(\tilde\Pi_\pm,\Upsilon_\pm)$; left multiplication preserves each plane, right multiplication mixes them. The pair names $S_\pm$ in one sentence and points at the biquaternion article, but never uses them as carriers: there is no basis, no matrix of left multiplication in that basis, and no statement of what a "spinor" is at this size.
- **The mixing rule.** Inside a plane, left multiplication by an element with a nonzero mixed coordinate mixes the idempotent and the nilpotent; the *Peirce index* rule is that left multiplication preserves the column index and right multiplication flips it. This is the operational content of "spinor", and it is absent.
- **The star carries a plane to a row, not to the other plane.** $S_\pm^{*}=T_\pm$, the right Peirce row, and not $S_\mp$. The pair says $S_\pm^*=T_\pm$ once, in passing, and does not draw the consequence: the two planes are not exchanged by the involution.
- **Every nontrivial idempotent is a product of two nilpotents.** And every nonzero nilpotent is trace-free, singular, of rank one, with a square-zero property that forces the strictly triangular form. The pair has "two nilpotents" in the arithmetic of the frame but not this factorisation theorem.
- **The two nilpotent lines are not conjugate by the standard torus.** They are exchanged by the Weyl element, and the distinction is the difference between the identity component and the other components of the frame's stabiliser.
- **The stabiliser torus.** The common stabiliser of the two standard idempotents in the unit group is $(\mathbb{C}^\times)^2/\mathbb{C}^\times$; the operators article has one "torus" and no computation of it.
- **The reciprocal scaling is a conjugation.** $(u,w)\mapsto(\mu u,\mu^{-1}w)$ is $\operatorname{Ad}_{\operatorname{diag}(\mu,\mu^{-1})}$; the operators article proves it for the pair but not for the frame.

### 9. The Four Words and the Four Traces

**In the pair.** The four quadratic invariants (plain, quaternionic, Hermitian, Krein) and the remark that each is a trace of a word in $M$, $\operatorname{adj}M$ and $M^\dagger$.

**Remaining ideas.**

- **The four words, as a list.** $MM'$, $\operatorname{adj}(M)M'$, $M^\dagger M'$, $\operatorname{adj}(M)^\dagger M'$, one per form; the words are not distinct as matrices in general, and they coincide on special elements. The pair gives the four *norms* and never the four *words*.
- **The four half-traces, in one table.** $\frac12\operatorname{Tr}(MM')$, $\frac12\operatorname{Tr}(\operatorname{adj}M\,M')$, $\frac12\operatorname{Tr}(M^\dagger M')$, $\frac12\operatorname{Tr}(\operatorname{adj}M^\dagger M')$, with their signatures, their null sets and their realifications. The pair's §*The Four Norms* is the diagonal of this table only.
- **The signatures of the realifications.** Each complex bilinear form realifies to signature $(4,4)$; the Hermitian form is definite. The two bilinear forms vanish on cones of real dimension six, the Hermitian one only at the origin.
- **The trace pairing is the invariant form.** Up to a scalar it is the unique symmetric bilinear form on the algebra invariant under both multiplications; the proof is three lines and it is the reason the trace form is *the* form of the block.
- **The words compose.** The product of two words is a word, the composition is the matrix product, and the trace kills the antisymmetric part; the conjugate of a word is computed by the four involutions. Nothing of this word algebra is in the pair.

### 14. The Conjugations and the Adjoints

**In the pair.** The transpose as the stitch, the adjugate as the image of quaternion conjugation, the dagger, the adjugate involution, and the fixed spaces of some of them.

**Remaining ideas.**

- **The table of the four involutions.** ${}^{\natural}$ (adjugate), $\bar{\cdot}$ (complex conjugation), ${}^{*}$ (dagger), ${}^{\flat}=-{}^{*}$ (anti-Hermitian conjugation), with the algebra definition, the fixed space, the anti-fixed space and the matrix image on one line each. The pair has three of the four operations scattered over three sections and never the fourth.
- **The Klein four-group.** ${}^{*}=\bar{\cdot}\circ{}^{\natural}={}^{\natural}\circ\bar{\cdot}$, and the two companions; the fourth is the negative of the third and is outside the group because the minus sign is not a homomorphism. This is a two-line theorem that organises the whole section, and it is absent.
- **Complex conjugation is not entrywise.** It is $M\mapsto\epsilon\bar M\epsilon^{-1}$ with $\epsilon=\operatorname{diag}(1,-1)$; the entrywise conjugate is the matrix of $\sigma(\tilde Q)$, a different element. The pair writes the quaternion subspace as a condition on the entries and never warns that $\bar M$ alone is the wrong operation — the single most common error at this size.
- **The four adjoints of the four forms.** Each involution is the switch of one form, and the four adjoints are the four words read on the second slot. This is the operator-level statement that the pair never makes.
- **Why four and not two.** The complex algebra has two independent real structures, ${}^{\natural}$ and $\bar{\cdot}$, and their product is the third; a real algebra has one, a complex algebra has two. The count of involutions is the count of real structures, and the pair's two-structure picture of the six subspaces does not explain where the four come from.
- **The adjugate of the dagger.** $\operatorname{adj}(M^\dagger)=(\operatorname{adj}M)^\dagger$ up to the central sign, and the three operations form the Klein group; the pair proves the adjugate is an involution but not how it interacts with the dagger.

---

## Part C — Not implemented

### 5. The Centraliser and the Double Centraliser

**What the pair has.** One sentence: "the two copies are mutual centralisers", about the left and right families of operators. Nothing about the centraliser of an element.

**The ideas.**

- **The commutant of an element.** $C(X)=\{Y:XY=YX\}$. For non-scalar $X$ it is $\mathbb{C}[X]=\operatorname{span}\{I_2,X\}$, of complex dimension two, and it is $\mathbb{C}[t]/(m_X)$.
- **The three types, in the eigenbasis.** Distinct eigenvalues: $C(X)=\{\operatorname{diag}(\alpha,\beta)\}\cong\mathbb{C}^2$. Repeated eigenvalue with $N\neq0$: $C(X)=\{aI_2+bN\}$, the dual numbers. Scalar: $C(X)=M_2(\mathbb{C})$, of dimension four.
- **The adjugate is in the commutant.** By Cayley–Hamilton, $\operatorname{adj}X=(\operatorname{tr}X)I_2-X$, so $\mathbb{C}[X]=\operatorname{span}\{I_2,\operatorname{adj}X\}$: the commutant is generated by the adjugate. This is the sharpest one-line statement of the topic, and it makes the four norms of the pair (§*The Four Norms*) a statement about the commutant.
- **The dagger lies in the commutant exactly when $X$ is normal.** So normality is a commutant condition, which is what makes the normal case of topic 6 a spectral statement.
- **The double centraliser.** $C(C(X))=\mathbb{C}[X]$ for non-scalar $X$, and $C(C(X))=\mathbb{C}I_2$ for scalar $X$; the chain $\mathbb{C}[X]\subseteq C(C(X))$ closes at the first step. The module reading is the double centraliser theorem for $\mathbb{C}[X]$ acting on $\mathbb{C}^2$.
- **The ambiguity of the eigenbasis is the commutant's torus.** The matrices $C$ with $C^{-1}XC$ diagonal are $\mathsf C_Q\cdot\operatorname{diag}(\alpha,\beta)$, so the freedom of topic 6 and the commutant of topic 5 are the same object.
- **Where it lives elsewhere.** The abstract statement is *Algebras of Endomorphisms* and *The Centraliser*; the biquaternion version is in the $M_4(\mathbb{C})$ block. At the $2\times2$ size it is a page.

### 7. The Jordan Basis and the Jordanising Matrix

**What the pair has.** One sentence: in the degenerate case "the element is either scalar, or non-scalar with a single eigenvalue and a nontrivial Jordan block, and the two projectors do not exist". No basis, no matrix, no frame.

**The ideas.**

- **The Jordan basis.** For a spectrally degenerate element with $\vec Q\neq0$, the basis $(\tilde\Pi_+,\Upsilon_-,\Upsilon_+,\tilde\Pi_-)$ adapted to the flag $\ker N\subset\ker N^2=\mathbb{B}$, with $N=\tilde Q-Q_te_t$; the multiplication table is again the matrix units, so the Jordan basis is a *second* frame with the same unit table. The pair's whole apparatus of coordinates by trace pairing transfers verbatim, and that is the point: two frames, one table.
- **The Jordanising matrix.** $\mathsf S_Q\in GL_2(\mathbb{C})$ with $\mathsf S_Q^{-1}M\mathsf S_Q=J_2(\lambda)=\lambda I_2+N$, its canonical choice, and the formula for its determinant. The general solution is $\mathsf S_Q\mathsf G$ with $\mathsf G$ upper triangular Toeplitz invertible.
- **The freedom is Toeplitz, not diagonal.** The eigenbasis freedom is $(\mathbb{C}^\times)^2$; the Jordan freedom is the affine group $\{a\mapsto a+b\}$ in the Toeplitz parameter, with the chain shift $b=-\beta/\alpha$ and $\det G=\alpha^2$. The two freedom groups are different, and comparing them is the content of the topic.
- **The centraliser of the block.** $C(J_2(\lambda))$ is the upper triangular Toeplitz algebra, the dual numbers; so the Jordan topic and the centraliser topic share their degenerate case.
- **The canonical frame from the Hermitian form.** The definite Hermitian form selects one point of the affine family; the canonical $\mathsf S_Q$ is $U\operatorname{diag}(1,s^{-1})$ with $U$ $*$-unitary, and its polar decomposition is the content. The defect $s$ measures the failure, and $\mathsf S_Q$ is $*$-unitary exactly when $2\langle\vec Q\rangle_*=1$.
- **No non-scalar element of the sector is normal.** The Jordan sector and the normal stratum of topic 6 are disjoint, which is the sharpest statement of what a Jordan block costs.
- **Where it lives elsewhere.** *The Jordan Basis of a Spectrally Degenerate Biquaternion* for the abstract frame.

### 8. Worked Examples

**What the pair has.** Three examples in the operators article (rank one, rank two, rank four) and one in the model. No worked-examples article.

**The ideas.**

- **The method, as a checklist.** From $\tau=\operatorname{Tr}X$ and $\delta=\det X$: the characteristic polynomial, the minimal polynomial, the spectral type, the rank, the projectors by the Lagrange formula, the commutant, the polar factors, the four flags (Hermitian, $*$-unitary, normal, singular), and the biquaternion preimage. The method is a page, and it is the only place where the whole apparatus is exercised on one object.
- **The eight matrices, and what each one isolates.** $2I_2$ (the scalar: central, commutant everything, polar trivial); $J=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ (the Jordan block: dual-number commutant, not normal); $D=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ (distinct real eigenvalues, diagonalisable but not normal); $S=\operatorname{diag}(2,0)$ (singular Hermitian, the pseudo-inverse $S^{+}$, the partial isometry); $R=\begin{pmatrix}1&2\\3&6\end{pmatrix}$ (rank one but not a projector: the null cone off the idempotent locus); $U=\frac{1}{\sqrt2}\begin{pmatrix}1&i\\i&1\end{pmatrix}$ (in $SU(2)$, its own polar factor); $H=\begin{pmatrix}2&1-i\\1+i&-1\end{pmatrix}$ (Hermitian, orthogonal projectors, real eigenvalues of both signs); $N=\begin{pmatrix}1&1\\-1&1\end{pmatrix}$ (normal, neither Hermitian nor $*$-unitary, $\sqrt2$ times an element of $SU(2)$).
- **The pattern table.** Hermitian $\Rightarrow$ normal $\Leftarrow$ $*$-unitary, with the two separations exhibited by $D$ and $N$; the singular Hermitian and the rank-one non-Hermitian both of rank one and determinant zero, separated by normality; the Jordan block as the only non-diagonalisable one.
- **The pseudo-inverse.** $S^{+}$ and the identities $SS^{+}S=S$, $S^{+}SS^{+}=S^{+}$, which the pair never names.

### 11. The Polar Decomposition of a Matrix

**What the pair has.** Nothing. The word "polar" does not occur in either article.

**The ideas.**

- **The matrix decomposition.** Every $M\in M_2(\mathbb{C})$ is $M=PV$ with $P=(MM^{\dagger})^{1/2}$ positive semidefinite and $V$ $*$-unitary when $M$ is invertible, a partial isometry in general; unique with $\ker V=\ker M$.
- **The polar decomposition is not the algebra's polar decomposition.** The algebra's polar form is $\tilde Q=r\zeta M_bM_r$ (modulus, unit, boost, rotor); the matrix's is $M=PV$. The two are different factorisations of the same matrix, and the comparison is the point of the topic: the algebra one is multiplicative in the algebra, the matrix one is spectral in the matrix.
- **The diffeomorphism.** $U(2)\times H^{++}\to GL_2(\mathbb{C})$, $(U,P)\mapsto UP$, is a diffeomorphism; its inverse is the polar decomposition. So $GL_2$ is a product of a compact group and a convex cone, which is the Cartan decomposition at this size.
- **The determinant split.** $\det M=\det P\det V$, with $\det P=|\det M|>0$ and $|\det V|=1$; on $SL_2$ this forces $r=1$ and $\zeta=\pm1$, so the algebra's modulus is the matrix's positive factor up to scale.
- **The closed form of $P$.** By Cayley–Hamilton, for Hermitian $Y\ge0$ with eigenvalues not both zero, $\sqrt Y$ is a degree-one polynomial in $Y$ with coefficients $\sqrt{\lambda_\pm}$; so $P$ is computable without diagonalising.
- **The singular case.** $P$ has the rank of $M$, $V$ is an isometry off the kernel and zero on it, and for $M=uv^{\mathsf T}$ one has $MM^{\dagger}=\|v\|^2uu^{\dagger}$ and $P=\|v\|\,uu^{\dagger}/\|u\|$.
- **The failure at the origin.** $M\mapsto P$ is continuous everywhere; $M\mapsto V$ is not continuous at $0$, because the direction of $V$ depends on the direction of approach. The pair's rank-one and null-cone discussion has no such statement, and it is the reason the polar decomposition is a diffeomorphism only on the invertible locus.
- **The singular value decomposition.** $M=U\Sigma W^{\dagger}$ from $P=U\Sigma U^{\dagger}$ and $W=U^{\dagger}V$; the singular values are the eigenvalues of $P$; $\sum s_i^2=\operatorname{Tr}(MM^{\dagger})$; the rank is the number of nonzero $s_i$; the multiset of singular values equals the multiset of eigenvalue moduli exactly when $M$ is normal.
- **The two halves as exponentials.** $P=\exp(H)$ with $H$ traceless Hermitian and $V=\exp(K)$ with $K$ traceless anti-Hermitian, so the decomposition is the product of a boost and a rotor; this is the matrix face of the algebra's $M_bM_r$.

### 12. Rank-One Matrices and the Determinantal Variety

**What the pair has.** The operators article separates the three rank cases of the *operators* ($\operatorname{rank}T_{A,B}=2\operatorname{rank}A\cdot\ldots$) and mentions the Segre variety for the pair cone. Nothing about rank-one matrices as a variety.

**The ideas.**

- **The factorisation theorem.** A nonzero $M$ has rank one exactly when $M=uv^{\mathsf T}$ with $u,v\neq0$, and the pair $(u,v)$ is defined up to the reciprocal scaling $u\mapsto\lambda u$, $v\mapsto\lambda^{-1}v$.
- **The two strata.** The trace splits the cone: $v^{\mathsf T}u=0$ gives $M^2=0$, the **pure** stratum of nilpotents; $v^{\mathsf T}u\neq0$ gives $M/(v^{\mathsf T}u)$ an idempotent, the **non-pure** stratum. So "rank one" is two different geometric objects glued along nothing, and the pair's rank-two and rank-one examples sit in different strata without the vocabulary to say so.
- **Rank-one idempotents are pairs of lines.** A rank-one idempotent is determined by its image line and its kernel line, a pair of distinct lines; $E_{11}$ and $E_{22}$ are the two coordinate pairs.
- **The annihilators.** For $M=uv^{\mathsf T}$, $\{X:XM=0\}=\{X:Xu=0\}$, and $\{X:MX=0\}$ is the dual condition; both are two-dimensional, and the left and right annihilators are the minimal ideals of the covector and vector lines. This is the operator-level reading of the rank-one element, and it is what the pair's "kernel and image" discussion lacks.
- **The ranks of the one-sided operators.** $L_M$ and $R_M$ have rank $2\operatorname{rank}M$, so a rank-one element gives an operator of rank two — the value that the pair's rank formula attributes to "one matrix per side" without the stratum.
- **The determinantal variety.** $\mathcal{D}=\{M:\det M=0\}$ is the cone over the Segre quadric $\mathbb{P}^1\times\mathbb{P}^1$; it is smooth away from the apex, and the tangent cone at the apex is the whole space. The pair has no quadric and no singularity.
- **The projective picture.** The pure stratum is the graph of the projective duality between the vector and the covector line, a conic of bidegree $(1,1)$ inside $\mathbb{P}^1\times\mathbb{P}^1$; the non-pure stratum is its complement. The two rulings of the quadric are the two families of lines, one for $u$ and one for $v$.
- **The biquaternion reading.** $\mathcal{D}$ is the image of the null cone $N=0$ under $\mathsf M_2$, so the algebraic statement "zero divisor" and the geometric statement "singular" are the same statement; that identity is stated once, in topic 10, and never cashed out.
- **The scaled idempotent.** $P^2=P$ and $P\neq0$ is not nilpotent but is a zero divisor: $P(e_t-P)=0$. The pair says "zero divisors are the singular matrices" and does not exhibit this example, which is the one that shows why "zero divisor" is not "nilpotent".

### 13. Spin, Qubits and the Bloch Vector

**What the pair has.** Nothing. No Pauli matrix, no density matrix, no Bloch vector.

**The ideas.**

- **The Pauli matrices are the images of the Hermitian units.** $\sigma_k=i\mathsf M_2(\vec e_k)$, so $\mathsf M_2(\vec e_k)=i\sigma_k$; the Hermitian units of the algebra are $i\vec e_k$ and the standard physics basis is the same three matrices with the sign absorbed. The pair's §*The Images of the Four Units* is one substitution away from this and does not make it.
- **The Hermitian condition in coordinates.** $\tilde Q\in\mathbb{M}_+$ exactly when $Q_t$ is real and the three $Q_k$ are purely imaginary; the four real coordinates are then the weight of the identity and the three weights of the Pauli matrices.
- **The spin operators and their algebra.** $S_k=\frac12\sigma_k$; $[\sigma_i,\sigma_j]=2i\epsilon_{ijk}\sigma_k$ and $\{\sigma_i,\sigma_j\}=2\delta_{ij}$; the commutator is anti-Hermitian, hence in $\mathbb{M}_-$, so the generators of the $*$-unitary group are the *anti*-Hermitian elements and the observables are the Hermitian ones. This is the two-role statement that the pair's half-splitting almost makes.
- **Pure states.** $\rho(\vec u)=\frac12(I_2+\vec u\cdot\sigma)$ for a real unit vector: Hermitian, idempotent, trace one, determinant zero. $\rho(\vec u)+\rho(-\vec u)=I_2$, and the antipodal map on the sphere is the complement of the state. Every pure state is a rank-one projector and hence a line of $\mathbb{C}^2$, and it lies on the null cone with scalar part $\frac12$ — but not in the pure stratum, because it is not nilpotent. That single sentence is the missing link between topics 12 and 13.
- **General states and the Bloch ball.** $\rho=\frac12(I_2+\vec r\cdot\sigma)$ with $\vec r\in\mathbb{R}^3$; $\det\rho=\frac14(1-|\vec r|^2)$; positive semidefinite $\iff|\vec r|\le1$; the pure states are the boundary sphere, the maximally mixed state is the centre, and the state space is the trace-one slice of the positive cone of $\mathbb{M}_+$.
- **The Born rule.** $p_\pm=\frac12(1\pm\vec r\cdot\vec u)$; the convex splitting of any state into the two pure states along its own axis.
- **Reading the vector back.** $r_k=\operatorname{Tr}(\rho\sigma_k)$, so the three Bloch coordinates are the three traces against the Pauli matrices — the same trace pairing as everywhere else in the block.
- **The qubit as a spinor.** A pure state is a rank-one projector, hence a line, hence a point of $\mathbb{P}^1$; the Hopf fibration $S^3\to S^2$ is the passage from the normalised spinor to the state, and the central phase $e^{i\alpha}$ acts on the spinor and trivially on the algebra.
- **Where the correspondence stops.** The Pauli matrices are not elements of $\mathbb{B}$ (they are $i\vec e_k$); the identification $\mathbb{B}\cong M_2(\mathbb{C})$ does not by itself single out the Hermitian real form; and nothing in the topic evolves a state. Three honest limits, and the third is the one that keeps the block from claiming to be quantum mechanics.

### 15. $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ and the Determinant

**What the pair has.** One sentence: the four unit matrices have determinant one. The operators article has $GL_2\times GL_2$ and $PGL_2$ for the pairs.

**The ideas.**

- **The group isomorphism.** $\mathbb{B}^\times\cong GL_2(\mathbb{C})$ as complex Lie groups, with the inverse polynomial in the entries (adjugate over determinant), so the group is algebraic at this size.
- **The determinant sequence.** $1\to SL_2\to GL_2\xrightarrow{\det}\mathbb{C}^\times\to1$, exact; the splitting $\lambda\mapsto\operatorname{diag}(\lambda,1)$ is not central; there is no central splitting, because a central one would need $\lambda^2=1$ for all $\lambda$.
- **The covering.** $\mathbb{C}^\times\times SL_2\to GL_2$, $(\lambda,A)\mapsto\lambda A$, is surjective with kernel $\{(\pm1,\pm I_2)\}$ of order two; dimensions $1+3=4$.
- **The level sets.** $N=c$ is a smooth hypersurface for $c\neq0$; $N=1$ is $SL_2$, non-compact ($\operatorname{diag}(r,r^{-1})$); $N=0$ is the null cone, singular along the apex, the cone over $\mathbb{P}^1\times\mathbb{P}^1$.
- **$GL_2$ acts on itself.** $SL_2\times SL_2$ acts by $(A,B)\cdot M=AMB^{-1}$, and the orbits are the level sets of the norm — the group-theoretic statement of the modulus.
- **The compact real form.** $U(2)$, $SU(2)=U(2)\cap SL_2$ of real dimension three, and the polar decomposition $GL_2=U(2)\cdot H^{++}$.
- **The topology.** $GL_2(\mathbb{C})\simeq U(2)$, so $\pi_1(GL_2)=\mathbb{Z}$; the generator is the central phase. $SL_2$ is simply connected. These two facts are the reason the double covers of topic 15 exist at all.
- **The Bruhat decomposition.** $GL_2=B\sqcup BwB$ with $B$ the upper triangular group and $w$ the swap: two cells, of dimensions $3$ and $4$, and the cell $BwB$ is exactly the set of matrices with $c\neq0$. The pair's two-chart diagonalisation is the Bruhat cell decomposition in disguise.
- **The centre and $PGL_2$.** The centre is $\mathbb{C}^\times I_2$; $PGL_2=GL_2/\mathbb{C}^\times$; a class has a determinant only up to squares, $\det(\lambda M)=\lambda^2\det M$. This is why the pair's automorphism group is $PGL_2$ and not $SL_2$.
- **The three double covers.** Conjugation on $M_2(\mathbb{C})$, on the Hermitian matrices and on $\mathbb{P}^1$ all have kernel $\{\pm I_2\}$, so $SL_2$ covers the Lorentz group and the Möbius group at once, while $SU(2)$ covers $SO(3)$. The pair's operators article proves that every automorphism is inner and stops before the cover, which is the interesting half.

### 16. The Projective Line and the Möbius Action

**What the pair has.** Nothing.

**The ideas.**

- **The dictionary between lines and minimal left ideals.** $L\mapsto I_L=\{M:M(\mathbb{C}^2)\subseteq L\}$ is a bijection from $\mathbb{P}^1$ onto the minimal left ideals, with $L_\infty=\operatorname{span}\{e_1\}$ and $L_0=\operatorname{span}\{e_2\}$ as the two coordinate points. The pair's $S_\pm$ are two points of this line, and the line itself is the missing object.
- **The action.** $M\cdot L=ML$ is an action of $GL_2$ on $\mathbb{P}^1$, with kernel the scalars, hence an action of $PGL_2$; it is transitive, and the stabiliser of a point is a Borel subgroup.
- **The chart and the Möbius formula.** In the chart $z=b/d$ the action is $z\mapsto\frac{az+b}{cz+d}$, the fractional linear map; the two coordinate points are $z=0$ and $z=\infty$, and the point at infinity is the line of the first basis vector.
- **Triple transitivity and the cross-ratio.** The action is simply transitive on ordered triples of distinct points, so the only invariant of a quadruple is the cross-ratio; in bracket form it is the ratio of the four Plücker brackets $\langle\xi,\eta\rangle=\xi_1\eta_2-\xi_2\eta_1$, which makes its invariance under $GL_2$ a determinant identity $\det(MC)=\det M\det C$.
- **The idempotents as pairs of points.** A rank-one idempotent is a pair (image line, kernel line) with the two distinct; $E_{11}$ and $E_{22}$ are the two coordinate pairs; the conjugacy class of rank-one idempotents is the set of ordered pairs of distinct points, of dimension two.
- **The real structure.** The involution $\sigma$ induces a $\mathbb{C}$-antilinear map on $\mathbb{P}^1$ without fixed points (*check the chart*: the legacy gives $z\mapsto-1/\bar z$, and the fixed-point equation $z\bar z=-1$ has no solution). Its absence of fixed points is the statement that the real structure has no real line, which is why the biquaternion algebra has no "real" splitting of $\mathbb{P}^1$ into fixed and anti-fixed points.

### 17. The Hermitian Sandwich

**What the pair has.** Nothing. The operators article has $T_{A,B}$ and its Kronecker display, but never the sandwich $X\mapsto MXM^{\dagger}$.

**The ideas.**

- **The congruence.** $\Theta_M(X)=MXM^{\dagger}$ for invertible $M$; it preserves the Hermitian and the anti-Hermitian halves, and it preserves the null cone, because $\det(MXM^{\dagger})=|\det M|^2\det X$. It is a congruence and not a similarity, so it does not preserve the spectrum.
- **Sylvester's law.** A congruence by an invertible matrix preserves rank, inertia and signature of a Hermitian form; hence $\Theta$ acts on the Hermitian half preserving the inertia types $(2,0)$, $(1,1)$, $(0,2)$ — the strata of the Minkowski form $a^2-|\vec b|^2$.
- **The anti-Hermitian half as Minkowski space.** Writing an anti-Hermitian matrix as $i(aI_2+\vec b\cdot\sigma)$, the determinant is $-a^2+|\vec b|^2$; a unit-norm $M$ acts on this four-dimensional real space by $SO^{+}(1,3)$, and the general $M=r\zeta U$ scales it. This is the vector action of the algebra, at the $2\times2$ size, in one line.
- **The two halves are one action.** Multiplication by the central $i$ exchanges $\mathbb{M}_+$ and $\mathbb{M}_-$, reverses the determinant sign and preserves the null cone; so the two sandwiches are one representation read on the two halves.
- **The infinitesimal picture.** Differentiating at the identity gives $X\mapsto[\mathcal R,X]+\{\mathcal H,X\}$, the sum of a commutator with the anti-Hermitian part and an anticommutator with the Hermitian part; the action is faithful.
- **Which subspaces survive.** The sandwich preserves the two halves and the null cone always, and preserves the other four remarkable subspaces exactly when $M$ is a central multiple of a real unit quaternion. The table of "preserved / not preserved" is the geometric content of the six subspaces of topic 2, and the pair's closure table has no action to compare with.
- **The positivity cone.** $MXM^{\dagger}$ is positive semidefinite when $X$ is, so $\Theta$ preserves the cone; on the trace-one slice it is the map that a quantum channel would be, which is where this topic meets topic 13.

### 18. The Killing Form

**What the pair has.** Nothing.

**The ideas.**

- **The form.** $\kappa(X,Y)=\operatorname{tr}(\operatorname{ad}_X\operatorname{ad}_Y)$ on the real eight-dimensional Lie algebra $\mathfrak{gl}_2(\mathbb{C})$; the formula
  $$\kappa(X,Y)=8\operatorname{Re}\operatorname{tr}(XY)-4\operatorname{Re}\bigl(\operatorname{tr}X\operatorname{tr}Y\bigr).$$
- **The radical is the centre.** $\operatorname{ad}_{I_2}=0$, and on $\mathfrak{sl}_2$ the form is nondegenerate, so the radical is exactly the scalars, of real dimension two. The degeneration is the Lie-algebra form of "the algebra is a central extension of the simple one".
- **The traceless part and the signature.** The traceless matrices split into Hermitian and anti-Hermitian parts, orthogonal for $\kappa$; on $\mathfrak{su}(2)$ the form is negative definite, $\kappa(X,X)=-8\operatorname{tr}(XX^{\dagger})$; on the real traceless matrices it is $\kappa(X,Y)=8\operatorname{tr}(XY)$ of signature $(3,3)$. The pair's six-subspace splitting is the same split, read without the form.
- **The two real forms.** $\mathfrak{sl}_2(\mathbb{C})$ has two real forms up to isomorphism, the compact $\mathfrak{su}(2)$ and the split $\mathfrak{sl}_2(\mathbb{R})$, and $\kappa$ separates them by its sign. This is the Lie-algebra statement behind the second real structure of topic 14.
- **Invariance.** $\kappa(\operatorname{Ad}_P X,\operatorname{Ad}_P Y)=\kappa(X,Y)$, so the form is the invariant bilinear form of the Lie algebra; for $\mathfrak{sl}_2$ it is the unique one up to scale, and it is four times the trace form.
- **Relation to the trace form.** On $\mathfrak{sl}_2$, $\kappa=4\operatorname{tr}(XY)$; on $\mathfrak{gl}_2$ the trace form alone is degenerate on the centre, and $\kappa$ is $8\operatorname{Re}\operatorname{tr}(XY)$ corrected by the term $-4\operatorname{Re}(\operatorname{tr}X\operatorname{tr}Y)$ that removes the central direction. The comparison table is three lines and it is the reason the trace pairing of topic 9 is *not* the Killing form.

### 19. The Functional Calculus

**What the pair has.** Nothing beyond the matrix exponential mentioned in passing and the Cayley–Hamilton identity.

**The ideas.**

- **The calculus.** For $f$ holomorphic on a neighbourhood of the spectrum, $f(X)=\frac{1}{2\pi i}\oint_\gamma f(z)(z-X)^{-1}dz$; on a diagonalisable $X$ it is $C\operatorname{diag}(f(\lambda_+),f(\lambda_-))C^{-1}$, and on a Jordan block it is $f(\lambda)I_2+f'(\lambda)N$. That last term is the whole reason the calculus is not "apply $f$ to the eigenvalues".
- **The homomorphism and the spectral mapping.** $f(g(X))=(f\circ g)(X)$, and $\operatorname{spec}f(X)=f(\operatorname{spec}X)$.
- **The exponential.** $\exp$ of the series; $\det(e^X)=e^{\operatorname{tr}X}$; the closed form
  $$e^{\tilde Q}=e^{Q_t}\Bigl(\cos B\,I_2+\frac{\sin B}{B}\,\mathsf M_2(\vec Q)\Bigr),\qquad B^2=Q_x^2+Q_y^2+Q_z^2.$$
  which is the algebra's own exponential read in the model.
- **One-parameter subgroups.** Every one-parameter subgroup of $GL_2$ is $t\mapsto e^{tX}$ for a unique $X$; the four elementary subgroups are the central phase, the rotor, the boost and the unipotent one; every $e^{tX}$ lies in the centraliser of $X$, which is topic 5 again.
- **The image and the kernel.** $\exp$ maps onto $GL_2$ (every invertible matrix has a logarithm); $\exp X=I_2$ iff $X$ is diagonalisable with eigenvalues in $2\pi i\mathbb{Z}$. Surjectivity is false in general dimension and true here, which is a fact about $2\times2$ worth stating.
- **The logarithm.** Existence iff invertible; the branches on each eigenvalue; the degenerate case (a logarithm of $\lambda I_2+N$ must commute with $N$, hence be affine in $N$); the principal branch on $\mathbb{C}\setminus(-\infty,0]$ with its power series and its two compositions.
- **The derivative.** $d\exp$ and $d\log$ at the identity are the identity; $d\log$ in the eigenbasis involves the projectors, which is topic 4 again.
- **The square roots, as the classifier.** $Y^2=X$ forces $Y\in C(X)$; the three spectral cases with their root counts (four generically, fewer at coincident eigenvalues); the nilpotent has none; the closed form by Cayley–Hamilton, $Y=(\sqrt\delta\,I_2+X)/\sqrt{\tau+2\sqrt\delta}$ with $\tau=\operatorname{tr}X$ and $\delta=\det X$, up to the signs of the two square roots; the classification table of "which matrices have a root and how many".
- **The worked examples of the calculus.** $e^{2e_t+\vec e_x}$, $\sqrt{\operatorname{diag}(4,9)}$, the roots of a Jordan block, the absence of a root for $N$, the roots of $I_2$ (the traceless involutions) and of $0$ (the nilpotent cone).

---

## Also unwritten, and not in the list

**The columns, the rows and the spinor spaces.** The legacy block also held *$M_2(\mathbb{C})$ Representation : The Columns, the Rows and the Spinor Spaces* (170 lines), which is not in the request's list. It is the module-level companion of topic 3: the carrier $\mathbb{C}^2$ as a column, the dual as a row, the two spinor spaces as the left ideals, and the pairing between them. If topic 3 is written, this is its second half.

**The 2×2 matrix element representation.** The umbrella draft *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (559 lines) is the ancestor of the surviving model article and is fully absorbed into it. Nothing remains of it.

---

## If this is to be written

**The natural groupings.** The eleven missing topics are not eleven independent articles. They fall into four clusters, and each cluster shares one apparatus.

1. **The spectral cluster** — the centraliser (5), the Jordan basis (7), the functional calculus (19). One apparatus: the commutant, the minimal polynomial and the division into diagonalisable and Jordan. Written in this order, the third reuses the first two, and the derivative of the logarithm reuses the projectors of topic 4.
2. **The cone cluster** — rank-one matrices (12), the polar decomposition (11), the singular values. One apparatus: $M=uv^{\mathsf T}$, $P=|M|$, and the strata of the determinant. Topic 11 needs topic 12 for its singular case, and topic 12 needs the polar decomposition for its "distance to the cone".
3. **The group cluster** — $GL_2/SL_2$ (15), the Killing form (18), the projective line (16), the Hermitian sandwich (17). One apparatus: the action of the group on the space it acts on, and the invariant forms. The Killing form is the infinitesimal face of the sandwich, and the projective line is the action on the minimal ideals.
4. **The quantum pair** — spin, qubits and the Bloch vector (13), with the Hermitian sandwich (17) as its operator face.

**The five that are cheap.** Topics 1, 2, 3, 9 and 14 are residues: each is a section, not an article, and each fills a hole that the two survivors leave visibly open — the presentation (1), the mirror and the two blocks (2), the spinor planes (3), the four words (9) and the table of the four involutions (14).

**The one that is expensive.** The functional calculus (19) is 513 legacy lines and is the only topic of the list that is genuinely a subject rather than a chapter. It also duplicates material that exists elsewhere in the corpus at the general size, so the decision there is whether the $2\times2$ version says anything the general one does not — and it does: the closed forms, the four roots of a generic square root, and the surjectivity of the exponential.

**What must not be repeated.** The $4\times4$ articles of the biquaternion block own the uncompressed statements; the operators article owns the pair, the Kronecker display and the length; the $M_4(\mathbb{C})$ block owns the general Peirce machinery. Every article above should cite them rather than re-derive, and the value added is the entry-size computation, which is what the legacy drafts did well.
