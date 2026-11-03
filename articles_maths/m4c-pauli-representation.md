# __$M_4(\mathbb{C})$ Pauli Representation__

## Introduction

**The subject.** The left and right regular matrices of a biquaternion, written in the Peirce frame that the root $\vec\Xi=i\vec e_z$ generates, and what that frame makes easy: the tensor display of the two matrices, the idempotents among the frame vectors, the pure swap that carries one matrix to the other, and the six subspaces as matrix conditions. The products, the coefficient matrix and the length are the subject of its companion, *$M_4(\mathbb{C})$ Pauli Representation : Operators*.

**The method.** One element generates the frame. The root is a vector whose square is the unit, $\vec\Xi^2=e_t$; its two spectral halves $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$ are idempotents, and the two mixed units $\vec\Upsilon_\pm=\tfrac12(i\vec e_x\pm\vec e_y)$ fill the off-diagonal slots of the Peirce decomposition. The frame is
$$
\mathcal{P}=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-),
$$
and the root is the only choice made in the article: the frame, the four coordinates, the $2\times2$ block and both matrices follow from it. §*The Root and the Peirce Frame* performs the construction.

**The order of the article.** The frame is built first, from a root and the multiplication table (§*The Root and the Peirce Frame*). The left family is then read by columns (§*The Left Family*), the right family by the same construction on the other side (§*The Right Family*), and the matrix that carries one to the other is a swap of two tensor slots (§*The Stitch Between the Two Families*). Every other frame is a conjugate of this one (§*Every Frame Is a Conjugate of This One*), and the conjugation that reaches the axis-free frame is computed in full, one entry at a time, in §*The Switch to the Axis-Free Matrices*: the two matrices $C_{\Pi}$ and $C_{\Pi}^{-1}$, their four columns, the two $2\times2$ blocks they split into, the recipe $L=C_{\Pi}^{-1}L^{\mathrm{axf}}C_{\Pi}$ and a worked element shown in both frames. The properties of this frame are listed next, and the roots that produce such frames are counted (§*What the Peirce Frame Makes Simple*, §*Which Roots Give a Peirce Frame*). The product, the trace, the determinant and the six subspaces follow (§*The Product*, §*The Trace*, §*The Determinant*, §*The Six Subspaces*), and the comparison with the coefficient basis and with a generic frame closes the article (§*The Comparison Table*).

**The algebra.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$, with $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$; the central scalar imaginary is $i$. Write $Q_\mu=q_\mu+iq'_\mu$ with $q_\mu,q'_\mu\in\mathbb{R}$, and put $B^2=Q_x^2+Q_y^2+Q_z^2$ and $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2=Q_t^2+Q_x^2+Q_y^2+Q_z^2$.

**The name.** The matrices
$$
\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
\sigma_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\qquad
\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}
$$
are the Pauli matrices, and the $2\times2$ image is written in them,
$$
\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i\bigl(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3\bigr),
$$
so that $\mathsf M_2(\vec e_k)=-i\sigma_k$. The representation is called Pauli because its block is the Pauli combination of the element; the $4\times4$ matrices are the two Kronecker products of that block with $\mathrm I_2$, read in the Peirce frame.

**The result in one line.** The left matrix is the $2\times2$ image taken twice, $L(\tilde Q)=\mathrm I_2\otimes\mathsf M_2(\tilde Q)$; the right matrix is the transposed image taken twice, $R(\tilde Q)=\mathsf M_2(\tilde Q)^{\mathsf T}\otimes\mathrm I_2$. The product is multiplicative on the left and anti-multiplicative on the right. The trace is $4Q_t$. The determinant is $\langle\tilde Q\rangle_{\natural}^2=(Q_t^2+B^2)^2$. The eigenvalues are $Q_t\pm iB$, each twice.

**The two copies.** The left copy is $\mathbb{B}_L=\rho_L(\mathbb{B})$, the right copy is $\mathbb{B}_R=\rho_R(\mathbb{B})$, and both are four-dimensional subalgebras of the ambient $M_4(\mathbb{C})=\operatorname{End}_{\mathbb{C}}(\mathbb{B})$. The left multiplication is $\rho_L(\tilde Q)(\tilde X)=\tilde Q\tilde X$; the right multiplication is $\rho_R(\tilde Q)(\tilde X)=\tilde X\tilde Q$.

**What this article leaves out.** The sixteen products $L_{e_\mu}^{\mathrm{pau}}R_{e_\nu}^{\mathrm{pau}}$ are a basis of the whole algebra $M_4(\mathbb{C})$, not only of the two copies, so every endomorphism has a coefficient matrix $c(M)$ in that basis and a length $\ell(M)=\operatorname{rank}c(M)$, the least number of products summing to it. That chain is the subject of the companion article *$M_4(\mathbb{C})$ Pauli Representation : Operators*, together with the congruence that makes the length survive a change of element basis. This article stops at the two families and at the algebra they generate.

**Boundaries.** The algebra, the multiplication table and the four conjugations are *The Biquaternion Algebra* and *The Element, the Coordinates and the Conjugations in the Biquaternion Algebra*. The idempotents and the Peirce decomposition are *Peirce Decompositions of the Biquaternion Algebra* and *The Peirce Basis of a Peirce Decomposition of the Biquaternion Algebra*. The general theory of the two families, of the stitch and of the change of frame is *Families of Matrix Representations*; this article is one instance of it, worked out in full, and the frame below is the canonical frame of *Matrix Representations Conventions*, §*The Matrix Models*. The six subspaces are defined and decomposed in *Subspaces and Decompositions of the Biquaternion Algebra*; this article reads their images in the Peirce frame. The same element in the coefficient basis is *$M_4(\mathbb{C})$ Axis-Free Representation*, and at the element size the block is *$M_2(\mathbb{C})$ Pauli Representation*.

## The Root and the Peirce Frame

**The root.** The element
$$
\vec\Xi=i\vec e_z
$$
is a vector, not a scalar: it lies in the vector subspace $\mathrm{Vect}(\mathbb{B})$. Its square is the unit,
$$
\vec\Xi^2=i^2\vec e_z^2=(-1)(-e_t)=e_t,
$$
so it is a pure square root of $e_t$. It is one of the three coordinate directions, with either sign: $\pm i\vec e_x$, $\pm i\vec e_y$, $\pm i\vec e_z$. The standard frame uses the $z$ root. The root is not central, and the choice of $z$ is a genuine choice of direction. Everything in this article is generated by it.

**The idempotents.** Put
$$
\tilde\Pi_\pm=\frac{e_t\pm\vec\Xi}{2}=\frac12(e_t\pm i\vec e_z).
$$
Then
$$
\tilde\Pi_+^2=\frac14(e_t+2\vec\Xi+\vec\Xi^2)=\frac14(2e_t+2\vec\Xi)=\tilde\Pi_+,
$$
and the same computation with $-\vec\Xi$ gives $\tilde\Pi_-^2=\tilde\Pi_-$. The two are orthogonal,
$$
\tilde\Pi_+\tilde\Pi_-=\frac14(e_t-\vec\Xi^2)=0,
$$
and they sum to the unit and differ by the root:
$$
\tilde\Pi_++\tilde\Pi_-=e_t,\qquad
\tilde\Pi_+-\tilde\Pi_-=\vec\Xi .
$$
Each is a non-central idempotent, and the pair is the standard pair of the matrix model.

**Why the root produces the frame.** An idempotent of the form $(e_t+\vec\Xi)/2$ with $\vec\Xi^2=e_t$ is determined by its root. The two idempotents are the two spectral projections of the root, and the root is recovered as their difference. The construction uses only the multiplication table and the choice of the square root; it uses no coordinates beyond that choice. The direction of the root is the only asymmetry in the frame.

**The frame.** The standard Peirce frame is the ordered basis
$$
\mathcal{P}=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-),
\qquad
\vec\Upsilon_\pm=\frac12(i\vec e_x\pm\vec e_y).
$$
The order is the one fixed above, and it is the order used for every matrix in this article. The frame is the canonical frame of *Matrix Representations Conventions*, §*The Matrix Models*, where the two displays $L=\mathrm I_2\otimes\mathsf M_2$ and $R=\mathsf M_2^{\mathsf T}\otimes\mathrm I_2$ are quoted; §*The Left Family* and §*The Right Family* derive them here from the frame.

**The name.** The frame is called Peirce because it is adapted to the two-sided Peirce decomposition of the algebra by the pair $(\tilde\Pi_+,\tilde\Pi_-)$: each frame vector lies in one of the four components $\tilde\Pi_\pm\mathbb{B}\tilde\Pi_\pm$, the two off-diagonal components are complex lines, and the frame takes one vector from each. A coordinate in this frame is a component of the decomposition, and the four components are the four entries of the $2\times2$ block of §*The Left Family*. The word Peirce names the frame; the word Pauli names the block.

**The multiplication table.** The four basis elements multiply as
$$
\tilde\Pi_+\tilde\Pi_+=\tilde\Pi_+,\qquad
\tilde\Pi_-\tilde\Pi_-=\tilde\Pi_-,\qquad
\tilde\Pi_+\tilde\Pi_-=\tilde\Pi_-\tilde\Pi_+=0,
$$
and
$$
\tilde\Pi_+\vec\Upsilon_-=\vec\Upsilon_-,\qquad
\tilde\Pi_-\vec\Upsilon_+=\vec\Upsilon_+,\qquad
\tilde\Pi_+\vec\Upsilon_+=\tilde\Pi_-\vec\Upsilon_-=0,
$$
$$
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,\qquad
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,\qquad
\vec\Upsilon_+^2=\vec\Upsilon_-^2=0,
$$
and
$$
\vec\Upsilon_+\tilde\Pi_+=\vec\Upsilon_+,\qquad
\vec\Upsilon_-\tilde\Pi_-=\vec\Upsilon_-,\qquad
\vec\Upsilon_+\tilde\Pi_-=\vec\Upsilon_-\tilde\Pi_+=0 .
$$
The two mixed units are nilpotent, and each pair multiplies to one of the idempotents. No coefficient and no imaginary unit appears in the table: it is the Peirce table of the standard pair, in the order above, and it is the only input of the two families below.

**The coordinates.** An element written in the frame is
$$
\tilde Q=P_+\tilde\Pi_++X_+\vec\Upsilon_++X_-\vec\Upsilon_-+P_-\tilde\Pi_-,
\qquad P_\pm,X_\pm\in\mathbb{C}.
$$
The four Peirce coordinates are the entries of the $2\times2$ image,
$$
A=\begin{pmatrix}P_+&X_-\\X_+&P_-\end{pmatrix},
\qquad
P_+=Q_t-iQ_z,\quad
X_+=-iQ_x+Q_y,\quad
X_-=-iQ_x-Q_y,\quad
P_-=Q_t+iQ_z,
$$
so the change from the coefficients $Q_\mu$ to the Peirce coordinates is the linear map displayed in §*The Switch to the Axis-Free Matrices*.

## The Left Family

**The operator.** The matrix $L(\tilde Q)$ is the matrix of $\rho_L(\tilde Q)$ in the frame $\mathcal{P}$. The map $\rho_L$ is injective and multiplicative, so its image is the four-dimensional subalgebra $\mathbb{B}_L\subset M_4(\mathbb{C})$, and the four matrices $L_{e_\mu}^{\mathrm{pau}}$ are a basis of it.

**The definition.** The $\nu$-th column of the left matrix is the coordinate column of the product of $\tilde Q$ with the $\nu$-th frame vector:
$$
L(\tilde Q)_{\mu\nu}=\bigl[\tilde Qf_\nu\bigr]_{\mu},\qquad
L(\tilde Q)=\bigl(\bigl[\tilde Q\tilde\Pi_+\bigr]\;\bigl[\tilde Q\vec\Upsilon_+\bigr]\;\bigl[\tilde Q\vec\Upsilon_-\bigr]\;\bigl[\tilde Q\tilde\Pi_-\bigr]\bigr).
$$
This is the definition of §*The Two Sides* of *Families of Matrix Representations*, read in the frame $\mathcal{P}$. Only the multiplication table of §*The Root and the Peirce Frame* enters, and no further choice is made.

**The display.** Write
$$
A=\mathsf M_2(\tilde Q)=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}
=
\begin{pmatrix}
Q_t-iQ_z&-iQ_x-Q_y\\
-iQ_x+Q_y&Q_t+iQ_z
\end{pmatrix}.
$$
Then
$$
L^{\mathrm{pau}}(\tilde Q)=\mathrm I_2\otimes A=
\begin{pmatrix}
a&b&0&0\\
c&d&0&0\\
0&0&a&b\\
0&0&c&d
\end{pmatrix}.
$$
The matrix is block diagonal with two equal blocks. The first block acts on the pair $(\tilde\Pi_+,\vec\Upsilon_+)$ and the second on the pair $(\vec\Upsilon_-,\tilde\Pi_-)$. One block on its own is §*The Left and Right Matrices* of *$M_2(\mathbb{C})$ Pauli Representation*, which continues this article at the element size. The sum of the first and fourth columns is the coordinate column of $\tilde Q$ in the Peirce frame, $(a,c,b,d)^{\mathsf T}$; neither column alone recovers the element.

**Why the block repeats.** The left action preserves the splitting $\mathbb{B}=\mathbb{B}\tilde\Pi_+\oplus\mathbb{B}\tilde\Pi_-$, because $\tilde Q\tilde X\tilde\Pi_+=\tilde Q(\tilde X\tilde\Pi_+)$ stays in the first summand and likewise for the second. Each summand has complex dimension two, and on each the action is the same block $A$, written in the pairs $(\tilde\Pi_+,\vec\Upsilon_+)$ and $(\vec\Upsilon_-,\tilde\Pi_-)$. The two blocks are therefore equal, and their equality is the statement $L(\tilde Q)=\mathrm I_2\otimes\mathsf M_2(\tilde Q)$.

**The four left matrices.** The four matrices are the images of the units under the left matrix map,
$$
L_{e_t}^{\mathrm{pau}}=\mathsf{M}_4^{L}(e_t)=\mathrm I_4,\qquad
L_{\vec e_x}^{\mathrm{pau}}=\mathsf{M}_4^{L}(\vec e_x)=\begin{pmatrix}0&-i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix},
$$
$$
L_{\vec e_y}^{\mathrm{pau}}=\mathsf{M}_4^{L}(\vec e_y)=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad
L_{\vec e_z}^{\mathrm{pau}}=\mathsf{M}_4^{L}(\vec e_z)=\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&i\end{pmatrix}.
$$
Each is $\mathrm I_2\otimes\mathsf M_2(\vec e_k)$ with $\mathsf M_2(\vec e_k)=-i\sigma_k$. The matrices are not signed permutations; their entries are $0,\pm1,\pm i$. Each has determinant $1$; the identity has trace $4$, and the three vector matrices have trace $0$. Since $\rho_L$ is injective and the four units are a basis of $\mathbb{B}$, the four matrices are linearly independent and span $\mathbb{B}_L$: they are a basis of the left copy.

**The example.** For $\tilde Q=(2+i)e_t+(1-i)\vec e_x+3\vec e_y+i\vec e_z$,
$$
A=\begin{pmatrix}3+i&-4-i\\2-i&1+i\end{pmatrix},\qquad
L^{\mathrm{pau}}(\tilde Q)=
\begin{pmatrix}
3+i&-4-i&0&0\\
2-i&1+i&0&0\\
0&0&3+i&-4-i\\
0&0&2-i&1+i
\end{pmatrix}.
$$
The trace is $8+4i=4(2+i)$, and the determinant is $117+44i=(11+2i)^2$, with $\langle\tilde Q\rangle_{\natural}=11+2i$.

**The product of two left matrices.** Write the quaternion product of two units as $e_\mu e_\nu=\varepsilon e_{\mu\nu}$ with $\varepsilon=\pm1$ and $e_{\mu\nu}$ a unit. Then
$$
L_{e_\mu}^{\mathrm{pau}} L_{e_\nu}^{\mathrm{pau}}=\varepsilon L_{e_{\mu\nu}}^{\mathrm{pau}},
$$
so the left product follows the order of the units, and the four matrices multiply as the units do up to sign, for example
$$
(L_{\vec e_x}^{\mathrm{pau}})^2=(L_{\vec e_y}^{\mathrm{pau}})^2=(L_{\vec e_z}^{\mathrm{pau}})^2=-\mathrm I_4,\qquad
L_{\vec e_x}^{\mathrm{pau}}L_{\vec e_y}^{\mathrm{pau}}=L_{\vec e_z}^{\mathrm{pau}},\qquad
L_{\vec e_y}^{\mathrm{pau}}L_{\vec e_x}^{\mathrm{pau}}=-L_{\vec e_z}^{\mathrm{pau}}.
$$
The set of the four left matrices together with their negatives is the quaternion group of order eight, and the closure under products up to sign is the multiplicativity of $\rho_L$ read on the basis.

**The trace and the determinant.** Every left basis matrix is invertible, with
$$
\det L_{e_\mu}^{\mathrm{pau}}=1,\qquad
\operatorname{Tr}L_{e_\mu}^{\mathrm{pau}}=4\delta_{\mu t}.
$$
A sum of basis matrices need not be invertible: $L_{\vec e_x}^{\mathrm{pau}}+R_{\vec e_x}^{\mathrm{pau}}$ has rank $2$, for instance. The algebra is simple and has zero divisors, and the invertibility of each basis vector does not extend to the complex span.

## The Right Family

**The definition.** The $\nu$-th column of the right matrix is the coordinate column of the product of the $\nu$-th frame vector with $\tilde Q$, the element on the other side:
$$
R(\tilde Q)_{\mu\nu}=\bigl[f_\nu\tilde Q\bigr]_{\mu},\qquad
R(\tilde Q)=\bigl(\bigl[\tilde\Pi_+\tilde Q\bigr]\;\bigl[\vec\Upsilon_+\tilde Q\bigr]\;\bigl[\vec\Upsilon_-\tilde Q\bigr]\;\bigl[\tilde\Pi_-\tilde Q\bigr]\bigr).
$$
The construction is the same as the left one with the order of the two factors exchanged, and it uses the same table. The map $\rho_R$ is injective, and its image $\mathbb{B}_R$ is a four-dimensional subalgebra of $M_4(\mathbb{C})$.

**The display.** In the same frame, with $A=\mathsf M_2(\tilde Q)$ and its entries $a,b,c,d$ as in §*The Left Family*,
$$
R^{\mathrm{pau}}(\tilde Q)=A^{\mathsf T}\otimes\mathrm I_2=
\begin{pmatrix}
a&0&c&0\\
0&a&0&c\\
b&0&d&0\\
0&b&0&d
\end{pmatrix}.
$$
The transpose is what makes the right action land on the first tensor factor: the block is transposed because its column index now names the frame vector on the left of the element. The right matrix is anti-multiplicative, and it commutes with the left matrix:
$$
R(\tilde Q_1\tilde Q_2)=R(\tilde Q_2)R(\tilde Q_1),\qquad
L(\tilde Q_1)R(\tilde Q_2)=R(\tilde Q_2)L(\tilde Q_1).
$$
The two identities are the two ways of reading the associative law: the first is $(\tilde X\tilde Q_1)\tilde Q_2=\tilde X(\tilde Q_1\tilde Q_2)$ read on the right, the second is $\tilde Q_1\tilde X\tilde Q_2$ read from either side.

**The four right matrices.** The four matrices are the images of the units under the right matrix map,
$$
R_{e_t}^{\mathrm{pau}}=\mathsf{M}_4^{R}(e_t)=\mathrm I_4,\qquad
R_{\vec e_x}^{\mathrm{pau}}=\mathsf{M}_4^{R}(\vec e_x)=\begin{pmatrix}0&0&-i&0\\0&0&0&-i\\-i&0&0&0\\0&-i&0&0\end{pmatrix},
$$
$$
R_{\vec e_y}^{\mathrm{pau}}=\mathsf{M}_4^{R}(\vec e_y)=\begin{pmatrix}0&0&1&0\\0&0&0&1\\-1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
R_{\vec e_z}^{\mathrm{pau}}=\mathsf{M}_4^{R}(\vec e_z)=\begin{pmatrix}-i&0&0&0\\0&-i&0&0\\0&0&i&0\\0&0&0&i\end{pmatrix}.
$$
Each is $\mathsf M_2(\vec e_k)^{\mathsf T}\otimes\mathrm I_2$. Each has determinant $1$ and trace $4\delta_{\mu t}$; the four are a basis of $\mathbb{B}_R$. The two bases are bases of two different four-dimensional subspaces of $M_4(\mathbb{C})$, not two bases of one space.

**The example.** For the same element $\tilde Q=(2+i)e_t+(1-i)\vec e_x+3\vec e_y+i\vec e_z$, the right matrix is the transposed block display,
$$
R^{\mathrm{pau}}(\tilde Q)=
\begin{pmatrix}
3+i&0&2-i&0\\
0&3+i&0&2-i\\
-4-i&0&1+i&0\\
0&-4-i&0&1+i
\end{pmatrix}.
$$
Its trace is $8+4i$ and its determinant $117+44i$, the same as those of $L(\tilde Q)$, as §*The Stitch Between the Two Families* requires.

**The product of two right matrices.** With the same notation, $e_\nu e_\mu=\varepsilon'e_{\nu\mu}$, so
$$
R_{e_\mu}^{\mathrm{pau}} R_{e_\nu}^{\mathrm{pau}}=\varepsilon' R_{e_{\nu\mu}}^{\mathrm{pau}},
$$
and the right product reverses the order of the units, because $R_aR_b=R_{ba}$. For example
$$
(R_{\vec e_x}^{\mathrm{pau}})^2=(R_{\vec e_y}^{\mathrm{pau}})^2=(R_{\vec e_z}^{\mathrm{pau}})^2=-\mathrm I_4,\qquad
R_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}=-R_{\vec e_z}^{\mathrm{pau}},\qquad
R_{\vec e_y}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}=R_{\vec e_z}^{\mathrm{pau}}.
$$
The four right matrices together with their negatives are again the quaternion group of order eight, with the product read backwards.

**The trace and the determinant.** The right matrices have the same invariants as the left ones,
$$
\det R_{e_\mu}^{\mathrm{pau}}=1,\qquad
\operatorname{Tr}R_{e_\mu}^{\mathrm{pau}}=4\delta_{\mu t},
$$
because the stitch of §*The Stitch Between the Two Families* is a transposition composed with a fixed permutation, and neither changes a determinant or a trace.

## The Stitch Between the Two Families

**The swap matrix.** Let $\mathsf P$ be the permutation matrix that exchanges the two tensor factors,
$$
\mathsf P\,(A\otimes B)\,\mathsf P=B\otimes A,\qquad
\mathsf P=
\begin{pmatrix}
1&0&0&0\\
0&0&1&0\\
0&1&0&0\\
0&0&0&1
\end{pmatrix},
\qquad
\mathsf P^2=\mathrm I_4 .
$$
The matrix is symmetric, and it is the exchange of the second and third coordinates of the frame.

**The stitch.** The right matrix is obtained from the left by transposition and the swap:
$$
R(\tilde Q)=\mathsf P\,L(\tilde Q)^{\mathsf T}\mathsf P .
$$
The identity is the tensor identity $\mathsf P(\mathrm I_2\otimes A^{\mathsf T})\mathsf P=A^{\mathsf T}\otimes\mathrm I_2$.

**The stitch in full.** The three steps are displayed on a general element. The transpose of the left matrix is
$$
{L^{\mathrm{pau}}(\tilde Q)}^{\mathsf T}=
\begin{pmatrix}
a&c&0&0\\
b&d&0&0\\
0&0&a&c\\
0&0&b&d
\end{pmatrix},
$$
the swap moves the two $2\times2$ blocks into the two tensor slots,
$$
\mathsf P\,{L^{\mathrm{pau}}(\tilde Q)}^{\mathsf T}=
\begin{pmatrix}
a&c&0&0\\
0&0&a&c\\
b&d&0&0\\
0&0&b&d
\end{pmatrix},
$$
and the second multiplication by $\mathsf P$ exchanges the second and third columns,
$$
\mathsf P\,{L^{\mathrm{pau}}(\tilde Q)}^{\mathsf T}\mathsf P=
\begin{pmatrix}
a&0&c&0\\
0&a&0&c\\
b&0&d&0\\
0&b&0&d
\end{pmatrix}
=R^{\mathrm{pau}}(\tilde Q).
$$
The swap sends a block in the second tensor slot to the first slot, and conversely. The stitch is an involution, because $\mathsf P^2=\mathrm I_4$ and transposition is an involution. It preserves the trace and the determinant:
$$
\operatorname{Tr}R(\tilde Q)=\operatorname{Tr}L(\tilde Q),\qquad
\det R(\tilde Q)=\det L(\tilde Q),
$$
since neither transposition nor conjugation by a fixed matrix changes them.

**No signs in this stitch.** The axis-free basis stitch carries the sign matrix $D=\operatorname{diag}(1,-1,-1,-1)$ on both sides. In the Peirce frame the signs are absorbed into the frame vectors, and the stitch is a pure swap. The two stitches describe the same exchange of the left and right copies in two frames.

### The Transpose Is Not the Conjugation

**The dictionary.** In the Peirce frame the transpose is not the quaternion conjugation. With the Pauli matrix $\sigma_2$ and
$$
C_L=\mathrm I_2\otimes\sigma_2,\qquad
C_R=\sigma_2\otimes\mathrm I_2,
$$
the transpose dictionaries are
$$
L(\tilde Q)^{\mathsf T}=C_L\,L(\tilde Q^{\natural})\,C_L,\qquad
R(\tilde Q)^{\mathsf T}=C_R\,R(\tilde Q^{\natural})\,C_R,
$$
and the Hermitian adjoints are
$$
L(\tilde Q)^{\dagger}=L(\tilde Q^{*}),\qquad
R(\tilde Q)^{\dagger}=R(\tilde Q^{*}),
$$
with $\tilde Q^{*}=\bar Q_te_t-\overline{\vec Q}$ the Hermitian conjugation of *The Element, the Coordinates and the Conjugations*.

**Why the two matrices differ.** The transpose acts on the tensor factor that carries the element: $C_L$ acts on the second factor, where $A$ sits in $L$, and $C_R$ acts on the first, where $A^{\mathsf T}$ sits in $R$. The conjugation $\natural$ is the transpose composed with the two copies of $\sigma_2$ in that factor, which is why a transposition costs a sign change of the vector part and nothing else.

**Why the adjoint is the conjugate transpose.** The adjoint identities hold for the Hermitian form $\langle X,Y\rangle_*=\operatorname{Sc}(XY^{*})$ because the four frame vectors are orthogonal and have the same norm,
$$
\langle\tilde\Pi_+,\tilde\Pi_+\rangle_*=\langle\vec\Upsilon_+,\vec\Upsilon_+\rangle_*
=\langle\vec\Upsilon_-,\vec\Upsilon_-\rangle_*=\langle\tilde\Pi_-,\tilde\Pi_-\rangle_*=\tfrac12,
$$
and all the cross products vanish. A frame orthogonal with equal norms gives the same adjoint as an orthonormal one, up to the common factor, so the adjoint in the frame is the conjugate transpose.

## Every Frame Is a Conjugate of This One

**Every frame at once.** Let $\mathcal{F}'$ be any frame, with change matrix $C$ whose columns are its four vectors written in $\mathcal{P}$. A vector whose Peirce coordinate column is $p$ has the column $Cp$ in $\mathcal{F}'$, so the two matrices are
$$
L'(\tilde Q)=C^{-1}L(\tilde Q)C,\qquad R'(\tilde Q)=C^{-1}R(\tilde Q)C .
$$
One matrix serves both families, because the frame is a property of the carrier and the side is a property of the action.

**One orbit.** Every frame arises this way from one $C\in GL_4(\mathbb{C})$, so the frames form a single orbit, and what changes from frame to frame is the array: its entries, its sparsity, the subring of $\mathbb{C}$ in which they lie, its blocks. What does not change is the element, and the trace $4Q_t$, the determinant $\langle\tilde Q\rangle_{\natural}^{2}$, the characteristic polynomial $((\lambda-Q_t)^2+B^2)^2$, the spectrum and the rank are the same in every frame.

**A change of frame, not of operator.** The conjugation leaves the trace, the determinant and the characteristic polynomial untouched. It is not a change of the element and not a change of the side; it is the same action written in another basis. An identity that holds in one frame may therefore fail in another, and the transpose identity of §*The Transpose Is Not the Conjugation* is the example.

**The axis-free frame on the orbit.** It is reached from the Peirce frame by the matrix $C_{\Pi}$ of the next section, whose four columns are the frame vectors written in the axis-free basis. The matrix, its inverse, the two dictionaries they carry and the conjugations performed entry by entry are the subject of that section.

## The Switch to the Axis-Free Matrices

**What the switch is.** One matrix and its inverse. The columns of the first are the four frame vectors written in the axis-free basis, the columns of the second are the four axis-free units written in the frame. Everything below is those two arrays, the two $2\times2$ blocks they split into, the eight unit matrices of the two families each displayed in both frames, one of the sixteen products, and a worked element.

### The Two Basis Matrices

**The notation of the switch.** Write $\tau_\mu$ for the four frame vectors in the order $\mathcal{P}$ and $e_\mu$ for the four units in the order of the coefficient basis:
$$
\tau_1=\tilde\Pi_+,\quad \tau_2=\vec\Upsilon_+,\quad \tau_3=\vec\Upsilon_-,\quad \tau_4=\tilde\Pi_-,
\qquad
e_1=e_t,\quad e_2=\vec e_x,\quad e_3=\vec e_y,\quad e_4=\vec e_z .
$$
The switch is then two arrays of coordinate columns,
$$
C_{\Pi}=\bigl([\tau_1]_e,\dots,[\tau_4]_e\bigr),
\qquad
C_{\Pi}^{-1}=\bigl([e_1]_\tau,\dots,[e_4]_\tau\bigr),
$$
and the two expansions they carry are
$$
\tau_\mu=\sum_{\nu=1}^{4}\bigl(C_{\Pi}\bigr)_{\nu\mu}e_\nu,
\qquad
e_\mu=\sum_{\nu=1}^{4}\bigl(C_{\Pi}^{-1}\bigr)_{\nu\mu}\tau_\nu .
$$
The first array is the matrix of the $\tau$ basis in terms of the axis-free basis, the second is the matrix of the axis-free basis in terms of the $\tau$ basis; each lists four vectors, one per column.

**The $\tau$ basis over the axf basis.** The columns are the four frame vectors, in the order $\mathcal{P}$:
$$
C_{\Pi}=
\begin{pmatrix}
\tfrac12&0&0&\tfrac12\\[2pt]
0&\tfrac{i}{2}&\tfrac{i}{2}&0\\[2pt]
0&\tfrac12&-\tfrac12&0\\[2pt]
\tfrac{i}{2}&0&0&-\tfrac{i}{2}
\end{pmatrix},
\qquad
\begin{array}{l}
\tilde\Pi_+=\tfrac12\bigl(e_t+i\vec e_z\bigr),\\[2pt]
\vec\Upsilon_+=\tfrac12\bigl(i\vec e_x+\vec e_y\bigr),\\[2pt]
\vec\Upsilon_-=\tfrac12\bigl(i\vec e_x-\vec e_y\bigr),\\[2pt]
\tilde\Pi_-=\tfrac12\bigl(e_t-i\vec e_z\bigr).
\end{array}
$$
The $k$-th column of $C_{\Pi}$ is the coordinate column of the $k$-th frame vector: $(1,0,0,i)/2$ for $\tilde\Pi_+$, $(0,i,1,0)/2$ for $\vec\Upsilon_+$, $(0,i,-1,0)/2$ for $\vec\Upsilon_-$ and $(1,0,0,-i)/2$ for $\tilde\Pi_-$.

**The axf basis over the $\tau$ basis.** The columns are the four units, in the axis-free order:
$$
C_{\Pi}^{-1}=
\begin{pmatrix}
1&0&0&-i\\
0&-i&1&0\\
0&-i&-1&0\\
1&0&0&i
\end{pmatrix},
\qquad
\begin{array}{l}
e_t=\tilde\Pi_++\tilde\Pi_-,\\[2pt]
\vec e_x=-i\vec\Upsilon_+-i\vec\Upsilon_-,\\[2pt]
\vec e_y=\vec\Upsilon_+-\vec\Upsilon_-,\\[2pt]
\vec e_z=-i\tilde\Pi_++i\tilde\Pi_-.
\end{array}
$$
The $k$-th column of $C_{\Pi}^{-1}$ is the coordinate column of the $k$-th unit: $(1,0,0,1)$ for $e_t$, $(0,-i,-i,0)$ for $\vec e_x$, $(0,1,-1,0)$ for $\vec e_y$ and $(-i,0,0,i)$ for $\vec e_z$. Each unit is a combination of two frame vectors and each frame vector a combination of two units, so the two arrays have two nonzeros in every row and in every column.

**The two dictionaries, side by side.** Reading the two arrays column by column gives the whole switch:

| frame vector | its column over axf | unit | its column over $\tau$ |
|---|---|---|---|
| $\tilde\Pi_+$ | $\tfrac12(1,0,0,i)^{\mathsf T}$ | $e_t$ | $(1,0,0,1)^{\mathsf T}$ |
| $\vec\Upsilon_+$ | $\tfrac12(0,i,1,0)^{\mathsf T}$ | $\vec e_x$ | $(0,-i,-i,0)^{\mathsf T}$ |
| $\vec\Upsilon_-$ | $\tfrac12(0,i,-1,0)^{\mathsf T}$ | $\vec e_y$ | $(0,1,-1,0)^{\mathsf T}$ |
| $\tilde\Pi_-$ | $\tfrac12(1,0,0,-i)^{\mathsf T}$ | $\vec e_z$ | $(-i,0,0,i)^{\mathsf T}$ |

**They are inverse, and normalised.** The two arrays satisfy
$$
C_{\Pi}C_{\Pi}^{-1}=\mathrm I_4,\qquad
\det C_{\Pi}=-\tfrac14,\qquad
C_{\Pi}^{\dagger}C_{\Pi}=\tfrac12\mathrm I_4,\qquad
C_{\Pi}^{-1}=2C_{\Pi}^{\dagger}.
$$
The factor $\tfrac12$ is the common squared norm of the four frame vectors, so the determinant $-\tfrac14$ is that normalisation and not an invariant of the algebra. The letter is the one of *Matrix Representations Conventions*, §*The $M_4(\mathbb{C})$ Axis-Free Representation*, where this array is called the Peirce change.

**Two blocks, and no mixing.** Both arrays vanish in the two blocks that join $\{e_t,\vec e_z\}$ to $\{\vec e_x,\vec e_y\}$, so the switch is two independent $2\times2$ switches:
$$
\begin{pmatrix}\tilde\Pi_+\\ \tilde\Pi_-\end{pmatrix}
=\tfrac12
\begin{pmatrix}1&i\\ 1&-i\end{pmatrix}
\begin{pmatrix}e_t\\ \vec e_z\end{pmatrix},
\qquad
\begin{pmatrix}\vec\Upsilon_+\\ \vec\Upsilon_-\end{pmatrix}
=\tfrac12
\begin{pmatrix}i&1\\ i&-1\end{pmatrix}
\begin{pmatrix}\vec e_x\\ \vec e_y\end{pmatrix}.
$$
Each block is a Hadamard matrix with one column multiplied by $i$, and the two blocks invert to
$$
\begin{pmatrix}1&1\\-i&i\end{pmatrix},
\qquad
\begin{pmatrix}-i&-i\\1&-1\end{pmatrix},
$$
which are the two blocks of $C_{\Pi}^{-1}$, read transposed: that array lists the units by columns and not by rows. This is why the two arrays have four zeros in each off-block position: the idempotents never mix with the nilpotents.

**The same dictionary on a column.** A coordinate column changes by the same two arrays,
$$
q_e=C_{\Pi}\,p,\qquad p=C_{\Pi}^{-1}q_e,
$$
where $q_e=(Q_t,Q_x,Q_y,Q_z)^{\mathsf T}$ and $p=(P_+,X_+,X_-,P_-)^{\mathsf T}$. Written out, $q_e=C_{\Pi}p$ is
$$
\begin{pmatrix}Q_t\\ Q_x\\ Q_y\\ Q_z\end{pmatrix}
=\frac12
\begin{pmatrix}
P_++P_-\\
iX_++iX_-\\
X_+-X_-\\
iP_+-iP_-
\end{pmatrix},
$$
which is the inverse of the four formulas of §*The Root and the Peirce Frame*: half the sum of the two idempotent coordinates is $Q_t$, half their difference multiplied by $i$ is $Q_z$, half the sum of the two mixed coordinates is $-iQ_x$, and half their difference is $Q_y$.

### The Eight Unit Matrices in Both Displays

**The rule.** The two families are conjugated by the same two arrays,
$$
L^{\mathrm{axf}}(\tilde Q)=C_{\Pi}\,L(\tilde Q)\,C_{\Pi}^{-1},
\qquad
L(\tilde Q)=C_{\Pi}^{-1}L^{\mathrm{axf}}(\tilde Q)\,C_{\Pi},
$$
$$
R^{\mathrm{axf}}(\tilde Q)=C_{\Pi}\,R(\tilde Q)\,C_{\Pi}^{-1},
\qquad
R(\tilde Q)=C_{\Pi}^{-1}R^{\mathrm{axf}}(\tilde Q)\,C_{\Pi}.
$$
One pair of arrays serves both families, because the frame is a property of the carrier and the side is a property of the action.

**The scalar unit.** $L_{e_t}^{\mathrm{axf}}=C_{\Pi}^{-1}\mathrm I_4C_{\Pi}=L_{e_t}^{\mathrm{pau}}=\mathrm I_4$, and the same on the right. The identity is fixed by every change of frame, so it has no display of its own.

**The unit $\vec e_x$.**
$$
L_{\vec e_x}^{\mathrm{axf}}=
\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},
\qquad
L_{\vec e_x}^{\mathrm{pau}}=C_{\Pi}^{-1}L_{\vec e_x}^{\mathrm{axf}}C_{\Pi}=
\begin{pmatrix}0&-i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix},
$$
$$
R_{\vec e_x}^{\mathrm{axf}}=
\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix},
\qquad
R_{\vec e_x}^{\mathrm{pau}}=C_{\Pi}^{-1}R_{\vec e_x}^{\mathrm{axf}}C_{\Pi}=
\begin{pmatrix}0&0&-i&0\\0&0&0&-i\\-i&0&0&0\\0&-i&0&0\end{pmatrix}.
$$

**The unit $\vec e_y$.**
$$
L_{\vec e_y}^{\mathrm{axf}}=
\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},
\qquad
L_{\vec e_y}^{\mathrm{pau}}=C_{\Pi}^{-1}L_{\vec e_y}^{\mathrm{axf}}C_{\Pi}=
\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},
$$
$$
R_{\vec e_y}^{\mathrm{axf}}=
\begin{pmatrix}0&0&-1&0\\0&0&0&-1\\1&0&0&0\\0&1&0&0\end{pmatrix},
\qquad
R_{\vec e_y}^{\mathrm{pau}}=C_{\Pi}^{-1}R_{\vec e_y}^{\mathrm{axf}}C_{\Pi}=
\begin{pmatrix}0&0&1&0\\0&0&0&1\\-1&0&0&0\\0&-1&0&0\end{pmatrix}.
$$

**The unit $\vec e_z$.**
$$
L_{\vec e_z}^{\mathrm{axf}}=
\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix},
\qquad
L_{\vec e_z}^{\mathrm{pau}}=C_{\Pi}^{-1}L_{\vec e_z}^{\mathrm{axf}}C_{\Pi}=
\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&i\end{pmatrix},
$$
$$
R_{\vec e_z}^{\mathrm{axf}}=
\begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix},
\qquad
R_{\vec e_z}^{\mathrm{pau}}=C_{\Pi}^{-1}R_{\vec e_z}^{\mathrm{axf}}C_{\Pi}=
\begin{pmatrix}-i&0&0&0\\0&-i&0&0\\0&0&i&0\\0&0&0&i\end{pmatrix}.
$$

**What the twelve arrays say.** In each pair the axis-free array is a signed permutation with entries $0,\pm1$, and the Peirce array is monomial with entries $0,\pm1,\pm i$. The positions differ, and the imaginary unit appears in the Peirce array because the switch carries it. One coincidence marks the relation: the Peirce matrix of $\vec e_y$ is the axis-free matrix of $\vec e_x$, so the two displays are two orders of the same four arrays and not two sets of objects.

**One step in full.** The two multiplications of the same vector are separated, starting from $L_{\vec e_x}^{\mathrm{axf}}$ displayed above:
$$
C_{\Pi}^{-1}L_{\vec e_x}^{\mathrm{axf}}=
\begin{pmatrix}0&-1&-i&0\\-i&0&0&-1\\-i&0&0&1\\0&-1&i&0\end{pmatrix},
\qquad
C_{\Pi}^{-1}L_{\vec e_x}^{\mathrm{axf}}C_{\Pi}=
\begin{pmatrix}0&-i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix}.
$$
The first factor rewrote the four columns in the frame, the second recombined them into the columns of the Peirce display. Every entry of the result is a sum of two entries of the middle array with coefficients $\pm\tfrac12$ and $\pm\tfrac i2$; the $(1,2)$ entry, for instance, is $\tfrac12(-1)i+\tfrac12(-i)1=-i$.

**The entry rule.** Behind the conjugation of any array is
$$
L(\tilde Q)_{\mu\nu}=\sum_{\rho,\sigma}\bigl(C_{\Pi}^{-1}\bigr)_{\mu\rho}\,L^{\mathrm{axf}}(\tilde Q)_{\rho\sigma}\,\bigl(C_{\Pi}\bigr)_{\sigma\nu},
$$
a sum of four terms, because each row of $C_{\Pi}^{-1}$ and each column of $C_{\Pi}$ has two nonzero entries. For $\mu=\nu=1$ the first row of $C_{\Pi}^{-1}$ is $(1,0,0,-i)$ and the first column of $C_{\Pi}$ is $(1,0,0,i)/2$, so only $\rho,\sigma\in\{1,4\}$ contribute and
$$
L_{11}(\tilde Q)=\tfrac12\bigl(Q_t-iQ_z-iQ_z+Q_t\bigr)=Q_t-iQ_z=a,
$$
the entry $a$ of §*The Left Family*. The same computation gives $b=-iQ_x-Q_y$, $c=-iQ_x+Q_y$ and $d=Q_t+iQ_z$; and an entry that vanishes in the Peirce display, such as the $(1,3)$, is a sum of four terms cancelling in pairs, $\tfrac12(-iQ_x+Q_y-Q_y+iQ_x)=0$.

### The Sixteen Products

**The conjugation passes through the products.** An endomorphism written in the basis of the sixteen products switches with the same coefficients:
$$
C_{\Pi}^{-1}MC_{\Pi}
=\sum_{\mu,\nu}c_{\mu\nu}\,C_{\Pi}^{-1}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}\,C_{\Pi}^{-1}R_{e_\nu}^{\mathrm{pau}}C_{\Pi}
=\sum_{\mu,\nu}c_{\mu\nu}\,L_{e_\mu}^{\mathrm{axf}}R_{e_\nu}^{\mathrm{axf}},
$$
so the coefficient column $c$ is the same in the two frames, and only the sixteen arrays that carry it change. The two bases of the ambient are therefore one basis written twice, and the companion article works with either.

**One product in both displays.** For $\mu=\nu=x$ the product is
$$
L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}=
\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&-1&0&0\\-1&0&0&0\end{pmatrix},
\qquad
L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}=
\begin{pmatrix}-1&0&0&0\\0&-1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},
$$
the second the conjugate of the first. The Peirce display reverses the two ends of the diagonal, the axis-free display is diagonal, and the trace $0$ and the rank $4$ are common to the two. The shape is general: each of the sixteen products is monomial in the frame, with entries $0,\pm1,\pm i$, and a signed permutation in the axis-free basis, with entries $0,\pm1$.

### The Worked Element, Both Ways

**The two coordinate columns.**
$$
q_e=\begin{pmatrix}2+i\\ 1-i\\ 3\\ i\end{pmatrix}=C_{\Pi}p,
\qquad
p=\begin{pmatrix}3+i\\ 2-i\\ -4-i\\ 1+i\end{pmatrix}=C_{\Pi}^{-1}q_e .
$$

**The two matrices.**
$$
L^{\mathrm{pau}}(\tilde Q)=
\begin{pmatrix}
3+i&-4-i&0&0\\
2-i&1+i&0&0\\
0&0&3+i&-4-i\\
0&0&2-i&1+i
\end{pmatrix},
\qquad
L^{\mathrm{axf}}(\tilde Q)=
\begin{pmatrix}
2+i&-1+i&-3&-i\\
1-i&2+i&-i&3\\
3&i&2+i&-1+i\\
i&-3&1-i&2+i
\end{pmatrix},
$$
and $C_{\Pi}^{-1}L^{\mathrm{axf}}(\tilde Q)C_{\Pi}$ returns the first. The block structure is gone in the axis-free array; the trace $8+4i=4Q_t$ and the determinant $117+44i=\langle\tilde Q\rangle_{\natural}^{2}$ are common to the two.

**What the switch costs, and what it buys.** The two blocks of the left matrix merge into one dense array, and the eight zeros of the Peirce display are lost. What is gained is the transpose dictionary, real entries for real elements and the cyclic symmetry of the three directions; the four rows of §*The Comparison Table* that record these trades are the ones named real matrices, cyclic symmetry, transpose and tensor display.

## What the Peirce Frame Makes Simple

**The ten properties.** In the Peirce frame the sixteen matrices $L_{e_\mu}^{\mathrm{pau}}$ and $R_{e_\nu}^{\mathrm{pau}}$ have all of the following at once.

**(a) They are monomial.** Exactly one nonzero entry in each row and in each column, of modulus one.

**(b) The entries lie in $\mathbb{Z}[i]$.** Every entry of the sixteen is $0$, $+1$, $-1$, $+i$ or $-i$; no other complex number appears.

**(c) They are unitary.** Each satisfies $M^{\dagger}M=\mathrm I_4$, so the left family lies in $U(4)$ and so does the right family.

**(d) The display is a tensor product.** $L(\tilde Q)=\mathrm I_2\otimes\mathsf M_2(\tilde Q)$ and $R(\tilde Q)=\mathsf M_2(\tilde Q)^{\mathsf T}\otimes\mathrm I_2$, the left action on the second factor and the right action on the first.

**(e) The idempotents are frame vectors.** $\tilde\Pi_+$ and $\tilde\Pi_-$ are the first and the fourth vectors, $\tilde\Pi_+\tilde\Pi_-=0$ and $\tilde\Pi_++\tilde\Pi_-=e_t$; the frame is adapted to the decomposition that the element itself produces.

**(f) The off-diagonal slots are lines.** $\vec\Upsilon_+$ spans the one-dimensional space $\tilde\Pi_-\mathbb{B}\tilde\Pi_+$ and $\vec\Upsilon_-$ spans $\tilde\Pi_+\mathbb{B}\tilde\Pi_-$, and both are nilpotent.

**(g) The stitch is a pure swap.** $R(\tilde Q)=\mathsf P L(\tilde Q)^{\mathsf T}\mathsf P$ with $\mathsf P^2=\mathrm I_4$: no signs and no diagonal factor.

**(h) The switch is half a swap.** The Gram matrix of the plain product in this frame is $\tfrac12\mathsf P$, so $C_{\Pi}^{\mathsf T}DC_{\Pi}=\tfrac12\mathsf P$ and the two frames differ by a swap and a factor two.

**(i) The invariants of a unit are trivial.** $\operatorname{Tr}L_{e_\mu}^{\mathrm{pau}}=4\delta_{\mu t}$ and $\det L_{e_\mu}^{\mathrm{pau}}=1$, and the same on the right.

**(j) The transpose is two copies of $\sigma_2$.** $L(\tilde Q)^{\mathsf T}=C_LL(\tilde Q^{\natural})C_L$ and $R(\tilde Q)^{\mathsf T}=C_RR(\tilde Q^{\natural})C_R$.

**One root, ten readings.** Properties (d) and (e) are the root: the idempotents are its two halves, and the split $\mathbb{B}=\mathbb{B}\tilde\Pi_+\oplus\mathbb{B}\tilde\Pi_-$ is the reason the block repeats. Properties (a), (b), (c) and (i) are one fact about the block, that $\mathsf M_2$ is a unitary monomial array of determinant one. Property (f) is the Peirce table of §*The Root and the Peirce Frame*. Properties (g) and (h) are the same swap, read on the two matrices. Property (j) is $\sigma_2$, the only Pauli matrix that is imaginary and antisymmetric. The ten are one frame seen ten ways.

**What the entries cannot be.** No entry of the sixteen is real except $0$ and $\pm1$, and those occur only in $L_{\vec e_y}^{\mathrm{pau}}$ and $R_{\vec e_y}^{\mathrm{pau}}$. The frame vectors are complex, so the display of a real element is not real: the real slice $\mathbb{H}\subset\mathbb{B}$ does not land in $M_4(\mathbb{R})$ here, and the quaternion block of §*The Six Subspaces* is the shape $A_{\mathbb{H}}(a,b)$ and not the entrywise real shape. This is the price of the tensor display, and the coefficient basis pays it in the other currency: it keeps the entries real and gives up the idempotents.

## Which Roots Give a Peirce Frame

**The roots of the unit.** A root is a vector $\vec\Xi=\sum_k a_k\vec e_k$ with $\vec\Xi^2=e_t$. The cross terms vanish, since $\vec e_k\vec e_l+\vec e_l\vec e_k=0$ for $k\neq l$, and $\vec e_k^2=-e_t$, so
$$
\vec\Xi^2=-\Bigl(a_x^2+a_y^2+a_z^2\Bigr)e_t .
$$
The roots are therefore the solutions of
$$
a_x^2+a_y^2+a_z^2=-1,
$$
one complex equation in three complex unknowns: a two-parameter family, of real dimension four. The root $i\vec e_z$ is one point of it, and so are $i(\vec e_x+\vec e_y)/\sqrt2$ and $i(0.6\,\vec e_y+0.8\,\vec e_z)$, since $0.36+0.64=1$.

**The root fixes the frame.** The two idempotents are the two halves of the root and the root is their difference, so the root and the pair are one datum. The off-diagonal component $\tilde\Pi_+\mathbb{B}\tilde\Pi_-$ is a complex line, so $\vec\Upsilon_-$ is fixed up to a scalar; $\vec\Upsilon_+$ is then fixed by $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_+$. The frame is therefore fixed by the root up to that scalar and up to the exchange of the two idempotents.

**The six coordinate roots.** The roots with a single nonzero coordinate are $\pm i\vec e_x$, $\pm i\vec e_y$, $\pm i\vec e_z$. They give the three coordinate frames and their two readings: the root $-\vec\Xi$ has the idempotents of $\vec\Xi$ exchanged, so its frame is the same one with the first and fourth vectors interchanged. The frames of $i\vec e_x$, $i\vec e_y$ and $i\vec e_z$ are carried into each other by the cyclic relabelling $x\mapsto y\mapsto z\mapsto x$, which preserves the relations $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$ and is therefore an automorphism of the algebra. So the six coordinate roots give one frame up to a cyclic relabelling and the exchange of the two idempotents.

**Any other root loses the sparsity.** Take a root with two nonzero coordinates, for example $i(\vec e_x+\vec e_y)/\sqrt2$. Its idempotent $\tilde\Pi_+=\tfrac12(e_t+i(a_x\vec e_x+a_y\vec e_y+a_z\vec e_z))$ has three nonzero coordinates in the coefficient basis, so the change matrix $C$ from the standard frame to this one is not monomial, and neither is its inverse. The sixteen arrays are then $C^{-1}L_{e_\mu}^{\mathrm{pau}}C$ and $C^{-1}R_{e_\nu}^{\mathrm{pau}}C$, and their entries leave $\{0,\pm1,\pm i\}$: the coefficients of $C$ and of $C^{-1}$ are carried into the product. The sparsity of §*What the Peirce Frame Makes Simple* therefore belongs to the six coordinate roots and not to the Peirce construction itself.

**Every frame with two idempotents is a root frame.** Suppose a frame contains two orthogonal idempotents summing to $e_t$. Their difference is
$$
\vec\Xi=2\tilde\Pi_+-e_t,
$$
whose scalar part is $2\cdot\tfrac12-1=0$, so it is a vector, and
$$
\vec\Xi^2=4\tilde\Pi_+-4\tilde\Pi_++e_t=e_t,
$$
so it is a root. Hence such a frame is a Peirce frame of some root, and no frame outside this family carries the idempotents of the element. The choice of the frame is the choice of a root, and there is nothing else to choose.

**What the choice costs.** The root picks a direction, and the frame is not unique: there are as many Peirce frames as roots, and they are all conjugate to one another (§*Every Frame Is a Conjugate of This One*). What singles out $i\vec e_z$ is not the algebra but the display: the coordinate roots are the ones whose frames have the monomial left matrices, the six of them give one frame up to relabelling, and $i\vec e_z$ is the one that *Matrix Representations Conventions* fixes.

## The Product

**The left product.** For all $\tilde Q_1,\tilde Q_2$,
$$
L(\tilde Q_1\tilde Q_2)=L(\tilde Q_1)L(\tilde Q_2),\qquad
L(\tilde Q^n)=L(\tilde Q)^n,\qquad
L(\tilde Q^{-1})=L(\tilde Q)^{-1},
$$
the last when $\tilde Q$ is invertible. The identity is the multiplicativity of $\rho_L$, read through the tensor display $L=\mathrm I_2\otimes\mathsf M_2$.

**The right product.** For all $\tilde Q_1,\tilde Q_2$,
$$
R(\tilde Q_1\tilde Q_2)=R(\tilde Q_2)R(\tilde Q_1),\qquad
R(\tilde Q^n)=R(\tilde Q)^n,\qquad
R(\tilde Q^{-1})=R(\tilde Q)^{-1}.
$$
The order is reversed because the right multiplication acts on the right factor; the powers and the inverse are not reversed, since they involve one element only.

**The two families commute.** For all $\tilde Q_1,\tilde Q_2$,
$$
L(\tilde Q_1)R(\tilde Q_2)=R(\tilde Q_2)L(\tilde Q_1).
$$
The identity is the associativity of the product, read on the two sides. It says that the left copy and the right copy are mutual commutants inside the ambient matrix algebra.

**The product of a left and a right basis matrix.** The product $L_{e_\mu}^{\mathrm{pau}} R_{e_\nu}^{\mathrm{pau}}$ is a monomial matrix with entries $0,\pm1,\pm i$; it need not lie in either copy. A left matrix and a right matrix commute, and this commutation is the defining property of the two copies.

## The Trace

**The trace is the scalar part.** For every $\tilde Q$,
$$
\operatorname{Tr}L(\tilde Q)=\operatorname{Tr}R(\tilde Q)=4Q_t.
$$
The trace is the sum of the four diagonal entries, each pair contributing $2Q_t$; the factor $4$ is the dimension of $\mathbb{B}$. The trace sees the scalar part and no vector coefficient.

**The trace of a basis matrix.** On the basis,
$$
\operatorname{Tr}L_{e_t}^{\mathrm{pau}}=\operatorname{Tr}R_{e_t}^{\mathrm{pau}}=4,\qquad
\operatorname{Tr}L_{\vec e_x}^{\mathrm{pau}}=\operatorname{Tr}L_{\vec e_y}^{\mathrm{pau}}=\operatorname{Tr}L_{\vec e_z}^{\mathrm{pau}}=0,
\qquad
\operatorname{Tr}R_{\vec e_x}^{\mathrm{pau}}=\operatorname{Tr}R_{\vec e_y}^{\mathrm{pau}}=\operatorname{Tr}R_{\vec e_z}^{\mathrm{pau}}=0.
$$
The trace is $\mathbb{C}$-linear and additive. It is not multiplicative; the trace of a product is not the product of the traces.

**The trace of a product.** For all $\tilde Q_1,\tilde Q_2$,
$$
\operatorname{Tr}\bigl(L(\tilde Q_1)L(\tilde Q_2)\bigr)
=4\operatorname{Sc}(\tilde Q_1\tilde Q_2),
$$
where $\operatorname{Sc}$ is the scalar part. The identity is the trace of the left matrix of the product, read through the preceding formula. The same identity holds for two right matrices. A left and a right matrix give
$$
\operatorname{Tr}\bigl(L(\tilde Q_1)R(\tilde Q_2)\bigr)=4Q_{1t}Q_{2t};
$$
the mixed trace sees the two scalar parts only.

## The Determinant

**The determinant is the square of the central scalar.** For every $\tilde Q$,
$$
\det L(\tilde Q)=\det R(\tilde Q)=\langle\tilde Q\rangle_{\natural}^2
=(Q_t^2+B^2)^2.
$$
The determinant is the square of the $2\times2$ determinant, since the $2\times2$ image has determinant $\langle\tilde Q\rangle_{\natural}$ and the regular matrix is two copies of it. It is a quartic in the four coefficients, and it vanishes exactly on the null cone $\langle\tilde Q\rangle_{\natural}=0$.

**The characteristic polynomial.** The characteristic polynomial of $L(\tilde Q)$ is
$$
\chi_{L(\tilde Q)}(\lambda)
=\bigl(\lambda^2-2Q_t\lambda+\langle\tilde Q\rangle_{\natural}\bigr)^2
=\bigl((\lambda-Q_t)^2+B^2\bigr)^2 .
$$
The eigenvalues are $\lambda_\pm=Q_t\pm iB$, where $B$ is a square root of $B^2=Q_x^2+Q_y^2+Q_z^2$, each with algebraic multiplicity two. Their sum is $4Q_t$, their product is $\langle\tilde Q\rangle_{\natural}^2$, and the two facts are the trace and the determinant. The same polynomial is the characteristic polynomial of $R(\tilde Q)$, because the two matrices are related by the swap and transposition.

**The determinant is multiplicative.** For all $\tilde Q_1,\tilde Q_2$,
$$
\det L(\tilde Q_1\tilde Q_2)=\det L(\tilde Q_1)\det L(\tilde Q_2),
$$
and the same identity holds for $R$. The determinant is the multiplicative invariant of the algebra; the trace is the additive one.

**The basis determinants.** Every basis matrix has determinant $1$:
$$
\det L_{e_\mu}^{\mathrm{pau}}=\det R_{e_\mu}^{\mathrm{pau}}=1\qquad(\mu=t,x,y,z).
$$
The determinant of a sum is not the sum of the determinants; a sum of two invertible matrices can be singular, as $L_{\vec e_x}^{\mathrm{pau}}+R_{\vec e_x}^{\mathrm{pau}}$ shows.

**The invertibility and the rank.** The following are equivalent: $\tilde Q$ is invertible; $\langle\tilde Q\rangle_{\natural}\neq0$; $\mathsf M_2(\tilde Q)$ is invertible; $L(\tilde Q)$ is invertible; $R(\tilde Q)$ is invertible. When $\langle\tilde Q\rangle_{\natural}=0$, the rank of the regular matrix is $0$, $2$ or $4$, never $1$ or $3$, because the matrix is two equal copies of the $2\times2$ image. The rank is twice the rank of $\mathsf M_2(\tilde Q)$.

## The Six Subspaces

**The table.** The six remarkable subspaces are defined in *Subspaces and Decompositions of the Biquaternion Algebra*. On the image of the Pauli representation they become the conditions of the table. Write $A$ for the $2\times2$ block, so $M=L(\tilde Q)=\mathrm I_2\otimes A$, and put
$$
A_{\mathbb{H}}(a,b)=\begin{pmatrix}a&b\\-\bar b&\bar a\end{pmatrix},\qquad
A_{i\mathbb{H}}(a,b)=\begin{pmatrix}a&b\\ \bar b&-\bar a\end{pmatrix}.
$$
Write $\vec q=(q_x,q_y,q_z)$ and $\vec q'=(q'_x,q'_y,q'_z)$, and recall $Q_\mu=q_\mu+iq'_\mu$, $B^2=Q_x^2+Q_y^2+Q_z^2$. In the table, $M^{\dagger}=\overline M^{\mathsf T}$ is the conjugate transpose. The table gives the condition on $M$ inside the image $\mathbb{B}_L$, the real dimension of the subspace, the trace of $M$, and the determinant of the $2\times2$ image. In the first row, $\lambda=Q_t$.

| Subspace | Defining condition | Condition on $M$ in the image | Real dim. | Trace | $\det\mathsf M_2(\tilde Q)$ |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\tilde Q^{\natural}=\tilde Q$ | $M=\lambda\mathrm I_4$ | $2$ | $4Q_t$ | $Q_t^2$ |
| $\mathrm{Vect}(\mathbb{B})$ | $\tilde Q^{\natural}=-\tilde Q$ | $\operatorname{Tr}M=0$ | $6$ | $0$ | $B^2$ |
| $\mathbb{H}_{\mathbb{B}}$ | $\overline{\tilde Q}=\tilde Q$ | $M=\mathrm I_2\otimes A_{\mathbb{H}}(a,b)$ | $4$ | $4q_t$ | $\sum q_\mu^2$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $\overline{\tilde Q}=-\tilde Q$ | $M=\mathrm I_2\otimes A_{i\mathbb{H}}(a,b)$ | $4$ | $4iq'_t$ | $-\sum(q'_\mu)^2$ |
| $\mathbb{M}_+$ | $\tilde Q^{*}=\tilde Q$ | $M=M^{\dagger}$ | $4$ | $4q_t$ | $q_t^2-\lvert\vec q'\rvert^2$ |
| $\mathbb{M}_-$ | $\tilde Q^{\flat}=\tilde Q$ | $M=-M^{\dagger}$ | $4$ | $4iq'_t$ | $-(q'_t)^2+\lvert\vec q\rvert^2$ |

**The determinant of $M$.** On every row the determinant of the $4\times4$ matrix is the square of the last column, $\det M=(\det\mathsf M_2(\tilde Q))^2$. The last column is the quadratic determinant of the $2\times2$ image; the determinant of the regular matrix is the quartic obtained by squaring it.

**The warning.** Apart from the centre, the conditions in the third column are exact only inside the image. The Hermitian matrices of the ambient $M_4(\mathbb{C})$ form a real space of dimension $16$, the anti-Hermitian another, the traceless matrices a complex space of dimension $15$. The real form $\mathbb{H}_{\mathbb{B}}$ is not the space of entrywise real matrices in this frame: the frame vectors are complex, and the quaternion-shaped block $A_{\mathbb{H}}(a,b)$ is the correct condition. The conditions select the correct subspaces only when read on $M=L(\tilde Q)$.

### The Centre Subspace

**The scalar matrices.** For $\tilde Q=Q_te_t$,
$$
L(Q_te_t)=Q_t\mathrm I_4,\qquad
\operatorname{Tr}M=4Q_t,\qquad
\det M=Q_t^4,\qquad
\det\mathsf M_2(\tilde Q)=Q_t^2.
$$
The image is the complex line $\mathbb{C}\mathrm I_4$, of real dimension $2$. It meets $\mathbb{M}_+$ in the real line $\mathbb{R}\mathrm I_4$ and $\mathbb{M}_-$ in the imaginary line $i\mathbb{R}\mathrm I_4$. It is the only subspace of real dimension $2$ and the only commutative one.

### The Vector Subspace

**The traceless matrices.** For $\tilde Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$,
$$
A=\begin{pmatrix}-iQ_z&-iQ_x-Q_y\\-iQ_x+Q_y&iQ_z\end{pmatrix},\qquad
L(\tilde Q)=\mathrm I_2\otimes A .
$$
The block $A$ is traceless, and so is $M$. The image is the complex span of $L_{\vec e_x}^{\mathrm{pau}},L_{\vec e_y}^{\mathrm{pau}},L_{\vec e_z}^{\mathrm{pau}}$, of real dimension $6$. The trace is $0$, the determinant of the $2\times2$ image is $B^2$, and the determinant of $M$ is $B^4$. Inside the image, the trace condition is equivalent to $Q_t=0$. The image is closed under the commutator and not under the product. It is not the space of skew-symmetric matrices in this frame; the transpose dictionary of the axis-free basis does not carry over to this frame without the matrices $C_L$ and $C_R$.

### The Quaternion Subspace

**The quaternion-shaped matrices.** For $\tilde Q=q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$ with real coefficients,
$$
A=A_{\mathbb{H}}(a,b)=\begin{pmatrix}a&b\\-\bar b&\bar a\end{pmatrix},
\qquad
a=q_t-iq_z,\quad b=-iq_x-q_y .
$$
Then
$$
\operatorname{Tr}M=4q_t,\qquad
\det\mathsf M_2(\tilde Q)=\sum_{\mu}q_\mu^2=q_t^2+q_x^2+q_y^2+q_z^2 .
$$
The image is the space of quaternion-shaped blocks, of real dimension $4$. The quadratic determinant is positive definite, and it vanishes only at $\tilde Q=0$. The image is closed under multiplication and is a division algebra. The block display is the usual quaternion matrix $\begin{pmatrix}a&b\\-\bar b&\bar a\end{pmatrix}$, written in the Peirce frame.

### The Anti-Quaternion Subspace

**The anti-quaternion-shaped matrices.** For $\tilde Q=iq'_te_t+iq'_x\vec e_x+iq'_y\vec e_y+iq'_z\vec e_z$,
$$
A=A_{i\mathbb{H}}(a,b)=\begin{pmatrix}a&b\\ \bar b&-\bar a\end{pmatrix},
\qquad
a=q'_z+iq'_t,\quad b=q'_x-iq'_y .
$$
Then
$$
\operatorname{Tr}M=4iq'_t,\qquad
\det\mathsf M_2(\tilde Q)=-\sum_{\mu}(q'_\mu)^2 .
$$
The image is the space of anti-quaternion-shaped blocks, of real dimension $4$. The quadratic determinant is non-positive, and it vanishes only at $\tilde Q=0$. The image is not closed under multiplication: the product of two anti-quaternion-shaped blocks is quaternion-shaped.

### The Hermitian Subspace

**The Hermitian matrices.** For $\tilde Q=q_te_t+iq'_x\vec e_x+iq'_y\vec e_y+iq'_z\vec e_z$,
$$
A=\begin{pmatrix}
q_t+q'_z&q'_x-iq'_y\\
q'_x+iq'_y&q_t-q'_z
\end{pmatrix},
\qquad
L(\tilde Q)=L(\tilde Q)^{\dagger},\qquad
\operatorname{Tr}M=4q_t,\qquad
\det\mathsf M_2(\tilde Q)=q_t^2-\lvert\vec q'\rvert^2 .
$$
The image is the space of Hermitian matrices of the regular form, of real dimension $4$. The condition is exact inside the image because $L(\tilde Q)^{\dagger}=L(\tilde Q^{*})$ and $L$ is injective. The quadratic determinant is indefinite: it is positive when $q_t^2>\lvert\vec q'\rvert^2$ and negative when $q_t^2<\lvert\vec q'\rvert^2$. The image is not a subalgebra.

### The Anti-Hermitian Subspace

**The anti-Hermitian matrices.** For $\tilde Q=iq'_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$,
$$
A=\begin{pmatrix}
i(q'_t-q_z)&-iq_x-q_y\\
-iq_x+q_y&i(q'_t+q_z)
\end{pmatrix},
\qquad
L(\tilde Q)=-L(\tilde Q)^{\dagger},\qquad
\operatorname{Tr}M=4iq'_t,\qquad
\det\mathsf M_2(\tilde Q)=-(q'_t)^2+\lvert\vec q\rvert^2 .
$$
The image is the space of anti-Hermitian matrices of the regular form, of real dimension $4$. The condition is $\tilde Q^{\flat}=\tilde Q$, that is $\tilde Q^{*}=-\tilde Q$. The quadratic determinant is indefinite, with the sign opposite to the Hermitian determinant. The image is a Lie algebra under the commutator, not a subalgebra under the product.

### The Three Splits

**The three decompositions.** The six subspaces pair into the three decompositions
$$
\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathrm{Vect}(\mathbb{B})
=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}
=\mathbb{M}_+\oplus\mathbb{M}_-,
$$
of real dimensions $2+6$, $4+4$ and $4+4$. The first is the scalar–vector split. The second is the real–imaginary split. The third is the Hermitian–anti-Hermitian split. No one of the three refines another.

**The intersections.** The centre meets $\mathbb{M}_+$ in $\mathbb{R}\mathrm I_4$ and $\mathbb{M}_-$ in $i\mathbb{R}\mathrm I_4$. The vector subspace meets $\mathbb{H}_{\mathbb{B}}$ in the real pure quaternions, of real dimension $3$, and $i\mathbb{H}_{\mathbb{B}}$ in the imaginary pure quaternions, of real dimension $3$. It meets $\mathbb{M}_+$ in $i$ times the real vector triple, and $\mathbb{M}_-$ in the real vector triple. The quaternion and anti-quaternion subspaces meet only at $0$, and so do the Hermitian and anti-Hermitian subspaces.

**The closure.** The centre and the quaternion subspace are subalgebras. The vector subspace is a Lie subalgebra under the commutator, not a subalgebra under the product. The anti-quaternion subspace and the two Hermitian subspaces are neither. Multiplication by $i$ exchanges $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, and it exchanges $\mathbb{M}_+$ and $\mathbb{M}_-$.

## The Comparison Table

**The three frames.** The table sets the Peirce frame beside the coefficient basis, which is the frame of *$M_4(\mathbb{C})$ Axis-Free Representation*, and beside a generic frame $C^{-1}L(\tilde Q)C$ with $C\in GL_4(\mathbb{C})$. It is stated here, at the end of this article, because the Peirce frame is the one this article builds; the coefficient article lists its own properties and does not compare them.

| Property | Peirce (this frame) | Coefficient (axis-free) | Generic |
|---|---|---|---|
| entries in $\{0,\pm1,\pm i\}$ | yes | yes | no |
| entries in $\{0,\pm1\}$ | no | yes | no |
| monomial | yes | yes | no |
| signed permutations | no | yes | no |
| real matrices | no | yes | no |
| orthogonal over $\mathbb{R}$ | no | yes | no |
| unitary over $\mathbb{C}$ | yes | yes | no |
| the entries are the signs of the multiplication table | no | yes | no |
| tensor-product display | yes | no | no |
| idempotents adapted to the frame | yes | no | no |
| cyclic symmetry of $x,y,z$ | no | yes | no |
| the stitch is a sign matrix $\operatorname{diag}(\pm1)$ | no | yes | no |
| transpose is the conjugation | no | yes | no |
| $Q_8$ acting on $\mathbb{R}^4$ | no | yes | no |

**The reading of the table.** No column says yes in every row. The two computed frames trade one bundle of properties for the other, and neither is a defect of the other: the Peirce frame keeps the tensor display, the idempotents and the unitary entries, and gives up realness, integrality and sparsity; the coefficient basis keeps the real integers and the signed permutations, and gives up the idempotents and the tensor display. The generic column has none of the properties, and it is the column of almost every frame.

**The invariants are common to all three columns.** Trace $4Q_t$, determinant $\langle\tilde Q\rangle_{\natural}^2$, characteristic polynomial $((\lambda-Q_t)^2+B^2)^2$, spectrum $Q_t\pm iB$ twice, rank in $\{0,2,4\}$: none of these is a row of the table, because none of them distinguishes the frames. They are properties of the element, and the element is the same in all of them.

**What the table does not decide.** It does not name a preferred representation and it does not compare elements: a row is a property of an array, and an array is a display of an operator in a frame. The two frames display the same operators, related by the Peirce change $C_{\Pi}$ of §*The Switch to the Axis-Free Matrices*, and each row says what one display makes visible and the other does not.

## Summary

The standard Peirce frame is built from the root $\vec\Xi=i\vec e_z$, whose square is $e_t$. The two idempotents are $\tilde\Pi_\pm=(e_t\pm\vec\Xi)/2$, the two mixed units are $\vec\Upsilon_\pm=(i\vec e_x\pm\vec e_y)/2$, and the frame is $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$. The root is the only choice made: it fixes the idempotents, the frame is fixed by them up to the scale of the mixed units, and the roots form a two-parameter family, of which the six coordinate roots give the three coordinate frames up to relabelling and the exchange of the idempotents.

The left matrix is $\mathrm I_2\otimes\mathsf M_2(\tilde Q)$ and the right matrix is $\mathsf M_2(\tilde Q)^{\mathsf T}\otimes\mathrm I_2$. The four left matrices and the four right matrices are monomial, with entries $0,\pm1,\pm i$, unitary, of determinant one; each family is a basis of its copy. The stitch between the two matrices is $R(\tilde Q)=\mathsf P L(\tilde Q)^{\mathsf T}\mathsf P$, a pure swap with no signs, and the switch from the coefficient basis is $L=C_{\Pi}^{-1}L^{\mathrm{axf}}C_{\Pi}$, $R=C_{\Pi}^{-1}R^{\mathrm{axf}}C_{\Pi}$, with $\det C_{\Pi}=-\tfrac14$ and $C_{\Pi}^{\mathsf T}DC_{\Pi}=\tfrac12\mathsf P$. The switch itself is one matrix and its inverse, in four columns each, and it splits into two $2\times2$ blocks: the idempotents in the plane of $e_t,\vec e_z$, the nilpotents in the plane of $\vec e_x,\vec e_y$, the two planes never mixed. The columns of $C_{\Pi}^{-1}$ read the other way give $e_t=\tilde\Pi_++\tilde\Pi_-$, $\vec e_x=-i(\vec\Upsilon_++\vec\Upsilon_-)$, $\vec e_y=\vec\Upsilon_+-\vec\Upsilon_-$, $\vec e_z=i(\tilde\Pi_--\tilde\Pi_+)$, and the coefficient columns change by $q_e=C_{\Pi}p$, $p=C_{\Pi}^{-1}q_e$.

The trace is $4Q_t$, the determinant is $\langle\tilde Q\rangle_{\natural}^2$, and the eigenvalues are $Q_t\pm iB$, each twice. The six subspaces are the scalar, traceless, quaternion-shaped, anti-quaternion-shaped, Hermitian and anti-Hermitian matrices of the image, of real dimensions $2,6,4,4,4,4$, with the traces and determinants of the table of §*The Six Subspaces*.

The sixteen products $L_{e_\mu}^{\mathrm{pau}}R_{e_\nu}^{\mathrm{pau}}$, the coefficient matrix $c(M)$ and the length $\ell(M)=\operatorname{rank}c(M)$ are the subject of the companion article *$M_4(\mathbb{C})$ Pauli Representation : Operators*, together with the congruence that makes the length survive a change of element basis.

The comparison of §*The Comparison Table* closes the article: no frame says yes in every row, the Peirce frame trades realness and sparsity for the tensor display and the idempotents, and the trace, the determinant, the spectrum and the rank are the same in every frame because they are properties of the element.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{P}=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$ | the standard Peirce frame |
| $\vec\Xi=i\vec e_z$ | the root, $\vec\Xi^2=e_t$ |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$ | the two idempotents |
| $\vec\Upsilon_\pm=\tfrac12(i\vec e_x\pm\vec e_y)$ | the two mixed units |
| $L_{e_\mu}^{\mathrm{pau}}$, $R_{e_\mu}^{\mathrm{pau}}$ | the left and right matrices of the four units |
| $L(\tilde Q)$, $R(\tilde Q)$ | the left and right matrices of $\tilde Q$ |
| $A=\mathsf M_2(\tilde Q)$ | the $2\times2$ image, the block of $L(\tilde Q)$ |
| $\sigma_1,\sigma_2,\sigma_3$ | the Pauli matrices, $\mathsf M_2(\vec e_k)=-i\sigma_k$ |
| $C_{\Pi}$ | the Peirce change, columns the frame vectors in the coefficient basis |
| $\tau_1,\dots,\tau_4$ | the four frame vectors $\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-$ |
| $e_1,\dots,e_4$ | the four units $e_t,\vec e_x,\vec e_y,\vec e_z$ |
| $q_e$, $p$ | the coefficient column and the Peirce column of an element, $q_e=C_{\Pi}p$ |
| $D=\operatorname{diag}(1,-1,-1,-1)$ | the Gram matrix of the plain product in the coefficient basis, $C_{\Pi}^{\mathsf T}DC_{\Pi}=\tfrac12\mathsf P$ |
| $\mathbb{B}_L,\mathbb{B}_R$ | the two four-dimensional copies, $\rho_L(\mathbb{B})$ and $\rho_R(\mathbb{B})$ |
| $\mathsf P$ | the swap matrix, $\mathsf P(A\otimes B)\mathsf P=B\otimes A$ |
| $C_L=\mathrm I_2\otimes\sigma_2$, $C_R=\sigma_2\otimes\mathrm I_2$ | the transpose dictionaries of the Peirce frame |
| $\langle\tilde Q\rangle_{\natural}$ | $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ |
| $\langle X,Y\rangle_*=\operatorname{Sc}(XY^{*})$ | the Hermitian form on $\mathbb{B}$ |
| $B^2$ | $Q_x^2+Q_y^2+Q_z^2$ |
| $q_\mu$, $q'_\mu$ | the real and imaginary parts of $Q_\mu$ |

## Further Reading

**Families of Matrix Representations** and the general theory:

- [Families of Matrix Representations](families-of-matrix-representations.html), for the two families, the stitch and the change of frame in general.
- [Subspaces and Decompositions of the Biquaternion Algebra](subspaces-and-decompositions-of-the-biquaternion-algebra.html), for the six subspaces and the three decompositions.
- [The Element, the Coordinates and the Conjugations in the Biquaternion Algebra](the-element-the-coordinates-and-the-conjugations.html), for the four conjugations and the coordinate systems.
- [$M_2(\mathbb{C})$ Pauli Representation](m2c-pauli-representation.html), for this article continued at the element size: the block $A$ read on its own, with the trace $2Q_t$, the determinant $\langle\tilde Q\rangle_{\natural}$ and the four norms.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the algebra and the multiplication table.
- [Matrix Representations Conventions](matrix-representations-conventions.html), for the canonical frame and the tensor displays of the two copies.
- [$M_4(\mathbb{C})$ Axis-Free Representation](m4c-axis-free-representation.html), for the same content in the coefficient basis and the sign stitch.
- [$M_4(\mathbb{C})$ Pauli Representation : Operators](m4c-pauli-representation-operators.html), for the products, the coefficient matrix, the length and its invariance.
