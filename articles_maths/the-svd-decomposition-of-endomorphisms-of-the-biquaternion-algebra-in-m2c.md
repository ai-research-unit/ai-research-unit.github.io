# __The SVD Decomposition of Endomorphisms of the Biquaternion Algebra in $M_2(\mathbb{C})$__

## Introduction

**The question.** Every endomorphism of the algebra can be written as a sum of four rank-one pieces, each a left multiplier times a linear form, and the coefficients of the sum are the weights. This article asks what that decomposition is in the display, where an endomorphism is a $4\times4$ array and the rank-one pieces are the rank-one matrices.

**Why it is the same statement.** This is the in-depth matrix reading of [The SVD Decomposition of Endomorphisms of the Biquaternion Algebra](the-svd-decomposition-of-endomorphisms-of-the-biquaternion-algebra.html). The display $\mathsf M_2$ identifies $\mathbb{B}$ with $M_2(\mathbb{C})$ and carries the Hilbert–Schmidt form to half the Frobenius form, which on the four coefficients is the ordinary Euclidean form. The statements are identical, and only the writing is new: the singular value decomposition of the abstract endomorphism is the singular value decomposition of its $4\times4$ array in the standard Euclidean structures on the domain and the range.

**What the article proves.** In this order. The Hilbert–Schmidt form on the display is $\tfrac12\operatorname{tr}(Y^{\dagger}X)$, which on coefficient columns is $\sum_\mu\bar y_\mu x_\mu$, so the coefficient space is $\mathbb{C}^4$ with its standard form. The rank-one endomorphism $\mathcal P_{\tilde U,\tilde V}$ has array $uv^{\dagger}$, so the rank-one endomorphisms are exactly the rank-one matrices. The spectral theorem for a positive semidefinite Hermitian array is the ordinary unitary diagonalisation. The decomposition $F=\sum_k\rho_k u_kv_k^{\dagger}$ has the singular values of the array as weights, and the three identities $\prod\rho_k=|\det F|$, $\sum\rho_k^2=\lVert F\rVert^2$ and $\rho_1=\lVert F\rVert_{\mathrm{op}}$ hold. A left multiplier has weights the two singular values of $A$ each twice, a two-sided operator has the products, and the two-sided operator $\mathrm{Sd}_A=AR_{A^{\dagger}}$ has the pattern $\rho_1^2,\rho_1\rho_2,\rho_1\rho_2,\rho_2^2$. The truncation is the Eckart–Young theorem.

**What the article does not do.** It does not compute the polar decomposition, which is [The Adjoints and the Polar Decomposition of an Operator at $n=2$](the-adjoints-and-the-polar-decomposition-of-an-operator-at-n-2.html); it does not classify the operators by length, which is [The Length and the Two Ranks at $n=2$](the-length-and-the-two-ranks-at-n-2.html); and it does not treat the element-level polar decomposition, which is [The Polar Decomposition from the Two Halves at $n=2$](the-polar-decomposition-from-the-two-halves-at-n-2.html).

**Conventions.** The display is $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$, with trace $2Q_t$ and determinant $N(\tilde Q)=Q_t^2+Q_x^2+Q_y^2+Q_z^2$. The Hilbert–Schmidt form on elements is

$$
\langle\tilde X,\tilde Y\rangle_{*}=\operatorname{Sc}(\tilde X\tilde Y^{*})=\tfrac12\operatorname{tr}(XY^{\dagger}),
$$

and the two norms of an element are $|\tilde Q|^2=\langle\tilde Q,\tilde Q\rangle_{*}=\sum_\mu|Q_\mu|^2$ and $N(\tilde Q)=\det A$. The operator form on $\operatorname{End}$ is $\langle F,G\rangle=\operatorname{Tr}(F^{\dagger}G)$ on the arrays, the full Frobenius form; a signed-permutation array has norm two, and the norm of an operator is $\sum_\mu\lVert F(e_\mu)\rVert^2$ taken over an orthonormal basis of the carrier. Any $4\times4$ array printed here is the axis-free array and not the Pauli array: the axis-free family is the unique representative, among the $96$ signed-permutation bases, whose sixteen operator arrays are signed permutations, so its entries are the multiplication table read aloud and every identity checked in it is an integer check ([$M_4(\mathbb{C})$ Axis-Free Representation : Operators](m4c-axis-free-representation-operators.html)). The Pauli and gamma arrays are a translation and are refused as primary, because one entry of one of their matrices is diagonal by privilege, which puts a spatial direction into the notation; the privilege is canonical and fixes no invariant.

**Boundaries.** The carrier and the form are the source article. The one-sided operators are [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html). The two-sided cone is [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html). The polar decomposition of an operator is [The Adjoints and the Polar Decomposition of an Operator at $n=2$](the-adjoints-and-the-polar-decomposition-of-an-operator-at-n-2.html). The $n=2$ spine is [The Symmetric and Antisymmetric Parts of the Operator Space at $n=2$](the-symmetric-and-antisymmetric-parts-of-the-operator-space-at-n-2.html) and [$\operatorname{End}(M_2(\mathbb{C}))$ as an Algebra: the Regular Representation](end-m2c-as-an-algebra-the-regular-representation.html).

**Letters.** The array of $F$ is $F\in M_4(\mathbb{C})$, its weights are $\rho_1\geq\rho_2\geq\rho_3\geq\rho_4\geq0$, the left singular vectors are $u_k$ and the right are $v_k$, both coefficient columns of unit norm. The adjoint is $F^{\dagger}$. The singular values of a $2\times2$ matrix $A$ are $s_1(A)\geq s_2(A)\geq0$.

## The Carrier and the Two Norms

**The form.** The Hilbert–Schmidt form of the source becomes, in the display,

$$
\langle\tilde X,\tilde Y\rangle_{*}=\tfrac12\operatorname{tr}(XY^{\dagger})
=\tfrac12\sum_{i,j=1}^{2}\bar Y_{ij}X_{ij},
$$

so in the Peirce frame the form is **half** the entrywise Euclidean form: a unit element has entrywise norm $\sqrt2$. In the basis of the four units $e_t,e_x,e_y,e_z$, which is orthonormal for the form, the same space is $\mathbb{C}^4$ with the standard form. The identity was checked on a hundred random pairs with residual below $2\cdot10^{-14}$.

**The two norms.** The definite norm is the Euclidean norm of the coefficient column,

$$
|\tilde Q|^2=\sum_\mu|Q_\mu|^2=|Q_t|^2+|Q_x|^2+|Q_y|^2+|Q_z|^2=\tfrac12\operatorname{tr}(AA^{\dagger}),
$$

and the multiplicative norm is the determinant,

$$
N(\tilde Q)=Q_t^2+Q_x^2+Q_y^2+Q_z^2=\det A .
$$

The first is conjugate-linear in the element and the second is complex-quadratic; the first is positive definite and the second is not. Both are read from the same four entries: the first from the moduli, the second from the squares.

**The inequality.** For every element,

$$
|N(\tilde Q)|\leq|\tilde Q|^2 ,
$$

with equality exactly when $A$ is a scalar multiple of a unitary matrix. In the display this is the inequality $|\det A|\leq\tfrac12\operatorname{tr}(AA^{\dagger})$ for a $2\times2$ matrix, that is the product of the singular values bounded by half the sum of their squares, with equality when they are equal.

**The two norms of the display.** They are the two elementary symmetric functions of the singular values $s_1,s_2$ of $A$:

$$
s_1^2+s_2^2=\operatorname{tr}(AA^{\dagger})=2|\tilde Q|^2,\qquad
s_1s_2=|\det A|=|N(\tilde Q)| .
$$

The pair $(s_1,s_2)$ therefore determines and is determined by the pair $(|\tilde Q|^2,|N(\tilde Q)|)$, and the weights of the element below are exactly $s_1,s_2$.

## The Endomorphisms and Their Adjoints

**The ambient space.** The endomorphisms form $M_4(\mathbb{C})$, of complex dimension sixteen, with the Hilbert–Schmidt form

$$
\langle F,G\rangle=\operatorname{Tr}(F^{\dagger}G).
$$

The form is positive definite, and the adjoint of an operator is the conjugate transpose of its array:

$$
\langle F(X),Y\rangle_{*}=\langle X,F^{\dagger}(Y)\rangle_{*}
\qquad\text{for all }X,Y
\quad\Longleftrightarrow\quad
F^{\dagger}=\bar F^{\mathsf T}.
$$

*Proof.* In coordinates the form on elements is the standard form of $\mathbb{C}^4$, so the adjoint of a linear map is the conjugate transpose of its matrix. Nothing in the algebra enters, and the statement is the elementary one.

**The rank-one endomorphisms.** For elements $\tilde U,\tilde V$ the operator

$$
\mathcal P_{\tilde U,\tilde V}(\tilde X)=\tilde U\langle\tilde X,\tilde V\rangle_{*}
$$

has the array

$$
\mathcal P_{\tilde U,\tilde V}=\tfrac12\,uv^{\mathsf T},
$$

where $u,v$ are the entry columns of $\tilde U,\tilde V$ in the Peirce frame, of entrywise norm $\sqrt2$ when the elements are units. In the basis of the four units the array is $uv^{\mathsf T}$ with $u,v$ of unit norm; the two displays differ by the frame and by nothing else. The transpose and not the dagger appears because the pairing is conjugate-linear in the first slot: the array acts on the conjugate column $\bar x$, and $\tfrac12uv^{\mathsf T}\bar x=\tfrac12\,u\,(v^{\mathsf T}\bar x)$ is the conjugate column of the value. *Proof.* $\langle X,V\rangle_{*}=\tfrac12 x^{\dagger}v$ is a scalar, so the array is $u$ times the row $\tfrac12v^{\mathsf T}$; its singular value is $\tfrac12\cdot\sqrt2\cdot\sqrt2=1$. The residual on a hundred random pairs is exactly $0$.

**The reading.** The rank-one endomorphisms of the algebra are exactly the rank-one matrices of the display. The word *rank-one* is therefore the same word on both sides, and a sum of rank-one endomorphisms is a sum of rank-one matrices with no change of language.

**The swap and the adjoint.** The swap $\sigma$ of the two sides acts on the array by $FM^{\mathsf T}F$ and the adjoint by $M^{\dagger}$. The two agree on the real arrays and differ by the entrywise conjugation elsewhere, which is the matrix form of the distinction between the plain adjoint and the Hermitian adjoint of [Adjoint Pair of $L$ and $R$ Operators in $M_2(\mathbb{C})$](adjoint-pair-of-l-and-r-operators-in-m2c.html).

## The Spectral Theorem

**The statement.** Let $H$ be a Hermitian array, $H^{\dagger}=H$, positive semidefinite in the sense that $x^{\dagger}Hx\geq0$ for every coefficient column $x$. Then there is an orthonormal basis $v_1,\dots,v_4$ of $\mathbb{C}^4$ and real numbers $\lambda_1\geq\dots\geq\lambda_4\geq0$ with

$$
Hv_k=\lambda_kv_k .
$$

**The proof.** The unit sphere of $\mathbb{C}^4$ is compact, so the continuous real function $x\mapsto x^{\dagger}Hx$ attains a maximum $\lambda\geq0$ at some unit vector $v$. Differentiating $t\mapsto(v+ty)^{\dagger}H(v+ty)/\lVert v+ty\rVert^2$ at $t=0$ gives $\operatorname{Re}\langle Hv-\lambda v,y\rangle=0$ for every $y$, and replacing $y$ by $iy$ kills the imaginary part, so $Hv=\lambda v$. The orthogonal complement of $v$ is invariant, because $\langle Hx,v\rangle=\langle x,Hv\rangle=\lambda\langle x,v\rangle=0$, and induction on the dimension gives the basis.

**What the display adds.** Nothing, and that is the point: the abstract proof and the matrix proof are the same four steps, because the form is definite and the carrier is finite-dimensional. The spectral theorem is not a theorem about the algebra; it is the spectral theorem for a Hermitian matrix, applied to the array of $F^{\dagger}F$.

**The square root.** A positive semidefinite array has a unique positive semidefinite square root with the same eigenvectors and the eigenvalues $\sqrt{\lambda_k}$. It commutes with $H$ and its square is $H$. The square root is computed by diagonalising $H$, and no algebra structure enters.

**The kernel.** The kernel is spanned by the eigenvectors of eigenvalue zero, since $x^{\dagger}Hx=\sum_k\lambda_k|\langle x,v_k\rangle|^2$ vanishes only when every component on a positive eigenspace vanishes.

## The Decomposition

**The theorem.** Every array $F\in M_4(\mathbb{C})$ has the form

$$
F=\sum_{k=1}^{4}\rho_k\,u_kv_k^{\dagger},
\qquad
\rho_1\geq\rho_2\geq\rho_3\geq\rho_4\geq0,
$$

with $\{u_k\}$ and $\{v_k\}$ orthonormal bases of $\mathbb{C}^4$. The numbers $\rho_k$ are the **weights**, the $u_k$ the left and the $v_k$ the right singular vectors.

**The proof.** Apply the spectral theorem to $H=F^{\dagger}F$, whose eigenvalues are $\lambda_k=\rho_k^2$ with orthonormal eigenvectors $v_k$. Put $u_k=Fv_k/\rho_k$ when $\rho_k>0$. Then $\langle u_j,u_k\rangle=\langle Fv_j,Fv_k\rangle/\rho_j\rho_k=\lambda_k\delta_{jk}/\rho_j\rho_k=\delta_{jk}$, so the $u_k$ are orthonormal on the positive part, and extending them to a basis gives the display. The identity was checked by reconstruction on twenty random arrays with residual below $2\cdot10^{-14}$.

**The operator form.** In the language of the algebra the same statement is

$$
F=\sum_k\rho_k\,\mathcal P_{\tilde U_k,\tilde V_k},
\qquad
F(\tilde X)=\sum_k\rho_k\,\tilde U_k\langle\tilde X,\tilde V_k\rangle_{*} .
$$

The two displays are one display, because $\mathcal P_{\tilde U,\tilde V}$ has the array $uv^{\mathsf T}$ in the basis of the four units, the transpose appearing because the pairing is conjugate-linear in the first slot.

**The unitary factors.** The decomposition is $F=\mathcal U\Sigma\mathcal V^{\dagger}$ with $\mathcal U,\mathcal V$ unitary arrays and $\Sigma$ the diagonal of the weights. The unitary arrays that come from the algebra are the two regular copies $L_U$ and $R_U$ with $U$ unitary, and their products $L_{U_1}R_{U_2}$; the general unitary array of the display is not of that form, and the difference is treated in [The Length and the Two Ranks at $n=2$](the-length-and-the-two-ranks-at-n-2.html).

**The rank.** The rank is the number of nonzero weights. The rank cases of the source are the rank cases of the array:

| weights | rank | form |
|---|---|---|
| $\rho_1,\rho_2,\rho_3,\rho_4>0$ | $4$ | four terms, invertible |
| $\rho_3=\rho_4=0$ | $2$ | two terms |
| $\rho_2=\rho_3=\rho_4=0$ | $1$ | one rank-one term |
| all zero | $0$ | $F=0$ |

A generic array has four distinct positive weights, because a coincidence of two weights is the vanishing of a discriminant and therefore a closed condition with no interior.

## The Weights of the Multiplication

### The Weights of One Multiplier

**The array.** The left multiplier $L_A$ has the array $\mathrm I_2\otimes A$, and the right multiplier $R_B$ has $B^{\mathsf T}\otimes\mathrm I_2$. Both are Kronecker products with an identity factor, so their weights are the singular values of the non-trivial factor, each repeated twice:

$$
\rho_{2k-1}(L_A)=\rho_{2k}(L_A)=s_k(A),\qquad k=1,2,
$$

and the same display with $s_k(B)$ for $R_B$. The check on twenty random elements gives a residual below $10^{-15}$.

**The two weights of an element.** The two numbers $s_1(A)\geq s_2(A)$ counted once each are the **weights of the element** $\tilde Q$. They carry the two norms and nothing else:

$$
s_1^2+s_2^2=2|\tilde Q|^2,\qquad s_1s_2=|N(\tilde Q)| .
$$

Solving the pair,

$$
s_{1,2}(A)=\sqrt{\ |\tilde Q|^2\pm\sqrt{|\tilde Q|^4-|N(\tilde Q)|^2}\ },
$$

and the radicand is non-negative because the two numbers $s_1^2,s_2^2$ have the sum and the product displayed.

**The three cases.** The singular values say whether the element is invertible, a zero divisor or zero:

| element | weights of the element | weights of $L_A$ | rank |
|---|---|---|---|
| invertible, $\det A\neq0$ | $s_1\geq s_2>0$ | $s_1,s_1,s_2,s_2$ | $4$ |
| zero divisor, $\det A=0$ | $s_1=|\tilde Q|$, $s_2=0$ | $s_1,s_1,0,0$ | $2$ |
| zero | $0,0$ | $0,0,0,0$ | $0$ |

A zero divisor has a positive definite norm and a vanishing determinant, so it is a good singular vector and not an invertible element. The degeneracy of the weights is exactly $\det A=0$, and the invertibility of the element and of its left multiplier are one condition.

**A worked element.** At $\tilde Q=e_t+\vec e_x+i\vec e_y$ the display is
$$
A=\mathrm I_2-i\sigma_1-i(i\sigma_2)=\mathrm I_2-i\sigma_1+\sigma_2
=\begin{pmatrix}1&-2i\\0&1\end{pmatrix},
$$
the two norms are $|\tilde Q|^2=3$ and $N(\tilde Q)=1$, and

$$
s_{1,2}=\sqrt{3\pm\sqrt{9-1}}=\sqrt{3\pm2\sqrt2}\ ,\qquad\text{that is}\qquad s_1=1+\sqrt2,\quad s_2=\sqrt2-1 .
$$

Their squares sum to $6=2\cdot3$ and their product is $1$. The pair of weights is the pair of norms rewritten.

**The equality case.** At $\tilde Q=e_t+2\vec e_x$ the two norms are $|\tilde Q|^2=5$ and $|N(\tilde Q)|=5$, the radicand vanishes and $s_1=s_2=\sqrt5$: the equality of the weights is the equality of the two norms, the condition under which the element is a scalar multiple of a unitary one.

### The Weights of Two Multipliers

**The products.** A two-sided operator has the array $B^{\mathsf T}\otimes A$, and the singular values of a Kronecker product are the pairwise products:

$$
\{\rho_k(L_AR_B)\}=\{s_i(A)s_j(B)\ :\ i,j=1,2\},
$$

ordered decreasingly. The identity follows from
$$
(B^{\mathsf T}\otimes A)^{\dagger}(B^{\mathsf T}\otimes A)
=\overline{B}B^{\mathsf T}\otimes A^{\dagger}A,
$$
a Kronecker product of positive semidefinite matrices, whose eigenvalues are the products of theirs. The check on twenty random pairs gives a residual below $3\cdot10^{-14}$.

**The rank.** The rank of a Kronecker product is the product of the ranks, so

$$
\operatorname{rank}(L_AR_B)=\operatorname{rank}A\cdot\operatorname{rank}B\in\{0,1,2,4\}.
$$

The value $3$ does not occur: a two-sided operator never has rank three. This is the first place where the tensor structure of the display is visible in a numerical invariant.

**The two-sided operator.** For the pair $(A,A^{\dagger})$ the array is $\bar A\otimes A$, whose singular values are $s_i(A)s_j(A)$. The weights are therefore

$$
s_1^2\ \geq\ s_1s_2\ \geq\ s_1s_2\ \geq\ s_2^2 ,
$$

the extremes the squares, the two middle weights equal and their common value the geometric mean of the extremes. The pattern is the mark of a two-sided operator whose second parameter is the star of the first.

**It is not self-adjoint.** The adjoint of $L_AR_{A^{\dagger}}$ is $L_{A^{\dagger}}R_A$, and the two agree only when $A$ is a scalar of modulus one times a Hermitian matrix; in general they differ. The weights are not the eigenvalues. At $A=-i\sigma_1$ the operator $-R_{\vec e_x}L_{\vec e_x}$ has eigenvalues $1,1,-1,-1$ and all four weights equal to one: it is an isometry with a negative eigenvalue, and the weights do not see the sign.

### The Sixteen Basis Operators

**The arrays.** The sixteen arrays $L_{e_\mu}R_{e_\nu}$ are signed permutation matrices in the axis-free frame. A signed permutation array has four nonzero entries, all of modulus one, so its singular values are $1,1,1,1$: every basis operator is an isometry of the coefficient space, whatever the element it multiplies by.

**The orthogonality.** The sixteen are mutually orthogonal for the Frobenius form, of norm two:

$$
\operatorname{Tr}\bigl((L_{e_\mu}R_{e_\nu})^{\dagger}L_{e_{\mu'}}R_{e_{\nu'}}\bigr)=2\,\delta_{\mu\mu'}\delta_{\nu\nu'} .
$$

The check is an integer check on the sixteen arrays, and it gives a diagonal Gram matrix with the constant entry two.

**The coefficient chart.** Every array has a unique expansion $F=\sum c_{\mu\nu}L_{e_\mu}R_{e_\nu}$, and the coefficient array is $c_{\mu\nu}=\tfrac14\operatorname{Tr}((L_{e_\mu}R_{e_\nu})^{\mathsf T}F)$. The chart is a linear isomorphism of $M_4(\mathbb{C})$ onto itself; it is not an isometry, because the basis arrays have norm two and the coefficient space carries the constant factor.

**The multiplicative basis.** The sixteen arrays form a group up to signs: the product of two basis arrays is again a basis array up to a sign, because the left and right copies each form the quaternion group. The group of order thirty-two generated by the two quaternion groups is the extra-special group of order $32$, and its centre is $\pm\mathrm I_4$.

## The Three Identities

**The product is the determinant.**

$$
\rho_1\rho_2\rho_3\rho_4=|\det F| ,
$$

because $\det(F^{\dagger}F)=|\det F|^2$ and the eigenvalues of $F^{\dagger}F$ are the squares of the weights.

**The sum of squares is the norm.**

$$
\rho_1^2+\rho_2^2+\rho_3^2+\rho_4^2=\lVert F\rVert^2=\sum_{\mu=1}^{4}\lVert F(e_\mu)\rVert^2 ,
$$

the Pythagorean theorem for the four orthogonal rank-one terms.

**The largest weight is the operator norm.** For every coefficient column $x$,

$$
\lVert Fx\rVert^2=\sum_k\rho_k^2|\langle x,v_k\rangle|^2\leq\rho_1^2\lVert x\rVert^2 ,
$$

with equality at $x=v_1$. The last weight, when the array is invertible, is the reciprocal of the operator norm of the inverse.

**The inequalities.** The three identities bound the action above, the action of the inverse below and the volume change exactly. They are the three numbers a matrix analysis of the display asks for, and each is a symmetric function of the weights.

## The Geometric Reading and the Truncation

**The ellipsoid.** The image of the unit ball of $\mathbb{C}^4$ is the ellipsoid whose semi-axes are the segments of length $\rho_k$ along $u_k$. The weights are the lengths, the left vectors the directions in the image and the right vectors the directions carried onto them.

**The two unitary factors.** The array is $\mathcal U\Sigma\mathcal V^{\dagger}$: a unitary array, then a scaling of the four coordinates, then a second unitary array. The unitary arrays are the isometries of the coefficient form; the two-sided ones among them are $L_{U_1}R_{U_2}$ with $U_1,U_2$ unitary, and the weights are the only part of the decomposition that is not a symmetry of the form.

**The truncation.** For $k<4$ put $F_k=\sum_{j\leq k}\rho_ju_jv_j^{\dagger}$. Then

$$
\lVert F-F_k\rVert^2=\sum_{j>k}\rho_j^2 ,
$$

and no array of rank at most $k$ is closer: for every $G$ of rank at most $k$,
$$
\lVert F-G\rVert\geq\lVert F-F_k\rVert .
$$

This is the Eckart–Young theorem, and it is the matrix form of the source's truncation. The proof is the observation that a rank-$k$ array agrees with $F$ on a subspace of dimension at least $4-k$ and therefore sees at least one of the discarded directions.

**The non-uniqueness.** The weights are unique; the singular vectors are not. A simple weight allows a phase, a repeated weight allows a unitary mixing inside its eigenspace. The array $F$ determines the four weights and the two subspaces, not the pair of bases.

## What the Decomposition Is Not

**Not a decomposition of the algebra.** The four terms are operators, not elements, and the weights are not elements of $\mathbb{B}$. A sum of rank-one operators is a statement about $M_4(\mathbb{C})$, and the algebra enters only through the identification of the rank-one operators with the pairs of elements.

**Not an eigenvalue decomposition.** The weights of $L_A$ are the singular values of $A$, not its eigenvalues. For a non-normal $A$ the two differ, and the difference is the whole content of the polar decomposition. At $A=\begin{pmatrix}0&2\\0&0\end{pmatrix}$ the eigenvalues are $0,0$ and the singular values are $2,0$: the operator has rank one and is nilpotent, and the weights see the rank and not the nilpotency.

**Not a canonical sum.** The terms depend on the choice of the singular bases and on the ordering of equal weights. Only the multiset of weights and the two singular subspaces are intrinsic.

**Not a statement about the multiplication.** The decomposition uses the Hilbert–Schmidt form and the array, and it holds for every endomorphism of every finite-dimensional complex space with a definite form. What the algebra adds is the identification of the rank-one operators with the pairs $(\tilde U,\tilde V)$ and the interpretation of the weights of a multiplier as the singular values of the element.

## Where $n=2$ Differs

**The number of terms.** The carrier is four-dimensional, so the sum has four terms and the weights are four numbers. The rank can be $0,1,2,4$ for a two-sided operator and any value $0$ to $4$ for a general endomorphism; at order $n$ the sum has $n^2$ terms.

**The two weights of an element.** An element has two weights because the display is $2\times2$, and each appears twice in the operator because the left copy doubles it. At order $n$ an element has $n$ weights each appearing $n$ times.

**The discriminant.** The weights of an element are determined by two numbers, $|\tilde Q|^2$ and $|N(\tilde Q)|$, and the formula for them is the quadratic formula. At a higher order the weights are the roots of a polynomial of degree $n$ and there is no closed formula.

**Nothing else differs.** The spectral theorem, the decomposition, the three identities and the truncation are statements about a finite-dimensional complex space with a definite form, and they are the same statements at every order.

## Summary

The Hilbert–Schmidt form of the algebra is $\tfrac12\operatorname{tr}(XY^{\dagger})$, which on coefficient columns is the standard form of $\mathbb{C}^4$, and the rank-one endomorphism $\mathcal P_{\tilde U,\tilde V}$ has the array $uv^{\mathsf T}$. The SVD of an endomorphism is therefore the SVD of its $4\times4$ array: $F=\sum_k\rho_ku_kv_k^{\dagger}$, with the weights the singular values, the left and right singular vectors the coordinate columns.

The three identities hold: the product of the weights is $|\det F|$, the sum of their squares is the Frobenius norm and also $\sum_\mu\lVert F(e_\mu)\rVert^2$, and the largest weight is the operator norm. A left multiplier has the weights $s_1,s_1,s_2,s_2$ of its element, a two-sided operator has the pairwise products and its rank is the product of the two ranks, and the two-sided operator $L_AR_{A^{\dagger}}$ has the geometric pattern $s_1^2,s_1s_2,s_1s_2,s_2^2$.

The sixteen basis operators are signed permutations of weight $1,1,1,1$, orthogonal of norm two. The truncation is the Eckart–Young theorem, the weights are unique and the singular vectors are not, and the weights of a multiplier are singular values and not eigenvalues.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle X,Y\rangle_{*}=\tfrac12\operatorname{tr}(XY^{\dagger})$ | the Hilbert–Schmidt form on elements |
| $\langle F,G\rangle=\operatorname{Tr}(F^{\dagger}G)$ | the Frobenius form on operators |
| $\mathcal P_{\tilde U,\tilde V}$ | the rank-one operator $X\mapsto\tilde U\langle X,\tilde V\rangle_{*}$ |
| $uv^{\mathsf T}$ | the array of $\mathcal P_{\tilde U,\tilde V}$ |
| $\rho_k$ | the weights, the singular values of the array |
| $s_1(A),s_2(A)$ | the singular values of the element |
| $|\tilde Q|^2$ | the definite norm, $\sum_\mu|Q_\mu|^2$ |
| $N(\tilde Q)=\det A$ | the multiplicative norm |
| $L_A,R_B$ | the one-sided multipliers, arrays $\mathrm I_2\otimes A$ and $B^{\mathsf T}\otimes\mathrm I_2$ |

## Further Reading

- [The SVD Decomposition of Endomorphisms of the Biquaternion Algebra](the-svd-decomposition-of-endomorphisms-of-the-biquaternion-algebra.html), for the source theorem, the spectral theorem and the weights of a multiplier.
- [The Adjoints and the Polar Decomposition of an Operator at $n=2$](the-adjoints-and-the-polar-decomposition-of-an-operator-at-n-2.html), for the polar decomposition that the SVD implies.
- [The Length and the Two Ranks at $n=2$](the-length-and-the-two-ranks-at-n-2.html), for the rank of a two-sided operator and the length of an endomorphism.
- [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html), for the one-sided arrays and their singular values.
- [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), for the cone of products and the rank-one coefficient arrays.
- [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html), for the display in which the arrays are written.
