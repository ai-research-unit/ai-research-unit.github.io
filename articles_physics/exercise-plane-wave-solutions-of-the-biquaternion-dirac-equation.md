# __Exercise: Plane-Wave Solutions of the Biquaternion Dirac Equation__

## Introduction

This is a worked exercise on the biquaternion Dirac equation, written **in the biquaternion algebra and in cells**. The five cells are defined once, in *The Five Cells*, and their arrays are collected in the Gamma section, so that they can be identified with the parent's; in the body the symbols $iR_{\vec e_x}^{\mathrm{axf}},iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},-iR_{\vec e_z}^{\mathrm{axf}}$ name left and right multiplications, and the working objects are biquaternions, not columns. The gammas are named only in the Gamma section; everywhere else the cells do the work: the four coordinate cells $c_\mu$, and the chirality $-iR_{\vec e_z}^{\mathrm{axf}}$. The parent article, *The Biquaternion Dirac Equation — Solutions and the Non-Relativistic Limit*, supplies the equation, the field, the two bases, and the mass shell. The present exercise re-derives the parent's results in the algebra and supplies what the parent leaves implicit: the explicit spinors, the normalisation in the biquaternion pairing, the spin sums as operator identities, the massless limit, the algebra of the cells and the change of basis.

Two forms of the equation appear below, and they must not be mixed. The **two-sided form** is one equation on a single biquaternion $\tilde\Psi$,
$$
\slashed p\,\tilde\Psi=m\tilde\Psi,\qquad \slashed p=E\,R_{i\vec e_x}^{\mathrm{axf}}-p_k\,L_{i\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},
$$
whose symbol carries a left and a right multiplication at once. The **chiral form** is a pair of equations on the two Peirce coordinates,
$$
(E-\boldsymbol\sigma\cdot\vec p)\,\psi_-=m\,\psi_+,\qquad
(E+\boldsymbol\sigma\cdot\vec p)\,\psi_+=m\,\psi_-,
$$
and it is the two-sided form read in the basis of the two chiralities. The first form lives in the operator algebra and is the one that states the commutation relations, the spin sums and the determinant; the second is the one in which the spinors are written. Problems 1, 2 and 4 use the pair, Problems 3, 5 and 7 the operator, and Problem 6 the norm.

The seven problems are: **(1)** the spinors at rest and at general momentum; **(2)** the covariant normalisation and the orthogonality; **(3)** the spin sums; **(4)** the massless limit and the helicity–chirality locking; **(5)** the algebra of the cells and the change of basis; **(6)** the biquaternionic mass shell; **(7)** the helicity blocks and the block determinant.

## The Dictionary of Operators

The translation is a dictionary of operators. A Dirac spinor is a biquaternion $\tilde\Psi$. Write $R_a$ and $L_a$ for right and left multiplication,
$$
R_a(\tilde Q)=\tilde Q a,\qquad L_a(\tilde Q)=a\tilde Q .
$$
Left multiplications compose in the order of the indices, $L_aL_b=L_{ab}$, and right multiplications in the reverse order, $R_aR_b=R_{ba}$; every left multiplication commutes with every right one, so a product $L_aR_b$ is read without ambiguity as $x\mapsto axb$. That reversal is the only subtlety of the calculus, and it is what makes the product of two cells below come out with the indices interchanged.

**The scalar $i$.** It is central, so multiplication by $i$ on the left and on the right are the same operator, $L_i=R_i=i$. A factor $i$ in front of a cell can therefore be pushed into its argument,
$$
iR_{\vec e_x}^{\mathrm{axf}}=R_{i\vec e_x}^{\mathrm{axf}},\qquad -iR_{\vec e_z}^{\mathrm{axf}}=R_{-i\vec e_z}^{\mathrm{axf}},\qquad iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=L_{i\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},
$$
and the two forms are used interchangeably below. With $i^2=-1$ and $\vec e_k^2=-e_t$ a product of two cells then collapses in one line:
$$
(R_{i\vec e_x}^{\mathrm{axf}})^2=R_{i^2\vec e_x^2}=R_{e_t}^{\mathrm{axf}}=1,\qquad
(L_{i\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})^2=L_{i^2\vec e_k^2}^{\mathrm{axf}}R_{\vec e_y^2}^{\mathrm{axf}}=L_{e_t}^{\mathrm{axf}}R_{-e_t}^{\mathrm{axf}}=-1,\qquad
(R_{-i\vec e_z}^{\mathrm{axf}})^2=R_{e_t}^{\mathrm{axf}}=1 .
$$
Each line is one use of $i^2=-1$ and one use of $\vec e_k^2=-e_t$. Both minus signs are needed, and dropping either of them flips the square.

**The corpus convention.** The corpus represents $\mathbb B$ on $\mathbb C^2$ by
$$
e_t\mapsto I_2,\qquad \vec e_x\mapsto-i\sigma_x,\quad \vec e_y\mapsto-i\sigma_y,\quad \vec e_z\mapsto-i\sigma_z,\qquad i\mapsto iI_2,
$$
so that
$$
i\vec e_k\mapsto\sigma_k,\qquad \vec e_k\mapsto-i\sigma_k .
$$
The factor $i$ is not decoration. $\sigma_k$ is Hermitian; $\vec e_k$ alone maps to an anti-Hermitian matrix. Every sign below follows from this line.

## The Five Cells

**The five cells, complete.** The Dirac space is $\mathbb C^4$, the same four complex dimensions as $\mathbb B$. Order the four components as $(\psi_{L1},\psi_{L2},\psi_{R1},\psi_{R2})$, the parent's chiral order. As operators on a pair $(\xi,\eta)$ of chiral biquaternions,
$$
iR_{\vec e_x}^{\mathrm{axf}}(\xi,\eta)=(\eta,\xi),\qquad
iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}(\xi,\eta)=(i\vec e_k\eta,\,-i\vec e_k\xi),\qquad
-iR_{\vec e_z}^{\mathrm{axf}}(\xi,\eta)=(-\xi,\eta).
$$
The arrays of the five, in the chiral basis and in the Dirac basis, are in the Gamma section.

The cell of the coordinate $x_\mu$ is
$$
c_\mu=iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}},\qquad \nu(t)=x,\quad \nu(k)=y ,
$$
that is $c_0=iR_{\vec e_x}^{\mathrm{axf}}=R_{i\vec e_x}^{\mathrm{axf}}$ and $c_k=iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=L_{i\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, since $L_{e_t}^{\mathrm{axf}}=1$. So each cell is a left multiplication times a right one, the time cell being a pure right multiplication. The temporal unit of the time cell is $e_t$, the identity; the three space cells carry $i\vec e_k$, the spatial unit times the scalar $i$, and that factor turns the anti-Hermitian $\vec e_k$ into the Hermitian $\sigma_k$. The index $\mu$ is the coordinate index: the cell is the one paired with $\partial/\partial x_\mu$ in the $\mathbb{M}_-$ frame, and the derivative is taken with respect to $x_\mu=(t',x,y,z)$, not with respect to $Q_\mu$. That is the precise sense in which the cells align with the coordinates.

**What each cell means.**

| object | entry | meaning |
|---|---|---|
| $iR_{\vec e_x}^{\mathrm{axf}}$ | $e_t$ | cell paired with $\partial/\partial t'$; exchanges the two chiral blocks |
| $iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | $i\vec e_k$ | cells paired with $\partial/\partial x_k$; each squares to $-1$ |
| $-iR_{\vec e_z}^{\mathrm{axf}}$ | $-e_t$ on the left, $+e_t$ on the right | chirality, $-1$ on the left and $+1$ on the right; $P_{L,R}=\tfrac12\bigl(1\mp(-iR_{\vec e_z}^{\mathrm{axf}})\bigr)$ |
| $\Omega=c_0c_1c_2c_3$ | $-R_{\vec e_z}^{\mathrm{axf}}$ | volume cell; $\Omega^2=-1$ and $i\Omega=R_{-i\vec e_z}^{\mathrm{axf}}$ is the chirality cell |

The Dirac basis is reached by right multiplication by $\tilde W=(e_t+\vec e_y)/\sqrt2$, the change of basis of Problem 5. There
$$
(iR_{\vec e_x}^{\mathrm{axf}})^{d}=R_{i\vec e_z}^{\mathrm{axf}},\qquad
(iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})^{d}=iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=L_{i\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
(-iR_{\vec e_z}^{\mathrm{axf}})^{d}=R_{i\vec e_x}^{\mathrm{axf}},
$$
and the arrays are in the Gamma section. In that basis $(iR_{\vec e_x}^{\mathrm{axf}})^{d}$ is diagonal on the Peirce components and separates the upper and the lower pair; that is why the non-relativistic limit is simplest there. The spatial cells do not change.

## Why Four Left Multiplications Do Not Suffice

**The four units cannot be four left multiplications.** $e_t=1$ is the identity, so it commutes with every $\vec e_k$: $\{e_t,\vec e_k\}=2\vec e_k\neq0$, while the cells must anticommute. No scalar helps, since a scalar commutes with everything. So no assignment of the four units to four left multiplications can satisfy the Clifford relations. Left multiplication is an injective complex-linear map $L:\mathbb B\to\mathrm{End}_{\mathbb C}(\mathbb B)$, so any family of left multiplications generates at most a four-complex-dimensional algebra. The Clifford algebra generated by four anticommuting cells has complex dimension sixteen. One cell must act elsewhere.

**The three completions.** There are three, and they are not equivalent. (a) The star: $iR_{\vec e_x}^{\mathrm{axf}}=\varkappa$, $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=\varkappa L_{-i\vec e_k}^{\mathrm{axf}}$ on the real eight-dimensional $\mathbb B$. (b) Left and right multiplications: the dictionary of this article, with $iR_{\vec e_x}^{\mathrm{axf}}$ and $-iR_{\vec e_z}^{\mathrm{axf}}$ right multiplications and $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ a product of a left and a right multiplication. (c) An odd element: the double $\mathbb B\oplus\mathbb B\eta$, whose block matrices are exactly the biquaternion-entry matrices listed in the Gamma section.

The star is antilinear in the coefficient $i$: $\varkappa L_i=-L_i\varkappa$. In (a) the coefficient $i$ is therefore not the quantum complex structure, and the standard chirality $i\Omega=R_{-i\vec e_z}^{\mathrm{axf}}$ is $\pm1$. Forms (b) and (c) are complex-linear and isomorphic as Clifford modules; they differ in the carrier, (b) one biquaternion with a spin and a chirality index, (c) a pair of chiral biquaternions. The exercise uses (b), because its spinors are single biquaternions and it needs $P_L\neq P_R$.

**The star still appears, but elsewhere.** $\varkappa$ is not a cell in this dictionary; it is the real structure that defines the Dirac adjoint, and it enters the pairing $\langle\tilde\Psi,\tilde\Phi\rangle_{\mathrm D}=\mathrm{Tr}(\tilde\Psi^{*}\tilde\Phi\,i\vec e_x)$ of Problem 2. The same algebra carries both the cells (left and right multiplications) and the antilinear operations (the star); they are different roles, and the exercise keeps them apart.

## The Carrier and the Matrix Models

**The carrier is $\mathbb C^4$; the cells are $4\times4$ matrices.** The biquaternion algebra has complex dimension four, on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$. The Dirac spinor is one biquaternion, so it has four complex components, and each $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$ is a $4\times4$ complex matrix on them. This is forced by dimension: $\mathrm{Cl}_{1,3}\otimes\mathbb C\cong M_4(\mathbb C)$ has complex dimension sixteen, and its irreducible module is $\mathbb C^4$. A $2\times2$ matrix cannot exist.

The corpus carries three matrix languages for the same four-dimensional space, and they must not be confused.

| model | map | image | what it carries |
|---|---|---|---|
| $M_2(\mathbb C)$ | $b\mapsto\mathsf M_2(b)$ | complex dimension 4 | the biquaternion and its product |
| $M_4(\mathbb C)_{\mathbb{B},L}$ | $b\mapsto L_b$ | complex dimension 4 | an isomorphic copy of $\mathbb B$; the left action, $\mathrm{diag}\bigl(\mathsf M_2(b),\mathsf M_2(b)\bigr)$ in the Peirce basis |
| $M_4(\mathbb C)$ (matrix representation) | a basis of $\mathbb B$ in $\mathbb B\otimes\mathbb B^{\mathrm{opp}}\cong\operatorname{End}_{\mathbb C}(\mathbb B)$ | complex dimension 16 | the five cells, and every complex-linear operator |

The middle row is the point. $M_2(\mathbb C)$ and $M_4(\mathbb C)_{\mathbb{B},L}$ are two pictures of the same four-dimensional algebra, not two sizes of Clifford algebra. The left regular image is a four-dimensional algebra, closed under products. The five cells generate a sixteen-dimensional algebra, so they cannot all lie in it. They live in the third row, the operator algebra whose matrix representation is $M_4(\mathbb C)$; the corpus builds it from the left and the right multiplications.

**How four and four become sixteen.** The two regular images are not disjoint. Each has complex dimension four, and they meet in the scalars, because $L_{e_t}^{\mathrm{axf}}=R_{e_t}^{\mathrm{axf}}=1$. Their sum therefore has dimension $4+4-1=7$, not $16$, and the direct sum $\mathbb B\oplus\mathbb B$ has complex dimension eight, so adding the right image to the left one doubles nothing. Composition does the doubling: the operator $L_aR_b$ is bilinear in the pair $(a,b)$, so the operators it produces span the tensor product
$$
\{L_aR_b\}=L(\mathbb B)\cdot R(\mathbb B)\;\cong\;\mathbb B\otimes\mathbb B^{\mathrm{opp}},
$$
of complex dimension $4\times4=16$. The product of two operators is a new operator, and the product of the two four-dimensional families fills the whole operator algebra: $4+4=7$, but $4\times4=16$.

**The matrix units.** The count is exact on the Peirce basis. With $\mathcal P=(\tilde\Pi_+,\vec\Upsilon_y,\vec\Upsilon_x,\tilde\Pi_-)$ and $P_i$ the $i$-th element, read each $P_i$ as a matrix unit $E_{a_i b_i}$ of the spin factor, so that $a_i=1+((i-1)\bmod 2)$ and $b_i=1+\lfloor(i-1)/2\rfloor$. Then
$$
L_{P_i}R_{P_j}=E_{r c},\qquad r=a_i+2\,(b_j-1),\quad c=b_i+2\,(a_j-1).
$$
The row $r$ carries the spin row $a_i$ of the first factor and the chirality index $b_j$ of the second; the column $c$ carries the two remaining indices. The map $(i,j)\mapsto(r,c)$ is a bijection of $\{1,2,3,4\}^2$ onto itself, so the sixteen products are the sixteen matrix units, each of coefficient one, and they are a basis of $\operatorname{End}_{\mathbb C}(\mathbb B)$.

The five cells are linear combinations of these products. That is why they are $4\times4$ matrices in the full $M_4(\mathbb C)$ and not elements of either regular image.

**The two-sided products and the five cells.** A cell is not a sandwich: it is a single two-sided operator $L_{a}R_{b}$ whose pair $(a,b)$ is fixed by the index. A sandwich has the second slot tied to the first, $b=a^{*}$; the five-cell set leaves it free. The two-sided product $L_{a}R_{b}$ sends $x$ to $axb$, and the five are the three cases
$$
c_0=L_{e_t}^{\mathrm{axf}}R_{\,i\vec e_x}^{\mathrm{axf}},\qquad
c_k=L_{i\vec e_k}^{\mathrm{axf}}R_{\,\vec e_y}^{\mathrm{axf}},\qquad
i\Omega=L_{e_t}^{\mathrm{axf}}R_{\,-i\vec e_z}^{\mathrm{axf}},
$$
that is the pairs $(a,b)=(e_t,i\vec e_x)$, $(i\vec e_k,\vec e_y)$ and $(e_t,-i\vec e_z)$: four coordinate cells and the chirality, which is not a coordinate cell and so carries no index $\mu$. In matrix form $L_{a}R_{b}=\mathsf M_{4L}(a)\mathsf M_{4R}(b)$, so each of the five is a product of a left regular matrix with a right one. The corpus's $M_4(\mathbb C)_{\mathbb{B},L}$ model supplies the left factor; the right factor is its transposed mirror.

**Comparison with the corpus's $M_4(\mathbb C)_{\mathbb{B},L}$ tables.** On the coefficient basis the corpus tabulates the left regular matrices
$$
\mathsf M_{4L}(b)=\bigl(b e_t,\ b \vec e_x,\ b \vec e_y,\ b \vec e_z\bigr)_{\text{columns}},
$$
which are real for real $b$. None of the five is one of them. The Peirce basis shows why. There
$$
\mathsf M_{4L}(b)=\mathrm{diag}\bigl(\mathsf M_2(b),\mathsf M_2(b)\bigr),
$$
so the left action preserves the two chiral planes and acts by the same block on each. $iR_{\vec e_x}^{\mathrm{axf}}$ and $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ exchange the two planes, and $-iR_{\vec e_z}^{\mathrm{axf}}$ acts on them with opposite signs. The left regular image cannot contain them.

The five use the right factor:
$$
iR_{\vec e_x}^{\mathrm{axf}}=i\mathsf M_{4R}(\vec e_x),\qquad
iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=i\mathsf M_{4L}(\vec e_k)\mathsf M_{4R}(\vec e_y),\qquad
-iR_{\vec e_z}^{\mathrm{axf}}=-i\mathsf M_{4R}(\vec e_z).
$$
The time and chirality cells are pure right matrices; the spatial ones are products. The factor $i$ is the scalar of $\mathbb B$, which multiplies the matrix. In the Peirce basis the contrast is one line: $\mathsf M_{4L}(i\vec e_x)=\mathrm{diag}(\sigma_x,\sigma_x)$ acts on each chiral plane separately, while $iR_{\vec e_x}^{\mathrm{axf}}$ exchanges the two blocks. Both are $4\times4$ and both use $\sigma_x$.

**The matrix replacement.** The block action displayed at the top is already the matrix formulation. Because $\mathbb B\cong\mathsf M_2(\mathbb C)$, each entry $e_t$ or $i\vec e_k$ is a $2\times2$ complex matrix, and the $2\times2$ block matrix over $\mathbb B$ is a $4\times4$ complex matrix with blocks $I_2$ and $\sigma_k$. This uses the $M_2(\mathbb C)$ model as the entry. The $M_4(\mathbb C)_{\mathbb{B},L}$ model is a different embedding of the same algebra: the left regular image, block diagonal in the Peirce basis. The five cells live in the full $M_4(\mathbb C)$, not in that image. So the replacement is possible on one condition: it must use both regular representations. The $2\times2$ block form over $\mathsf M_2(\mathbb C)$ is the full $M_4(\mathbb C)$, which contains both.

The explicit arrays in the Gamma section are in the Peirce basis. The corpus's $M_4(\mathbb C)_{\mathbb{B},L}$ tables use the coefficient basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$; the two bases are related by the change of basis $\mathsf S$ of *The Polarized Module of the Biquaternion Algebra*, and neither the Clifford relations nor the spectrum depends on the choice.

## The Kronecker Form

**The two factors are two $M_2(\mathbb C)$ models.** In the Peirce basis the enveloping algebra splits as $M_2(\mathbb C)\otimes M_2(\mathbb C)$, and the carrier as $\mathbb C^2_{\rm chir}\otimes\mathbb C^2_{\rm spin}$. The order is that of $\mathcal P$, since $\mathsf M_2(\tilde\Pi_+)=E_{11}$, $\mathsf M_2(\vec\Upsilon_y)=E_{21}$, $\mathsf M_2(\vec\Upsilon_x)=E_{12}$ and $\mathsf M_2(\tilde\Pi_-)=E_{22}$: chirality is the outer index and spin the inner one, which is the parent's order $(\psi_{L1},\psi_{L2},\psi_{R1},\psi_{R2})$. With
$$
L_a=1\otimes\mathsf M_2(a),\qquad R_b=\mathsf M_2(b)^{T}\otimes1,
$$
the five are the Kronecker products
$$
R_{i\vec e_x}^{\mathrm{axf}}=\sigma_x\otimes1,\qquad L_{i\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=i\sigma_y\otimes\sigma_k,\qquad R_{-i\vec e_z}^{\mathrm{axf}}=-\sigma_z\otimes1,
$$
listed with their arrays in the Gamma section. These are $4\times4$ matrices. The first factor is chirality, the second is spin. The formula is the tensor factorization of the chiral representation, and the two factors are two $M_2(\mathbb C)$ models, not the two halves of a $2\times2$ matrix.

**The $2\times2$ array is a coordinate layout.** Write the four components as a $2\times2$ array $X$, with $X_{ij}$ the component of spin $i$ and chirality $j$. Reading the array column by column gives $(\psi_{L1},\psi_{L2},\psi_{R1},\psi_{R2})$, the Peirce order. In this layout the $4\times4$ operator is
$$
X\longmapsto \mathsf M_2(a)\,X\,\mathsf M_2(b),
$$
a product of two $2\times2$ factors acting on the two indices. It is not a $2\times2$ matrix: the array has four entries, and the operator on the four entries is $4\times4$. With the corpus map,
$$
\mathsf M_2(i\vec e_k)=\sigma_k,\qquad \mathsf M_2(\vec e_y)=-i\sigma_y,
$$
and $\sigma_y^T=-\sigma_y$, so $\mathsf M_2(\vec e_y)^T=+i\sigma_y$. Hence
$$
L_{i\vec e_k}^{\mathrm{axf}}=1\otimes\sigma_k,\qquad
R_{i\vec e_x}^{\mathrm{axf}}=\sigma_x\otimes 1,\quad R_{\vec e_y}^{\mathrm{axf}}=i\sigma_y\otimes 1,\quad R_{i\vec e_z}^{\mathrm{axf}}=\sigma_z\otimes 1 .
$$
The three left multiplications form a Pauli triple of the spin factor; the three right multiplications form a Pauli triple of the chirality factor. The side on which a unit multiplies is what decides which factor it acts on, and the products give back the five cells whose arrays are in the Gamma section.

The unit $\vec e_y$ is not a spatial direction in this formula. On the right it is the chirality epsilon $i\sigma_y$, not a rotation. The formula assigns the three chirality units so that $(iR_{\vec e_x}^{\mathrm{axf}})^2=1$, $(iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})^2=-1$ and $(-iR_{\vec e_z}^{\mathrm{axf}})^{2}=1$; the asymmetry is the asymmetry of the Pauli triple, not a choice of spatial axis.

**Frame covariance.** The formula is written in a frame, and no direction is privileged. Let $(t_1,t_2,t_3)$ be an orthonormal triad and $(u,w)$ an orthonormal pair of real unit vectors; then
$$
iR_{\vec e_x}^{\mathrm{axf}}=R_{iw},\qquad iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=L_{i t_k}R_u
$$
satisfy the same Clifford relations for every such choice: the two squares are $R_{e_t}^{\mathrm{axf}}$ and $L_{e_t}^{\mathrm{axf}}R_{-e_t}^{\mathrm{axf}}$, and the cross term is $L_{it_k}R_{iwu+uiw}$, which vanishes because $u$ and $w$ are orthogonal. The exercise takes $t_k=\vec e_k$, $u=\vec e_y$, $w=\vec e_x$, the frame in which the chirality factor is the standard $(\sigma_x,i\sigma_y,\sigma_z)$. A change of the triad is a spatial rotation; a change of $(u,w)$ is a change of chirality basis, conjugation by a unit biquaternion. Neither changes the physics.

The check is the algebra itself, and it is the collapse rule of the dictionary. Since $R$ and $L$ commute, the product of the four coordinate cells is the volume cell,
$$
c_0c_1c_2c_3=iR_{\vec e_x}^{\mathrm{axf}}\,iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=-R_{\vec e_z}^{\mathrm{axf}},
$$
and $i$ times it is the chirality cell, $i\Omega=i\,(-R_{\vec e_z}^{\mathrm{axf}})=R_{-i\vec e_z}^{\mathrm{axf}}$. The anticommutators are two applications of the same rule. For the time cell against a space cell,
$$
iR_{\vec e_x}^{\mathrm{axf}}\,iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}+iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,iR_{\vec e_x}^{\mathrm{axf}}=L_{i\vec e_k}^{\mathrm{axf}}\bigl(R_{i\vec e_z}^{\mathrm{axf}}+R_{-i\vec e_z}^{\mathrm{axf}}\bigr)=0,
$$
because $i\vec e_x\vec e_y=i\vec e_z$ and $\vec e_y\,i\vec e_x=-i\vec e_z$, and the two coefficients differ by the sign of $i$. For two space cells,
$$
L_{i\vec e_j}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,L_{i\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}+L_{i\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,L_{i\vec e_j}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=L_{i^2(\vec e_j\vec e_k+\vec e_k\vec e_j)}^{\mathrm{axf}}=0,
$$
because $i$ is central and quaternion units anticommute. So $\{c_\mu,c_\nu\}=2g_{\mu\nu}$ with $g=\mathrm{diag}(-1,+1,+1,+1)$, without a matrix.

## The Field and the Two Forms of the Equation

**The field and its two Peirce components.** Let

$$
\tilde\Pi_+=\frac{e_t+i\vec e_z}{2},\qquad \tilde\Pi_-=\frac{e_t-i\vec e_z}{2},
$$

be the Peirce idempotents, and let

$$
\vec\Upsilon_x=\frac{i\vec e_x-\vec e_y}{2},\qquad \vec\Upsilon_y=\frac{i\vec e_x+\vec e_y}{2}
$$

be the off-diagonal matrix units, so that $\{\tilde\Pi_+,\vec\Upsilon_y\}$ is a basis of $\mathbb{B}\tilde\Pi_+$ and $\{\vec\Upsilon_x,\tilde\Pi_-\}$ is a basis of $\mathbb{B}\tilde\Pi_-$. A two-component spinor $\chi=(\chi_1,\chi_2)$ is realised in the algebra by

$$
\Psi_+(\chi)=\chi_1\tilde\Pi_++\chi_2\vec\Upsilon_y\in\mathbb{B}\tilde\Pi_+,\qquad
\Psi_-(\chi)=\chi_1\vec\Upsilon_x+\chi_2\tilde\Pi_-\in\mathbb{B}\tilde\Pi_- .
$$

The field is

$$
\tilde\Psi=\Psi_+(\psi_+)+\Psi_-(\psi_-),
$$

with $\psi_\pm\in\mathbb{C}^2$ its two Peirce coordinates. The Peirce components are $\tilde\Psi_\pm=\tilde\Psi\tilde\Pi_\pm$. In the chiral basis they are the two chiralities, $\psi_+$ left-handed and $\psi_-$ right-handed, and they are selected by the projectors

$$
P_L=\frac{1+iR_{\vec e_z}^{\mathrm{axf}}}{2}=R_{\tilde\Pi_+},\qquad P_R=\frac{1-iR_{\vec e_z}^{\mathrm{axf}}}{2}=R_{\tilde\Pi_-},
\qquad \tilde\Psi_+=P_L\tilde\Psi,\quad \tilde\Psi_-=P_R\tilde\Psi .
$$

In the Dirac basis the same two components are the large and the small component. They are still the Peirce components of $\tilde\Pi_\pm$, and what changes is their meaning: there the diagonal cell is $(iR_{\vec e_x}^{\mathrm{axf}})^d=R_{i\vec e_z}^{\mathrm{axf}}$, so the Peirce projectors separate large from small, while the chirality is $(R_{-i\vec e_z}^{\mathrm{axf}})^d=R_{i\vec e_x}^{\mathrm{axf}}$, whose idempotents are $\tfrac12(1\pm i\vec e_x)$ and not $\tilde\Pi_\pm$.

**The two-sided form and the chiral pair.** For a plane wave of four-momentum $p_\mu=(E,\vec p)$ the Dirac operator is the contraction of the cells with the momentum, written $\slashed p$ as in the corpus,

$$
\slashed p=iR_{\vec e_x}^{\mathrm{axf}}p_{0}-\sum_k iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}p_{k}
=iR_{\vec e_x}^{\mathrm{axf}}E-\sum_k iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}p_k
=E\,R_{i\vec e_x}^{\mathrm{axf}}-p_k\,L_{i\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},
$$

where the eigenvalue $p_0=E$ and the scalar $i$ of the time cell have been collected into the single right multiplication $R_{i\vec e_x}^{\mathrm{axf}}$. The name carries the two-sided character: one term is a pure right multiplication, the other three are left times right. The two-sided Dirac equation is the eigenvalue problem of that operator,

$$
\slashed p\,\tilde\Psi=m\tilde\Psi,
$$

and, written on the element,

$$
E\,\tilde\Psi\,i\vec e_x-i\,(\vec p\cdot\vec e)\,\tilde\Psi\,\vec e_y=m\,\tilde\Psi ,
$$

In Peirce coordinates this is the pair

$$
(E-\boldsymbol\sigma\cdot\vec p)\,\psi_-=m\,\psi_+,\qquad
(E+\boldsymbol\sigma\cdot\vec p)\,\psi_+=m\,\psi_- ,
$$

in the chiral basis, and

$$
(E-m)\,\psi_+=(\boldsymbol\sigma\cdot\vec p)\,\psi_-,\qquad
(E+m)\,\psi_-=(\boldsymbol\sigma\cdot\vec p)\,\psi_+
$$

in the Dirac basis, where the operator is $E\,R_{i\vec e_z}^{\mathrm{axf}}-p_k\,L_{i\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ by the cell table above. The two pairs are the same equation in the two bases: they differ by the place of the mass, which is what the change of basis moves.

**Conventions.** Natural units $\hbar=c=1$ in the solutions; $\hbar$ and $c$ are restored in Problem 6. The metric of the spacetime gradient is $g_{\mu\nu}[\mathbb{M}_-]$, and the Clifford metric of the cells is $g=-\eta$. The two-spinors are $\xi^{(1)}=(1,0)^T$, $\xi^{(2)}=(0,1)^T$, with $\xi^{(r)\dagger}\xi^{(s)}=\delta_{rs}$; $\eta^{(1)},\eta^{(2)}$ are the negative-frequency rest spinors, with $\eta^{(r)\dagger}\eta^{(s)}=\delta_{rs}$; $\chi_\pm$ are the helicity eigenspinors, $\boldsymbol\sigma\cdot\vec u_p\,\chi_\pm=\pm\chi_\pm$, with $\vec u_p=\vec p/|\vec p|$. In the $\mp$ and $\pm$ pairs below the upper sign goes with $\chi_+$ and the lower with $\chi_-$. The Hermitian conjugate $^*$ is the coefficient conjugation composed with the quaternion conjugation, $\tilde Q^*=\overline{\tilde Q^\natural}$, and under the matrix representation $\mathsf{M}_2$ it is the conjugate transpose.

## Problem 1: The spinors at rest and at general momentum

**Statement.** Solve $\slashed p\,\tilde w=m\tilde w$ and $\slashed p\,\tilde v=-m\tilde v$ explicitly at rest and at general momentum, in the chiral and in the Dirac basis.

**Solution.** The equation was written above as a pair on the Peirce coordinates. In the **chiral basis** the pair is

$$
(E-\boldsymbol\sigma\cdot\vec p)\,\psi_-=m\psi_+,\qquad (E+\boldsymbol\sigma\cdot\vec p)\,\psi_+=m\psi_- .
$$

Eliminating $\psi_-$ gives $(E^2-\vec p^2)\psi_+=m^2\psi_+$, so the pair is soluble exactly on the mass shell $E^2=\vec p^2+m^2$. For the positive-frequency branch, take $\psi_+=\sqrt{E\mp|\vec p|}\,\chi_\pm$, with the upper sign for $\chi_+$ and the lower for $\chi_-$; the first equation gives $\psi_-=\sqrt{E\pm|\vec p|}\,\chi_\pm$. The helicity label is fixed by the sign: the two solutions are

$$
\boxed{\;\tilde w_\pm(\vec p)=\sqrt{E\mp|\vec p|}\;\Psi_+(\chi_\pm)+\sqrt{E\pm|\vec p|}\;\Psi_-(\chi_\pm)\;}
$$

For the negative-frequency branch, the same pair with $m\to-m$ gives $\psi_+=-\sqrt{E\mp|\vec p|}\,\chi_\pm$ and $\psi_-=\sqrt{E\pm|\vec p|}\,\chi_\pm$:

$$
\boxed{\;\tilde v_\pm(\vec p)=-\sqrt{E\mp|\vec p|}\;\Psi_+(\chi_\pm)+\sqrt{E\pm|\vec p|}\;\Psi_-(\chi_\pm)\;}
$$

**At rest.** With $\vec p=0$ and $E=m$, the two branches lie in the left ideals generated by the two idempotents of $i\vec e_x$,

$$
\tilde w(0)\,(1-i\vec e_x)=0,\qquad \tilde v(0)\,(1+i\vec e_x)=0,
$$

so that $\tilde w(0)\in\mathbb{B}\tfrac12(1+i\vec e_x)$ and $\tilde v(0)\in\mathbb{B}\tfrac12(1-i\vec e_x)$.

Equivalently, the positive-frequency amplitude has equal Peirce coordinates and the negative-frequency amplitude has opposite ones:

$$
\tilde w_\pm(0)=\sqrt{m}\,\bigl(\Psi_+(\chi_\pm)+\Psi_-(\chi_\pm)\bigr),\qquad
\tilde v_\pm(0)=\sqrt{m}\,\bigl(-\Psi_+(\chi_\pm)+\Psi_-(\chi_\pm)\bigr).
$$

The two rest amplitudes are therefore the two eigenspaces of $iR_{\vec e_x}^{\mathrm{axf}}=R_{i\vec e_x}^{\mathrm{axf}}$, with eigenvalues $+1$ and $-1$; each is two-dimensional over $\mathbb{C}$, and the two spin states are the two choices of $\chi_\pm$.

**The Dirac basis.** The change of basis is right multiplication by the unit biquaternion

$$
\tilde W=\frac{e_t+\vec e_y}{\sqrt2},\qquad \tilde W^{-1}=\tilde W^{\natural}=\frac{e_t-\vec e_y}{\sqrt2},
$$

as Problem 5 shows. In the Dirac basis the operator is $D_d=E\,R_{i\vec e_z}^{\mathrm{axf}}-p_k\,L_{i\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, and $D_d\tilde w^{(r)}=m\tilde w^{(r)}$ reads as the pair $(E-m)\psi_+=(\boldsymbol\sigma\cdot\vec p)\psi_-$, $(E+m)\psi_-=(\boldsymbol\sigma\cdot\vec p)\psi_+$. The solutions are

$$
\boxed{\;\tilde w^{(r)}(\vec p)=\sqrt{E+m}\;\Psi_+(\xi^{(r)})+\sqrt{E-m}\;\Psi_-(\boldsymbol\sigma\cdot\vec u_p\,\xi^{(r)})\;}
$$

$$
\boxed{\;\tilde v^{(r)}(\vec p)=\sqrt{E-m}\;\Psi_+(\boldsymbol\sigma\cdot\vec u_p\,\eta^{(r)})+\sqrt{E+m}\;\Psi_-(\eta^{(r)})\;}
$$

At rest these collapse to a single Peirce component,

$$
\tilde w^{(r)}(0)=\sqrt{2m}\,\Psi_+(\xi^{(r)}),\qquad
\tilde v^{(r)}(0)=\sqrt{2m}\,\Psi_-(\eta^{(r)}),
$$

which is the biquaternion statement that the large component of the rest spinor is the first Peirce component. Both formulas are the parent's, with the four-component column replaced by the pair of Peirce coordinates.

**Explicit components.** With $\vec u_p=(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta)$ and the helicity spinors

$$
\chi_+=\begin{pmatrix}\cos(\theta/2)\\ e^{i\phi}\sin(\theta/2)\end{pmatrix},\qquad
\chi_-=\begin{pmatrix}-e^{-i\phi}\sin(\theta/2)\\ \cos(\theta/2)\end{pmatrix},
$$

the chiral solutions have the coordinate pairs

$$
(\psi_+,\psi_-)=\bigl(\sqrt{E\mp|\vec p|}\,\chi_\pm,\ \sqrt{E\pm|\vec p|}\,\chi_\pm\bigr),
$$

and the Dirac solutions have

$$
(\psi_+,\psi_-)=\bigl(\sqrt{E+m}\,\xi^{(r)},\ \sqrt{E-m}\,(\boldsymbol\sigma\cdot\vec u_p)\,\xi^{(r)}\bigr).
$$

These are the four-component spinors of the parent, read as coordinates in the two Peirce components rather than as entries of a column.

## Problem 2: Covariant normalisation and orthogonality

**Statement.** Verify $\bar w^{(r)}w^{(s)}=2m\delta_{rs}$, $\bar v^{(r)}v^{(s)}=-2m\delta_{rs}$, $\bar w^{(r)}v^{(s)}=0$, and the Hermitian products.

**Solution.** Write $\bar w w=\langle\tilde w,\tilde w\rangle_{\mathrm D}$ for the Dirac bilinear. The Dirac adjoint is the Hermitian pairing twisted by the representative of $iR_{\vec e_x}^{\mathrm{axf}}$. In the chiral basis,

$$
\langle\tilde\Psi,\tilde\Phi\rangle_{\mathrm D}=\mathrm{Tr}\bigl(\tilde\Psi^{*}\tilde\Phi\,i\vec e_x\bigr)
=\psi_+^\dagger\phi_-+\psi_-^\dagger\phi_+ ,
$$

and in the Dirac basis the twist is $i\vec e_z$, the representative of $iR_{\vec e_x}^{\mathrm{axf}}$ there. Under $\mathsf M_2$ the twist $i\vec e_x$ is $\sigma_x$, so the pairing is the ordinary conjugate-transpose bilinear twisted by $\sigma_x\otimes1$, the matrix of the time cell; the trace in the algebra is what replaces the sum over the four components. The single algebraic input is the unit-vector identity

$$
(i\vec u_p)^2=i^2\,\vec u_p^{\,2}=(-1)(-e_t)=e_t,
$$

which is the biquaternion form of $(\boldsymbol\sigma\cdot\vec u_p)^2=I_2$: the two minus signs, one from $i^2=-1$ and one from $\vec u_p^{\,2}=-e_t$, cancel.

For the chiral solutions, $\psi_+=\sqrt{E\mp|\vec p|}\,\chi_\pm$ and $\psi_-=\sqrt{E\pm|\vec p|}\,\chi_\pm$. The Hermitian product is diagonal,

$$
\mathrm{Tr}\bigl(\tilde w_\pm^{*}\tilde w_\pm\bigr)=\psi_+^\dagger\psi_++\psi_-^\dagger\psi_-=(E\mp|\vec p|)+(E\pm|\vec p|)=2E,
$$

and the Dirac pairing is

$$
\langle\tilde w_\pm,\tilde w_\pm\rangle_{\mathrm D}
=\psi_+^\dagger\psi_-+\psi_-^\dagger\psi_+
=\sqrt{E^2-\vec p^2}\,\chi_\pm^\dagger\chi_\pm+\sqrt{E^2-\vec p^2}\,\chi_\pm^\dagger\chi_\pm=2m .
$$

Opposite helicities are orthogonal, $\langle\tilde w_+,\tilde w_-\rangle_{\mathrm D}=0$. For the negative-frequency branch the first coordinate carries the minus sign, and the same computation gives $-2m$. The mixed term cancels because the two products are opposite:

$$
\langle\tilde w_\pm,\tilde v_\pm\rangle_{\mathrm D}
=\sqrt{E^2-\vec p^2}\,\chi_\pm^\dagger\chi_\pm-\sqrt{E^2-\vec p^2}\,\chi_\pm^\dagger\chi_\pm=0 .
$$

In the Dirac basis the same three statements hold with the twist $i\vec e_z$, and the spin labels $r,s$ replace the helicity labels. The Hermitian products are

$$
\mathrm{Tr}\bigl(\tilde w^{*}\tilde w\bigr)=2E,\qquad \mathrm{Tr}\bigl(\tilde v^{*}\tilde v\bigr)=2E,
$$

and the mixed Hermitian product vanishes at opposite momenta,

$$
\mathrm{Tr}\bigl(\tilde w^{(r)*}(\vec p)\,\tilde v^{(s)}(-\vec p)\bigr)=0,
$$

which is the parent's relation with the spin labels $r,s$.

The bilinear $\bar ww=\langle\tilde w,\tilde w\rangle_{\mathrm D}$ is a Lorentz scalar and its value $2m$ is the covariant normalisation; it is not the probability density, which is the positive quantity $\mathrm{Tr}(\tilde w^*\tilde w)=2E$. As a numerical check, for $m=1$ and $|\vec p|=0.6$, hence $E=1.166190$, direct evaluation gives $\bar ww=2.0000$, $\bar vv=-2.0000$, $\bar wv=0$, and $\mathrm{Tr}(\tilde w^*\tilde w)=\mathrm{Tr}(\tilde v^*\tilde v)=2.3324=2E$.

## Problem 3: The spin sums

**Statement.** Verify the completeness relations

$$
\sum_{\pm}\tilde w_\pm\,\langle\tilde w_\pm,\cdot\rangle_{\mathrm D}=\slashed p+m,\qquad
\sum_{\pm}\tilde v_\pm\,\langle\tilde v_\pm,\cdot\rangle_{\mathrm D}=\slashed p-m .
$$

**Solution.** The left-hand side is an operator on $\mathbb{B}$, of rank two: for every $\tilde\Phi$,

$$
\sum_{\pm}\tilde w_\pm\,\langle\tilde w_\pm,\tilde\Phi\rangle_{\mathrm D}
=\sum_{\pm}\tilde w_\pm\bigl(\psi_{\pm,+}^\dagger\phi_-+\psi_{\pm,-}^\dagger\phi_+\bigr).
$$

On the chiral solutions, $\psi_{\pm,+}=\sqrt{E\mp|\vec p|}\,\chi_\pm$ and $\psi_{\pm,-}=\sqrt{E\pm|\vec p|}\,\chi_\pm$. The two-spinor completeness relations are $\sum_\pm\chi_\pm\chi_\pm^\dagger=I_2$ and $\sum_\pm(\pm1)\chi_\pm\chi_\pm^\dagger=\boldsymbol\sigma\cdot\vec u_p$. Substituting, the four Peirce blocks are

$$
\sum_\pm\psi_{\pm,+}\psi_{\pm,-}^\dagger=mI_2,\qquad
\sum_\pm\psi_{\pm,+}\psi_{\pm,+}^\dagger=EI_2-|\vec p|\,\boldsymbol\sigma\cdot\vec u_p,
$$

and their conjugates. Restoring the algebra, $E I_2-|\vec p|\,\boldsymbol\sigma\cdot\vec u_p$ is $E-p_k\sigma_k$ and $mI_2$ is $m$, so

$$
\sum_{\pm}\tilde w_\pm\,\langle\tilde w_\pm,\cdot\rangle_{\mathrm D}
=E\,R_{i\vec e_x}^{\mathrm{axf}}-p_k\,L_{i\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}+m=\slashed p+m .
$$

The negative-frequency sum is identical in structure with the roles of the two Peirce components interchanged, and gives $\slashed p-m$.

**The on-shell identity.** The trace of $\slashed p$ vanishes, because every cell is off-diagonal in the chirality factor, so the trace of $\slashed p+m$ over the four amplitude coordinates is $4m$. The two sums are complementary in the same way as the two factors,

$$
(\slashed p+m)(\slashed p-m)=\slashed p^2-m^2 .
$$

The symbol squares to a multiple of the identity:

$$
\slashed p^2=E^2R_{(i\vec e_x)^2}^{\mathrm{axf}}+p_jp_k\,L_{i\vec e_j}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}L_{i\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}
=E^2+p_jp_k\,L_{-\vec e_j\vec e_k}^{\mathrm{axf}}R_{-e_t}^{\mathrm{axf}}
=E^2-\vec p^{\,2} ,
$$

with the plus in front of the double sum because $(\slashed p)^2$ squares the minus of the space term, and the cross terms vanishing because $R_{i\vec e_x}^{\mathrm{axf}}$ and $L_{i\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ anticommute. On the mass shell $\slashed p^2=m^2$, so $(\slashed p+m)(\slashed p-m)=0$ and the two branches close the amplitude space, exactly as in the matrix language.

**Check in the Dirac basis.** The same relations hold with the spin index $r$ replacing the helicity index, once the Dirac-basis spinors of Problem 1 are used:

$$
\sum_{r=1}^{2}\tilde w^{(r)}\bigl\langle\tilde w^{(r)},\cdot\bigr\rangle_{\mathrm D}=\slashed p+m,\qquad
\sum_{r=1}^{2}\tilde v^{(r)}\bigl\langle\tilde v^{(r)},\cdot\bigr\rangle_{\mathrm D}=\slashed p-m .
$$

The proof uses $\sum_r\xi^{(r)}\xi^{(r)\dagger}=I_2$ in place of the helicity sums. A numerical evaluation at the same kinematics confirms both equalities on a basis of $\mathbb{B}$.

## Problem 4: The massless limit and helicity–chirality locking

**Statement.** Take $m=0$ and exhibit the helicity–chirality locking in the Peirce components.

**Solution.** In the chiral basis the massless equation $\slashed p\,\tilde\Psi=0$ splits into its two Peirce components,

$$
(\slashed p\,\tilde\Psi)\tilde\Pi_+=0,\qquad
(\slashed p\,\tilde\Psi)\tilde\Pi_-=0,
$$

which are the two Weyl equations

$$
(E-\boldsymbol\sigma\cdot\vec p)\,\psi_-=0,\qquad (E+\boldsymbol\sigma\cdot\vec p)\,\psi_+=0 .
$$

For $m=0$ the dispersion is $E=|\vec p|$, and the positive-frequency solutions of Problem 1 become

$$
\tilde w_+(\vec p)=\sqrt{2E}\,\Psi_-(\chi_+),\qquad
\tilde w_-(\vec p)=\sqrt{2E}\,\Psi_+(\chi_-).
$$

The first has only the right-handed Peirce component, the second only the left-handed one. The two labels are locked: **positive helicity goes with right-handedness and negative helicity with left-handedness.** In the algebra this is the statement that $\tilde w_+$ is annihilated by $P_L$ and $\tilde w_-$ by $P_R$:

$$
P_L\tilde w_+=0,\qquad P_R\tilde w_-=0 .
$$

The mass term is the only term that couples the two Peirce components: in the chiral pair, $m\psi_+$ and $m\psi_-$ are the off-diagonal entries, and setting $m=0$ decouples them. At fixed momentum each Weyl equation selects one complex helicity state, and the two together give the two massless states; the Dirac equation is recovered as the pair. Restoring $c$ and $\hbar$ and passing to the time-dependent form gives the parent's Weyl equations

$$
i\hbar\,\frac{\partial}{\partial t'}\,\psi_R=c\,\boldsymbol\sigma\cdot\vec p\;\psi_R,\qquad
i\hbar\,\frac{\partial}{\partial t'}\,\psi_L=-c\,\boldsymbol\sigma\cdot\vec p\;\psi_L,
$$

with $\vec p=-i\hbar\nabla$ in the operator form and $\boldsymbol\sigma\cdot\vec p=\pm|\vec p|$ on the helicity states. The magnitude $|\vec p|$, which the energy $c|\vec p|$ carries, is part of the right-hand side and cannot be dropped.

## Problem 5: The algebra of the cells and the change of basis

**Statement.** Verify the Clifford relations in the algebra, identify $-iR_{\vec e_z}^{\mathrm{axf}}$, and determine how the cells change under the change of basis.

**Solution.** The relations were verified in the introduction from the multiplication table. The chirality operator is

$$
-iR_{\vec e_z}^{\mathrm{axf}}=R_{-i\vec e_z}^{\mathrm{axf}},\qquad (-iR_{\vec e_z}^{\mathrm{axf}})^2=R_{(-i\vec e_z)^2}^{\mathrm{axf}}=R_{i^2\vec e_z^2}=R_{e_t}^{\mathrm{axf}}=1,
$$

and it anticommutes with every cell. Write the three spatial cells with no leading $i$, as in the dictionary, and use $R_aR_b=R_{ba}$:

$$
R_{-i\vec e_z}^{\mathrm{axf}}R_{i\vec e_x}^{\mathrm{axf}}+R_{i\vec e_x}^{\mathrm{axf}}R_{-i\vec e_z}^{\mathrm{axf}}=R_{-\vec e_y}^{\mathrm{axf}}+R_{\vec e_y}^{\mathrm{axf}}=0,
$$
$$
L_{i\vec e_k}^{\mathrm{axf}}\bigl(R_{-i\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}+R_{\vec e_y}^{\mathrm{axf}}R_{-i\vec e_z}^{\mathrm{axf}}\bigr)=L_{i\vec e_k}^{\mathrm{axf}}\bigl(R_{-i\vec e_x}^{\mathrm{axf}}+R_{i\vec e_x}^{\mathrm{axf}}\bigr)=0,
$$

because $\vec e_x\vec e_z=-\vec e_y$ while $\vec e_z\vec e_x=+\vec e_y$ in the first line, and $\vec e_z\vec e_y=-\vec e_x$ while $\vec e_y\vec e_z=+\vec e_x$ in the second. Each time the two products differ by the sign of one unit, and the factor $i\cdot(-i)=+1$ does not change it. Compare the squares: there the two factors contribute $i\cdot i=i^2=-1$.

The projectors are $P_L=R_{\tilde\Pi_+}$ and $P_R=R_{\tilde\Pi_-}$; they satisfy $P_L+P_R=1$, $P_LP_R=0$, and $P_L(-iR_{\vec e_z}^{\mathrm{axf}})=-P_L$, $P_R(-iR_{\vec e_z}^{\mathrm{axf}})=P_R$. They are the Peirce projectors of the algebra; in the Peirce basis they project onto the two chiral blocks.

**The action on the two chiral columns.** On the pair $(\psi_+,\psi_-)$ the three operators act as
$$
iR_{\vec e_x}^{\mathrm{axf}}:(\psi_+,\psi_-)\mapsto(\psi_-,\psi_+),\qquad
-iR_{\vec e_z}^{\mathrm{axf}}:(\psi_+,\psi_-)\mapsto(-\psi_+,\psi_-),\qquad
iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}:(\psi_+,\psi_-)\mapsto(\sigma_k\psi_-,-\sigma_k\psi_+).
$$
These are the blocks of the parent's chiral matrices: the exchange block of $iR_{\vec e_x}^{\mathrm{axf}}$, the diagonal blocks $(-I_2,I_2)$ of $-iR_{\vec e_z}^{\mathrm{axf}}$, and the off-diagonal $\sigma_k$ blocks of $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$. The blocks follow from the multiplication table of the four units.

**The change of basis.** Right multiplication by $\tilde W=(e_t+\vec e_y)/\sqrt2$ is a unit-norm biquaternion, and it sends the chiral basis to the Dirac basis:

$$
\tilde\Psi_d=\tilde\Psi_c\,\tilde W .
$$

The cells transform by conjugation. Since $\tilde W^{-1}i\vec e_x\tilde W=i\vec e_z$ and $\tilde W^{-1}(-i\vec e_z)\tilde W=i\vec e_x$,

$$
(iR_{\vec e_x}^{\mathrm{axf}})^{d}=R_{i\vec e_z}^{\mathrm{axf}},\qquad (iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})^{d}=iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=L_{i\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad (-iR_{\vec e_z}^{\mathrm{axf}})^{d}=R_{i\vec e_x}^{\mathrm{axf}}.
$$

The spatial cells are unchanged because $\tilde W^{-1}\vec e_y\tilde W=\vec e_y$; only $iR_{\vec e_x}^{\mathrm{axf}}$ and $-iR_{\vec e_z}^{\mathrm{axf}}$ change. In the Dirac basis $(iR_{\vec e_x}^{\mathrm{axf}})^{d}$ is diagonal on the Peirce components, which is why that basis separates the large and the small component in the non-relativistic limit. The $4\times4$ matrix $U$ of the parent is the regular representation of this right multiplication on the four-dimensional space of the two Peirce coordinates.

**The Lorentz generators.** In the algebra they are the commutators of the cells, $S_{\mu\nu}=\frac i4[c_\mu,c_\nu]$, which are again left and right multiplications; the $i$'s inside the cells cancel first:

$$
[\,iR_{\vec e_x}^{\mathrm{axf}},\,iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,]=L_{i\vec e_k}^{\mathrm{axf}}\bigl(R_{\vec e_y i\vec e_x}^{\mathrm{axf}}-R_{i\vec e_x\vec e_y}^{\mathrm{axf}}\bigr)=L_{i\vec e_k}^{\mathrm{axf}}\bigl(R_{-i\vec e_z}^{\mathrm{axf}}-R_{i\vec e_z}^{\mathrm{axf}}\bigr)=-2L_{i\vec e_k}^{\mathrm{axf}}R_{i\vec e_z}^{\mathrm{axf}}=2L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}},
$$
$$
[\,iL_{\vec e_j}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\,iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,]=L_{i\vec e_j}^{\mathrm{axf}}L_{i\vec e_k}^{\mathrm{axf}}R_{\vec e_y\vec e_y}^{\mathrm{axf}}-L_{i\vec e_k}^{\mathrm{axf}}L_{i\vec e_j}^{\mathrm{axf}}R_{\vec e_y\vec e_y}^{\mathrm{axf}}=L_{\vec e_j\vec e_k}^{\mathrm{axf}}+L_{\vec e_j\vec e_k}^{\mathrm{axf}}=2L_{\vec e_j\vec e_k}^{\mathrm{axf}},
$$

because $\vec e_y\vec e_x=-\vec e_z$ while $\vec e_x\vec e_y=+\vec e_z$, $\vec e_y\vec e_y=-e_t$, and $i^2=-1$ twice: once in $L_{i\vec e_k}^{\mathrm{axf}}R_{i\vec e_z}^{\mathrm{axf}}=i^2L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ and once in $L_{i\vec e_j}^{\mathrm{axf}}L_{i\vec e_k}^{\mathrm{axf}}=i^2L_{\vec e_j\vec e_k}^{\mathrm{axf}}$. Hence

$$
S_{0k}=\frac i2\,L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}},\qquad
S_{jk}=\frac i2\,L_{\vec e_j\vec e_k}^{\mathrm{axf}},
$$

with one $i$ left in each, and no $i$ inside a unit. Both are block diagonal on the Peirce components, so $[S_{\mu\nu},-iR_{\vec e_z}^{\mathrm{axf}}]=0$. The rotations $S_{jk}$ carry no chirality factor and act with the same sign on the two components; the boosts $S_{0k}$ carry the chirality sign, through the right factor $R_{\vec e_z}^{\mathrm{axf}}$.

This is the algebraic content of the parent's statement that rotations are chirality-even and boosts are chirality-odd.

## Problem 6: The biquaternionic mass-shell condition

**Statement.** Verify the mass-shell condition of the parent and recover the relativistic energy–momentum relation.

**Solution.** The plane-wave ansatz carries the wave biquaternion

$$
\tilde P/\hbar=\frac{i\omega}{c}\,e_t+\vec k,\qquad \vec k=k_1\vec e_x+k_2\vec e_y+k_3\vec e_z ,
$$

an element of the material sector $\mathbb{M}_-$: imaginary scalar part and real vector part. The biquaternion norm is $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^2$, so

$$
\langle\tilde P/\hbar\rangle_{\natural}=\left(\frac{i\omega}{c}\right)^2+k_1^2+k_2^2+k_3^2=-\frac{\omega^2}{c^2}+\vec k^2 ,
$$

the sign change being $i^2=-1$. The dispersion relation is $\omega^2=c^2\vec k^2+m^2c^4/\hbar^2$. Substituting,

$$
\langle\tilde P/\hbar\rangle_{\natural}=-\frac{1}{c^2}\left(c^2\vec k^2+\frac{m^2c^4}{\hbar^2}\right)+\vec k^2=-\frac{m^2c^2}{\hbar^2},
$$

which is the parent's condition

$$
\boxed{\;\tilde P\tilde P^{\natural}=-m^2c^2\;}.
$$

Equivalently, with $E=\hbar\omega$ and $\vec p=\hbar\vec k$, the norm is quadratic, so $\langle\tilde P/\hbar\rangle_{\natural}=\langle\tilde P\rangle_{\natural}/\hbar^2=-m^2c^2/\hbar^2$. The mass shell is not a new postulate: it is the statement that the four-wavevector is a timelike element of $\mathbb{M}_-$ with the same biquaternion norm as the four-momentum.

The two roots $\omega=\pm\sqrt{c^2\vec k^2+m^2c^4/\hbar^2}$ are the two frequency branches, and they are the two families $\tilde w$ and $\tilde v$ constructed above; the two spin labels within each branch give the four-dimensional complex solution space. As a numerical check, for an electron ($mc^2=0.510998950\ \mathrm{MeV}$) at $|\vec p|=1\ \mathrm{MeV}/c$, the dispersion gives $E=1.122996\ \mathrm{MeV}$ and $E^2-\vec p^2c^2=0.261120\ \mathrm{MeV}^2=(mc^2)^2$; the wave biquaternion has $\langle\tilde P/\hbar\rangle_{\natural}=-6.706054\times10^{24}\ \mathrm{m}^{-2}$, agreeing with $-m^2c^2/\hbar^2$ to the digits shown.

## Problem 7: The helicity blocks and the block determinant

**Statement.** Show that the momentum-space Dirac operator commutes with the helicity operator and splits into two $2\times2$ blocks, compute the determinant of each block, and read the mass shell as the vanishing of a block determinant.

**Solution.** The symbol is $\slashed p$ of Problem 3, and the massive operator is $\mathcal D(p)=\slashed p-m$.

**The symbol squares to the interval.** By the collapse rule, $(R_{i\vec e_x}^{\mathrm{axf}})^{2}=\mathrm I$ and $(L_{i\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})^{2}=-\mathrm I$, and the four cells anticommute, so the cross terms cancel and

$$
\slashed p^2=p^2\,\mathrm I,\qquad p^2=E^2-\vec p^{\,2}.
$$

**The helicity grading.** For $\vec p\neq0$ put

$$
\Xi=-i\,\vec u_p,\qquad \Xi^2=i^2\,\vec u_p^{\,2}=(-1)(-e_t)=e_t ,
$$

so that $L_\Xi$ has eigenvalues $\pm1$, each twice. The symbol commutes with it. The time term is a right multiplication and commutes with every left multiplication; the space terms contribute

$$
\Bigl[-\sum_k p_k\,L_{i\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\,L_\Xi\Bigr]=-L_{i[\vec p\cdot\vec e,\,\Xi]}^{\mathrm{axf}}\,R_{\vec e_y}^{\mathrm{axf}}=0,
$$

because $\Xi$ is proportional to $\vec p\cdot\vec e$, so the two elements commute and their left multiplications commute as well. The mass is a scalar, so it commutes too. Hence $\mathcal D(p)$ is block diagonal in the eigenbasis of $L_\Xi$, with two $2\times2$ blocks, one per helicity.

**The block determinant.** A block $\slashed p_\pm$ obeys $\slashed p_\pm^2=p^2\,\mathrm I_2$ and is not a multiple of the identity for $\vec p\neq0$, so for $p^2>0$ its two eigenvalues are $\pm\sqrt{p^2}$ and

$$
\det\bigl(\slashed p_\pm-m\,\mathrm I_2\bigr)=\bigl(\sqrt{p^2}-m\bigr)\bigl(-\sqrt{p^2}-m\bigr)=m^2-p^2=\tilde P\tilde P^{\natural}+m^2,
$$

using $\tilde P\tilde P^{\natural}=-p^2$ of Problem 6. The same number comes from the eigenvalues. Since $\tilde P=iE+\vec p\cdot\vec e$, the left multiplication $L_{\tilde P}$ has the two eigenvalues $\lambda_\pm=i\bigl(E\mp|\vec p|\bigr)$, each twice, and one more $i^2=-1$ gives $\lambda_+\lambda_-=i^2\bigl(E^2-\vec p^{\,2}\bigr)=-\bigl(E^2-\vec p^{\,2}\bigr)=\tilde P\tilde P^{\natural}$. The block determinant is $\lambda_+\lambda_-+m^2$. The mass multiplies the block, it does not square into it, so the determinant of the whole symbol is the product of the two block determinants,

$$
\boxed{\;\det\mathcal D(p)=\bigl(m^2-p^2\bigr)^2\;},
$$

the square of the Klein–Gordon symbol. The two blocks carry the same pair of eigenvalues: they are isospectral, so the block determinant is the only frame-independent datum a single block has.

**The mass shell is the vanishing of a block determinant.** Each block determinant is $m^2-p^2$, so the symbol is singular exactly when $p^2=m^2$. At that momentum each block has a one-dimensional kernel: two zero modes, one per helicity, and these are the two spin states of the particle. Off the shell each block is invertible and the propagator is the inverse of the pair.

**Worked case, $\vec p\parallel\vec e_z$.** With $B=|\vec p|$ and the helicity basis ordered block by block, the symbol is

$$
\mathcal D=\begin{pmatrix}
-m & -i(E+B) & 0 & 0\\
i(E-B) & -m & 0 & 0\\
0 & 0 & -m & -i(E+B)\\
0 & 0 & i(E-B) & -m
\end{pmatrix},
$$

the two blocks identical, each with determinant $m^2-(E+B)(E-B)=m^2-p^2$ and eigenvalues $-(m+\sqrt{p^2})$ and $\sqrt{p^2}-m$. For $m=1.3$, $E=2$, $B=0.9$: $p^2=3.19$, each block determinant $-1.5$, each block spectrum $\{-3.086057,\,0.486057\}$, total determinant $2.25=(m^2-p^2)^2$.

**Worked case, on the shell.** For $m=1.3$ and $\vec p=(0.4,-0.7,0.9)$ the energy is $E=\sqrt{m^2+\vec p^{\,2}}=1.774824$. Each block determinant is zero, each block spectrum is $\{-2m,\,0\}=\{-2.6,\,0\}$, and the whole symbol has rank two, with a one-dimensional kernel per helicity.

**Numerical check.** The identities were recomputed on 100 random real four-momenta: the largest off-block entry $1.1\times10^{-15}$; the block determinant against $m^2-p^2$ $1.8\times10^{-14}$; the two block spectra against each other $1.0\times10^{-14}$; $\slashed p^2$ against $p^2\,\mathrm I$ $7.6\times10^{-15}$; $\lambda_+\lambda_-$ against $\tilde P\tilde P^{\natural}$ $1.6\times10^{-14}$; the total determinant against $(m^2-p^2)^2$ $2.3\times10^{-13}$.

**What the splitting is, and what it is not.** It says that the mass does not see the helicity, and therefore that a massive state is a pair of helicity blocks with equal spectra and unequal contents. The entries of a block depend on the choice of basis inside an eigenspace and are not physical; the determinant and the spectrum are. Three boundaries belong with the statement. At $\vec p=0$ the operator $\Xi$ is undefined: the symbol is $E R_{i\vec e_x}^{\mathrm{axf}}-m$, the spin label is the fixed Peirce index and not the helicity, and the block decomposition is that of Problem 5. For a spacelike momentum $p^2<0$ the two eigenvalues $\pm\sqrt{p^2}$ are imaginary and the block determinant $m^2+|p^2|$ does not vanish: that is the off-shell region, not a second shell. For a null momentum $p^2=0$ the determinant identity still holds, but the massless block $\slashed p_\pm$ is nilpotent there and the massive block keeps the determinant $m^2$: this is the exceptional case of the massless wall.

## The Legacy Gamma Formulation

The gammas are the five cells written as matrices; the body writes the cells themselves.

**The five matrices, complete.** As block matrices over $\mathbb B$, acting on a pair $(\xi,\eta)$ of biquaternions,
$$
\gamma_0=\begin{pmatrix}0&e_t\\e_t&0\end{pmatrix},\qquad
\gamma_k=\begin{pmatrix}0&i\vec e_k\\-i\vec e_k&0\end{pmatrix},\qquad
\gamma_5=\begin{pmatrix}-e_t&0\\0&e_t\end{pmatrix}.
$$
Under $\mathsf M_2$ each block becomes a $2\times2$ complex matrix; assembling the four blocks, the five objects read
$$
\gamma_0=\begin{pmatrix}0&0&1&0\\0&0&0&1\\1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
\gamma_1=\begin{pmatrix}0&0&0&1\\0&0&1&0\\0&-1&0&0\\-1&0&0&0\end{pmatrix},
$$
$$
\gamma_2=\begin{pmatrix}0&0&0&-i\\0&0&i&0\\0&i&0&0\\-i&0&0&0\end{pmatrix},\qquad
\gamma_3=\begin{pmatrix}0&0&1&0\\0&0&0&-1\\-1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
\gamma_5=\begin{pmatrix}-1&0&0&0\\0&-1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}.
$$
These are the Peirce arrays, the ones the literature prints. In the axis-free display, which is the display of the body, the same five are
$$
\gamma_0=\begin{pmatrix}0&-i&0&0\\i&0&0&0\\0&0&0&i\\0&0&-i&0\end{pmatrix},\qquad
\gamma_1=\begin{pmatrix}0&0&0&i\\0&0&-i&0\\0&-i&0&0\\i&0&0&0\end{pmatrix},
$$
$$
\gamma_2=\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&i\end{pmatrix},\qquad
\gamma_3=\begin{pmatrix}0&-i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix},\qquad
\gamma_5=\begin{pmatrix}0&0&0&i\\0&0&-i&0\\0&i&0&0\\-i&0&0&0\end{pmatrix},
$$
the signed permutations $\gamma_0=iR_{\vec e_x}^{\mathrm{axf}}$ and $\gamma_k=iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_{\nu(k)}}^{\mathrm{axf}}$, carried into the Peirce arrays by $C_{\Pi}$. The block forms and the Dirac basis below stay in the Peirce display.

**The Dirac basis.** It is the same set after $U=\frac1{\sqrt2}\begin{pmatrix}I_2&I_2\\-I_2&I_2\end{pmatrix}$:
$$
\gamma_0^d=\begin{pmatrix}I_2&0\\0&-I_2\end{pmatrix}=
\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&-1&0\\0&0&0&-1\end{pmatrix},\qquad
\gamma_k^d=\gamma_k,
$$
$$
\gamma_5^d=\begin{pmatrix}0&I_2\\I_2&0\end{pmatrix}=
\begin{pmatrix}0&0&1&0\\0&0&0&1\\1&0&0&0\\0&1&0&0\end{pmatrix}.
$$

**The Kronecker form.**
$$
\gamma_0=\sigma_x\otimes1,\qquad \gamma_k=i\sigma_y\otimes\sigma_k,\qquad \gamma_5=-\sigma_z\otimes1 .
$$

**The action on the two chiral columns.**
$$
\gamma_0:(\psi_+,\psi_-)\mapsto(\psi_-,\psi_+),\qquad
\gamma_5:(\psi_+,\psi_-)\mapsto(-\psi_+,\psi_-),\qquad
\gamma_k:(\psi_+,\psi_-)\mapsto(\sigma_k\psi_-,-\sigma_k\psi_+).
$$

**The dictionary.** The five are the cells of the body,
$$
\gamma_0=c_0=R_{i\vec e_x}^{\mathrm{pau}},\qquad
\gamma_k=c_k=L_{i\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\gamma_5=i\Omega=R_{-i\vec e_z}^{\mathrm{pau}},
$$

The same in the axis-free display:

$$
\gamma_0=c_0=R_{i\vec e_x}^{\mathrm{axf}},\qquad
\gamma_k=c_k=L_{i\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
\gamma_5=i\Omega=R_{-i\vec e_z}^{\mathrm{axf}},
$$

with $\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}$. The volume element is $\Omega=\gamma_0\gamma_1\gamma_2\gamma_3=-R_{\vec e_z}^{\mathrm{pau}}$, so $i\Omega=i\bigl(-R_{\vec e_z}^{\mathrm{pau}}\bigr)=R_{-i\vec e_z}^{\mathrm{pau}}=\gamma_5$: the factor $i$ is what turns the real $\vec e_z$ into $-i\vec e_z$, and $i^2=-1$ is what makes $\Omega^2=-1$ and $\gamma_5^2=+1$.

**The identities the bodies cite.** In the $\gamma$ reading, with $\epsilon_{0123}=+1$,
$$
\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$
$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=i\bigl(g_{ac}\gamma_d-g_{ad}\gamma_c\bigr),\qquad
S_{cd}=\tfrac i4[\gamma_c,\gamma_d],
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4g_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(g_{\mu\nu}g_{\rho\sigma}-g_{\mu\rho}g_{\nu\sigma}+g_{\mu\sigma}g_{\nu\rho}\bigr).
$$
**The contraction sums.** A contraction of a product with the four cells is a frame statement, because a cell's square is. In the Euclidean frame, where every cell squares to $+I_4$,

$$
\sum_\mu\gamma_\mu\gamma_\mu=4I_4,\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\mu=-2\gamma_\alpha,
$$

$$
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\mu=4\delta_{\alpha\beta}I_4,\qquad
\sum_\mu\gamma_\mu\gamma_\delta\gamma_\beta\gamma_\alpha\gamma_\mu=+2\gamma_\delta\gamma_\beta\gamma_\alpha .
$$

The four are one rule: a sum of this shape returns $(-1)^k(4-2k)$ times the $k$-vector it surrounds, for $k=0,1,2,3$. For $k=2$ the factor vanishes unless the two indices coincide, where the inside is the identity and the sum is $4I_4$; for $k=3$ the factor is $+2$ and not $-2$, and that sign is the one most easily lost. In the $\mathbb{M}_-$ frame the metric enters, only the first keeps its shape, $\sum_\mu\gamma_\mu\gamma_\mu=-2I_4$, and the others acquire metric factors: $\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\mu=2(g_{\alpha\alpha}+1)\gamma_\alpha$, which is $4\gamma_0$ for the time index and $0$ for a spatial one.

**The display.** Every array printed in this section is given twice, with one exception: the Dirac basis is one further rotation of the Peirce arrays and is printed once. Each pair gives the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The seven problems test the parent's plane-wave solutions and confirm them in the algebra.

1. **The spinors.** In the chiral basis, $\tilde w_\pm=\sqrt{E\mp|\vec p|}\,\Psi_+(\chi_\pm)+\sqrt{E\pm|\vec p|}\,\Psi_-(\chi_\pm)$ and $\tilde v_\pm=-\sqrt{E\mp|\vec p|}\,\Psi_+(\chi_\pm)+\sqrt{E\pm|\vec p|}\,\Psi_-(\chi_\pm)$; in the Dirac basis, $\tilde w^{(r)}=\sqrt{E+m}\,\Psi_+(\xi^{(r)})+\sqrt{E-m}\,\Psi_-(\boldsymbol\sigma\cdot\vec u_p\,\xi^{(r)})$ and $\tilde v^{(r)}=\sqrt{E-m}\,\Psi_+(\boldsymbol\sigma\cdot\vec u_p\,\eta^{(r)})+\sqrt{E+m}\,\Psi_-(\eta^{(r)})$. At rest the positive-frequency amplitude has equal Peirce coordinates and the negative-frequency amplitude opposite ones; in the Dirac basis each sits in a single Peirce component.
2. **Normalisation.** The covariant values $2m$, $-2m$ and $0$ follow from the single identity $(i\vec u_p)^2=e_t$; the Hermitian products are $2E$.
3. **Spin sums.** The completeness relations $\sum\tilde w\,\langle\tilde w,\cdot\rangle_{\mathrm D}=\slashed p+m$ and $\sum\tilde v\,\langle\tilde v,\cdot\rangle_{\mathrm D}=\slashed p-m$ hold as operator identities on $\mathbb{B}$, and $(\slashed p+m)(\slashed p-m)=0$ on shell.
4. **Massless limit.** Each helicity eigenstate becomes a single Peirce component, with positive helicity right-handed and negative helicity left-handed; the mass term is the only coupling of the two components.
5. **Cells.** The Clifford algebra is the multiplication table: $iR_{\vec e_x}^{\mathrm{axf}}=R_{i\vec e_x}^{\mathrm{axf}}$, $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=L_{i\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, $-iR_{\vec e_z}^{\mathrm{axf}}=R_{-i\vec e_z}^{\mathrm{axf}}$; the change of basis is right multiplication by $\tilde W=(e_t+\vec e_y)/\sqrt2$, which sends $iR_{\vec e_x}^{\mathrm{axf}}$ to $R_{i\vec e_z}^{\mathrm{axf}}$ and leaves $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ unchanged; the Lorentz generators are $S_{0k}=\frac i2L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ and $S_{jk}=\frac i2L_{\vec e_j\vec e_k}^{\mathrm{axf}}$.
6. **Mass shell.** The condition $\tilde P\tilde P^{\natural}=-m^2c^2$ is the biquaternion-norm statement $\langle\tilde P/\hbar\rangle_{\natural}=-m^2c^2/\hbar^2$, and reproduces $E^2=\vec p^2c^2+m^2c^4$.
7. **Helicity blocks.** The symbol squares to the interval, $\slashed p^2=p^2\,\mathrm I$, and commutes with $L_\Xi$, $\Xi=-i\vec u_p$, so it splits into two $2\times2$ blocks of determinant $m^2-p^2=\lambda_+\lambda_-+m^2$; the blocks are isospectral, $\det\mathcal D(p)=(m^2-p^2)^2$, and the mass shell is the vanishing of each block determinant, with a one-dimensional kernel per helicity.

Two objects are needed by the exercise and are not displayed in the parent: the chiral negative-frequency spinors $\tilde v_\pm$ (Problem 1) and the change-of-basis biquaternion $\tilde W$ (Problem 5). The constructions above reproduce the parent's stated results.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb B=\mathbb C\otimes_\mathbb R\mathbb H$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $R_a,L_a$ | Right and left multiplication, $R_a(\tilde Q)=\tilde Q a$, $L_a(\tilde Q)=a\tilde Q$ |
| $iR_{\vec e_x}^{\mathrm{axf}}=R_{i\vec e_x}^{\mathrm{axf}}$, $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=L_{i\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | The five cells as algebra operations |
| $c_\mu=iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$ | The cell of the coordinate $x_\mu$: $c_0=iR_{\vec e_x}^{\mathrm{axf}}$ and $c_k=iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ |
| $-iR_{\vec e_z}^{\mathrm{axf}}=R_{-i\vec e_z}^{\mathrm{axf}}$ | Chirality cell |
| $\Omega=c_0c_1c_2c_3=-R_{\vec e_z}^{\mathrm{axf}}$ | Volume cell; $\Omega^2=-1$ and $i\Omega=R_{-i\vec e_z}^{\mathrm{axf}}$ |
| $\tilde\Pi_\pm=\frac12(e_t\pm i\vec e_z)$ | Peirce idempotents; $P_{L,R}=R_{\tilde\Pi_\pm}$ |
| $\vec\Upsilon_x,\vec\Upsilon_y$ | Off-diagonal matrix units |
| $\boldsymbol\sigma=(\sigma_x,\sigma_y,\sigma_z)$ | Pauli matrices, $\mathsf M_2(i\vec e_k)=\sigma_k$ |
| $\chi_\pm$, $\vec u_p=\vec p/\lvert\vec p\rvert$ | Helicity eigenspinors, $\boldsymbol\sigma\cdot\vec u_p\,\chi_\pm=\pm\chi_\pm$ |
| $\xi^{(r)},\eta^{(r)}$ | Rest spinors of the Dirac basis, positive- and negative-frequency |
| $\Psi_\pm(\chi)$ | Spinor realised in $\mathbb B\tilde\Pi_\pm$ |
| $\tilde\Psi=\Psi_+(\psi_+)+\Psi_-(\psi_-)$ | The Dirac field as a biquaternion |
| $\langle\tilde\Psi,\tilde\Phi\rangle_{\mathrm D}=\mathrm{Tr}(\tilde\Psi^*\tilde\Phi\,i\vec e_x)$ | Dirac pairing in the chiral basis |
| $\slashed p=iR_{\vec e_x}^{\mathrm{axf}}p_{0}-\sum_k iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}p_{k}=E R_{i\vec e_x}^{\mathrm{axf}}-p_kL_{i\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | Momentum-space Dirac operator |
| $\tilde W=(e_t+\vec e_y)/\sqrt2$ | Change of basis, chiral $\to$ Dirac |
| $S_{0k}=\frac i2L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$, $S_{jk}=\frac i2L_{\vec e_j\vec e_k}^{\mathrm{axf}}$ | Lorentz generators, $S_{\mu\nu}=\frac i4[c_\mu,c_\nu]$ |
| $\tilde P/\hbar=i\omega/c\,e_t+\vec k$ | Wave biquaternion |
| $\tilde P\tilde P^{\natural}=-m^2c^2$ | Mass-shell condition |
| $p^2=E^2-\vec p^{\,2}$ | Interval of the four-momentum, $\hbar=c=1$ |
| $\mathcal D(p)=\slashed p-m$ | Massive symbol; $\slashed p$ is the massless one |
| $\Xi=-i\vec u_p$ | Helicity element, $\Xi^2=i^2\vec u_p^{\,2}=e_t$; $L_\Xi$ grades the symbol into two blocks |
| $\lambda_\pm=i(E\mp\lvert\vec p\rvert)$ | Eigenvalues of $L_{\tilde P}$; $\lambda_+\lambda_-=\tilde P\tilde P^{\natural}$ |
| $\det\mathcal D(p)=(m^2-p^2)^2$ | Block determinant $m^2-p^2$ per helicity, squared in the symbol |

## Further Reading

- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the plane-wave spinors, the normalisations, and the spin sums in the standard notation.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the spin sums, the chiral and Dirac representations, and the Lorentz generators.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the two representations, the spinor normalisation, and the completeness relations.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Clifford algebra and the spinor representations.
- The representation theory used above: [The $M_4(\mathbb{C})$ Axis-Free Representation](../articles_maths/m4c-axis-free-representation.html), [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](../articles_maths/the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), and [The Polarized Module of the Biquaternion Algebra](../articles_maths/the-polarized-module-of-the-biquaternion-algebra.html).
- The parent article of this exercise: [The Biquaternion Dirac Equation — Solutions and the Non-Relativistic Limit](the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html), and its companions [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) and [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html).
