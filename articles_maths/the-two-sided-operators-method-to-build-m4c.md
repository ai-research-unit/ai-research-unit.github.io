# __The Two-Sided Operators Method to Build $M_4(\mathbb{C})$__

## Introduction

**The problem.** The algebra $M_4(\mathbb{C})$ is usually introduced as the algebra of $4\times4$ matrices, with the sixteen matrix units $E_{ij}$ as its basis. That presentation starts from matrices. The physics of the corpus starts from the biquaternion algebra $\mathbb{B}$, and the matrices that appear there are left multiplications, right multiplications and gamma matrices. The matrix units are not the objects the physics uses.

**The method.** Start from $\mathbb{B}$ and its carrier $\mathbb{B}\cong\mathbb{C}^4$. For $a,b\in\mathbb{B}$ define the two one-sided operators $L_a(x)=ax$ and $R_b(x)=xb$. The products $T_{a,b}=L_aR_b$, and their sums, form an algebra of operators on a four-dimensional space. That algebra is the whole of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$. Choosing the coefficient basis of $\mathbb{B}$ turns the operators into $4\times4$ matrices, and the method produces sixteen explicit matrices $T_{\mu\nu}=L_{e_\mu}R_{e_\nu}$. This article builds the algebra that way, displays the sixteen matrices, and proves the properties that make them the matrices to use.

**The result.** The sixteen $T_{\mu\nu}$ are signed permutation matrices of determinant one. They are orthogonal for the Hilbert–Schmidt form, with $\operatorname{tr}(T_{\mu\nu}^{*}T_{\rho\sigma})=4\delta_{\mu\rho}\delta_{\nu\sigma}$. They are closed under multiplication up to sign, and the thirty-two matrices $\pm T_{\mu\nu}$ form a group of order $32$. The coefficients of any matrix in this basis are sixteen traces, and the rank of the coefficient matrix is the length, the least number of products. Every matrix unit is a sum of four of the sixteen, so the matrix-unit basis is the worst basis for the product.

**The terminology.** $M_4(\mathbb{C})$ is the matrix representation of the operator algebra $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$, not the biquaternion algebra itself. The biquaternion algebra is four-dimensional and is not a matrix algebra until a basis of the carrier is chosen. The operator algebra is sixteen-dimensional; the choice of the coefficient basis writes it as $M_4(\mathbb{C})$. Three objects are in play, and the article keeps them apart.

| Object | What it is | Dimension |
|---|---|---|
| $\mathbb{B}$ | the biquaternion algebra | $4$ |
| $\mathcal{E}=\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$ | the algebra of two-sided operators | $16$ |
| $M_4(\mathbb{C})$ | the matrix representation of $\mathcal{E}$ in a basis of $\mathbb{B}$ | $16$ |

The carrier is $\mathbb{B}\cong\mathbb{C}^4$; it is not $M_4(\mathbb{C})$.

**The article.** §*The Starting Point* fixes the algebra and its carrier. §*The Two One-Sided Operators* displays $L_a$ and $R_b$. §*The Method* states and proves the construction. §*The Sixteen Matrices* displays the result and its invariants. §*The Group of Order Thirty-Two* proves the closure. §*Multiplication* gives the two tables. §*Orthogonality and the Coefficient Formula* proves the trace formula. §*The Matrix Units in the Method's Basis* gives the sixteen expansions and the length. §*The Peirce Dictionary* identifies the Peirce products. §*The Coefficient Matrix and the Length* states the computational rule, §*The Gamma Frame* records the physics frame, and §*Why These Matrices* states the case. The worked computation is the companion article.

**Sources and boundaries.** The left regular model and its product rules are *$M_4(\mathbb{C})_{\mathbb{B},L}$ Model : The Product, the Trace and the Determinant*; the Peirce coordinates are *$M_4(\mathbb{C})_{\mathbb{B},L}$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes*; the operator construction is *$M_4(\mathbb{C})_{\mathbb{B},L}$ Representation : The Two-Sided Operators on the Biquaternion Algebra*; the abstract theorem is *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*; the Clifford reading is *The Dirac Algebra and Biquaternions: A Dictionary*. No form, no norm and no topology beyond the Hilbert–Schmidt pairing is used.

## The Starting Point

**The algebra.** Let $\mathbb{B}$ be the complexified quaternion algebra, with basis $e_t,e_x,e_y,e_z$ and product
$$
e_t^2=e_t,\qquad e_x^2=e_y^2=e_z^2=-e_t,\qquad
e_xe_y=e_z,\quad e_ye_z=e_x,\quad e_ze_x=e_y,
$$
and the reverse products negative: $e_ye_x=-e_z$, $e_ze_y=-e_x$, $e_xe_z=-e_y$. The unit is $e_t$, written $1$ when no confusion is possible.

**The carrier.** The algebra acts on itself by multiplication, so its underlying complex vector space is a four-dimensional carrier. In the basis $(e_t,e_x,e_y,e_z)$ a vector has coordinates $(a_t,a_x,a_y,a_z)$, and the carrier is $\mathbb{C}^4$.

**The algebra is simple but not a division algebra.** It is isomorphic to $M_2(\mathbb{C})$. A nonzero element need not be invertible: the norm
$$
N(a)=a_t^2+a_x^2+a_y^2+a_z^2
$$
can vanish for $a\ne0$, and then $a$ is a zero divisor. For example $(1+ie_x)(1-ie_x)=1-e_x^2=0$. The units are the elements with $N(a)\ne0$. This matters below: $L_a$ is invertible exactly when $a$ is a unit.

**The multiplication table of the basis.** Row $\mu$, column $\nu$, entry $e_\mu e_\nu$. It is the quaternion table, and it is the left table of §*Multiplication*.

| $e_\mu e_\nu$ | $e_t$ | $e_x$ | $e_y$ | $e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $e_x$ | $e_y$ | $e_z$ |
| $e_x$ | $e_x$ | $-e_t$ | $e_z$ | $-e_y$ |
| $e_y$ | $e_y$ | $-e_z$ | $-e_t$ | $e_x$ |
| $e_z$ | $e_z$ | $e_y$ | $-e_x$ | $-e_t$ |

## The Two One-Sided Operators

### Left multiplication

**Definition.** For $a\in\mathbb{B}$, let $L_a$ be the matrix of $x\mapsto ax$ in the coefficient basis $e_t,e_x,e_y,e_z$, ordered $t,x,y,z$. The map $L$ is the left regular representation.

**The four basis matrices.** With $e_x^2=e_y^2=e_z^2=-e_t$ and $e_xe_y=e_z$, $e_ye_z=e_x$, $e_ze_x=e_y$,

$$
L_t=\mathrm{I}_4,\qquad
L_x=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad
L_y=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
L_z=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}.
$$

**The laws.** $L_aL_b=L_{ab}$, $L_t=\mathrm{I}_4$, and $L_a$ is invertible exactly when $a$ is a unit. The image $L(\mathbb{B})$ has complex dimension four.

### Right multiplication

**Definition.** For $b\in\mathbb{B}$, let $R_b$ be the matrix of $x\mapsto xb$.

**The four basis matrices.**

$$
R_t=\mathrm{I}_4,\qquad
R_x=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix},\qquad
R_y=\begin{pmatrix}0&0&-1&0\\0&0&0&-1\\1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
R_z=\begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix}.
$$

**The relation to the left family.** Let $D=\operatorname{diag}(1,-1,-1,-1)$ and let $b^{\dagger}=(b_t,-b_x,-b_y,-b_z)$ be the quaternion conjugate. Then

$$
R_b=D\,L_{b^{\dagger}}\,D .
$$

**The laws.** $R_aR_b=R_{ba}$, $R_{e_t}=\mathrm{I}_4$, and $R_b$ is invertible exactly when $b$ is a unit. The image $R(\mathbb{B})$ has complex dimension four.

### The two-sided matrices

**Definition.** For $a,b\in\mathbb{B}$,

$$
T_{a,b}=L_aR_b .
$$

**The laws.** $T_{a,b}T_{c,d}=T_{ac,db}$, because $L_aR_bL_cR_d=L_{ac}R_{db}$. The left and right families commute, $L_aR_b=R_bL_a$, and they meet in the scalars:

$$
L(\mathbb{B})\cap R(\mathbb{B})=\mathbb{C}\,\mathrm{I}_4 .
$$

**The basis.** The sixteen matrices

$$
T_{\mu\nu}=T_{e_\mu,e_\nu}=L_\mu R_\nu,\qquad \mu,\nu\in\{t,x,y,z\},
$$

are a basis of $M_4(\mathbb{C})$. The dimension count is $4\cdot4=16$.

**Every one is a signed permutation.** Each $T_{\mu\nu}$ has exactly one nonzero entry in every row and every column, and that entry is $\pm1$. The left factor permutes and signs the rows; the right factor permutes and signs the columns.


## The Method

### The construction in five steps

**Step 1.** Start from the biquaternion algebra $\mathbb{B}$ and its four-dimensional carrier. No matrix is chosen yet.

**Step 2.** Form the eight one-sided operators $L_t,L_x,L_y,L_z$ and $R_t,R_x,R_y,R_z$. They are linear maps of the carrier to itself.

**Step 3.** Form the products $T_{a,b}=L_aR_b$ and all their linear combinations. This is the algebra generated by the two commuting copies $L(\mathbb{B})$ and $R(\mathbb{B})$.

**Step 4.** Prove that this algebra is the whole of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, of complex dimension sixteen. The proof is the proposition below.

**Step 5.** Choose the coefficient basis of the carrier. The operators become $4\times4$ matrices, and the method produces the sixteen matrices $T_{\mu\nu}=L_{e_\mu}R_{e_\nu}$ displayed in §*The Sixteen Matrices*.

**What the method does not do.** It does not choose a gamma frame, a form, a norm or a grading. Those are further choices inside the matrix algebra. It does not identify $\mathbb{B}$ with $M_4(\mathbb{C})$: $\mathbb{B}$ is four-dimensional, and $M_4(\mathbb{C})$ is the matrix representation of the sixteen-dimensional operator algebra.

### The theorem

**Proposition (the two-sided map is an isomorphism).** The map
$$
\Phi:\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\longrightarrow\operatorname{End}_{\mathbb{C}}(\mathbb{B}),
\qquad \Phi(a\otimes b^{\mathrm{opp}})=L_aR_b,
$$
is an isomorphism of algebras. Hence
$$
\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\cong\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_4(\mathbb{C}).
$$

**Proof.** Multiplicativity: in the opposite algebra the product is reversed, so
$$
(a\otimes b^{\mathrm{opp}})(c\otimes d^{\mathrm{opp}})=ac\otimes(db)^{\mathrm{opp}},
$$
and $\Phi$ of this is $L_{ac}R_{db}=L_aL_cR_dR_b=L_aR_bL_cR_d$, which is the product of the images.

Injectivity: choose a matrix-unit basis $F_{ij}$ of $\mathbb{B}\cong M_2(\mathbb{C})$. The elements $F_{ij}\otimes F_{kl}^{\mathrm{opp}}$ are a basis of the tensor product, sixteen in number. Their images act by $X\mapsto F_{ij}XF_{kl}$, and since $F_{ij}F_{ab}F_{kl}=\delta_{ja}\delta_{bk}F_{il}$, the image is the matrix unit of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ that sends $F_{jk}$ to $F_{il}$ and the other $F_{ab}$ to $0$. The sixteen images are the sixteen matrix units of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ in the basis $\{F_{ab}\}$; they are linearly independent. So $\Phi$ is injective.

Dimensions: the domain has dimension $4\cdot4=16$, and the target has dimension $4^2=16$. An injective linear map between spaces of the same finite dimension is an isomorphism.

**The matrices follow.** The coefficient basis of $\mathbb{B}$ is related to the matrix-unit basis by an invertible change of basis. The sixteen images $T_{\mu\nu}=L_{e_\mu}R_{e_\nu}$ are the images of the basis $e_\mu\otimes e_\nu^{\mathrm{opp}}$, so they are a basis of $M_4(\mathbb{C})$. No counting of matrix entries is needed: the dimension comes from the two factors.

### What has been built

**The algebra.** After Step 5 the algebra is literally $M_4(\mathbb{C})$: its elements are the $4\times4$ complex matrices, with the usual product. But the construction remembers where each matrix came from. The matrix $T_{\mu\nu}$ is the operator $x\mapsto e_\mu xe_\nu$, and the label $(\mu,\nu)$ is the pair of biquaternions that produces it.

**The two regular images.** $L(\mathbb{B})$ and $R(\mathbb{B})$ are the two four-dimensional subalgebras. They commute and meet in the scalars. Neither is the whole algebra; their products are.

**The matrix units are derived, not primitive.** The standard basis $E_{ij}$ is a basis of the algebra, but it is not the basis the construction produces. The relation between the two is computed in §*The Matrix Units in the Method's Basis*: every $E_{ij}$ is a sum of four of the $T_{\mu\nu}$.

## The Sixteen Matrices

### The display

**The sixteen matrices, in the coefficient basis.** The labels are the two indices: the first is the left parameter, the second the right parameter.

$$
T_{tt}=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
T_{tx}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix},\qquad
T_{ty}=\begin{pmatrix}0&0&-1&0\\0&0&0&-1\\1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
T_{tz}=\begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix}.
$$

$$
T_{xt}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad
T_{xx}=\begin{pmatrix}-1&0&0&0\\0&-1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
T_{xy}=\begin{pmatrix}0&0&0&1\\0&0&-1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix},\qquad
T_{xz}=\begin{pmatrix}0&0&-1&0\\0&0&0&-1\\-1&0&0&0\\0&-1&0&0\end{pmatrix}.
$$

$$
T_{yt}=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
T_{yx}=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&-1&0&0\\-1&0&0&0\end{pmatrix},\qquad
T_{yy}=\begin{pmatrix}-1&0&0&0\\0&1&0&0\\0&0&-1&0\\0&0&0&1\end{pmatrix},\qquad
T_{yz}=\begin{pmatrix}0&1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&-1&0\end{pmatrix}.
$$

$$
T_{zt}=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix},\qquad
T_{zx}=\begin{pmatrix}0&0&1&0\\0&0&0&-1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
T_{zy}=\begin{pmatrix}0&-1&0&0\\-1&0&0&0\\0&0&0&-1\\0&0&-1&0\end{pmatrix},\qquad
T_{zz}=\begin{pmatrix}-1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&-1\end{pmatrix}.
$$

**The order of the labels matters.** The two matrices $T_{tx}$ and $T_{xt}$ are different:

$$
T_{tx}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix},\qquad
T_{xt}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix}.
$$

They agree in the first two rows and differ in the last two. A computation that confuses them returns the wrong coefficient; the companion article *The Coefficient Matrix of a Two-Sided Operator: A Worked Computation* records the trap.

### The invariants

**The table.** The trace is the usual trace, the determinant the usual determinant, the rank the usual rank, the order the least $k\ge1$ with $T^k=\mathrm{I}_4$, and the last column is $T^2$.

| Matrix | Trace | Determinant | Rank | Order | Square |
|---|---|---|---|---|---|
| $T_{tt}$ | $4$ | $1$ | $4$ | $1$ | $\mathrm{I}_4$ |
| $T_{tx}$ | $0$ | $1$ | $4$ | $4$ | $-\mathrm{I}_4$ |
| $T_{ty}$ | $0$ | $1$ | $4$ | $4$ | $-\mathrm{I}_4$ |
| $T_{tz}$ | $0$ | $1$ | $4$ | $4$ | $-\mathrm{I}_4$ |
| $T_{xt}$ | $0$ | $1$ | $4$ | $4$ | $-\mathrm{I}_4$ |
| $T_{xx}$ | $0$ | $1$ | $4$ | $2$ | $\mathrm{I}_4$ |
| $T_{xy}$ | $0$ | $1$ | $4$ | $2$ | $\mathrm{I}_4$ |
| $T_{xz}$ | $0$ | $1$ | $4$ | $2$ | $\mathrm{I}_4$ |
| $T_{yt}$ | $0$ | $1$ | $4$ | $4$ | $-\mathrm{I}_4$ |
| $T_{yx}$ | $0$ | $1$ | $4$ | $2$ | $\mathrm{I}_4$ |
| $T_{yy}$ | $0$ | $1$ | $4$ | $2$ | $\mathrm{I}_4$ |
| $T_{yz}$ | $0$ | $1$ | $4$ | $2$ | $\mathrm{I}_4$ |
| $T_{zt}$ | $0$ | $1$ | $4$ | $4$ | $-\mathrm{I}_4$ |
| $T_{zx}$ | $0$ | $1$ | $4$ | $2$ | $\mathrm{I}_4$ |
| $T_{zy}$ | $0$ | $1$ | $4$ | $2$ | $\mathrm{I}_4$ |
| $T_{zz}$ | $0$ | $1$ | $4$ | $2$ | $\mathrm{I}_4$ |

**The pattern.** Every matrix is invertible, of determinant one and of rank four. The trace is $4$ only for $T_{tt}$, the identity, and $0$ for the other fifteen. The order is $4$ exactly when one index is $t$ and the other is spatial: $T_{t\sigma}$ and $T_{\sigma t}$ with $\sigma=x,y,z$ square to $-\mathrm{I}_4$. The two-spatial matrices square to $+\mathrm{I}_4$.

**Proof of the pattern.** The matrix $T_{\mu\nu}$ is a signed permutation, so it is orthogonal and its determinant is $\pm1$. The group $\{\pm T\}$ is generated by the six matrices $L_x,L_y,L_z,R_x,R_y,R_z$, each of determinant $1$ by the displayed matrices, and the determinant is a homomorphism; hence all thirty-two elements have determinant $1$. The trace and the order columns are read from the sixteen displayed matrices: the trace is $4$ only for the identity, and the square is $-\mathrm{I}_4$ exactly for the six matrices with one $t$ index and one spatial index. The square column also follows from the two multiplication tables of §*Multiplication*.

### The group of order thirty-two

**Theorem.** The thirty-two matrices $\pm T_{\mu\nu}$ are distinct and form a group; it is isomorphic to
$$
\bigl(Q_8\times Q_8\bigr)/\{\pm(1,1)\},
$$
where $Q_8=\{\pm1,\pm i,\pm j,\pm k\}$, and it has order $32$.

**Proof.** Closure: the product of two elements of $\{\pm T\}$ is
$$
(\pm T_{\mu\nu})(\pm T_{\rho\sigma})=\pm T_{\mu\nu}T_{\rho\sigma}=\pm T_{\mu\rho,\sigma\nu},
$$
by the composition law of §*The Two-Sided Matrices*. The result is again in $\{\pm T\}$. The set is finite, contains $\mathrm{I}_4=T_{tt}$, and every element is invertible, so it is a group. Distinctness: $T_{\mu\nu}=T_{\rho\sigma}$ gives $L_{\mu}^{-1}L_{\rho}=R_{\nu}R_{\sigma}^{-1}$, an element of $L(\mathbb{B})\cap R(\mathbb{B})=\mathbb{C}\mathrm{I}_4$; both sides are signed basis matrices, so both are $\mathrm{I}_4$, hence $\mu=\rho$ and $\nu=\sigma$. If $T_{\mu\nu}=-T_{\rho\sigma}$, the same argument gives $\mathrm{I}_4=-\mathrm{I}_4$, which is false. So the thirty-two are distinct.

For the isomorphism, let $Q_8^{L}=\{\pm\mathrm{I}_4,\pm L_x,\pm L_y,\pm L_z\}$ and $Q_8^{R}=\{\pm\mathrm{I}_4,\pm R_x,\pm R_y,\pm R_z\}$. Each is a copy of $Q_8$. They commute and meet in $\{\pm\mathrm{I}_4\}$, so their product has order $8\cdot8/2=32$, and it is the set $\{\pm T_{\mu\nu}\}$. The map $(A,B)\mapsto AB$ from $Q_8^{L}\times Q_8^{R}$ has kernel $\{(1,1),(-1,-1)\}$, hence the displayed quotient.

**The matrices are not a group of order sixteen.** The sixteen $T_{\mu\nu}$ alone are not closed: $T_{tx}T_{xt}=T_{xx}$ is in the set, but $T_{xy}T_{yz}=-T_{zx}$ is not. One sign is missing. The group needs the thirty-two signed matrices.

## Multiplication

### The two tables

**The left table.** Row $\mu$, column $\nu$, entry $L_\mu L_\nu$. The product is a signed basis matrix.

| $L_\mu L_\nu$ | $L_t$ | $L_x$ | $L_y$ | $L_z$ |
|---|---|---|---|---|
| $L_t$ | $L_t$ | $L_x$ | $L_y$ | $L_z$ |
| $L_x$ | $L_x$ | $-L_t$ | $L_z$ | $-L_y$ |
| $L_y$ | $L_y$ | $-L_z$ | $-L_t$ | $L_x$ |
| $L_z$ | $L_z$ | $L_y$ | $-L_x$ | $-L_t$ |

**The right table.** Row $\nu$, column $\sigma$, entry $R_\nu R_\sigma$. It is the table of the opposite quaternion algebra, so the signs sit in the other cells.

| $R_\nu R_\sigma$ | $R_t$ | $R_x$ | $R_y$ | $R_z$ |
|---|---|---|---|---|
| $R_t$ | $R_t$ | $R_x$ | $R_y$ | $R_z$ |
| $R_x$ | $R_x$ | $-R_t$ | $-R_z$ | $R_y$ |
| $R_y$ | $R_y$ | $R_z$ | $-R_t$ | $-R_x$ |
| $R_z$ | $R_z$ | $-R_y$ | $R_x$ | $-R_t$ |

**The two tables are not the same.** The left table is the quaternion table: $L_xL_y=L_z$. The right table is the reverse: $R_xR_y=-R_z$, because $R_aR_b=R_{ba}$ and $e_ye_x=-e_z$. This is the source of every sign in the corpus that looks like a sign error.

### The product rule

**The rule.** Read the left table at $(\mu,\rho)$ and the right table at $(\nu,\sigma)$:
$$
L_\mu L_\rho=\varepsilon_1L_\lambda,\qquad
R_\nu R_\sigma=\varepsilon_2R_\tau .
$$
Then
$$
T_{\mu\nu}T_{\rho\sigma}
=L_\mu L_\rho\,R_\nu R_\sigma
=\varepsilon_1\varepsilon_2\,T_{\lambda\tau}.
$$
The right index pair is not reversed in the formula; the reversal is already in the right table, whose row is the first factor and whose column is the second.

**In one line.**
$$
T_{\mu\nu}T_{\rho\sigma}=\varepsilon_1\varepsilon_2\,T_{\lambda\tau},
\qquad
(\lambda,\varepsilon_1)=\text{left table}(\mu,\rho),
\quad
(\tau,\varepsilon_2)=\text{right table}(\nu,\sigma).
$$

**The general law.** $T_{a,b}T_{c,d}=T_{ac,db}$. The product of two two-sided operators is a two-sided operator. The set of all $T_{a,b}$ is closed under multiplication, and it is the whole algebra.

### Three examples

**A product in the set.** $T_{tx}T_{xt}$: the left table at $(t,x)$ gives $L_x$ with sign $+1$; the right table at $(x,t)$ gives $R_x$ with sign $+1$. Hence
$$
T_{tx}T_{xt}=T_{xx}.
$$

**A product with a sign.** $T_{xy}T_{yz}$: the left table at $(x,y)$ gives $L_z$ with sign $+1$; the right table at $(y,z)$ gives $-R_x$. Hence
$$
T_{xy}T_{yz}=-T_{zx}.
$$

**A square.** $T_{zy}T_{zy}$: the left table at $(z,z)$ gives $-L_t$; the right table at $(y,y)$ gives $-R_t$; the product is $(-\mathrm{I}_4)(-\mathrm{I}_4)=\mathrm{I}_4$. This is the entry of the invariant table.

## Orthogonality and the Coefficient Formula

**Theorem.** For all indices,
$$
\operatorname{tr}\bigl(T_{\mu\nu}^{*}T_{\rho\sigma}\bigr)=4\,\delta_{\mu\rho}\delta_{\nu\sigma}.
$$

**Proof.** Every $T_{\mu\nu}$ is a signed permutation matrix, so it is orthogonal and $T_{\mu\nu}^{*}=T_{\mu\nu}^{-1}$. The inverse is $\pm T_{\mu\nu}$, because $T_{\mu\nu}^{2}=\pm\mathrm{I}_4$ by the invariant table. More generally,
$$
T_{\mu\nu}^{*}T_{\rho\sigma}=\pm T_{\mu\nu}T_{\rho\sigma}=\pm T_{\lambda\tau}
$$
for some indices $\lambda,\tau$. The trace of $T_{\lambda\tau}$ is $4$ when $\lambda=\tau=t$ and $0$ otherwise, by the invariant table. The indices $\lambda,\tau$ are $t$ exactly when $\mu=\rho$ and $\nu=\sigma$, because the product of two basis quaternions is the identity only when the factors are equal. Hence the trace is $4$ on the diagonal and $0$ off it.

**The trace of a two-sided operator.** For all $a,b\in\mathbb{B}$,
$$
\operatorname{tr}(L_aR_b)=4\,a_tb_t .
$$
The two sides are bilinear in $(a,b)$, and they agree on the sixteen basis pairs by the invariant table.

**The coefficient formula.** Let $A\in M_4(\mathbb{C})$ and write
$$
A=\sum_{\mu,\nu}c_{\mu\nu}(A)\,T_{\mu\nu}.
$$
Then
$$
c_{\mu\nu}(A)=\tfrac14\operatorname{tr}\bigl(T_{\mu\nu}^{*}A\bigr).
$$

**Proof.** Multiply the expansion by $T_{\rho\sigma}^{*}$ and take the trace. Orthogonality leaves $4c_{\rho\sigma}$.

**The formula in entries.** Since $T_{\mu\nu}$ is a signed permutation,
$$
\operatorname{tr}\bigl(T_{\mu\nu}^{*}A\bigr)
=\sum_{i,j}(T_{\mu\nu})_{ij}A_{ij},
$$
because $T_{\mu\nu}^{*}=T_{\mu\nu}^{\mathsf T}$ and the transpose moves the entry $(i,j)$ to $(j,i)$. In practice one reads the four nonzero positions of $T_{\mu\nu}$ and adds the corresponding entries of $A$ with their signs, then divides by four. The companion article carries out the sixteen sums entry by entry for one matrix.

## The Matrix Units in the Method's Basis

### The sixteen expansions

**Theorem.** Every matrix unit is a sum of four of the $T_{\mu\nu}$ with coefficients $\pm\tfrac14$:
$$
E_{ij}=\tfrac14\sum_{\mu,\nu}\varepsilon^{\,ij}_{\mu\nu}T_{\mu\nu},
\qquad \varepsilon^{\,ij}_{\mu\nu}\in\{\pm1\},
$$
and each row of the coefficient array has exactly four nonzero entries.

**The table.** The matrix units are those of the coefficient basis, the same basis in which the $T_{\mu\nu}$ are displayed.

| Matrix unit | Expansion |
|---|---|
| $E_{11}$ | $\tfrac14\bigl(T_{tt}-T_{xx}-T_{yy}-T_{zz}\bigr)$ |
| $E_{12}$ | $\tfrac14\bigl(-T_{tx}-T_{xt}+T_{yz}-T_{zy}\bigr)$ |
| $E_{13}$ | $\tfrac14\bigl(-T_{ty}-T_{xz}-T_{yt}+T_{zx}\bigr)$ |
| $E_{14}$ | $\tfrac14\bigl(-T_{tz}+T_{xy}-T_{yx}-T_{zt}\bigr)$ |
| $E_{21}$ | $\tfrac14\bigl(T_{tx}+T_{xt}+T_{yz}-T_{zy}\bigr)$ |
| $E_{22}$ | $\tfrac14\bigl(T_{tt}-T_{xx}+T_{yy}+T_{zz}\bigr)$ |
| $E_{23}$ | $\tfrac14\bigl(T_{tz}-T_{xy}-T_{yx}-T_{zt}\bigr)$ |
| $E_{24}$ | $\tfrac14\bigl(-T_{ty}-T_{xz}+T_{yt}-T_{zx}\bigr)$ |
| $E_{31}$ | $\tfrac14\bigl(T_{ty}-T_{xz}+T_{yt}+T_{zx}\bigr)$ |
| $E_{32}$ | $\tfrac14\bigl(-T_{tz}-T_{xy}-T_{yx}+T_{zt}\bigr)$ |
| $E_{33}$ | $\tfrac14\bigl(T_{tt}+T_{xx}-T_{yy}+T_{zz}\bigr)$ |
| $E_{34}$ | $\tfrac14\bigl(T_{tx}-T_{xt}-T_{yz}-T_{zy}\bigr)$ |
| $E_{41}$ | $\tfrac14\bigl(T_{tz}+T_{xy}-T_{yx}+T_{zt}\bigr)$ |
| $E_{42}$ | $\tfrac14\bigl(T_{ty}-T_{xz}-T_{yt}-T_{zx}\bigr)$ |
| $E_{43}$ | $\tfrac14\bigl(-T_{tx}+T_{xt}-T_{yz}-T_{zy}\bigr)$ |
| $E_{44}$ | $\tfrac14\bigl(T_{tt}+T_{xx}+T_{yy}-T_{zz}\bigr)$ |

**Two examples in full.** For $E_{11}$ the four diagonal $T$'s enter with the signs of the coordinates: the trace sum $1-(-1)-(-1)-(-1)=4$ gives the coefficient $1$, while the off-diagonal entries cancel. For $E_{12}$ the four $T$'s with exactly one $t$ index enter; the two $t$-first matrices give the first column, and the two $t$-second matrices give the second.

**The coefficient array is a signed permutation.** In each expansion the four indices $(\mu,\nu)$ are distinct, and each row index and each column index occurs exactly once. The array $\varepsilon^{\,ij}$ is therefore a signed permutation matrix, of rank four.

### Length four

**Corollary.** The length of every matrix unit is four:
$$
\ell(E_{ij})=4 .
$$

**Proof.** The length is the rank of the coefficient matrix (Theorem of §*The Coefficient Matrix and the Length*). The expansion has four nonzero coefficients in a permutation pattern, so the coefficient matrix has rank four.

**The meaning.** The matrix units are the worst possible basis for the product: each of them needs four two-sided operators. A physics table written in matrix units hides a factor of four in every entry. A table written in the method's basis shows one product per entry.

## The Peirce Dictionary

**The Peirce basis.** Let $P_0=\tilde\Pi_+$, $P_1=\vec\Upsilon_y$, $P_2=\vec\Upsilon_x$, $P_3=\tilde\Pi_-$, the four Peirce elements of *$M_4(\mathbb{C})_{\mathbb{B},L}$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes*, in the order $(t,x,y,z)$ of the coefficient basis.

**Theorem.** In the Peirce basis the sixteen products $L_{P_i}R_{P_j}$ are exactly the sixteen matrix units, with coefficient $+1$:
$$
L_{P_i}R_{P_j}=\mathsf{E}_{r(i,j),c(i,j)},
$$
where $\mathsf{E}_{rc}$ is the matrix unit of the Peirce basis. The correspondence is the table below.

| $i\backslash j$ | $0$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|
| $0$ | $\mathsf{E}_{11}$ | $\mathsf{E}_{13}$ | $\mathsf{E}_{31}$ | $\mathsf{E}_{33}$ |
| $1$ | $\mathsf{E}_{21}$ | $\mathsf{E}_{23}$ | $\mathsf{E}_{41}$ | $\mathsf{E}_{43}$ |
| $2$ | $\mathsf{E}_{12}$ | $\mathsf{E}_{14}$ | $\mathsf{E}_{32}$ | $\mathsf{E}_{34}$ |
| $3$ | $\mathsf{E}_{22}$ | $\mathsf{E}_{24}$ | $\mathsf{E}_{42}$ | $\mathsf{E}_{44}$ |

**Proof.** The four Peirce elements form a system of $2\times2$ matrix units, not four orthogonal idempotents: their table is the matrix-unit table $E_{ij}E_{kl}=\delta_{jk}E_{il}$ of the model article. Multiplying the four elements in the coefficient basis, and conjugating each of the sixteen products $L_{P_i}R_{P_j}$ by the Peirce change $S$, gives a matrix with a single nonzero entry in the Peirce basis, at the position of the table, with value $+1$. The computation is sixteen products of $4\times4$ matrices, and no case is exceptional.

**The two bases are adapted to different questions.** The coefficient basis makes the $T_{\mu\nu}$ signed permutations. The Peirce basis makes the products $L_{P_i}R_{P_j}$ matrix units. Neither basis does both: in the Peirce basis the $T_{\mu\nu}$ are monomial with entries in $\{1,-1,i,-i\}$ but not matrix units; in the coefficient basis the Peirce products are sums of four $T$'s whose coefficient array has rank one, so each is a single product.

**Why the two are consistent.** Both are bases of the same sixteen-dimensional algebra. The change of basis between them is the Peirce change $S$ of the model article, of determinant $-\tfrac14$, and the lengths agree because the length is basis-independent.

## The Coefficient Matrix and the Length

**Definition.** For $A\in M_4(\mathbb{C})$, the coefficient matrix is
$$
c(A)=\bigl(c_{\mu\nu}(A)\bigr)_{\mu,\nu\in\{t,x,y,z\}},
\qquad
c_{\mu\nu}(A)=\tfrac14\operatorname{tr}\bigl(T_{\mu\nu}^{*}A\bigr).
$$

**Theorem (reconstruction).** $A=\sum_{\mu,\nu}c_{\mu\nu}(A)T_{\mu\nu}$.

**Theorem (products are outer products).** For $a=\sum_\mu a_\mu e_\mu$ and $b=\sum_\nu b_\nu e_\nu$,
$$
c(L_aR_b)=a\,b^{\mathsf T},
$$
the outer product of the coordinate column of $a$ and the coordinate column of $b$.

**Proof.** $L_aR_b=\sum_{\mu,\nu}a_\mu b_\nu T_{\mu\nu}$, and the coefficients are unique.

**Corollary.** A matrix is a single two-sided operator exactly when its coefficient matrix has rank at most one. The rank is the length:
$$
\ell(A)=\operatorname{rank}c(A).
$$

**Proof.** A decomposition $A=\sum_{k=1}^{r}L_{a_k}R_{b_k}$ gives $c(A)=\sum_k a_kb_k^{\mathsf T}$, a sum of $r$ rank-one matrices, so $\operatorname{rank}c(A)\le r$. Conversely, a rank-$r$ factorisation $c(A)=UV$ with $U,V$ of size $4\times r$ gives $A=\sum_{k=1}^{r}L_{u_k}R_{v_k}$, where $u_k$ and $v_k$ are the columns. Hence the least $r$ is the rank.

**The algorithm.** In practice:

1. Compute the sixteen traces $c_{\mu\nu}=\tfrac14\operatorname{tr}(T_{\mu\nu}^{*}A)$.
2. Assemble the $4\times4$ matrix $c(A)$.
3. Compute its rank, by minors or by row reduction. That rank is the length.
4. If the rank is one, read $c=a b^{\mathsf T}$ and return $A=L_aR_b$.
5. If the rank is $r$, factor $c=UV$ with $U,V$ of size $4\times r$ and return the $r$ products $L_{u_k}R_{v_k}$.
6. Reconstruct $A=\sum c_{\mu\nu}T_{\mu\nu}$ as a check.

**What the length is not.** It is not the matrix rank. The identity has matrix rank four and length one. The matrix unit $E_{11}$ has matrix rank one and length four. The companion article computes a matrix of matrix rank four and length two.

**The invariance.** The length is invariant under conjugation by $GL_4(\mathbb{C})$, because the two-sided operators are exactly the rank-one matrices, and conjugation preserves rank. It is also invariant under the finite group of order $32$, which permutes the $T_{\mu\nu}$ up to sign.

## The Gamma Frame

**The five matrices.** In the corpus frame $(\beta,\delta)=(e_y,e_x)$,
$$
\gamma^0=iT_{tx},\qquad
\gamma^1=iT_{xy},\qquad
\gamma^2=iT_{yy},\qquad
\gamma^3=iT_{zy},\qquad
\gamma_5=-iT_{tz}.
$$

**The Clifford relations.** With the metric $g=\operatorname{diag}(1,-1,-1,-1)$,
$$
\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}\mathrm{I}_4,
\qquad
\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3,
\qquad
\{\gamma_5,\gamma^\mu\}=0.
$$

**The chirality projectors.**
$$
P_{\pm}=\tfrac12\bigl(\mathrm{I}_4\pm\gamma_5\bigr)
=\tfrac12\bigl(T_{tt}\mp iT_{tz}\bigr).
$$
Both are single products up to a scalar: $P_+$ and $P_-$ are linear combinations of two $T$'s, not products themselves.

**The reading.** The gammas are five of the sixteen $T$'s up to the scalar $i$. The products of the gammas are the other eleven, up to scalars. The Dirac algebra is the method's algebra with a chosen five-element frame, not a different algebra.

**The frame is not canonical.** The five displayed matrices are one choice among the frames of the companion article. The basis $\{T_{\mu\nu}\}$ is canonical once the coefficient basis is fixed; the gamma frame inside it is not.

## Why These Matrices

**Six reasons.**

1. **The matrices are the operators.** Each $T_{\mu\nu}$ is $x\mapsto e_\mu xe_\nu$. A table entry written as $T_{\mu\nu}$ says which left and right multiplications produce it. A table entry written as $E_{ij}$ says only which entry of a matrix is nonzero.
2. **The product is closed up to sign.** The thirty-two matrices $\pm T_{\mu\nu}$ form a group. Products, inverses and powers stay in a finite set. In the matrix-unit basis the product of two basis elements is either zero or a third, but the coefficients of a general product spread over sixteen terms.
3. **The coefficients are traces.** Orthogonality gives $c_{\mu\nu}=\tfrac14\operatorname{tr}(T_{\mu\nu}^{*}A)$ with norm $2$. There is no linear system to solve.
4. **The coefficient rank is the length.** The least number of products is the rank of a $4\times4$ matrix. This is the natural measure of complexity of an operator, and it is basis-independent.
5. **The physics matrices are sparse in this basis.** The gammas, the chirality projectors, the mass bilinear and the Lorentz generators are linear combinations of a few $T$'s with coefficients in $\{1,-1,i,-i\}$.
6. **The matrix units are the wrong default.** Every $E_{ij}$ has length four. A table in matrix units overstates the number of products by a factor of four in every entry.

**The caveat.** The matrix units remain the canonical basis of the abstract algebra: they are the definition of the product, and the theorems of the category are stated in them. The eigenbasis remains canonical for spectral theory. The Peirce basis remains canonical for the chiral blocks. The sixteen matrices are the default for the operator question, not a replacement for the others.

**A test.** Take a matrix from a physics table. If it is a gamma, a projector, a field strength or a mass term, it has a short expression in the method's basis. Compute the sixteen traces and the rank. If the rank is small, the matrix is a short product, and the table is hiding a product structure. If the rank is four, the matrix is a genuinely complicated operator.

## A Worked Example

**The matrix.**
$$
M=\begin{pmatrix}1&2&0&0\\0&1&0&0\\0&0&1&2\\0&0&0&1\end{pmatrix}.
$$

**The coefficients.** The sixteen traces give
$$
c(M)=\begin{pmatrix}1&0&0&0\\-1&0&0&0\\0&0&0&0\\0&0&-1&0\end{pmatrix}.
$$

**The length.** The rank is two, so $\ell(M)=2$, while the matrix rank of $M$ is four. A decomposition is
$$
M=L_{e_t-e_x}R_{e_t}+L_{e_z}R_{-e_y}
=T_{tt}-T_{xt}-T_{zy}.
$$

**The caution.** The matrix looks like two copies of a Jordan block, but it is not a left regular matrix: in the coefficient basis a left matrix has equal entries $(1,2)$ and $(2,1)$ up to sign, and $M$ has $2$ and $0$. The block look is a property of the coefficient basis, not of the Peirce decomposition.

**The full computation.** *The Coefficient Matrix of a Two-Sided Operator: A Worked Computation* carries out the sixteen traces, the transpose products, the rank by minors, the factorisation and the reconstruction, entry by entry.

## Summary

The algebra $M_4(\mathbb{C})$ is built by the two-sided operators method, which produces the sixteen matrices $T_{\mu\nu}=L_{e_\mu}R_{e_\nu}$, all signed permutations of determinant one. They are orthogonal for the Hilbert–Schmidt form with $\operatorname{tr}(T_{\mu\nu}^{*}T_{\rho\sigma})=4\delta_{\mu\rho}\delta_{\nu\sigma}$, so the coefficients of a matrix are sixteen traces. They are closed under multiplication up to sign, and the thirty-two matrices $\pm T_{\mu\nu}$ form a group of order $32$, isomorphic to $(Q_8\times Q_8)/\{\pm(1,1)\}$. The product rule is read from two $4\times4$ tables, the left quaternion table and the right opposite table. Every matrix unit is a sum of four $T$'s with coefficients $\pm\tfrac14$, so every matrix unit has length four; the matrix-unit basis is the worst basis for the product. In the Peirce basis the sixteen products $L_{P_i}R_{P_j}$ are exactly the sixteen matrix units with coefficient $+1$. The coefficient matrix of a product is an outer product, and the rank of the coefficient matrix is the length, the least number of two-sided operators. The gamma frame is five of the sixteen matrices up to the scalar $i$. The sixteen matrices are the default for matrices that come from operators; they do not replace the matrix units for the abstract algebra, the eigenbasis for spectral theory or the Peirce basis for the chiral blocks.

$$
\boxed{\ \operatorname{tr}(T_{\mu\nu}^{*}T_{\rho\sigma})=4\delta_{\mu\rho}\delta_{\nu\sigma},\qquad
c_{\mu\nu}(A)=\tfrac14\operatorname{tr}(T_{\mu\nu}^{*}A),\qquad
\ell(A)=\operatorname{rank}c(A).\ }
$$

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, $\mathbb{C}\otimes_\mathbb{R}\mathbb{H}\cong M_2(\mathbb{C})$ |
| $e_t,e_x,e_y,e_z$ | the coefficient basis, with $e_t=1$ and $e_x^2=e_y^2=e_z^2=-e_t$ |
| $L_a$ | left multiplication $x\mapsto ax$ |
| $R_b$ | right multiplication $x\mapsto xb$ |
| $T_{a,b}=L_aR_b$ | the two-sided operator $x\mapsto axb$ |
| $T_{\mu\nu}$ | $T_{e_\mu,e_\nu}$, the sixteen basis matrices |
| $E_{ij}$ | the matrix units of the coefficient basis |
| $\mathsf{E}_{ij}$ | the matrix units of the Peirce basis |
| $P_0,P_1,P_2,P_3$ | the four Peirce elements, in the order $(t,x,y,z)$ |
| $c(A)$ | the coefficient matrix, $c_{\mu\nu}=\tfrac14\operatorname{tr}(T_{\mu\nu}^{*}A)$ |
| $\ell(A)$ | the length, the least number of products |
| $Q_8$ | the quaternion group $\{\pm1,\pm i,\pm j,\pm k\}$ |
| $\gamma^\mu,\gamma_5$ | the gamma frame of the corpus |
| $D$ | $\operatorname{diag}(1,-1,-1,-1)$, the carrier of the right family |

## Further Reading

- [$M_4(\mathbb{C})_{\mathbb{B},L}$ Representation : The Two-Sided Operators on the Biquaternion Algebra](m4c-representation-the-two-sided-operators-on-the-biquaternion-algebra.html), for the construction, the gamma frame and the product question.
- [$M_4(\mathbb{C})_{\mathbb{B},L}$ Model : The Product, the Trace and the Determinant](m4c-model-the-product-the-trace-and-the-determinant.html), for the left regular model and its trace and determinant.
- [$M_4(\mathbb{C})_{\mathbb{B},L}$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes](m4c-model-the-peirce-coordinates-matrix-units-and-the-spinor-planes.html), for the Peirce basis, the chiral blocks and the matrix units $L_{P_i}R_{P_j}$.
- [The Matrix Algebra $M_4(\mathbb{C})$](the-matrix-algebra-m4c.html), for the algebra, the matrix units and the construction from the two-sided map.
- [The Operators of the Peirce Decomposition of $M_4(\mathbb{C})$](the-operators-of-the-peirce-decomposition-of-m4c.html), for the operators $L_a,R_a,T_{a,b}$ on the sixteen-dimensional algebra.
- [The Coefficient Matrix of a Two-Sided Operator: A Worked Computation](the-coefficient-matrix-of-a-two-sided-operator-a-worked-computation.html), for the sixteen traces, the rank and the factorisation of one matrix.
- [The Numerical Range of the Two-Sided Operators of $M_4(\mathbb{C})$](the-numerical-range-of-the-two-sided-operators-of-m4c.html), for the field of values of the sandwich on the sixteen-dimensional algebra.
- [The Dirac Algebra and Biquaternions: A Dictionary](../articles_physics/the-dirac-algebra-and-biquaternions-a-dictionary.html), for the explicit chiral matrices of one frame.
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for the abstract theorem $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}\cong\operatorname{End}_{\mathbb{C}}(\mathbb{B})$.
