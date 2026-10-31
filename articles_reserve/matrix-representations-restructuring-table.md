# __Matrix Representations : The Restructuring Table__

## Introduction

This table is the working plan for the gathered series *Matrix Representations*. One row is one article. The four content columns say what that article carries in each of the three displays and what it carries independently of them.

The three displays are the $4\times4$ coefficient frame, the $2\times2$ entry model and the $4\times4$ Peirce frame, in the order of the columns. The coefficient frame is written $S_3$ because its vector part is the set $\{\vec e_x,\vec e_y,\vec e_z\}$; the name records the set. The ordered frame is only $C_3$-covariant, and an odd permutation exchanges the left and right families. The Peirce frame is written z because its idempotent pair is built on $\vec e_z$. The $2\times2$ model is the entry model: its four entries are the four coefficients, through $\mathsf M_2(\vec e_k)=-i\sigma_k$.

**The columns.**

1. The title, with the common prefix *Matrix Representations :*.
2. What the article states once, in a form that no frame changes: definitions, invariants, laws.
3. What exists only, or differently, in the $S_3$ frame.
4. What exists only, or differently, in the $2\times2$ entry model.
5. What exists only, or differently, in the z frame.

**How to read an empty cell.** An empty cell means the subject has no content in that display. There are three: the $2\times2$ cells of items 14, 15 and 16, which are operators on the four-dimensional carrier and have no $2\times2$ form. Every other cell carries content. The $S_3$ cells of items 11 and 12 carry only the determinant of the change, because their basis is chosen per element and the $S_3$ frame is fixed for the algebra.

## The Table

| # | Title | Common | $S_3$ frame, $4\times4$ | $2\times2$ entry model | z frame, $4\times4$ |
|---|---|---|---|---|---|
| 1 | Matrix Representations : The Models and the Change of Frame | $\mathbb{B}\cong M_2(\mathbb{C})$; the bracket $[F]_{\mathcal{B}}$; the change law $[F]_{\mathcal{B}'}=C^{-1}[F]_{\mathcal{B}}C$; entries are frame-dependent, trace, determinant, spectrum and rank are not | the explicit $[\mathsf M_4^{L}]_{\mathrm{coef}}$; the change $C_\Pi$ and $\det C_\Pi=-\tfrac14$ | the four assignments $\mathrm I_2,-i\sigma_1,-i\sigma_2,-i\sigma_3$; $\operatorname{tr}=2Q_t$; $\det=\langle\tilde Q\rangle_\natural$ | $\mathsf M_4^{L}=I_2\otimes\mathsf M_2$; $\operatorname{diag}(B,B)$; $\mathsf M_4^{R}=\mathsf M_2^{\mathsf T}\otimes I_2$ |
| 2 | Matrix Representations : The Product, the Trace and the Determinant | multiplicativity; $\operatorname{tr}=4Q_t$ in $4\times4$ and $2Q_t$ in $2\times2$; $\det=\langle\tilde Q\rangle_\natural^2$ and $\langle\tilde Q\rangle_\natural$; unit criterion $\langle\tilde Q\rangle_\natural\neq0$ | the product rule with signed entries; every entry is one coefficient with a sign | the Pauli assignment; the product rule; the adjugate and the inverse | $I_2\otimes B$; $\det(I_2\otimes B)=\det(B)^2$; the unit table |
| 3 | Matrix Representations : The Six Subspaces as Matrix Conditions | six overlapping subspaces of real dimensions $2,6,4,4,4,4$, cut out by the signs of the four conjugations; not a direct sum; the table | entrywise conditions; $\natural$ is transposition; the real forms are entrywise real | conditions in $X$, $X^{\mathsf T}$, $X^{\dagger}$ and $\operatorname{adj}X$ | conditions on the single block $B$, each repeated twice |
| 4 | Matrix Representations : The Four Words and the Four Traces | the four products read as four traces; the trace pairing; the conjugate of a word | the four slots $XY$, $X^{\mathsf T}Y$, $XY^{\dagger}$, $X^{\mathsf T}Y^{\dagger}$; entrywise traces | the same four words in $2\times2$; the pairing with its normalisation | the tensor reading; the four traces on $\mathbb{B}_L$ and $\mathbb{B}_R$ |
| 5 | Matrix Representations : Trace, Determinant and the Biquaternion Norm | the characteristic polynomial; the four norms as invariants | the explicit matrix; $\operatorname{tr}=4Q_t$, $\det=\langle\tilde Q\rangle_\natural^2$; the level sets of the determinant | $\lambda^2-2Q_t\lambda+\langle\tilde Q\rangle_\natural$; the level sets | $\det(I_2\otimes B)=\det(B)^2$; the spectrum $\lambda_\pm$ twice |
| 6 | Matrix Representations : The Conjugations and the Adjoints | the four involutions; the adjugate; the four adjoints | $\natural$ is transposition: the reason the frame exists | $\natural=\operatorname{adj}$; $*=\dagger$; $\bar{\cdot}$ entrywise | $\natural$ is $C M^{\mathsf T}C^{-1}$ with $C=-\sigma_2\otimes\sigma_2$; the two mixed units exchanged |
| 7 | Matrix Representations : The Killing Form | one scalar $\kappa$ for both models; radical the centre; $\kappa=-8\vec X\cdot\vec Y$ on the vector part | the coordinate form; $\kappa=2\operatorname{tr}(XY)-\tfrac12\operatorname{tr}X\operatorname{tr}Y$ | $\kappa=4\operatorname{tr}(XY)-2\operatorname{tr}X\operatorname{tr}Y$; the $\mathfrak{sl}_2$ form | the same formula with the $4\times4$ trace, doubled against $2\times2$ |
| 8 | Matrix Representations : $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ and the Determinant | the unit group; the determinant sequence; the level sets of the norm; the centre; the covers | the entrywise determinant; the Bruhat decomposition | $SL_2$; the Bruhat cells; $SU(2)\to SO(3)$ and $SL_2(\mathbb{C})\to SO^{+}(1,3)$ | $\det(I_2\otimes B)=\det(B)^2$; the two copies of the group |
| 9 | Matrix Representations : Peirce Coordinates, Matrix Units and the Spinor Planes | the Peirce table; the coordinate isomorphism; four corners; two planes | the units $E_{ij}$ as coefficient matrices | the four entries are the four corners; the columns are the spinors; $E_{12}$ and $E_{21}$ nilpotent | the two coordinate planes of the carrier; the columns as their bases; the nilpotents as off-diagonal units |
| 10 | Matrix Representations : The Spectral Projectors | $\rho_\pm$ idempotent, complementary, commuting with $M$; trace $2$ and rank $2$ in $4\times4$, trace $1$ and rank $1$ in $2\times2$ | the explicit matrices in coefficient coordinates | $\rho_\pm=\tfrac12(\mathrm I_2\mp iX/B)$ with $X=\mathsf M_2(\vec Q)$; rank one | $\rho_\pm=\tfrac12(\mathrm I_4\pm\mathsf M_4^{L}(\vec\Xi))$; diagonal on the standard axis; general element by conjugation |
| 11 | Matrix Representations : The Eigenbasis and the Diagonalising Matrix | four vectors, two per eigenvalue; $\lambda_\pm=Q_t\pm iB$; the determinant of the change is fixed | only the change: $C_\Pi C_Q^{(4)}$, determinant $\tfrac14$ | $C_Q$; $\det C_Q=2B(B-Q_z)$; the two charts | $C_Q^{(4)}$, determinant $-1$; $\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$; two copies |
| 12 | Matrix Representations : The Jordan Basis and the Jordanising Matrix | one eigenvalue; two blocks of size two; the determinant of the change is fixed | $\tfrac14$ in the corner order, $-\tfrac14$ in the chain order | $J_2(Q_t)$; the singular value $s=\sqrt{2\langle\vec Q\rangle_*}$ | $J_2(Q_t)\otimes\mathrm I_2$; the freedom is the invertible commutant $GL_2(\mathbb{C})\ltimes M_2(\mathbb{C})$, with $*$-unitary part $U(2)$ |
| 13 | Matrix Representations : The Centraliser and the Double Centraliser | the commutant; the three spectral types; the double centraliser; dimension $2$ and $4$ in $2\times2$, $4$ and $16$ in $4\times4$ | the commutant as the matrices solving $MX=XM$ entrywise | $\mathbb{C}[X]=\operatorname{span}\{\mathrm I_2,X\}$, dimension $2$ | the commutant is the right multiplications, dimension $4$ |
| 14 | Matrix Representations : The Left Regular Operators | the law; the kernel and the image; the rank trichotomy; $\operatorname{rank}=2\operatorname{rank}(B)$; the spectrum $\lambda_\pm$ twice | the explicit matrix; $\operatorname{tr}=4Q_t$; $\det=\langle\tilde Q\rangle_\natural^2$ | | $I_2\otimes B$; the four matrices $L_\mu$ of the units |
| 15 | Matrix Representations : The Right Regular Operators | the anti-representation law; the kernel and the image; $\operatorname{rank}=2\operatorname{rank}(B)$; the spectrum | $D\mathsf M^{\mathsf T}D$ | | $B^{\mathsf T}\otimes I_2$; the exchange $S$ |
| 16 | Matrix Representations : The Two-Sided Operators | $T_{\mu\nu}=L_\mu R_\nu$; the sixteen are a basis of $M_4(\mathbb{C})$; the composition; the cone of products | signed permutations of determinant $1$, orthogonal for Hilbert–Schmidt | | $\mathsf M_2(b)^{\mathsf T}\otimes\mathsf M_2(a)$; the gamma frame; $\gamma_5$ |
| 17 | Matrix Representations : The Hermitian Sandwich | $\Theta_{\tilde Q}(X)=\tilde QX\tilde Q^{*}$; the two halves and the null cone preserved for every invertible element; the four other subspaces preserved exactly for central multiples of real unit quaternions; $\Theta$ multiplicative exactly for $*$-unitary $M$ | the four-vector form on the anti-Hermitian half; the Lorentz matrix | $MXM^{\dagger}$; Lorentz on the anti-Hermitian half, real congruence on the Hermitian half | $\operatorname{conj}(B)\otimes B$; the two halves |
| 18 | Matrix Representations : The Functional Calculus | $f(M)$ by the homomorphism; the exponential, the logarithm, the square root; the group law; the branches | the series entrywise; the determinant and the trace of $f$ | $f(X)=C_Q\operatorname{diag}(f(\lambda_\pm))C_Q^{-1}$; the kernel: eigenvalues in $2\pi i\mathbb{Z}$, not discrete | $f(I_2\otimes B)=I_2\otimes f(B)$; the closed-form exponential |
| 19 | Matrix Representations : The Polar Decomposition of a Matrix | $M=UP$; $P=(M^{\dagger}M)^{1/2}$; the singular case | the explicit $P$ in coefficient coordinates | the closed form of $P_2$; the SVD; the boost reading | $P=I_2\otimes P_2$ |
| 20 | Matrix Representations : Rank-One Matrices and the Determinantal Variety | the rank stratification; $\operatorname{rank}=2\operatorname{rank}(B)$; the determinantal variety; the annihilators; the nilpotents | the determinant defines the variety; the two strata in signed coordinates | rank one; the two strata; the annihilator planes | the two strata in the block $B$ |
| 21 | Matrix Representations : Spin, Qubits and the Bloch Vector | the algebra of the spin operators; eigenvalues $\pm\hbar/2$; the Born rule | the coefficient matrices of $i\vec e_k$ | the Pauli matrices; pure states; the Bloch vector | $\Sigma_k$ block-diagonal, $I_2\otimes\sigma_k$ up to sign; two copies of the qubit, each eigenvalue twice |
| 22 | Matrix Representations : The Projective Line and the Möbius Action | lines as minimal left ideals; the $GL_2(\mathbb{C})$ action; the cross-ratio | the planes in coefficient coordinates | $\mathbb{C}P^1$; the Möbius formula; the idempotents; the Plücker form | the two minimal left ideals are the two coordinate planes |
| 23 | Matrix Representations : Worked Examples | eight elements; the common checklist of invariants | each matrix in the coefficient frame | each $2\times2$ matrix | each matrix in the Peirce frame |

## What the Table Shows

**The common column carries more than expected.** Items 2, 5 and 19 state their result once and the three displays are corollaries. Item 7 states one scalar; its matrix formula is normalised per model, $2\operatorname{tr}(XY)-\tfrac12\operatorname{tr}X\operatorname{tr}Y$ in $4\times4$ and $4\operatorname{tr}(XY)-2\operatorname{tr}X\operatorname{tr}Y$ in $2\times2$, and the two agree because the trace doubles.

**Three subjects have no $2\times2$ form.** Items 14, 15 and 16 are operators on the four-dimensional carrier. The $2\times2$ model represents the element, not the operator, so the cell is empty by construction, not by omission. Item 21 is the borderline case: the spin operators exist in both, but the $4\times4$ version is two copies of the $2\times2$ one.

**Two subjects have no $S_3$ operator display.** Items 11 and 12 choose a basis adapted to the element. The $S_3$ frame is fixed for the algebra, so it cannot host a per-element basis; its only content is the determinant of the change, $\tfrac14$.

**The z frame is the only place where the $2\times2$ is a compression.** In the Peirce frame the left regular matrix is $I_2\otimes B$, so the $2\times2$ block is visible twice. In the coefficient frame no block of $\mathsf M_4^{L}$ equals $B$ or $-B$. Items 14, 19 and 20 record the consequence.

**Three rows need a note.** Item 1 absorbs *The General Endomorphisms*; items 11 and 12 are the existing spectral articles, kept apart because their regimes differ.

**Item 1 is load-bearing.** Every other row names a frame, and item 1 is the only place where the change law and $C_\Pi$ are fixed. Removing it would make the other 22 rows unverifiable against each other.

## Progress

Written so far, in table order, under `articles_maths/`:

1. `matrix-representations-the-models-and-the-change-of-frame.md`
2. `matrix-representations-the-product-the-trace-and-the-determinant.md`
3. `matrix-representations-the-six-subspaces-as-matrix-conditions.md`
4. `matrix-representations-the-four-words-and-the-four-traces.md`
5. `matrix-representations-trace-determinant-and-the-biquaternion-norm.md`
6. `matrix-representations-the-conjugations-and-the-adjoints.md`
7. `matrix-representations-the-killing-form.md`
8. `matrix-representations-gl2-sl2-and-the-determinant.md`
9. `matrix-representations-peirce-coordinates-matrix-units-and-the-spinor-planes.md`
10. `matrix-representations-the-spectral-projectors.md`

The old files are untouched. The new files are not yet in `maths.md`.
