# __The Computational Cost of Biquaternion Arithmetic__

## Introduction

The companion articles develop the biquaternion algebra as mathematics: its conjugations, its subspaces, its ideals, its spectrum. This article asks a different question about the same object. **What does one product cost?** A biquaternion has four complex coefficients, hence eight real parameters, and the naive count of the real multiplications needed to multiply two of them is not sixteen but **sixty-four**. That count can be reduced to **twenty-four**, and the reduction is not a programming trick: it is a bilinear identity, of the same family as Gauss's three-multiplication rule for complex numbers and as Karatsuba's rule for polynomials.

The result is interesting for a reason worth stating at the outset. The algebra $\mathbb{B}$ is isomorphic to the complex matrix algebra $M_2(\mathbb{C})$, and an isomorphism usually means that the two objects cost the same. They do — but the biquaternion form stores the same information in a smaller working array, and the bilinear identity exploits exactly the redundancy that the isomorphism creates. The algebra is therefore not a more expensive way of writing a complex matrix; it is a way of writing it that leaves the arithmetic cheaper or equal, component by component.

The material is drawn from a paper of Kaviraj, Komorovsky, Saue and Repisky on relativistic electronic structure, where the algebra arises as the natural language of time-reversal symmetric and antisymmetric matrix structures, and where the multiplication algorithm is implemented in a library (HMATLIB, inside the ReSpect package) for CPU and CPU/GPU execution. The paper's benchmarks are reported at the end of this article; they are its own measurements, not this corpus's.

The article owns the **cost accounting**: the count of real multiplications for a product, the same count for matrix-valued biquaternions, the block structure of the complex image that a machine consumes, and the reduction of a biquaternion Hermitian eigenvalue problem to smaller complex ones. The algebra itself, its representations and its spectral theory are owned by the mathematical corpus and are cited rather than repeated. The framework claims of the physics corpus are neither used nor tested here: a cheap product is a fact about arithmetic, not about the world.

The article is organised as follows. The next section fixes what is being counted. The two sections after it give the naive count and the bilinear reduction. The following three treat matrix-valued biquaternions, the complex image with its blocks, and the eigenvalue problem. Then come the framework reading, the source's benchmarks, the negative claims, and the summary.

## What Is Being Counted

The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, $e_1e_2 = -e_2e_1 = e_3$, and central scalar imaginary $i$. A general element is

$$
\tilde{Q} = Q_0e_0 + Q_1e_1 + Q_2e_2 + Q_3e_3, \qquad Q_\mu = q_\mu + iq'_\mu \in \mathbb{C},
$$

with the eight real parameters $q_\mu, q'_\mu$ of *Conventions in the Biquaternion Universe*. To multiply two elements a machine must combine their sixteen real parameters; the question is how many **real multiplications** the combination needs, additions being counted as free.

The count below is a count of multiplications of the algebraic kind, and its two levels are worth naming before they are used:

- a **coefficient product** is one multiplication of a coefficient of the first factor by a coefficient of the second;
- a **real product** is one multiplication of two real numbers, which is what a scalar product of two complex numbers costs in the naive scheme.

A complex multiplication costs four real multiplications and two real additions in the naive scheme, and three real multiplications and five real additions under Gauss's rule. The naive count for a biquaternion product is therefore four times its coefficient count; the reduced count exploits both the algebra and the complex arithmetic. Both reductions are exact: no approximation and no special case is involved.

The slice structure of *Conventions in the Biquaternion Universe* fixes what the extreme counts mean. An element of the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$ has all four coefficients real, and an element of the antiquaternion subspace $i\mathbb{H}_{\mathbb{B}}$ has all four coefficients purely imaginary; these are the two cheapest cases, and they are the cases that correspond to the time-reversal symmetric and antisymmetric matrix structures of the source. A general element of $\mathbb{B}$ uses all eight parameters and is the most expensive case. Throughout, "a product with all eight components active" means a product of two general elements.

## The Naive Count

Write the two factors as scalar part plus vector part, $\tilde{P} = S_1 + \mathbf{V}_1$ and $\tilde{Q} = S_2 + \mathbf{V}_2$, with $S$ complex scalars and $\mathbf{V}$ complex vectors. The product is

$$
\tilde{P}\tilde{Q} = \bigl(S_1S_2 - \mathbf{V}_1\cdot\mathbf{V}_2\bigr) + \bigl(S_1\mathbf{V}_2 + S_2\mathbf{V}_1 + \mathbf{V}_1\times\mathbf{V}_2\bigr).
$$

The sign of the cross term is the corpus's: with $e_1e_2 = e_3$ the outer product is $+\mathbf{V}_1\times\mathbf{V}_2$, so that $e_1e_2$ returns $e_3$; the source's convention reverses the order of the vector units and carries the opposite sign, which is a relabelling and changes no count.

Counting the coefficient products that appear above, one by one:

| term | coefficient products |
|---|---|
| $S_1S_2$ | $1$ |
| $\mathbf{V}_1\cdot\mathbf{V}_2$ | $3$ |
| $S_1\mathbf{V}_2$ | $3$ |
| $S_2\mathbf{V}_1$ | $3$ |
| $\mathbf{V}_1\times\mathbf{V}_2$ | $6$ |
| **total** | $\mathbf{16}$ |

The naive scheme therefore costs sixteen complex multiplications, or **sixty-four real multiplications**, for a product with all eight components active. On the real-quaternion slice the same scheme costs $4\times4 = 16$ real multiplications, and on the antiquaternion slice the purely imaginary coefficients can be multiplied as real numbers, again sixteen. The naive count is the baseline against which the next section's algorithm is measured.

## The Bilinear Product: Sixty-Four to Twenty-Four

The reduction rests on writing the four coefficients of the product as fixed linear combinations of **eight** products of linear combinations of the input coefficients. Four of the eight are the "corner" products of individual components; the other four are Hadamard products, that is products of the two vectors $(M_0,M_1,\mathsf{M}_2,M_3)$ and $(N_0,N_1,N_2,N_3)$ with the four rows of the Sylvester sign matrix of order four.

In the corpus's basis the scheme reads as follows. Let $\tilde{M} = M_0e_0 + \dots + M_3e_3$ and $\tilde{N} = N_0e_0 + \dots + N_3e_3$ with complex coefficients, and let the four Hadamard products be

$$
H_1 = (M_0+M_1+\mathsf{M}_2+M_3)(N_0+N_1+N_2+N_3),
$$
$$
H_2 = (M_0+M_1-\mathsf{M}_2-M_3)(N_0+N_1-N_2-N_3),
$$
$$
H_3 = (M_0-M_1+\mathsf{M}_2-M_3)(N_0-N_1+N_2-N_3),
$$
$$
H_4 = (M_0-M_1-\mathsf{M}_2+M_3)(N_0-N_1-N_2+N_3),
$$

and let the four corner products be $P_{00} = M_0N_0$, $P_{32} = M_3N_2$, $P_{13} = M_1N_3$, $P_{21} = \mathsf{M}_2N_1$. Then the coefficients $Q_\mu$ of the product satisfy

$$
4Q_0 = 8P_{00} - (H_1+H_2+H_3+H_4),
$$
$$
4Q_1 = (H_1+H_2-H_3-H_4) - 8P_{32},
$$
$$
4Q_2 = (H_1-H_2+H_3-H_4) - 8P_{13},
$$
$$
4Q_3 = (H_1-H_2-H_3+H_4) - 8P_{21}.
$$

The scheme uses eight coefficient products and nothing else: the Hadamard combinations supply each coefficient with the sign pattern of one Sylvester row, and the four corner products cancel the diagonal contributions that the Hadamard products carry along with them. The factors of two and four are the price of that cancellation; they are additions and scalings, which the count treats as free.

This is the corpus transcription of the source's scheme, which is stated there in the reversed vector-unit order. The source writes it as eight intermediate products $P_1,\dots,P_8$, with the four coefficient products $P_1 = M_1N_1$, $P_2 = M_4N_3$, $P_3 = \mathsf{M}_2N_4$, $P_4 = M_3N_2$ in its own numbering and the four Hadamard products $P_5,\dots,P_8$ of the same shape as $H_1,\dots,H_4$, and it gives the four coefficients as $Q_1 = 2P_1 - \tfrac14(P_5+P_6+P_7+P_8)$ and its three companions with the sign patterns $+\,+\,--\,$, $\,+\,-+\,-$ and $\,+\,\,--\,+$. The two forms differ only by the relabelling of the vector units; both were recomputed here and both reproduce the direct product exactly.

Each of the eight intermediate products is a complex multiplication, so the bilinear scheme alone costs $8\times4 = 32$ real multiplications, against the naive sixty-four. **Gauss's three-multiplication rule** for complex numbers,

$$
(M_R + iM_I)(N_R + iN_I) = (T_1 - T_2) + i(T_3 - T_1 - T_2), \qquad T_1 = M_RN_R,\ T_2 = M_IN_I,\ T_3 = (M_R+M_I)(N_R+N_I),
$$

evaluates each of the eight in three real multiplications instead of four, so the total becomes $8\times3 = 24$. The source reports that no further reduction of the count is possible for the algebra as a whole: twenty-four is the multiplication rank of the biquaternion product, in the sense in which three is the rank of the complex product and three that of the two-term polynomial product.

For the slices the scheme already terminates at the coefficient level: a real-quaternion product has real coefficients and needs the eight Hadamard and corner products alone, that is **eight** real multiplications against the naive sixteen; the same holds with purely imaginary coefficients. The reduction is therefore a factor of two on each slice and of $64/24 \approx 2.7$ on the full algebra.

**Verification.** The two forms of the scheme, the corner-Hadamard form above and the source's own, were each checked against the direct product rule on 100 random pairs of elements with coefficients of $|q_\mu| \le 5$ and $|q'_\mu| \le 5$, in exact integer arithmetic, with zero mismatches; the real-quaternion and antiquaternion slices were checked on 100 random pairs each, likewise with zero mismatches. The counts quoted in the tables were checked by counting the multiplications performed by the evaluated expressions.

## Matrix-Valued Biquaternions

The scheme above has coefficients that are complex *scalars*, and it is bilinear over the real numbers: every output is a scalar linear combination of the eight intermediate products. **Nothing in it uses the commutativity of the coefficients**, so it applies unchanged when the coefficients are replaced by matrices. That is the step from a biquaternion to a *matrix-valued* biquaternion, an element of $\mathbb{B}^{n\times m}$: each of the four coefficients becomes an $n\times m$ complex matrix, and the product rule keeps exactly its scalar-vector shape,

$$
Q_1Q_2 = \bigl(S_1S_2 - \mathbf{V}_1\cdot\mathbf{V}_2\bigr) + \bigl(S_1\mathbf{V}_2 + S_2\mathbf{V}_1 + \mathbf{V}_1\times\mathbf{V}_2\bigr),
$$

with the dot and cross products understood entrywise, in the order of matrix multiplication, and with the coefficients no longer commuting. The eight intermediate products are then products of matrices, evaluated with a single real matrix-multiplication kernel; the dot and cross products are absorbed into them and are never formed separately.

The counts therefore repeat at matrix level, with "real multiplication" replaced by "real matrix multiplication":

| case | naive | bilinear | bilinear with Gauss |
|---|---|---|---|
| general matrix-valued biquaternion | $64$ | $32$ | $\mathbf{24}$ |
| real-quaternion matrix | $16$ | $\mathbf{8}$ | $\mathbf{8}$ |
| antiquaternion matrix | $16$ | $\mathbf{8}$ | $\mathbf{8}$ |

One biquaternion product with all components active costs eight matrix-matrix products instead of the naive sixty-four, and Gauss brings it to twenty-four: the same arithmetic is obtained with $24/64$ of the multiplication work. What the scheme does **not** change is the asymptotic order: a matrix product is $O(n^3)$ in the dimension, and the constant is what has been reduced.

The memory side is worth recording next to the count. A matrix-valued biquaternion of size $n\times n$ holds four complex matrices, that is $8n^2$ real numbers; its complex image, defined in the next section, is a $2n\times 2n$ complex matrix, which holds $8n^2$ real numbers as well. The two representations of the same array are therefore the same size, and the source reports that under a 32-bit integer workspace limit the array form reaches roughly twice the dimension of the complex form before the limit binds — the limit being that of the eigensolver workspace rather than of the matrix itself.

## The Complex Image and Its Blocks

The object a machine actually consumes is not the algebra but its matrix image. For a matrix-valued biquaternion $\tilde{Q}$ with complex component matrices $Q_0,Q_1,Q_2,Q_3$ of size $n\times m$, the image is the $2n\times2m$ complex matrix

$$
M = \sum_{\mu=0}^{3} \Phi(e_\mu)\otimes Q_\mu, \qquad \Phi(e_0) = I_2,
$$

where $\Phi$ is the isomorphism of *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* and $\otimes$ is the Kronecker product, taken with $\Phi$ first: the indices of $\Phi$ are the block indices of the image and the array indices run inside the blocks. With $\Phi(e_k) = -i\sigma_k$ in the corpus convention the image is $I_2\otimes Q_0$ plus the three Pauli–Kronecker terms multiplied by $-i$, and the four quadrants of a square image, of size $n\times n$, are the blocks $A, B, C, D$ below. The order of the two factors is a convention, the two orders being exchanged by a permutation of indices; the source assembles it in the same order, and the corpus's array-level statement of the correspondence is in *The Clifford Algebra Representation*.

Three properties of this image are used constantly, and each is exact:

1. **It is a homomorphism for the entrywise product.** If the array product is taken entrywise, with each entry multiplied in $\mathbb{B}$, then the image of the product is the product of the images. Verified on 100 random arrays of sizes up to $3\times3$;
2. **Its trace is the biquaternion trace.** The ordinary trace of the $2n\times2n$ image equals $2\,\mathrm{tr}(Q_0)$, twice the trace of the scalar component matrix, which is exactly the corpus's trace $2\,\mathrm{Sc}$ summed over the diagonal. Verified on the same 100 arrays;
3. **Its dagger is the array dagger.** Transposing the array and applying the Hermitian conjugation in the algebra to every entry carries the image to the conjugate transpose. Verified on the same 100 arrays.

The inner $2\times2$ blocks of the image carry the slice structure. For a real-quaternion array, whose coefficients are complex matrices with real entries only, the image takes the **time-reversal symmetric** block form

$$
M^+ = \begin{pmatrix} A & B \\ -B^{*} & A^{*} \end{pmatrix}, \qquad A = Q_0 - iQ_3,\quad B = -iQ_1 - Q_2 ,
$$

and for an antiquaternion array, whose coefficients are purely imaginary, the **time-reversal antisymmetric** form

$$
M^- = \begin{pmatrix} G & H \\ H^{*} & -G^{*} \end{pmatrix}, \qquad G = Q_0 - iQ_3,\quad H = -iQ_1 - Q_2 .
$$

Both were verified entry by entry on 100 random arrays for each slice, in the corpus's $\Phi$ convention, and both are the standard statements that a matrix commuting with, or anticommuting with, the time-reversal operation has a Hermitian and an anti-Hermitian block structure. In the source's language the two forms are the objects of the two halves $\mathbb{H}_R$ and $i\mathbb{H}_R$ of the algebra, which are the corpus's $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$; the correspondence is with the two halves of the complex-conjugation split, and it is not the $\mathbb{M}_\pm$ split, a point returned to below.

## The Eigenvalue Problem

The most expensive routine of the source's library is not the product but the diagonalisation of a Hermitian matrix-valued biquaternion, and the arithmetic of the two is coupled through the image. LAPACK and its GPU counterparts provide no eigensolver for biquaternion matrices, so a Hermitian biquaternion array is mapped to its complex Hermitian image and handed to the standard complex Hermitian routine. The mapping costs no information: the image of a Hermitian biquaternion array is a Hermitian complex matrix, because the dagger of the array is the conjugate transpose of its image.

The economy comes from the blocks. When the image is **block diagonal**,

$$
M = \begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix},
$$

the problem separates into two diagonalisations of half the dimension, with a further reduction when the blocks are related by symmetry. When the image is **block anti-diagonal**,

$$
M = \begin{pmatrix} 0 & A \\ B & 0 \end{pmatrix},
$$

a Hadamard-type unitary transformation turns it into a block-diagonal matrix whose two blocks differ by a sign. With

$$
U_\alpha = \frac{1}{\sqrt2}\begin{pmatrix} I & I \\ \alpha I & -\alpha I \end{pmatrix}, \qquad |\alpha| = 1 ,
$$

one has $M' = U_\alpha^{\dagger}MU_\alpha$ block diagonal exactly when $\alpha^{*}B = \alpha A$, and then the blocks are $\alpha A$ and $-\alpha A$. The relevant root is fixed by the relation between the two non-zero blocks: when they are opposite, $B = -A$, the condition holds for $\alpha = \pm i$, and when they are equal, $B = A$, for $\alpha = \pm 1$. Both occur in the source's symmetry classes, for a single active vector component: $e_2$ alone gives $B = -A$ and $e_1$ alone gives $B = A$, while $e_3$ alone is already block diagonal and needs no rotation. When the two blocks are not simply related, the unitary matrix is completed by a complex matrix $G$ built from the singular value decomposition $A = U\Sigma V^{\dagger}$ of the upper block as $G = VU^{\dagger}$, which restores the condition $AG = (AG)^{*}$.

The identity was verified on 100 random block-anti-diagonal matrices of the stated form, with the two blocks linked by $B = \alpha^2A$ and with the four fourth roots of unity as $\alpha$, in exact arithmetic and with zero mismatches. It is a statement of linear algebra — a rotation of a two-block matrix into its eigenbasis — and the biquaternion content is only the guarantee that the blocks carry the stated structure, so that the reduction applies.

## The Cost in the Framework's Terms

The two splits of the algebra do not align, and the arithmetic makes the misalignment concrete.

The eight real parameters split into the real-quaternion and antiquaternion halves, $\mathbb{B} = \mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$, on the criterion of complex conjugation, and that is the split the multiplication algorithm respects: when both factors lie in one half the product costs eight real multiplications instead of twenty-four, because the coefficients are then real or purely imaginary and the complex step of the scheme disappears. The corpus's sector split $\mathbb{B} = \mathbb{M}_-\oplus\mathbb{M}_+$ cuts across it, as *Conventions in the Biquaternion Universe* records: an element of $\mathbb{M}_-$ has an imaginary scalar part and a real vector part, so it uses one parameter of the antiquaternion half and three of the real-quaternion half. A sector-restricted problem is therefore **not** automatically the cheap one; only the complex-conjugation halves are, and a product whose factors mix the halves costs what the full algebra costs.

The trace is where the arithmetic and the physics meet most directly. The corpus's trace, $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$, is the Born rule; the machine's trace, taken on the complex image of a matrix-valued biquaternion, is the same number. The probability read off the arithmetic is the probability the algebra defines, with no normalisation imported from the implementation.

Beyond the trace and the block structure, the framework enters the cost accounting only through the problem's symmetry. The source's whole construction rests on the fact, developed in the corpus's articles on Kramers degeneracy, that in a time-reversal symmetric problem the Hamiltonian is real-quaternion and in a time-reversal antisymmetric problem it is purely imaginary-quaternion; and it is precisely those two restricted classes that the eight-multiplication regime serves. A problem with both, such as a magnetic perturbation or an open-shell non-collinear system, is the twenty-four-multiplication case. The cost therefore organises itself along the corpus's symmetry classes rather than along its sectors.

## The Benchmarks

The source measures a library, not a theorem, and the numbers below are its own on a single NVIDIA H200 system, with the corresponding runs on A100 and GH200 systems reported in its appendix. The multiplication kernel is the bilinear scheme of this article for the biquaternion library, against an isomorphic complex-matrix library of the same package, at matrix dimension $N = 44000$ with all components active:

| comparison | pure CPU | hybrid CPU/GPU |
|---|---|---|
| biquaternion, bilinear vs complex | $\approx 1.2\times$ | $\approx 2.7\times$ |
| real quaternion, bilinear vs complex | $\approx 3.5\times$ | $\approx 7.3\times$ |

The real-quaternion case gains more because its naive count is already sixteen and its bilinear count eight, so less of the advantage is spent on complex arithmetic. For the Hermitian eigenvalue problem at $N = 43000$, the complete CPU/GPU workflow — including the biquaternion-to-complex mapping and the host-device transfers — is reported as approximately $12$ times faster than the CPU oneAPI MKL route and $61$ times faster than the NVHPC OpenBLAS route.

The breakdown of the diagonalisation time on the H200 is worth one table, because it shows where the time goes as the dimension grows:

| $N$ | total (s) | eigensolver (s) | transfers (s) |
|---|---|---|---|
| $8000$ | $2.733$ | $1.077$ | $1.248$ |
| $16000$ | $11.867$ | $6.263$ | $4.948$ |
| $24000$ | $31.237$ | $19.015$ | $11.128$ |
| $32000$ | $64.678$ | $43.288$ | $19.651$ |
| $40000$ | $114.937$ | $81.708$ | $30.654$ |
| $43000$ | $139.173$ | $100.884$ | $35.426$ |

Host-device transfer accounts for about $46\%$ of the total at $N = 8000$, falling to about $26\%$ at $N = 43000$ as the cubic eigensolver overtakes it. Two further facts of the source's implementation belong here because they are consequences of the array form. The backend eigensolver's workspace outgrows a signed 32-bit index at $N \approx 32760$ on the CPU route and $N \approx 23170$ on the GPU route, and the library switches automatically to the 64-bit interface there; and the eight-component array reaches a larger dimension than the complex image before the 32-bit limit binds, which the source reports as a doubling of the accessible dimension from about $46000$ to about $92000$.

The numbers are hardware-specific and were not reproduced in this corpus. What is transferable is the count: eight matrix products instead of sixty-four, twenty-four real products instead of sixty-four, and the reduction of a Hermitian problem to two of half the dimension where the blocks permit it.

## What Is Not Claimed

1. **Biquaternions are not claimed to be cheap in general.** The advantage is measured against the naive component-wise algorithm and the isomorphic complex one; it depends on how many of the eight components are active, and a problem using one half of the algebra is cheaper than one using both.
2. **This is not a physical result.** The multiplication count for an algebra cannot support or refute any claim about which algebra describes the world. The framework's use of the algebra is the subject of the other physics articles.
3. **The asymptotic cost is unchanged.** The bilinear scheme reduces the constant of an $O(n^3)$ matrix product and does nothing to the exponent. The eigenvalue problem remains cubic, and the GPU gains largely come from parallelism rather than from the count.
4. **Twenty-four is the optimal count for the full algebra**, as the source reports; it is not optimality for every problem, and a problem with fewer active components admits smaller counts by the omission of terms.
5. **The benchmarks are the source's.** They are reported for their shape and their order of magnitude, not reproduced here, and they belong to particular hardware, libraries and compiler stacks.
6. **The corpus's mathematical account is unchanged.** The articles on the matrix representations, the ideals, the spectral theory and the norm own the algebra; this article adds a cost to objects they define and alters none of them.

## Physical Readings

The counts can be read as the price of the two-sector description. The real count of a product is the count of a pair of four-vectors, the block forms of the two halves are the real and the imaginary sectors, and Gauss's three-multiplication rule is a statement about the complex structure, so the arithmetic's structure and the algebra's structure are the same list. Read on the forms, the fact that the four-product lattice costs what it costs is the computational face of the multiplication table that fixes the physical products.

## Summary

Multiplying two general biquaternions naively costs sixteen complex multiplications, that is sixty-four real multiplications. The bilinear scheme of the source — the general quaternionic bilinear identity evaluated in eight intermediate products, combined with Gauss's three-multiplication rule for each complex product — brings the count to twenty-four: eight Hadamard products of the two coefficient vectors, four corner products, and Gauss's rule, with no further reduction possible for the full algebra. On the real-quaternion and antiquaternion halves the scheme stops at eight real multiplications against the naive sixteen, because the coefficients are already real or purely imaginary.

The same scheme applies unchanged to matrix-valued biquaternions, because it is bilinear with scalar coefficients and never uses commutativity: a fully populated matrix-valued product costs twenty-four real matrix-matrix multiplications instead of sixty-four, and a real-quaternion one eight instead of sixteen. The memory of the array form equals that of its $2n\times2n$ complex image, and the array form reaches roughly twice the dimension before a 32-bit workspace limit binds.

The image is the object the machine consumes, and its structure is the corpus's structure: a real-quaternion array is a complex matrix with the time-reversal symmetric block form, an antiquaternion array one with the time-reversal antisymmetric form, the image of the entrywise product is the product of the images, the trace of the image is the biquaternion trace $2\,\mathrm{Sc}$, and the image of the dagger is the conjugate transpose. A Hermitian biquaternion eigenvalue problem is mapped to the complex image and reduced, when the blocks are diagonal or anti-diagonal, to two problems of half the dimension by a Hadamard-type unitary rotation.

The split the arithmetic respects is $\mathbb{B} = \mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$, not the sector split $\mathbb{B} = \mathbb{M}_-\oplus\mathbb{M}_+$; the two cuts cross, so a sector-restricted problem need not be the cheap one. The source's measurements on modern CPU and GPU systems show the count turning into speed, by factors from about $1.2$ to about $7.3$ on multiplication and by about $12$ and $61$ on diagonalisation, at dimensions in the tens of thousands. All of it is arithmetic about an algebra: it neither supports nor threatens the claim that the algebra is the world's.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_1e_2=e_3$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $Q_\mu=q_\mu+iq'_\mu$ | Complex coefficients; the eight real parameters are $q_\mu,q'_\mu$ |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | Real-quaternion and antiquaternion halves, the complex-conjugation split |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Material and informational sectors, the dagger split, crossing the halves |
| $S_1+\mathbf{V}_1$, $S_2+\mathbf{V}_2$ | Scalar and vector parts of the two factors |
| $H_1,\dots,H_4$ | The four Hadamard (Sylvester) products of the coefficient vectors |
| $P_{00},P_{32},P_{13},P_{21}$ | The four corner products, in the corpus basis |
| coefficient product | one product of a coefficient of one factor by a coefficient of the other |
| real product | one product of two real numbers; a naive complex product costs four |
| $24$ | the multiplication count of one general biquaternion product, corner–Hadamard with Gauss |
| $8$ | the count on either half, $\mathbb{H}_{\mathbb{B}}$ or $i\mathbb{H}_{\mathbb{B}}$ |
| $\tilde{Q}\in\mathbb{B}^{n\times m}$ | A matrix-valued biquaternion; four coefficient matrices of size $n\times m$ |
| $M=I_n\otimes\Phi(Q_0)+\sum_k\Phi(e_k)\otimes Q_k$ | The complex image, size $2n\times2m$ |
| $M^+=\begin{pmatrix}A&B\\-B^{*}&A^{*}\end{pmatrix}$ | Image block of a real-quaternion array |
| $M^-=\begin{pmatrix}G&H\\H^{*}&-G^{*}\end{pmatrix}$ | Image block of an antiquaternion array |
| $\mathrm{tr}(M)=2\,\mathrm{tr}(Q_0)$ | The image trace is the biquaternion trace $2\,\mathrm{Sc}$ on the diagonal |
| $U_\alpha=\frac{1}{\sqrt2}\begin{pmatrix}I&I\\\alpha I&-\alpha I\end{pmatrix}$ | Hadamard-type unitary, $|\alpha|=1$, $M$ block anti-diagonal |
| $\alpha^{*}B=\alpha A$ | The condition for $U_\alpha^{\dagger}MU_\alpha$ to be block diagonal |
| $G=VU^{\dagger}$ | The completing matrix from the SVD $A=U\Sigma V^{\dagger}$ |

## Further Reading

- S. Kaviraj, S. Komorovsky, T. Saue and M. Repisky, "Biquaternion Algebra with Bilinear Multiplication: A General, Elegant, and Computationally Advantageous Framework for Relativistic Electronic Structure Calculations on CPUs and GPUs", arXiv:2609.02081 [physics.chem-ph] (2026), for the bilinear multiplication algorithm, the eight-component array layout, the Hadamard structure-aware diagonalisation, the block form of the Hermitian eigenvalue problem, and the benchmarks reported here.
- T. D. Howell and J.-C. Lafon, "The complexity of the quaternion product", Technical Report, Cornell University, as cited in the source, for the original bilinear quaternion product that the biquaternion algorithm extends.
- Donald E. Knuth, *The Art of Computer Programming*, Vol. 2: *Seminumerical Algorithms*, 3rd ed. (Addison-Wesley, 1997), §4.6.4, for the three-multiplication scheme for complex numbers and for the multiplication-rank framework in which the count of twenty-four is optimal.
- K. G. Dyall and K. Fægri Jr., *Introduction to Relativistic Quantum Chemistry* (Oxford University Press, 2007), for the relativistic electronic-structure setting, in which the time-reversal symmetric and antisymmetric matrix structures arise.
- T. Saue, "Relativistic Hamiltonians for chemistry: A primer", *ChemPhysChem* **12** (2011) 3077–3094, for the four-component Dirac Hamiltonian, its symmetry structure, and the time-reversal classes that the cost classes follow.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Clifford and matrix identifications of the algebra used in the complex image.
- The mathematical companions *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, *Biquaternion Objects and Their Matrix Correspondences* and *Biquaternion Spectral Theory*, for the isomorphism $\Phi$ used in the image, the index of the algebra's objects against their matrix images, and the spectral theory that the diagonalisation here serves.
- The physics companions *Conventions in the Biquaternion Universe* and *Kramers Degeneracy and Antiunitary Symmetry in Biquaternionic Form*, for the parameter conventions, the crossing of the two decompositions of the eight parameters, and the time-reversal classes.
