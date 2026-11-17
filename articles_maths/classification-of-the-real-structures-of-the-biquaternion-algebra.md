# __Classification of the Real Structures of the Biquaternion Algebra, including Lie Algebras and Lie Groups__

## Introduction and Scope

The companion article *Classification of the Structures of the Biquaternion Algebra* classifies the structures that change the ground field: it proves that the complex algebra $\mathbb{B}=M_2(\mathbb{C})$ has exactly two real forms, states the two real structures, and computes their fixed sets. It stops there. The fixed sets are algebras, and each of them carries three different structures at once: the associative product, the commutator bracket, and the symmetrized product. This article develops the three layers in full for the two real forms, and it adds the group layer that the algebras determine.

The two real forms are the **split** form, which is the algebra $M_2(\mathbb{R})$ of the real $2\times2$ matrices, and the **compact** form, which is the division algebra $\mathbb{H}$ of the quaternions. Both live inside one algebra, and both are computed in one coordinate system. In the corpus coordinates fixed below, the split form is

$$
\mathbb{B}^{\sigma_{\mathrm{split}}}=\operatorname{span}_{\mathbb{R}}\{e_t,\ \vec e_y,\ i\vec e_x,\ i\vec e_z\}\cong M_2(\mathbb{R}),
$$

and the compact form is

$$
\mathbb{B}^{\sigma_{\mathrm{comp}}}=\mathbb{B}_H=\operatorname{span}_{\mathbb{R}}\{e_t,\ \vec e_x,\ \vec e_y,\ \vec e_z\}\cong\mathbb{H}.
$$

The first four elements are the matrices $I$, $J$, $\sigma_1$ and $\sigma_3$ of the Pauli dictionary, and the second four are the quaternion base. Every computation below is performed on these two lists of four elements.

**Scope.** This article develops the full structure of the two real forms of $\mathbb{B}$: their associative, Lie and Jordan subalgebras, their Killing forms and signatures, their involutions and intersections with the six subspaces, and the Lie groups attached to each Lie subalgebra. It recaps the classification from the companion article without reproving it; it cites [The Lie Correspondence and the Adjoint Representation](the-lie-correspondence-and-the-adjoint-representation.html) for the general theory of covers and central quotients; and it does not treat the complex form of $\mathbb{B}_{\mathbb{R}}$ or the operator level.

The order is as follows. The next section recaps the two real structures and fixes the coordinates. The third, fourth and fifth sections treat the associative, Lie and Jordan layers of the split form; the sixth, seventh and eighth sections treat the same three layers of the compact form. The ninth section computes the involutions inside each form and the intersections with the six subspaces. The tenth section gives the Lie groups attached to each Lie subalgebra, in two tables, with the centre, the discrete central subgroups and the fundamental group of each quotient. The eleventh section compares the two forms; the twelfth states what the lattices and the groups do not determine; the thirteenth hands off.

## The Two Real Structures and Their Fixed Sets

**The two maps.** A real structure on the complex algebra $\mathbb{B}$ is a conjugate-linear multiplicative involution, and the two that exist are

$$
\sigma_{\mathrm{comp}}(\tilde Q)=\overline{Q_t}e_t+\overline{Q_x}\vec e_x+\overline{Q_y}\vec e_y+\overline{Q_z}\vec e_z ,
$$

the coefficient conjugation, whose fixed set is the quaternion subspace, and

$$
\sigma_{\mathrm{split}}(\tilde Q)=\vec e_y\,\sigma_{\mathrm{comp}}(\tilde Q)\,\vec e_y^{-1}=-\vec e_y\,\overline{\tilde Q}\,\vec e_y ,
$$

the inner twist of the coefficient conjugation by the unit $\vec e_y$, whose fixed set is the real matrices. The names record the analysis: the compact form is the division algebra and its group is compact, and the split form is the matrix algebra and its group is not. The definitions, the proof that the fixed sets are as stated, and the proof that these are the only two real forms up to isomorphism are in [Classification of the Structures of the Biquaternion Algebra](classification-of-the-structures-of-the-biquaternion-algebra.html).

**Warning (the naming is not the obvious one).** The word real in the two names does not refer to real coefficients. The elements with real coefficients are $\mathbb{B}_H$, they form the division algebra, and they are the compact form; the split form is the twist, and its elements include $i\vec e_x$ and $i\vec e_z$ and exclude $\vec e_x$ and $\vec e_z$. The witness that separates the two is the idempotent $\tfrac12(e_t+i\vec e_x)$, which lies in the split form and is a zero divisor, and which has no counterpart in the division algebra.

**The master table.** The two forms are recorded once, and referred to throughout.

| form | subspace of $\mathbb{B}$ | dimension over $\mathbb{R}$ | isomorphic to | division |
|---|---|---|---|---|
| split | $\operatorname{span}_{\mathbb{R}}\{e_t,\vec e_y,i\vec e_x,i\vec e_z\}$ | $4$ | $M_2(\mathbb{R})$ | no |
| compact | $\operatorname{span}_{\mathbb{R}}\{e_t,\vec e_x,\vec e_y,\vec e_z\}$ | $4$ | $\mathbb{H}$ | yes |

**The split form in matrices.** Under the dictionary $e_t\mapsto I_2$, $\vec e_x\mapsto-i\sigma_1$, $\vec e_y\mapsto-i\sigma_2$, $\vec e_z\mapsto-i\sigma_3$ of [$M_2(\mathbb{C})$ Pauli Representation](m2c-pauli-representation.html), the four elements of the split form become

$$
e_t\mapsto I=\begin{pmatrix}1&0\\0&1\end{pmatrix},\quad
\vec e_y\mapsto J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
i\vec e_x\mapsto \sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
i\vec e_z\mapsto \sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
$$

which are four real matrices and a real basis of $M_2(\mathbb{R})$. Their products are

$$
J^2=-I,\qquad \sigma_1^2=\sigma_3^2=I,\qquad J\sigma_1=-\sigma_3,\qquad \sigma_1 J=\sigma_3,\qquad \sigma_1\sigma_3=J,\qquad \sigma_3 J=-\sigma_1 ,
$$

and they are read off from the multiplication of the vector units: $\vec e_y^2=-e_t$ gives $J^2=-I$, and $\vec e_y(i\vec e_x)=i\vec e_y\vec e_x=-i\vec e_z$ gives $J\sigma_1=-\sigma_3$. The signs are the whole content of the split case: one of the three square roots of $-I$ in the compact form becomes a square root of $+I$, and the algebra stops being a division algebra.

**The split form in corpus coordinates.** The same information, without matrices:

$$
e_y^2=-e_t,\qquad (i\vec e_x)^2=e_t,\qquad (i\vec e_z)^2=e_t,\qquad e_y(i\vec e_x)=-i\vec e_z,\qquad (i\vec e_x)(i\vec e_z)=e_y .
$$

Three elements of the traceless part have squares $-e_t$, $+e_t$, $+e_t$, and the signature $(2,1)$ of the trace form on the traceless part is visible in these three signs. This is why the Lie algebra of the split form has signature $(2,1)$ and the Lie algebra of the compact form has signature $(3,0)$; the computation is in the fourth and seventh sections.

**The compact form in corpus coordinates.** The four elements $e_t,\vec e_x,\vec e_y,\vec e_z$ satisfy

$$
\vec e_x^{\,2}=\vec e_y^{\,2}=\vec e_z^{\,2}=-e_t,\qquad \vec e_x\vec e_y=\vec e_z,\quad \vec e_y\vec e_z=\vec e_x,\quad \vec e_z\vec e_x=\vec e_y ,
$$

which is the quaternion table of [Introduction to the Algebra of Biquaternions](the-biquaternion-algebra.html). Every nonzero element is invertible, with inverse $\tilde q^{-1}=\tilde q^{\natural}/(\tilde q\tilde q^{\natural})$ and $\tilde q\tilde q^{\natural}$ a positive real multiple of $e_t$.

**What this article adds.** Three layers and one group layer.

| layer | operation | of the split form | of the compact form |
|---|---|---|---|
| associative | $\tilde X\tilde Y$ | $M_2(\mathbb{R})$ | $\mathbb{H}$ |
| Lie | $[\tilde X,\tilde Y]=\tilde X\tilde Y-\tilde Y\tilde X$ | $\mathfrak{gl}(2,\mathbb{R})$ | $\mathfrak u(2)$ |
| Jordan | $\tilde X\circ\tilde Y=\tfrac12(\tilde X\tilde Y+\tilde Y\tilde X)$ | $M_2(\mathbb{R})^{+}$ | $\mathbb{H}^{+}$ |
| group | the exponential of each Lie subalgebra | subgroups of $GL(2,\mathbb{R})$ and their quotients | subgroups of $U(2)$ and their quotients |

The four rows are different structures on the same set. A subalgebra in one row is not a subalgebra in another, a classification in one row does not translate to another, and the article keeps the rows apart for that reason.

## Associative Subalgebras of the Split Form

**The centre and the ideals.** The centre of $M_2(\mathbb{R})$ is the scalar line $\mathbb{R}I$, and $M_2(\mathbb{R})$ is central simple: it has no two-sided ideal other than $0$ and itself. Both statements are the real case of the corresponding statements for $M_2(\mathbb{C})$, and the second follows from the first by the density argument used below. In corpus coordinates the centre is $\mathbb{R}e_t$.

**Theorem (unital subalgebras up to conjugacy).** Let $A\subset M_2(\mathbb{R})$ be a subalgebra containing $I$. Then exactly one of the following holds, up to conjugation by $GL(2,\mathbb{R})$:

1. $A=\mathbb{R}I$, of dimension $1$;
2. $A=\mathbb{R}I\oplus\mathbb{R}P$ with $P$ a projection of rank one, of dimension $2$, isomorphic to $\mathbb{R}\oplus\mathbb{R}$;
3. $A=\mathbb{R}I\oplus\mathbb{R}J'$ with $J'^2=-I$, of dimension $2$, isomorphic to $\mathbb{C}$;
4. $A=\mathbb{R}I\oplus\mathbb{R}N$ with $N^2=0$ and $N\neq0$, of dimension $2$, the algebra of dual numbers;
5. $A=\mathfrak{b}=\{X:X(L)\subset L\}$ for a line $L\subset\mathbb{R}^2$, of dimension $3$, the parabolic subalgebra;
6. $A=M_2(\mathbb{R})$, of dimension $4$.

*Proof.* A unital subalgebra has dimension at most $4$, and the cases of dimension $1$, $3$ and $4$ are settled first.

Dimension $1$: $A$ contains $I$, so $A=\mathbb{R}I$.

Dimension $3$: $A$ acts on $\mathbb{R}^2$. If $\mathbb{R}^2$ were a simple $A$-module, then $A$ would act densely on it and would be dense in the endomorphism algebra of the module, that is in $M_2(\mathbb{R})$, which no three-dimensional subspace is. So there is a line $L$ with $A(L)\subset L$, hence $A$ is contained in the parabolic $\mathfrak{b}$ of the line $L$, which has dimension $3$; since $A$ also has dimension $3$, $A=\mathfrak{b}$. All lines are conjugate under $GL(2,\mathbb{R})$, so all parabolics are conjugate, and this is one case and not two.

Dimension $2$: choose $X\in A$ with $X\notin\mathbb{R}I$. Then $A=\mathbb{R}I\oplus\mathbb{R}X$, because both sides have dimension $2$ and the right side is contained in the left. Since $X^2$ lies in $A$, there are real $a,b$ with $X^2=aX+bI$, and the three cases are the three possible discriminants. If the discriminant $a^2+4b$ is positive, $X$ has two distinct real eigenvalues, $X$ is diagonalizable over $\mathbb{R}$, and $A$ is conjugate to the diagonal algebra $\mathbb{R}I\oplus\mathbb{R}P$ with $P$ a projection. If the discriminant is negative, $X$ has a conjugate pair of non-real eigenvalues, and $X$ is conjugate to a complex structure $J'$ with $J'^2=-I$, so $A\cong\mathbb{C}$. If the discriminant vanishes, $X^2=aX-\tfrac{a^2}{4}I$, the element $N=X-\tfrac{a}{2}I$ satisfies $N^2=0$, and $N\neq0$ because $X\notin\mathbb{R}I$; then $A=\mathbb{R}I\oplus\mathbb{R}N$. The three cases are exclusive and each is a single conjugacy class, because two projections of rank one, two complex structures, and two nonzero nilpotents are each conjugate under $GL(2,\mathbb{R})$. ∎

**The continuous families.** The classification has six entries and is finite, but three of the entries are not single subalgebras: they are continuous families, and the families must be counted as part of the answer. The set of complex structures

$$
\mathcal{J}=\{J'\in M_2(\mathbb{R}):J'^2=-I\}
$$

is traced by a traceless matrix $J'=\begin{pmatrix}a&b\\c&-a\end{pmatrix}$ with $a^2+bc=-1$, which is a two-sheeted hyperboloid in the three-dimensional space of traceless matrices; each sheet is a hyperbolic plane. Passing from $J'$ to $-J'$ does not change the subalgebra $\mathbb{R}I\oplus\mathbb{R}J'$, so the family of copies of $\mathbb{C}$ is two-dimensional. The set of projections of rank one is also two-dimensional, and the set of lines $\mathbb{R}N$ spanned by a nonzero nilpotent is a circle. So the answer to the classification question is: six types, three of them continuous families of dimensions two, two and one.

**Warning (the lattice is not finite).** The subalgebra lattice of $M_2(\mathbb{R})$ is not finite: the copies of $\mathbb{C}$ form a continuous family, and so do the projections and the nilpotent lines. A classification here means a classification of types up to conjugacy, with the continuous parameters identified. The corresponding statement for the compact form, in the sixth section, is the opposite one, and the contrast is the point of the comparison in the eleventh section.

**The parabolics in corpus coordinates.** The parabolic of the line spanned by the first basis vector is the algebra of upper triangular matrices, which in the four elements of the split form is

$$
\mathfrak{b}=\operatorname{span}_{\mathbb{R}}\{e_t,\ i\vec e_z,\ N\},\qquad N=\tfrac12(i\vec e_x-\vec e_y),
$$

and the verification is a product: $(i\vec e_z)N=\tfrac12\big((i\vec e_z)(i\vec e_x)-(i\vec e_z)\vec e_y\big)=\tfrac12(\vec e_y-(-i\vec e_x))=N$, and $N^2=\tfrac14\big((i\vec e_x)^2-(i\vec e_x)\vec e_y-\vec e_y(i\vec e_x)+\vec e_y^{\,2}\big)=\tfrac14(e_t-i\vec e_z+i\vec e_z-e_t)=0$. The element $i\vec e_z$ is the diagonal matrix $\sigma_3$, and $N$ is the elementary matrix $E_{12}$, so $\mathfrak{b}$ is the algebra of the matrices $\begin{pmatrix}a&b\\0&d\end{pmatrix}$ written in the corpus base.

**Non-unital subalgebras.** Without the unit the lattice is larger and is not classified here; three examples fix the shape of it.

- $\mathbb{R}N$ for a nonzero nilpotent: one-dimensional, with $N^2=0$.
- $\operatorname{span}_{\mathbb{R}}\{E_{11},E_{12}\}$, the matrices $\begin{pmatrix}a&b\\0&0\end{pmatrix}$: two-dimensional, and it contains no unit, since every element has zero determinant.
- $\operatorname{span}_{\mathbb{R}}\{E_{11},E_{22}\}$: two-dimensional, abelian, and it is the diagonal algebra of the previous list, which does contain the unit.

The second example shows that the unital hypothesis is doing work: it excludes algebras whose elements are all singular, and those are exactly the algebras that a rank-one projection and a nilpotent generate.

## Lie Subalgebras of the Split Form

**The Lie algebra.** The commutator turns $M_2(\mathbb{R})$ into the real Lie algebra $\mathfrak{gl}(2,\mathbb{R})$, of dimension $4$, with centre $\mathbb{R}I$ and derived algebra $\mathfrak{sl}(2,\mathbb{R})$, the traceless part, of dimension $3$. In corpus coordinates

$$
\mathfrak{sl}(2,\mathbb{R})=\operatorname{span}_{\mathbb{R}}\{i\vec e_x,\ \vec e_y,\ i\vec e_z\},
$$

and the brackets are

$$
[i\vec e_x,\vec e_y]=-2i\vec e_z,\qquad [\vec e_y,i\vec e_z]=2i\vec e_x,\qquad [i\vec e_z,i\vec e_x]=2\vec e_y .
$$

The signs differ from the quaternion brackets of the vector part by the factor $i$ absorbed into two of the three generators, and that factor is the difference between $\mathfrak{sl}(2,\mathbb{R})$ and $\mathfrak{su}(2)$.

**Theorem (subalgebras of $\mathfrak{sl}(2,\mathbb{R})$).** Up to conjugation by $GL(2,\mathbb{R})$, the subalgebras of $\mathfrak{sl}(2,\mathbb{R})$ are:

1. $0$;
2. the elliptic line $\mathbb{R}J'$ with $J'^2=-I$, compact, one conjugacy class;
3. the hyperbolic line $\mathbb{R}H'$ with $H'$ semisimple with two distinct real eigenvalues and zero trace, one conjugacy class;
4. the parabolic line $\mathbb{R}N$ with $N\neq0$ and $N^2=0$, one conjugacy class;
5. the Borel subalgebra $\mathfrak{b}_0=\operatorname{span}_{\mathbb{R}}\{H',N\}$ with $[H',N]=N$, solvable and non-abelian, of dimension $2$, one conjugacy class;
6. $\mathfrak{sl}(2,\mathbb{R})$.

*Proof.* The dimension is at most $3$. A nonzero element of $\mathfrak{sl}(2,\mathbb{R})$ is elliptic, hyperbolic or nilpotent according as its eigenvalues are $\pm i\lambda$, $\pm\lambda$ with $\lambda\neq0$, or $0,0$ with the element nonzero. Within each type the elements are conjugate: an elliptic element is conjugate to $\lambda J$, a hyperbolic one to $\lambda\sigma_3$, and a nilpotent one to $\lambda N$, and the scalar is removed by conjugating with a diagonal matrix of determinant one. Hence the three one-dimensional cases, and each is a single class.

A two-dimensional subalgebra $\mathfrak{a}$ cannot be abelian. For let $X\in\mathfrak{a}$ be nonzero. If $X$ is elliptic its centralizer is $\mathbb{R}J'$, of dimension $1$, so $\mathfrak{a}$ would have dimension $1$. If $X$ is hyperbolic its centralizer is $\mathbb{R}H'$, again of dimension $1$. If every nonzero element of $\mathfrak{a}$ were nilpotent, then $\mathfrak{a}$ would be a two-dimensional subspace of the nilpotent cone, which is a cone and contains no plane. So $\mathfrak{a}$ contains a hyperbolic element $H'$ and an element $Y$ not proportional to it, and $H'$ and $Y$ span $\mathfrak{a}$. The centralizer of $H'$ in $\mathfrak{sl}(2,\mathbb{R})$ is the line $\mathbb{R}H'$, and that alone does not give $[H',Y]\in\mathbb{R}Y$: the bracket could carry a component along $H'$, and the component has to be removed. The removal uses the eigenspace decomposition. If $H'$ has eigenvalues $\pm\lambda$ then $\operatorname{ad}_{H'}$ has eigenvalues $0,\pm2\lambda$ on $\mathfrak{sl}(2,\mathbb{R})$, the $0$ eigenspace is $\mathbb{R}H'$, and the two remaining eigenspaces are lines. Write $Y=Y_{+}+Y_{-}+cH'$ with $[H',Y_{\pm}]=\pm2\lambda\,Y_{\pm}$. Then $[H',Y]=2\lambda(Y_{+}-Y_{-})$ lies in $\mathfrak{a}=\operatorname{span}\{H',Y\}$, so $Y_{+}-Y_{-}=\alpha H'+\beta(Y_{+}+Y_{-})$ for some real $\alpha,\beta$; the three eigencomponents lie in three distinct eigenspaces, so comparing them gives $\alpha=0$ and $\beta=1$ from the $+$ part against $\beta=-1$ from the $-$ part, which forces one of $Y_{+},Y_{-}$ to vanish. Hence $[H',Y]=\pm2\lambda\,Y$ after replacing $Y$ by its nonzero eigencomponent, and the eigencomponent is still outside $\mathbb{R}H'$. Rescaling $Y$ gives $N$ with $[H',N]=N$; rescaling $H'$ then gives it eigenvalues $\pm\tfrac12$, and $N$ is a nilpotent eigenvector, so $\mathfrak{a}=\operatorname{span}_{\mathbb{R}}\{H',N\}$ with $H'$ conjugate to $\sigma_3$ and $N$ to $E_{12}$. This is the Borel, one class. ∎

**How the centre extends the list.** The decomposition $\mathfrak{gl}(2,\mathbb{R})=\mathfrak{sl}(2,\mathbb{R})\oplus\mathbb{R}I$ is a direct sum of Lie algebras, and it organises the subalgebras of the full algebra. One notation is fixed here and used below: $\mathfrak{b}_0$ is the two-dimensional Borel of $\mathfrak{sl}(2,\mathbb{R})$, and $\mathfrak{b}$ is the three-dimensional Borel of $\mathfrak{gl}(2,\mathbb{R})$, the one of case 2 above with $\mathfrak{k}=\mathfrak{b}_0$.

**Proposition.** Let $\mathfrak{a}\subset\mathfrak{gl}(2,\mathbb{R})$ be a Lie subalgebra and let $\pi$ be the projection onto $\mathfrak{sl}(2,\mathbb{R})$ along $\mathbb{R}I$. Then exactly one of the following holds.

1. $\mathfrak{a}\subset\mathfrak{sl}(2,\mathbb{R})$, and $\mathfrak{a}$ is one of the six entries of the theorem.
2. $\mathfrak{a}\supset\mathbb{R}I$, and then $\mathfrak{a}=\mathbb{R}I\oplus\mathfrak{k}$ with $\mathfrak{k}=\mathfrak{a}\cap\mathfrak{sl}(2,\mathbb{R})$ one of the six entries.
3. $\mathfrak{a}\cap\mathbb{R}I=0$ and $\mathfrak{a}\not\subset\mathfrak{sl}(2,\mathbb{R})$, and then $\mathfrak{a}$ is the graph of a linear map $\lambda:\mathfrak{k}\to\mathbb{R}$ with $\lambda([\mathfrak{k},\mathfrak{k}])=0$, where $\mathfrak{k}=\pi(\mathfrak{a})$ is one of the six entries.

*Proof.* Cases 1 and 2 are immediate from the direct sum: if $\mathfrak{a}$ contains $I$ and $X$, it contains $X-\tfrac12(\operatorname{tr}X)I$, so $\mathfrak{a}=\mathbb{R}I\oplus(\mathfrak{a}\cap\mathfrak{sl}(2,\mathbb{R}))$. In case 3, $\pi$ is injective on $\mathfrak{a}$, so $\mathfrak{a}$ is the graph $\{X+\lambda(X)I:X\in\mathfrak{k}\}$ for a linear $\lambda$, and the bracket of two such elements is $[X,Y]$, which must again lie in the graph; hence $\lambda([X,Y])=0$ for all $X,Y\in\mathfrak{k}$. ∎

Two consequences. First, there is no subalgebra of dimension $3$ in case 3: for $\mathfrak{k}=\mathfrak{sl}(2,\mathbb{R})$ the derived algebra is all of $\mathfrak{k}$, so $\lambda=0$ and $\mathfrak{a}=\mathfrak{sl}(2,\mathbb{R})$ falls in case 1. Second, for $\mathfrak{k}$ the Borel $\mathfrak{b}_0$, with $[\mathfrak{b}_0,\mathfrak{b}_0]=\mathbb{R}N$, a functional vanishing on $N$ is free on $H'$, and the family

$$
\mathfrak{a}_c=\operatorname{span}_{\mathbb{R}}\{H'+cI,\ N\},\qquad c\in\mathbb{R},
$$

is a one-parameter family of two-dimensional subalgebras, of which $c=0$ gives $\mathfrak{b}_0$, the Borel of $\mathfrak{sl}(2,\mathbb{R})$, and $c\neq0$ the transverse ones: distinct $c$ give distinct classes, because conjugation preserves the trace functional and the trace of $H'+cI$ is $2c$.

**The one-dimensional subalgebras.** Every one-dimensional subalgebra of $\mathfrak{gl}(2,\mathbb{R})$ is $\mathbb{R}X$ for some $X\neq0$, and two such lines are conjugate exactly when $X$ and $X'$ are conjugate up to a scalar. The types are therefore the projective classes of matrices:

| type of $X$ | model | parameter |
|---|---|---|
| scalar | $I$ | none |
| split, distinct eigenvalues | $\operatorname{diag}(1,t)$ | $t\in\mathbb{P}^1(\mathbb{R})\setminus\{1\}$, up to $t\leftrightarrow 1/t$ |
| complex eigenvalues | $aI'+bJ'$, $b\neq0$ | $a/b\in\mathbb{R}$ |
| nonzero nilpotent | $N$ | none |
| Jordan block | $I+\mu N$, $\mu\neq0$ | $\mu\in\mathbb{R}^{\times}$ |

The five rows are the five projective Jordan types, and three of them carry a continuous parameter. This is the reason the Lie lattice is larger than the associative one: a one-dimensional subspace of a four-dimensional space is a point of $\mathbb{P}^3(\mathbb{R})$, and the condition of being a subalgebra of a non-abelian algebra is vacuous in dimension one, so all of $\mathbb{P}^3(\mathbb{R})$ survives and the classification is by conjugacy alone.

**The Killing form.** For $\mathfrak{gl}(2,\mathbb{R})$ the Killing form is

$$
K(X,Y)=4\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y),
$$

which is the restriction of the form of $\mathfrak{gl}(2,\mathbb{C})$ to a real form. Its values on the standard lists are collected in one table; the signatures are computed in the algebra itself, not in the ambient $\mathbb{B}_{\mathbb{R}}$.

| algebra | dimension | $K$ | signature | radical |
|---|---|---|---|---|
| $\mathfrak{sl}(2,\mathbb{R})$ | $3$ | $4\operatorname{tr}(XY)$ | $(2,1)$ | $0$ |
| Borel $\mathfrak{b}=\mathbb{R}I\oplus\mathfrak{b}_0$ | $3$ | as restricted, rank $1$ | $(1,0)$ | $\operatorname{span}\{e_t,N\}$ |
| Cartan $\mathfrak{h}$ | $2$ | $0$ | $(0)$ | the algebra |
| $\mathfrak{so}(2)$ | $1$ | $0$ | $(0)$ | the algebra |
| $\mathfrak{gl}(2,\mathbb{R})$ | $4$ | $4\operatorname{tr}(XY)-2\operatorname{tr}X\operatorname{tr}Y$ | $(2,1)$ with a null line | $\mathbb{R}I$ |

The three entries of the third row are worth a comment each. On $\mathfrak{sl}(2,\mathbb{R})$ the form is nondegenerate by simplicity, and its signature $(2,1)$ is computed on the basis $i\vec e_x,\vec e_y,i\vec e_z$, where the values are $8,-8,8$. On the Borel the form is degenerate: the algebra is solvable, so $K$ vanishes on the derived algebra, and the radical is the two-dimensional space spanned by $I$ and the nilpotent. On the abelian algebras the form is identically zero, which is the general fact that a solvable algebra has $K(\mathfrak{g},[\mathfrak{g},\mathfrak{g}])=0$ pushed to its extreme. The two nondegenerate rows are the semisimple content, and the degenerate rows carry no information beyond the dimension.

**Remark (the biquaternion reading of the signature).** In the basis $i\vec e_x,\ \vec e_y,\ i\vec e_z$ of $\mathfrak{sl}(2,\mathbb{R})$ the signature is read off the star. Two of the three generators are Hermitian, $i\vec e_x$ and $i\vec e_z$, and one is anti-Hermitian, $\vec e_y$, because $(i\vec e_k)^{*}=+i\vec e_k$ and $\vec e_k^{*}=-\vec e_k$. The Killing form takes the value $+8$ on the two Hermitian ones and $-8$ on the anti-Hermitian one, so the signature $(2,1)$ is the count of Hermitian and anti-Hermitian directions. The split real form is exactly the real form of $\mathfrak{sl}(2,\mathbb{C})$ in which the star fixes two of the three generators; in the compact form it fixes none, and the signature is $(0,3)$. The difference between the two rows of the table is a difference between two counts, and not a difference of computation.

**Remark (a difference of convention).** The numbers above are the intrinsic Killing forms, computed with the trace taken in the algebra itself. The companion article records the signature of the same form computed with the trace taken in the eight-dimensional ambient algebra $\mathbb{B}_{\mathbb{R}}$, and the two conventions agree on signatures for $\mathfrak{sl}(2,\mathbb{R})$, $\mathfrak{su}(2)$ and $\mathfrak{so}(3,1)$ and differ on the abelian algebras, where the intrinsic form vanishes and the ambient restriction does not. The convention of this article is the intrinsic one, because the groups of the tenth section are attached to the algebras and not to the ambient space.

**The ideals.** The two-sided ideals of the Lie algebra $\mathfrak{gl}(2,\mathbb{R})$ are $0$, $\mathbb{R}I$, $\mathfrak{sl}(2,\mathbb{R})$ and the whole algebra. For $\mathfrak{sl}(2,\mathbb{R})$ is simple, so an ideal $\mathfrak{j}$ not contained in $\mathbb{R}I$ projects onto $\mathfrak{sl}(2,\mathbb{R})$, and then $\mathfrak{j}$ contains $[\mathfrak{gl},\mathfrak{j}]=[\mathfrak{sl},\mathfrak{sl}]=\mathfrak{sl}$ and is either $\mathfrak{sl}$ or $\mathfrak{gl}$; and an ideal contained in the centre is $0$ or $\mathbb{R}I$. The same list is the list of ideals of the associative algebra, with $\mathfrak{sl}(2,\mathbb{R})$ excluded, since the traceless part is not closed under multiplication; the two lists are different and must not be identified.

**Warning (a Lie subalgebra is not an associative subalgebra).** The traceless part $\mathfrak{sl}(2,\mathbb{R})$ is a Lie subalgebra and not an associative subalgebra: the product of two traceless matrices has trace $\operatorname{tr}(XY)$, which is generally nonzero, as the product $(i\vec e_x)(i\vec e_z)=e_y$ shows. In the other direction the diagonal algebra $\mathbb{R}I\oplus\mathbb{R}\sigma_3$ is an associative subalgebra and an abelian Lie subalgebra. The two lattices share elements and are not the same lattice, and every statement below names the layer it belongs to.

## Jordan Subalgebras of the Split Form

**The Jordan product.** On $M_2(\mathbb{R})$ the symmetrized product

$$
\tilde X\circ\tilde Y=\tfrac12\big(\tilde X\tilde Y+\tilde Y\tilde X\big)
$$

is commutative and satisfies the Jordan identity, so $M_2(\mathbb{R})^{+}$ is a Jordan algebra. The layer is the third structure on the same set, and it is the one whose lattice is the smallest of the three.

**The key identity.** For traceless $2\times2$ matrices,

$$
XY+YX=\operatorname{tr}(XY)\,I .
$$

*Proof.* Write $X=\sum_k x_k\sigma_k$ and $Y=\sum_k y_k\sigma_k$, using that a traceless $2\times2$ matrix is a real combination of $\sigma_1,\sigma_2,\sigma_3$, and use $\sigma_j\sigma_k+\sigma_k\sigma_j=2\delta_{jk}I$. Then $XY+YX=\sum_{j,k}x_jy_k(\sigma_j\sigma_k+\sigma_k\sigma_j)=2\Big(\sum_k x_ky_k\Big)I$, while $\operatorname{tr}(XY)=\sum_{j,k}x_jy_k\operatorname{tr}(\sigma_j\sigma_k)=2\sum_k x_ky_k$. ∎

**Theorem (the Jordan lattice is a Grassmannian).** The map

$$
V\longmapsto \mathbb{R}I\oplus V
$$

is a bijection between the linear subspaces $V\subset\mathfrak{sl}(2,\mathbb{R})$ and the unital Jordan subalgebras of $M_2(\mathbb{R})^{+}$, and it is an isomorphism of lattices, with $V_1\subset V_2$ exactly when $\mathbb{R}I\oplus V_1\subset\mathbb{R}I\oplus V_2$.

*Proof.* Let $X=aI+U$ and $Y=bI+W$ with $U,W$ traceless. Then

$$
X\circ Y=\tfrac12\big(abI+aW+bU+UW+abI+aW+bU+WU\big)=abI+aW+bU+\tfrac12(UW+WU),
$$

and $\tfrac12(UW+WU)=\tfrac12\operatorname{tr}(UW)I$ by the identity above, so

$$
X\circ Y=\Big(ab+\tfrac12\operatorname{tr}(UW)\Big)I+aW+bU ,
$$

which lies in $\mathbb{R}I\oplus V$ whenever $U,W\in V$. So every $\mathbb{R}I\oplus V$ is a Jordan subalgebra. Conversely, if $J$ is a unital Jordan subalgebra, then $J=\mathbb{R}I\oplus(J\cap\mathfrak{sl}(2,\mathbb{R}))$, because $X\in J$ gives $X-\tfrac12(\operatorname{tr}X)I\in J$; and $J\cap\mathfrak{sl}(2,\mathbb{R})$ is a linear subspace. The two constructions are inverse. ∎

**The consequence.** The Jordan lattice of the split form is the lattice of subspaces of a three-dimensional vector space, that is the union of four Grassmannians. Its continuous parameters are those of the Grassmannians themselves, and no further parameter appears: there is no modulus in the product, only the choice of the subspace. Isomorphic algebras can come from different subspaces, and they do exactly when the restricted forms agree up to the scale of the generator; for a line $\mathbb{R}X$ that means the ratio $Q(X)/Q(X')$ is a square.

**The isomorphism types.** The type of $\mathbb{R}I\oplus V$ is decided by the quadratic form

$$
Q(U)=\tfrac12\operatorname{tr}(U^2),
$$

restricted to $V$; on $\mathfrak{sl}(2,\mathbb{R})$ this form has signature $(2,1)$, computed on $i\vec e_x,\vec e_y,i\vec e_z$ as $+1,-1,+1$. The product on $V$ is $U\circ W=\tfrac12\operatorname{tr}(UW)I$, so the algebra $\mathbb{R}I\oplus V$ is determined by the restriction $Q|_V$ alone: an isomorphism carries $I$ to $I$ and $V$ to $V$, and on $V$ it is an isometry of the restrictions up to the scale of the generator. The signature of $Q|_V$ is therefore an invariant, and the table lists the eight signature types, with one witness each. Inside a type of dimension $0$ or $2$ the restricted form is unique up to isometry; inside a type of dimension $1$ the scale of the generator is a further invariant, so the lines of a given sign form a continuous family.

| $\dim V$ | signature of $Q$ on $V$ | Jordan algebra | witness in corpus coordinates |
|---|---|---|---|
| $0$ | — | $\mathbb{R}$ | $\mathbb{R}e_t$ |
| $1$ | $(1,0)$ | $\mathbb{R}\oplus\mathbb{R}$ | $\operatorname{span}\{e_t,i\vec e_x\}$ |
| $1$ | $(0,1)$ | $\mathbb{C}^{+}$ | $\operatorname{span}\{e_t,\vec e_y\}$ |
| $1$ | $(0,0)$ | dual numbers, $N\circ N=0$ | $\operatorname{span}\{e_t,N\}$ |
| $2$ | $(2,0)$ | $H_2(\mathbb{R})$, the symmetric matrices | $\operatorname{span}\{e_t,i\vec e_x,i\vec e_z\}$ |
| $2$ | $(1,1)$ | the indefinite three-dimensional algebra | $\operatorname{span}\{e_t,\vec e_y,i\vec e_x\}$ |
| $2$ | $(1,0)$ | the degenerate three-dimensional algebra | $\operatorname{span}\{e_t,i\vec e_x+\vec e_y,i\vec e_z\}$ |
| $3$ | $(2,1)$ | $M_2(\mathbb{R})^{+}$ | the whole algebra |

**The witnesses in matrices.** The two-dimensional positive case is the space of symmetric matrices: $e_t$, $i\vec e_x$ and $i\vec e_z$ become $I$, $\sigma_1$ and $\sigma_3$, which are symmetric, and the symmetric matrices are closed under $\circ$ because $XY+YX$ is symmetric when $X$ and $Y$ are.

The three two-dimensional cases separate by two elementary elements, and the separation runs in one direction only.

- The *indefinite* case $\operatorname{span}\{I,J,\sigma_1\}$ contains the element $J+\sigma_1$, and $(J+\sigma_1)\circ(J+\sigma_1)=\tfrac12(J^2+J\sigma_1+\sigma_1 J+\sigma_1^2)=\tfrac12(-I-\sigma_3+\sigma_3+I)=0$, so it contains a nonzero element with square zero. The *positive* case contains none, because it is isomorphic to the symmetric matrices, which are formally real; that is what separates the first two rows.
- The *degenerate* case is $\operatorname{span}\{I,N_{+},\sigma_3\}$ with $N_{+}=\sigma_1+J=i\vec e_x+\vec e_y$ (not to be confused with the nilpotent $N=\tfrac12(i\vec e_x-\vec e_y)$ of the Lie layer), and $N_{+}^2=\sigma_1^2+J^2+\sigma_1J+J\sigma_1=I-I+\sigma_3-\sigma_3=0$, so it too contains a nonzero nilpotent and the nilpotent count does not separate it from the indefinite case. What separates them is the other direction: the indefinite case contains $J$, which satisfies $J\circ J=-I$, and the degenerate case contains no element at all with square $-I$. Indeed an element $aI+bN_{+}+c\sigma_3$ squares to $(a^2+c^2)I+2abN_{+}+2ac\sigma_3$, because $N_{+}\sigma_3+\sigma_3N_{+}=\operatorname{tr}(N_{+}\sigma_3)I=0$, and its scalar part $a^2+c^2$ is never $-1$. The degenerate algebra is therefore a third type and not a copy of either of the other two.


**Remark (idempotents).** The Jordan algebra $\mathbb{R}I\oplus V$ has a nontrivial idempotent exactly when $V$ contains an element $U$ with $Q(U)>0$. For then $W=U/\sqrt{Q(U)}$ satisfies $W^{2}=I$, and $P=\tfrac12(I+W)$ satisfies $P\circ P=\tfrac14(I+2W+W^{2})=\tfrac12(I+W)=P$ and $P\neq0,I$; conversely an idempotent $P\neq0,I$ has trace $1$ and the scalar-free part $2P-I$ has square $I$ and positive $Q$. The split three-dimensional algebra therefore has idempotents and the algebra $H_2(\mathbb{R})$ has them too, while a Jordan algebra whose form is negative definite on $V$ has only $0$ and $I$. The count of idempotents is the coarsest invariant of the layer, and it is the one used in the comparison of the eleventh section.

## Associative Subalgebras of the Compact Form

**The centre and the division property.** The centre of $\mathbb{H}$ is the real line $\mathbb{R}e_t$, and $\mathbb{H}$ is a division algebra: every nonzero element is invertible, with $\tilde q^{-1}=\tilde q^{\natural}/(\tilde q\tilde q^{\natural})$ and $\tilde q\tilde q^{\natural}=(q_t^2+q_x^2+q_y^2+q_z^2)e_t$ a positive multiple of the unit. The only two-sided ideals are $0$ and $\mathbb{H}$, and the argument is shorter than in the split case: an ideal containing a nonzero element contains its inverse, hence contains the unit, hence is everything.

**Theorem (subalgebras of $\mathbb{H}$).** The subalgebras of $\mathbb{H}$ are $0$, the real line $\mathbb{R}e_t$, the copies of $\mathbb{C}$, and $\mathbb{H}$ itself. In particular there is no subalgebra of dimension $3$, and every nonzero subalgebra contains the unit.

*Proof.* Let $A\neq0$ be a subalgebra and let $u\in A$ be nonzero. If $u\notin\mathbb{R}e_t$, write $u=ae_t+p$ with $p$ pure and $p\neq0$. Then $p^2=-|p|^2e_t$ gives $u^2=2au-(a^2+|p|^2)e_t$, a quadratic relation with a nonzero constant term: the coefficient $b=-(a^2+|p|^2)$ cannot vanish, and $b=0$ would give $u(u-a e_t)=0$ and hence $u=ae_t$ in a division algebra. So $u^2-2au=b e_t$ lies in $A$ with $b e_t\neq0$, and $e_t\in A$.

Now suppose $A$ contains a non-real element. Then $e_t\in A$ and $A$ is unital. The algebra $\mathbb{R}[u]\cong\mathbb{C}$ is a two-dimensional unital subalgebra of $A$. If $A\neq\mathbb{R}[u]$, choose $v\in A\setminus\mathbb{R}[u]$; then $A$ contains the real span of $a+bv$ for $a,b\in\mathbb{R}[u]$, which is the complex span of $1$ and $v$ and has real dimension $4$, so $A=\mathbb{H}$. Hence a unital subalgebra of a division algebra is $\mathbb{R}$, a copy of $\mathbb{C}$, or the whole algebra; and a subalgebra containing no non-real element lies in $\mathbb{R}e_t$ and equals $0$ or $\mathbb{R}e_t$. ∎

**Remark (no non-unital subalgebras).** The last sentence of the proof is the whole difference with the split form. In $M_2(\mathbb{R})$ the nilpotent $N$ spans a subalgebra $\mathbb{R}N$ that contains no unit, and $\operatorname{span}\{E_{11},E_{12}\}$ is a two-dimensional subalgebra without a unit. In $\mathbb{H}$ no such algebra exists, because a nonzero element is invertible, its square is never zero, and a nonzero subalgebra containing a non-real element is forced to contain the unit by the quadratic relation. The absence of nilpotents is not a technicality: it is what makes the lattice finite.

**The copies of $\mathbb{C}$.** A two-dimensional unital subalgebra of $\mathbb{H}$ is $\mathbb{R}[u]$ for an element $u\notin\mathbb{R}e_t$ with $u^2$ a negative real multiple of the unit, that is $\mathbb{R}e_t\oplus\mathbb{R}p$ with $p$ pure and $p^2=-e_t$. The pure elements with square $-e_t$ are the points of the unit sphere

$$
S^2=\{p\in\operatorname{Im}\mathbb{H}:p^2=-e_t\},
$$

and the copy attached to $p$ and the copy attached to $-p$ are the same. Conjugation by an invertible element $q$ acts on the pure part by $p\mapsto qpq^{-1}$, and the map from the invertibles to this action is the twofold cover $\mathbb{H}^{\times}\to SO(3)$, which is transitive on $S^2$. So the copies of $\mathbb{C}$ form a single conjugacy class, and the parameter space of the class is the sphere modulo the antipodal identification, that is the real projective plane.

**Warning (finite types, continuous parameter).** The contrast with the split form is sharp and it is the point of the section. The compact form has four isomorphism types of subalgebra and one continuous parameter, the choice of a point of $S^2$. The split form has six types and three continuous families, two of them two-dimensional. The difference is a direct consequence of the division property: a division algebra has no nilpotents, so the degenerate two-dimensional cases of the split form have no counterpart, and the quadratic form that decides the remaining cases is definite, so its level sets are spheres rather than hyperboloids.

**The copy of $\mathbb{C}$ that also lies in the split form.** The intersection $\mathbb{B}_H\cap M_2(\mathbb{R})$ is the real span of $e_t$ and $\vec e_y$, and $\vec e_y^{\,2}=-e_t$, so it is a copy of $\mathbb{C}$. It is one of the copies counted in this section and it is also a subalgebra of the split form. So the two forms share their circles of scalars in a definite way: the copies inside the compact form are parametrized by $S^2$, and one of them, up to the antipodal identification, lies in the split form.

## Lie Subalgebras of the Compact Form

**The Lie algebra.** The commutator on $\mathbb{H}$ gives the real Lie algebra $\mathfrak u(2)$, of dimension $4$. In corpus coordinates

$$
\mathfrak u(2)=\mathbb{B}_{\Phi}=\operatorname{span}_{\mathbb{R}}\{i e_t,\ \vec e_x,\ \vec e_y,\ \vec e_z\},
$$

with centre $\mathbb{R}(i e_t)$ and derived algebra

$$
\mathfrak{su}(2)=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\ \vec e_y,\ \vec e_z\},
$$

the traceless part; the decomposition $\mathfrak u(2)=\mathfrak{su}(2)\oplus\mathfrak u(1)$ is a direct sum of Lie algebras, the second factor being the centre. The brackets are

$$
[\vec e_x,\vec e_y]=2\vec e_z,\qquad [\vec e_y,\vec e_z]=2\vec e_x,\qquad [\vec e_z,\vec e_x]=2\vec e_y ,
$$

and they differ from the brackets of $\mathfrak{sl}(2,\mathbb{R})$ in two signs, which is the difference between the compact and the split real form of $\mathfrak{sl}(2,\mathbb{C})$.

**Remark (the biquaternion reading of the anti-Hermitian condition).** The two defining conditions translate without residue. In the dictionary $e_t\mapsto I_2$, $\vec e_k\mapsto-i\sigma_k$, Hermitian conjugation is the star,

$$
M_2(\tilde Q^{*})=M_2(\tilde Q)^{\dagger},
$$

for every biquaternion $\tilde Q$, so $A^{\dagger}=-A$ reads $\tilde Q^{*}=-\tilde Q$ and the traceless condition reads $Q_t=0$. Hence $\mathfrak u(2)$ is the anti-Hermitian subspace, which is $\mathbb{B}_{\Phi}$, and $\mathfrak{su}(2)$ is its scalar-free part, the real pure quaternions. The partner subspace is the Hermitian one, $\mathbb{B}_{\Psi}$, and every biquaternion splits as

$$
\tilde Q=\tfrac12\bigl(\tilde Q-\tilde Q^{*}\bigr)+\tfrac12\bigl(\tilde Q+\tilde Q^{*}\bigr),
$$

the first term anti-Hermitian and the second Hermitian, so the two subspaces span $\mathbb{B}$ over $\mathbb{R}$. The pair $(\mathbb{B}_{\Phi},\mathbb{B}_{\Psi})$ is the biquaternion form of the classical pair (anti-Hermitian, Hermitian) of a matrix algebra, and it splits the two layers between them: $\mathbb{B}_{\Phi}$ is closed under the bracket and is the ambient algebra of the compact form, $\mathbb{B}_{\Psi}$ is closed under the Jordan product and is the space of Hermitian observables, and neither is closed under the associative product.

**Remark (why the physics generators carry the factor $i$).** The Pauli matrices are Hermitian, so the units $\vec e_k=-i\sigma_k$ are anti-Hermitian, and the factor $-i$ is the whole content of the dictionary. Two readings of one matrix follow:

$$
x\sigma_1+y\sigma_2+z\sigma_3=i\bigl(x\vec e_x+y\vec e_y+z\vec e_z\bigr),\qquad \tfrac i2\bigl(x\sigma_1+y\sigma_2+z\sigma_3\bigr)=-\tfrac12\bigl(x\vec e_x+y\vec e_y+z\vec e_z\bigr).
$$

The first is the imaginary pure quaternion and is Hermitian; the second is the real pure quaternion, up to the global factor $-\tfrac12$, and is anti-Hermitian. A generator written $\tfrac i2\sigma_k$ is therefore anti-Hermitian for the biquaternion reason that $\sigma_k$ is Hermitian and $i$ is the imaginary unit of the coefficient field. The statement "the Lie algebra consists of anti-Hermitian matrices" is the statement "$\mathfrak{su}(2)$ is the real vector part", and the three generators are the three real units, with no further factor needed.

**Theorem (subalgebras of $\mathfrak{su}(2)$).** The subalgebras of $\mathfrak{su}(2)$ are $0$, the lines $\mathbb{R}X$ with $X\neq0$, and $\mathfrak{su}(2)$. All lines are conjugate.

*Proof.* A two-dimensional subalgebra $\mathfrak{a}$ is abelian or it is not. If it is abelian, take $X\in\mathfrak{a}$ nonzero; the centralizer of $X$ in $\mathfrak{su}(2)$ is the line $\mathbb{R}X$, since the only elements commuting with $X$ are its real multiples, so $\mathfrak{a}$ would have dimension $1$. If it is not abelian, then after a change of basis $[X,Y]=Y$, and such an algebra is not unimodular, since $\operatorname{tr}(\operatorname{ad}X)=1$; but every subalgebra of a compact Lie algebra is compact, and every compact Lie algebra is unimodular, because $\operatorname{ad}X$ is skew for an invariant inner product and a skew matrix has zero trace. So there is no two-dimensional subalgebra. For the last statement, $\operatorname{Ad}$ maps $SU(2)$ onto $SO(3)$, acting on $\mathfrak{su}(2)\cong\mathbb{R}^3$ by rotations, and rotations are transitive on lines. ∎

**Remark (the inclusion $\mathfrak{so}(2)\subset\mathfrak{su}(2)$, and why $i$ leaves).** The real skew matrices are the line $\mathbb{R}\vec e_y$, since $\vec e_y=-i\sigma_2$ is the one unit of $\{\vec e_x,\vec e_y,\vec e_z\}$ with a real matrix, and $e^{t\vec e_y}$ is the rotation of angle $t$. The line is therefore a *real* subspace of $\mathfrak{su}(2)$, and the choice of which unit carries it is a choice of axis, moved by conjugation with the invertibles of $\mathbb{B}_H$. Multiplication by $i$ leaves the algebra:

$$
\tilde Q^{*}=-\tilde Q\ \Longrightarrow\ (i\tilde Q)^{*}=+i\tilde Q ,
$$

so $i\,\mathfrak{su}(2)$ is the Hermitian scalar-free subspace, spanned by $i\vec e_x,i\vec e_y,i\vec e_z$, and it meets $\mathfrak{su}(2)$ only at $0$. The two halves fill the vector subspace:

$$
\mathbb{B}_V=\mathfrak{su}(2)\oplus i\,\mathfrak{su}(2),
$$

of dimension six, which is one of the six remarkable subspaces, and it is closed under the bracket alone: the product $uv$ of two real pure quaternions splits as the scalar part $-\langle u,v\rangle e_t$ and the pure part $\tfrac12(uv-vu)$, so the associative product leaves the subspace whenever $\langle u,v\rangle\neq0$, and the Jordan product is the scalar part alone. The matrix statement $iA\notin\mathfrak{su}(n)$ for real skew $A$ is thus the biquaternion statement that the anti-Hermitian and Hermitian halves of the vector part are two different three-planes.

**Remark (general $n$, and the case $n=2$ read off the dictionary).** For general $n$ the same split reads

$$
\mathfrak{su}(n)=\mathfrak{so}(n)\oplus i\operatorname{Sym}_0(n,\mathbb{R}),
$$

the real skew part and the imaginary symmetric traceless part. The biquaternion algebra is a matrix algebra of one size, so only $n=2$ occurs here, and there the split is read off the reality of the entries: $\mathfrak{so}(2)$ is the unit with the real matrix, $\mathbb{R}\vec e_y$, and $i\operatorname{Sym}_0(2,\mathbb{R})$ is the span of the two units whose matrices are imaginary times symmetric, $\vec e_x=-i\sigma_1$ and $\vec e_z=-i\sigma_3$. The general-$n$ formula enters this article as the analogue of a decomposition, not as a theorem about $\mathbb{B}$.

**Theorem (subalgebras of $\mathfrak u(2)$).** Up to conjugation by $U(2)$, the subalgebras of $\mathfrak u(2)$ are:

1. $0$ and $\mathfrak u(2)$;
2. the centre $\mathbb{R}(i e_t)$, a line;
3. the compact lines $\mathbb{R}X$ with $X\in\mathfrak{su}(2)$ nonzero, one conjugacy class;
4. the mixed lines $\mathbb{R}(X+t\,i e_t)$ with $X\in\mathfrak{su}(2)$ nonzero and $t\neq0$, a one-parameter family with parameter $|t|/|X|$;
5. the abelian planes $\operatorname{span}_{\mathbb{R}}\{i e_t,X\}$ with $X\in\mathfrak{su}(2)$ nonzero, one conjugacy class;
6. $\mathfrak{su}(2)$.

*Proof.* Let $\mathfrak{a}\subset\mathfrak u(2)$ have dimension $2$ or $3$. If $\mathfrak{a}$ contains the centre, then $\mathfrak{a}=\mathbb{R}(i e_t)\oplus(\mathfrak{a}\cap\mathfrak{su}(2))$, and the second summand is a subalgebra of $\mathfrak{su}(2)$ of dimension $1$ or $2$; dimension $2$ is impossible by the previous theorem, so a subalgebra of dimension $2$ containing the centre is an abelian plane, and one of dimension $3$ containing the centre does not exist. If $\mathfrak{a}$ does not contain the centre, the projection to $\mathfrak{su}(2)$ along the centre is injective, so $\mathfrak{a}$ is the graph of a linear $\lambda$ over a subalgebra $\mathfrak{b}$ of $\mathfrak{su}(2)$, and the bracket condition reads $\lambda([\mathfrak{b},\mathfrak{b}])=0$. Over a line this condition is empty, so all $\lambda$ occur and the graphs are the lines of the third and fourth entries; over $\mathfrak{b}=\mathfrak{su}(2)$ the derived algebra is everything, so $\lambda=0$ and the graph is $\mathfrak{su}(2)$. The parameter $|t|/|X|$ is invariant under conjugation, because $U(2)$ acts on $\mathfrak{su}(2)$ by rotations and fixes the centre, so mixed lines with different $|t|/|X|$ are not conjugate. ∎

**The Killing form.** For $\mathfrak u(2)$ the Killing form is the restriction of the form of $\mathfrak{gl}(2,\mathbb{C})$:

$$
K(X,Y)=4\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y).
$$

The values are collected in one table, the signature again being computed in the algebra itself.

| algebra | dimension | $K$ | signature | radical |
|---|---|---|---|---|
| $\mathfrak{su}(2)$ | $3$ | $4\operatorname{tr}(XY)$ | $(0,3)$, negative definite | $0$ |
| abelian plane | $2$ | $0$ | $(0)$ | the algebra |
| the centre | $1$ | $0$ | $(0)$ | the algebra |
| $\mathfrak u(2)$ | $4$ | $4\operatorname{tr}(XY)-2\operatorname{tr}X\operatorname{tr}Y$ | $(0,3)$ with a null line | $\mathbb{R}(i e_t)$ |

The values on the three generators are $4\operatorname{tr}(\vec e_x^{\,2})=4(-2)=-8$ and cyclically, so $K=-8$ times the identity in the basis $\vec e_x,\vec e_y,\vec e_z$; in the rescaled basis $\vec e_k/2$ the form is $-2$ times the identity, which is the normalisation of [Classification of the Structures of the Biquaternion Algebra](classification-of-the-structures-of-the-biquaternion-algebra.html). The form of $\mathfrak u(2)$ is negative semidefinite because $\mathfrak u(2)$ is the algebra of a compact group, and its radical is exactly the centre, which is the general statement that the radical of the Killing form of a reductive algebra is its centre.

**The two signatures side by side.** The same three-dimensional complex algebra $\mathfrak{sl}(2,\mathbb{C})$ has two real forms in this article, and their Killing forms differ in the sign of one eigenvalue:

$$
\mathfrak{sl}(2,\mathbb{R}):\ (2,1),\qquad \mathfrak{su}(2):\ (0,3).
$$

The change of sign is the change of the real form, and it is the whole reason the two Lie groups differ in compactness. The three signatures of [The Killing Form of $\mathfrak{sl}_2$ and Its Three Signatures](the-killing-form-of-sl-2-and-its-three-signatures.html) are the three real forms of one complex algebra read in one place; the two rows above are two of those three, the third being $\mathfrak{so}(3,1)$.

**The ideals.** The ideals of $\mathfrak u(2)$ are $0$, the centre $\mathbb{R}(i e_t)$, $\mathfrak{su}(2)$ and $\mathfrak u(2)$. The argument is the same as for $\mathfrak{gl}(2,\mathbb{R})$, with the centre in place of $\mathbb{R}I$ and the compact simple algebra in place of the split one.

## Jordan Subalgebras of the Compact Form

**The Jordan algebra.** On $\mathbb{H}$ the symmetrized product gives the Jordan algebra $\mathbb{H}^{+}$, and the layer is the third structure on the same set.

**Theorem (the Jordan lattice is again a Grassmannian).** The map $V\mapsto\mathbb{R}e_t\oplus V$ is a bijection between the linear subspaces of the pure part $\operatorname{Im}\mathbb{H}=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$ and the unital Jordan subalgebras of $\mathbb{H}^{+}$, and it is an isomorphism of lattices.

*Proof.* For pure $p,q$ the product $pq$ has scalar part $-\langle p,q\rangle$ and pure part $p\times q$, so $pq+qp=-2\langle p,q\rangle e_t$ is a real multiple of the unit. Hence for $X=ae_t+p$ and $Y=be_t+q$,

$$
X\circ Y=\big(ab-\langle p,q\rangle\big)e_t+aq+bp ,
$$

which lies in $\mathbb{R}e_t\oplus V$ whenever $p,q\in V$. Conversely $J=\mathbb{R}e_t\oplus(J\cap\operatorname{Im}\mathbb{H})$ for a unital Jordan subalgebra $J$, because $X-\tfrac12(\operatorname{tr}X)e_t$ has pure part equal to that of $X$. ∎

**The isomorphism types.** The type is decided by the quadratic form $Q(U)=\tfrac12\operatorname{tr}(U^2)$ restricted to $V$, and on the pure part this form is negative definite, with value $-1$ on each of $\vec e_x,\vec e_y,\vec e_z$. So there are four types and no more.

| $\dim V$ | signature of $Q$ on $V$ | Jordan algebra | witness in corpus coordinates |
|---|---|---|---|
| $0$ | — | $\mathbb{R}$ | $\mathbb{R}e_t$ |
| $1$ | $(0,1)$ | $\mathbb{C}^{+}$ | $\operatorname{span}\{e_t,\vec e_x\}$ |
| $2$ | $(0,2)$ | the negative-definite three-dimensional algebra | $\operatorname{span}\{e_t,\vec e_x,\vec e_y\}$ |
| $3$ | $(0,3)$ | $\mathbb{H}^{+}$ | the whole algebra |

**Remark (no idempotents).** The Jordan algebra $\mathbb{H}^{+}$ has exactly two idempotents, $0$ and $e_t$. For if $P=ae_t+p$ satisfies $P\circ P=P$, then $2ap=p$ and $a^2-\langle p,p\rangle=a$; a nonzero $p$ would give $a=\tfrac12$ and $\langle p,p\rangle=a^2-a=-\tfrac14$, which is impossible for a negative definite form. So the negative definiteness of the form, which is what makes $\mathbb{H}$ a division algebra, is also what removes the idempotents from the Jordan layer. The split form has the idempotent $\tfrac12(e_t+i\vec e_x)$ in its Jordan layer as well, and that one element separates the two Jordan algebras.

**Remark (the two lattices are the same lattice).** The subspaces of a three-dimensional real vector space form one lattice, and both Jordan layers are that lattice: the split form uses the traceless part of $M_2(\mathbb{R})$ with the form of signature $(2,1)$, and the compact form uses the pure part of $\mathbb{H}$ with the form of signature $(0,3)$. The lattices are isomorphic; the algebras are not. This is the example used in the twelfth section to show that a Jordan lattice does not determine a Jordan algebra.

## The Involutions Inside Each Real Form and the Six Subspaces

**The six subspaces.** The ambient algebra carries six distinguished real subspaces, the fixed and anti-fixed spaces of the three involutions $\natural$, $\overline{\phantom{Q}}$ and ${}^{*}$:

| subspace | condition | $\dim_{\mathbb{R}}$ |
|---|---|---|
| $\mathbb{B}_C$ | $\tilde Q^{\natural}=\tilde Q$ | $2$ |
| $\mathbb{B}_V$ | $\tilde Q^{\natural}=-\tilde Q$ | $6$ |
| $\mathbb{B}_H$ | $\overline{\tilde Q}=\tilde Q$ | $4$ |
| $\mathbb{B}_{iH}$ | $\overline{\tilde Q}=-\tilde Q$ | $4$ |
| $\mathbb{B}_{\Psi}$ | $\tilde Q^{*}=\tilde Q$ | $4$ |
| $\mathbb{B}_{\Phi}$ | $\tilde Q^{\flat}=\tilde Q$ | $4$ |

Two of the six are the ambient objects of the two layers. $\mathbb{B}_{\Phi}$ is closed under the bracket and equals $\mathfrak u(2)$, the Lie algebra of the compact form, and $\mathbb{B}_{\Psi}$ is closed under the Jordan product and is the Hermitian space. Neither is closed under the associative product, and the two subspaces are the reason the compact form carries a Lie algebra and a Jordan algebra on the same ambient algebra.

Their definitions, their bases and the table of their intersections are in [Subspaces and Decompositions of the Biquaternion Algebra](subspaces-and-decompositions-of-the-biquaternion-algebra.html) and in [Classification of the Structures of the Biquaternion Algebra](classification-of-the-structures-of-the-biquaternion-algebra.html). This section does not repeat the ambient table. It computes what each subspace becomes inside each real form, and the answer is different for the two forms.

**The involution inside the split form is the transpose.** The involution ${}^{*}$ maps the split form to itself. On an element with real coefficients on $e_t$ and $\vec e_y$ and imaginary coefficients on $\vec e_x$ and $\vec e_z$, the map ${}^{*}=\overline{\phantom{Q}}\circ\natural$ conjugates the imaginary coefficients and negates the vector part, and the two effects compose to a swap of the two kinds of coefficient. On the four basis elements the result is

$$
e_t^{*}=e_t,\qquad \vec e_y^{*}=-\vec e_y,\qquad (i\vec e_x)^{*}=i\vec e_x,\qquad (i\vec e_z)^{*}=i\vec e_z ,
$$

which in the matrices $I$, $J$, $\sigma_1$, $\sigma_3$ reads

$$
I\mapsto I,\qquad J\mapsto -J,\qquad \sigma_1\mapsto\sigma_1,\qquad \sigma_3\mapsto\sigma_3 ,
$$

and that is exactly the transpose: the three symmetric generators are fixed and the antisymmetric one changes sign. So on the split form the ambient involution is the transpose, its fixed space is the three-dimensional space of symmetric matrices, and its anti-fixed space is the line of antisymmetric matrices.

**The involution inside the compact form is the quaternion conjugation.** On the compact form the coefficient conjugation is the identity, since the coefficients are real, so ${}^{*}$ coincides with $\natural$: the unit is fixed and each pure unit changes sign. The fixed space is the real line $\mathbb{R}e_t$ and the anti-fixed space is the three-dimensional pure part. The same computation shows that ${}^{\flat}=-{}^{*}$ has the opposite spaces, so the Hermitian and anti-Hermitian rows of the table below repeat the dimensions of the scalar and pure rows.

**The intersections with the split form.** The split form is $\operatorname{span}_{\mathbb{R}}\{e_t,\vec e_y,i\vec e_x,i\vec e_z\}$, and intersecting it with the six subspaces gives the following table.

| subspace | intersection with $M_2(\mathbb{R})$ | $\dim_{\mathbb{R}}$ | in matrices |
|---|---|---|---|
| $\mathbb{B}_C$ | $\operatorname{span}\{e_t\}$ | $1$ | $\mathbb{R}I$ |
| $\mathbb{B}_V$ | $\operatorname{span}\{\vec e_y,i\vec e_x,i\vec e_z\}$ | $3$ | traceless matrices |
| $\mathbb{B}_H$ | $\operatorname{span}\{e_t,\vec e_y\}$ | $2$ | $\mathbb{R}I\oplus\mathbb{R}J\cong\mathbb{C}$ |
| $\mathbb{B}_{iH}$ | $\operatorname{span}\{i\vec e_x,i\vec e_z\}$ | $2$ | $\operatorname{span}\{\sigma_1,\sigma_3\}$ |
| $\mathbb{B}_{\Psi}$ | $\operatorname{span}\{e_t,i\vec e_x,i\vec e_z\}$ | $3$ | symmetric matrices |
| $\mathbb{B}_{\Phi}$ | $\operatorname{span}\{\vec e_y\}$ | $1$ | antisymmetric matrices |

The rows check each other three times. The centre and the vector part meet the split form in spaces of dimensions $1$ and $3$, whose sum is $4$: that is the decomposition of the split form into scalars and traceless part. The Hermitian and anti-Hermitian subspaces meet it in spaces of dimensions $3$ and $1$, whose sum is $4$: that is the eigenspace decomposition of the transpose. The quaternion and antiquaternion subspaces meet it in spaces of dimensions $2$ and $2$, whose sum is $4$: that is the decomposition into real and imaginary coefficients, the coefficient conjugation being an involution of the split form.

**The intersections with the compact form.** The compact form is $\mathbb{B}_H$, and the table is shorter.

| subspace | intersection with $\mathbb{H}$ | $\dim_{\mathbb{R}}$ | description |
|---|---|---|---|
| $\mathbb{B}_C$ | $\operatorname{span}\{e_t\}$ | $1$ | real scalars |
| $\mathbb{B}_V$ | $\operatorname{span}\{\vec e_x,\vec e_y,\vec e_z\}$ | $3$ | pure quaternions |
| $\mathbb{B}_H$ | $\mathbb{H}$ | $4$ | the whole form |
| $\mathbb{B}_{iH}$ | $0$ | $0$ | nothing |
| $\mathbb{B}_{\Psi}$ | $\operatorname{span}\{e_t\}$ | $1$ | real scalars |
| $\mathbb{B}_{\Phi}$ | $\operatorname{span}\{\vec e_x,\vec e_y,\vec e_z\}$ | $3$ | pure quaternions |

The last two rows are the general fact that ${}^{*}=\natural$ on the compact form: the fixed space of ${}^{*}$ is the fixed space of $\natural$, which is the real line, and the anti-fixed space of ${}^{\flat}=-{}^{*}$ is the anti-fixed space of $\natural$, which is the pure part. So the Hermitian and anti-Hermitian subspaces cut out of the compact form exactly the scalar and pure parts, in the same order as the quaternion conjugation does.

**Comparison of the two tables.** The two tables are not rescalings of one another, and the difference is structural.

- In the split form the involution ${}^{*}$ is the transpose, with a three-dimensional fixed space and a one-dimensional anti-fixed space; in the compact form it is the quaternion conjugation, with a one-dimensional fixed space and a three-dimensional anti-fixed space. The two chains are exchanged.
- The exchange is the source of the difference between $\mathfrak{sl}(2,\mathbb{R})$ and $\mathfrak{su}(2)$ at the Lie level. Inside $\mathfrak{sl}(2,\mathbb{R})$ the anti-fixed space of the transpose is the line $\mathbb{R}\vec e_y$, which is $\mathfrak{so}(2)$, so

$$
\mathfrak{sl}(2,\mathbb{R})=\mathfrak{so}(2)\oplus\mathfrak{p},\qquad \mathfrak{p}=\{X:X^{*}=X,\ \operatorname{tr}X=0\},
$$

with $\mathfrak{so}(2)$ a line and $\mathfrak{p}$ the plane $\operatorname{span}\{i\vec e_x,i\vec e_z\}$. That is the Cartan decomposition of the split form. Inside $\mathfrak{su}(2)$ the involution ${}^{*}$ is minus the identity, so the anti-fixed space is the whole algebra and there is no splitting of the same kind; the compact form is already the compact part.
- The quaternion subspace meets the split form in a copy of $\mathbb{C}$, and the antiquaternion subspace meets it in a real two-plane that is not a subalgebra, since $(i\vec e_x)(i\vec e_z)=\vec e_y$ lies outside $\operatorname{span}\{i\vec e_x,i\vec e_z\}$. The compact form meets the quaternion subspace in itself and the antiquaternion subspace in nothing.

**Warning (an ambient subspace is not an intersection).** The six subspaces live in the ambient algebra, where their dimensions are $2,6,4,4,4,4$. Their intersections with a real form have dimensions $1,3,2,2,3,1$ in the split case and $1,3,4,0,1,3$ in the compact case, and neither list is obtained by reading the ambient list form by form. A statement about a subspace of $\mathbb{B}$ is not a statement about a subalgebra of a real form, and the two tables above are the ones to use when the question concerns a real form.

## The Lie Groups Attached to the Lie Subalgebras

**The general correspondence, cited.** By the Lie correspondence, stated and proved in [The Lie Correspondence and the Adjoint Representation](the-lie-correspondence-and-the-adjoint-representation.html), every finite-dimensional real Lie algebra has a simply connected Lie group, unique up to isomorphism; every connected Lie group with that algebra is a quotient of the simply connected cover by a discrete central subgroup; and the fundamental group of the quotient is that subgroup. The general theory is not reproduced here. This section applies it to the subalgebras of the split and compact forms, and the application is the contribution of the article.

**The split form.** The table gives, for each Lie subalgebra, the simply connected group, its centre, its discrete central subgroups, the connected quotients, and the fundamental group of each quotient.

| algebra | $\dim$ | simply connected group | centre | discrete central subgroups | connected quotients and $\pi_1$ |
|---|---|---|---|---|---|
| $\mathfrak{sl}(2,\mathbb{R})$ | $3$ | $\widetilde{SL}(2,\mathbb{R})$ | $\mathbb{Z}$ | $n\mathbb{Z}$ | $SL(2,\mathbb{R})=\widetilde{SL}/2\mathbb{Z}$, $\pi_1=\mathbb{Z}$; $PSL(2,\mathbb{R})=\widetilde{SL}/\mathbb{Z}$, $\pi_1=\mathbb{Z}$; $\widetilde{SL}/n\mathbb{Z}$, $\pi_1=n\mathbb{Z}$ |
| Borel $\mathfrak{b}$ | $3$ | $B^{+}$, upper triangular with positive diagonal | $\mathbb{R}_{>0}\cong\mathbb{R}$ | $\Gamma_a=\{a^n I:n\in\mathbb{Z}\}\cong\mathbb{Z}$, $a>0$, $a\neq1$ | $B^{+}$, $\pi_1=0$; $B^{+}/\Gamma_a\cong B^{+}/\mathbb{Z}$, $\pi_1=\mathbb{Z}$ |
| Cartan $\mathfrak{h}$ | $2$ | $\mathbb{R}^2$ | $\mathbb{R}^2$ | the lattices $\Lambda$ | $\mathbb{R}^2/\Lambda$, $\pi_1=\Lambda\cong\mathbb{Z}$ or $\mathbb{Z}^2$ |
| $\mathfrak{so}(2)=\mathbb{R}\vec e_y$ | $1$ | $\mathbb{R}$ | $\mathbb{R}$ | $a\mathbb{Z}$ | $S^1=\mathbb{R}/a\mathbb{Z}$, $\pi_1=\mathbb{Z}$ |
| $\mathbb{R}\sigma_3$ | $1$ | $\mathbb{R}$ | $\mathbb{R}$ | $a\mathbb{Z}$ | $S^1$, $\pi_1=\mathbb{Z}$ |
| $\mathbb{R}N$ | $1$ | $\mathbb{R}$ | $\mathbb{R}$ | $a\mathbb{Z}$ | $S^1$, $\pi_1=\mathbb{Z}$ |
| $\mathfrak{gl}(2,\mathbb{R})$ | $4$ | $\widetilde{SL}(2,\mathbb{R})\times\mathbb{R}$ | $\mathbb{Z}\times\mathbb{R}$ | $n\mathbb{Z}\times\{0\}$, $\{0\}\times a\mathbb{Z}$, and the slanted $\{(n,n\alpha):n\in\mathbb{Z}\}$ with $\alpha\notin\mathbb{Q}$ | $GL^{+}(2,\mathbb{R})$, $\pi_1=\mathbb{Z}$; $PSL(2,\mathbb{R})\times\mathbb{R}$, $\pi_1=\mathbb{Z}$; $\widetilde{SL}(2,\mathbb{R})\times S^1$, $\pi_1=\mathbb{Z}\oplus\mathbb{Z}$ |

Four entries deserve a word.

- $\mathfrak{sl}(2,\mathbb{R})$ is simple, so its simply connected group has centre $\mathbb{Z}$ and not $\mathbb{Z}/2$; the centre of $SL(2,\mathbb{R})$ is $\{\pm I\}$, which is the image of $2\mathbb{Z}$. The two quotients that occur in geometry are $SL(2,\mathbb{R})$ and $PSL(2,\mathbb{R})$, and both have fundamental group $\mathbb{Z}$, because $SL(2,\mathbb{R})$ is homotopy equivalent to its maximal compact subgroup $SO(2)$.
- The Borel is the case where the centre of the cover is connected, and it is worth a careful word, because connectedness of the centre is often confused with triviality of its discrete subgroups. $B^{+}$ is diffeomorphic to $\mathbb{R}^3$ and is simply connected, and its centre is $Z(B^{+})=\{aI:a>0\}\cong\mathbb{R}_{>0}\cong\mathbb{R}$. That centre is connected and non-compact, and it has plenty of discrete subgroups: $\Gamma_a=\{a^nI:n\in\mathbb{Z}\}\cong\mathbb{Z}$ for every $a>0$ with $a\neq1$. Each quotient $B^{+}/\Gamma_a$ is a connected Lie group with Lie algebra $\mathfrak{b}$, is not simply connected, and has $\pi_1\cong\mathbb{Z}$; the quotient is a cylinder bundle over $\mathbb{R}^2$ rather than the total space $\mathbb{R}^3$. What is special about $B^{+}$ is not that it has no quotients but that its centre is *connected*, so that its centre is a vector group rather than a torus or a finite group, and that no quotient of it is compact.
- The Cartan is abelian, so the simply connected group is $\mathbb{R}^2$ and its centre is all of itself; every quotient is a cylinder or a torus, according to the rank of the lattice.
- $\mathfrak{gl}(2,\mathbb{R})$ is the direct sum $\mathfrak{sl}(2,\mathbb{R})\oplus\mathbb{R}$, so everything is read off from the first, third and fourth rows: $GL^{+}(2,\mathbb{R})\cong SL(2,\mathbb{R})\times\mathbb{R}_{>0}$, its fundamental group is $\mathbb{Z}$, and its cover is the product of the two covers. Its centre is $\mathbb{Z}\times\mathbb{R}$, and the discrete subgroups of that group are more numerous than the coordinate ones: besides $n\mathbb{Z}\times\{0\}$ and $\{0\}\times a\mathbb{Z}$ there are the slanted subgroups $\{(n,n\alpha):n\in\mathbb{Z}\}$, which are discrete because $\alpha\notin\mathbb{Q}$, and their quotients are further connected groups with algebra $\mathfrak{gl}(2,\mathbb{R})$, all of fundamental group $\mathbb{Z}$. The row lists the coordinate cases, which are the ones that arise as products of quotients of the two factors; it is not the full list of quotients.

**Remark (the two connected groups of a line).** Every one-dimensional Lie algebra is isomorphic to $\mathbb{R}$, and it has exactly two connected groups, $\mathbb{R}$ itself and $S^1=\mathbb{R}/a\mathbb{Z}$. The three one-dimensional entries of the table are therefore the same Lie algebra with three different embeddings, and the groups are the same two groups in each row. The rows are separated because the embeddings differ: the elliptic line $\mathbb{R}\vec e_y$ exponentiates to the circle $SO(2)\subset SL(2,\mathbb{R})$, while the hyperbolic line $\mathbb{R}\sigma_3$ exponentiates to the closed subgroup of positive diagonal matrices, which is a copy of $\mathbb{R}$ and not a circle, and the circle quotient of that line is not a subgroup of $GL(2,\mathbb{R})$ at all. 

**Remark (the circle and the hyperbola are two exponentials of one line).** The two groups of the line $\mathbb{R}$ are read off the star in $\mathbb{B}$. The anti-Hermitian unit $\vec e_y$ has a real skew matrix, so

$$
\exp(t\vec e_y)=\begin{pmatrix}\cos t&-\sin t\\ \sin t&\cos t\end{pmatrix}
$$

is a rotation for every $t$, and the image is the circle $SO(2)$. The Hermitian unit $i\vec e_z$ has the real symmetric matrix $\operatorname{diag}(1,-1)$, so

$$
\exp(t\,i\vec e_z)=\operatorname{diag}(e^{t},e^{-t})
$$

is real, symmetric and positive definite for every $t$, and the image is a non-compact copy of $\mathbb{R}$, the diagonal of $SL(2,\mathbb{R})$. Both lines are the same Lie algebra $\mathbb{R}$, the first is anti-Hermitian and the second Hermitian, and the difference between a circle and a hyperbola is the difference of sign under the star. The quotient that turns the hyperbola into a circle exists as a group and is not a subgroup of $GL(2,\mathbb{R})$, which is the group-theoretic face of the same statement.
The Lie algebra does not see the difference; the group does.

**The compact form.** The same table for the subalgebras of $\mathfrak u(2)$.

| algebra | $\dim$ | simply connected group | centre | discrete central subgroups | connected quotients and $\pi_1$ |
|---|---|---|---|---|---|
| $\mathfrak{su}(2)$ | $3$ | $SU(2)$ | $\mathbb{Z}/2$ | $0$, $\mathbb{Z}/2$ | $SU(2)$, $\pi_1=0$; $SO(3)=SU(2)/\{\pm I\}$, $\pi_1=\mathbb{Z}/2$ |
| abelian plane | $2$ | $\mathbb{R}^2$ | $\mathbb{R}^2$ | the lattices $\Lambda$ | $\mathbb{R}^2/\Lambda$, $\pi_1=\Lambda$ |
| the centre $\mathbb{R}(ie_t)$ | $1$ | $\mathbb{R}$ | $\mathbb{R}$ | $a\mathbb{Z}$ | $S^1$, $\pi_1=\mathbb{Z}$ |
| a compact line | $1$ | $\mathbb{R}$ | $\mathbb{R}$ | $a\mathbb{Z}$ | $S^1$, $\pi_1=\mathbb{Z}$ |
| a mixed line | $1$ | $\mathbb{R}$ | $\mathbb{R}$ | $a\mathbb{Z}$ | $S^1$, $\pi_1=\mathbb{Z}$ |
| $\mathfrak u(2)$ | $4$ | $SU(2)\times\mathbb{R}$ | $(\mathbb{Z}/2)\times\mathbb{R}$ | $\langle(-I,\tfrac12)\rangle$, $\{I\}\times a\mathbb{Z}$ | $U(2)$, $\pi_1=\mathbb{Z}$; $SU(2)\times S^1$, $\pi_1=\mathbb{Z}$ |

Three entries deserve a word.

- $\mathfrak{su}(2)$ is simple and compact, so its simply connected group is $SU(2)$ and its centre is $\{\pm I\}$, and there are exactly two connected groups, $SU(2)$ and $SO(3)$. This is the two-to-one cover of rotations, and it is the model for all the others.
- $\mathfrak u(2)$ is not semisimple, and its simply connected group is the product $SU(2)\times\mathbb{R}$. The map $(A,t)\mapsto e^{i\pi t}A$ is a surjection onto $U(2)$ whose kernel is generated by $(-I,\tfrac12)$, an infinite cyclic subgroup; so $U(2)$ is the quotient of the product by a discrete central subgroup, its fundamental group is $\mathbb{Z}$, and its centre is the circle $\{\lambda I:|\lambda|=1\}$.
- The abelian plane is the Cartan of $\mathfrak u(2)$ and behaves exactly as the Cartan of the split form does: simply connected group $\mathbb{R}^2$, centre $\mathbb{R}^2$, quotients the cylinders and the tori.

**The twofold covers.** Two entries are the covers that matter in geometry:

$$
SU(2)\longrightarrow SO(3),\qquad \widetilde{SL}(2,\mathbb{R})\longrightarrow SL(2,\mathbb{R})\longrightarrow PSL(2,\mathbb{R}).
$$

The first is the quotient by the centre $\{\pm I\}$ of the compact form, and it is the double cover of the rotation group. The second is the pair of quotients of the cover of the split form, by $2\mathbb{Z}$ and by $\mathbb{Z}$. The geometric realisation of the first is the action of $SU(2)$ on $\mathbb{R}^3$ by rotations, and the realisation of the second is the action of $SL(2,\mathbb{R})$ on the hyperbolic plane; both are computed in [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), and the group theory of this section is what makes those actions well defined.

**Warning (the algebra does not determine the group).** $\mathfrak{sl}(2,\mathbb{R})$ is the algebra of three connected groups and of infinitely many of their quotients, and $\mathfrak{su}(2)$ is the algebra of two. The choice of the discrete central subgroup is extra data, invisible to the algebra, and the fundamental group of the group is that subgroup. The two tables above list the connected groups with each of these algebras as far as the discrete central subgroups are tabulated, and the list is short only because the algebras are small; the row for $\mathfrak{gl}(2,\mathbb{R})$ shows that even a four-dimensional algebra has infinitely many connected groups.

**Remark (why the group layer is the useful one).** The algebras in the two tables are the same three or four algebras in both forms, and the groups are different. The compact form gives $SU(2)$, a compact group with finite centre; the split form gives $\widetilde{SL}(2,\mathbb{R})$, a non-compact group with infinite centre. The difference is invisible in the brackets and it is the first thing one needs in an application: every irreducible representation of $SU(2)$ is finite dimensional, and the unitary dual of $\widetilde{SL}(2,\mathbb{R})$ is not, and the reason is the centre and the topology, not the bracket.

## Comparison of the Two Real Forms

**What they share.** Both are four-dimensional real algebras, central simple, with centre $\mathbb{R}e_t$, and both have the same complexification, namely $M_2(\mathbb{C})\oplus M_2(\mathbb{C})$ read as a complex algebra. Both contain the real line $\mathbb{R}e_t$ and copies of $\mathbb{C}$, and both contain a copy of the three-dimensional simple algebra, in different real forms. Both are fixed sets of real structures of one complex algebra, related by an inner twist.

**Where they differ.** The comparison is collected in one table.

| feature | split form $M_2(\mathbb{R})$ | compact form $\mathbb{H}$ |
|---|---|---|
| division | no: the idempotent $\tfrac12(e_t+i\vec e_x)$ is a zero divisor | yes |
| associative subalgebras | six types, three continuous families | four types, one sphere of copies of $\mathbb{C}$ |
| two-dimensional associative subalgebras | $\mathbb{R}\oplus\mathbb{R}$, $\mathbb{C}$, dual numbers | $\mathbb{C}$ only |
| nilpotents | yes, $\mathbb{R}N$ | none |
| Lie algebra | $\mathfrak{gl}(2,\mathbb{R})$, centre $\mathbb{R}I$ | $\mathfrak u(2)$, centre $\mathbb{R}(ie_t)$ |
| the star inside the simple part | fixes $i\vec e_x$ and $i\vec e_z$, negates $\vec e_y$: two Hermitian generators | negates all three: no Hermitian generator |
| simple part | $\mathfrak{sl}(2,\mathbb{R})$, signature $(2,1)$ | $\mathfrak{su}(2)$, signature $(0,3)$ |
| Killing form of the full algebra | indefinite, degenerate | negative semidefinite, degenerate |
| Jordan algebra | $M_2(\mathbb{R})^{+}$, with the idempotent $\tfrac12(e_t+i\vec e_x)$ | $\mathbb{H}^{+}$, no nontrivial idempotent |
| Jordan types, by signature | eight, including $H_2(\mathbb{R})$ | four, no formally real type |
| intersections with the six subspaces | $1,3,2,2,3,1$ | $1,3,4,0,1,3$ |
| simply connected group of the simple part | $\widetilde{SL}(2,\mathbb{R})$, centre $\mathbb{Z}$ | $SU(2)$, centre $\mathbb{Z}/2$ |
| fundamental group | $\pi_1(SL(2,\mathbb{R}))=\mathbb{Z}$ | $\pi_1(SO(3))=\mathbb{Z}/2$ |

**The one-line summary.** The two forms differ in three places and agree everywhere else: they differ in the presence of zero divisors, which is the algebraic difference; in the sign of the Killing form, which is the Lie difference; and in the idempotents of the Jordan algebra, which is the Jordan difference. All three are one difference seen three times, and it is the sign of the square of an element, $+e_t$ in the split form and $-e_t$ in the compact form. In the ambient language the same difference is the sign under the star: the compact form is the anti-Hermitian subspace $\mathbb{B}_{\Phi}=\mathfrak u(2)$, whose simple part $\mathfrak{su}(2)$ has three anti-Hermitian generators and the signature $(0,3)$, while the split form is the real form in which the star fixes two of the three generators and the signature is $(2,1)$. The two signatures are two counts of Hermitian directions, and the sign of the square and the sign under the star are the same sign read in the two layers.

**The internal thread.** The three differences have a common witness, and the witness is an element $U$ with $U^2=+e_t$, that is $i\vec e_x$ or $i\vec e_z$; $U$ itself is not an idempotent, since $U\notin\mathbb{R}e_t$. From $U$ one builds the idempotent $P=\tfrac12(e_t+U)$, and the three layers read the pair $(U,P)$ differently. In the associative layer $P$ is a genuine idempotent, so $M_2(\mathbb{R})$ has zero divisors and $\mathbb{H}$ has none. In the Lie layer $U$ is a generator with positive Killing self-pairing, $K(U,U)>0$, which is the sign that makes the signature $(2,1)$ of the split form and $(0,3)$ of the compact form. In the Jordan layer $P$ is again an idempotent, so the split form has a formally real part and an idempotent count that the compact form cannot match. The two forms are the two answers to the single question of whether an element $U$ with $U^2=+e_t$ exists, and the rest of the classification follows from that answer.

## What the Lattices and the Groups Do Not Determine

**The Jordan lattice does not determine the Jordan algebra.** The Jordan lattices of $M_2(\mathbb{R})^{+}$ and of $\mathbb{H}^{+}$ are both the lattice of subspaces of a three-dimensional real vector space, so they are isomorphic as lattices; the algebras are not isomorphic, because one has a nontrivial idempotent and the other does not. This is the cleanest instance of the failure in the article, and it is the reason the comparison of the previous section used the quadratic form and not only the lattice.

**The associative lattice does not determine the algebra.** At the associative level the statement is standard and is quoted here without proof: the lattice of subalgebras records only the inclusions between subspaces closed under multiplication, and two non-isomorphic algebras can have isomorphic lattices. The Jordan example above is the version of the statement that this article verifies in full, since both lattices there are exhibited explicitly.

**The Jordan lattice does not determine the Lie structure.** The same Grassmannian arises from the split form and from the compact form, and the two Lie algebras are $\mathfrak{gl}(2,\mathbb{R})$ and $\mathfrak u(2)$, with different real forms of the simple part and different signatures. A classification in the Jordan layer says nothing about the Lie layer, in either direction.

**The Lie lattice does not determine the group.** The algebra $\mathfrak{su}(2)$ is the algebra of $SU(2)$ and of $SO(3)$, and $\mathfrak{sl}(2,\mathbb{R})$ is the algebra of $\widetilde{SL}(2,\mathbb{R})$, of $SL(2,\mathbb{R})$ and of $PSL(2,\mathbb{R})$. The passage from the algebra to a group requires the choice of a discrete central subgroup, and the fundamental group of the group is that choice. This is the tenth section read backwards.

**The six subspaces do not descend.** Each real form carries only the parts of the six subspaces that its own involution allows, and the two intersection tables are different. A statement about $\mathbb{B}_{\Psi}$ in the ambient algebra is not a statement about either real form; the correct translation is the intersection.

**Warning (three layers, three classifications).** The associative, the Lie and the Jordan structures are different structures on one underlying set, and a classification in one layer does not translate into a classification in another. The article treats them in separate sections for that reason, and the tables of the eleventh section are arranged by layer for the same reason. The single exception is the shared witness of the last paragraph of that section, and it is worth noting precisely because it is an exception: one element, three layers.

## Hand-off

**Recap.** The two real forms are the split form $M_2(\mathbb{R})=\operatorname{span}_{\mathbb{R}}\{e_t,\vec e_y,i\vec e_x,i\vec e_z\}$ and the compact form $\mathbb{H}=\operatorname{span}_{\mathbb{R}}\{e_t,\vec e_x,\vec e_y,\vec e_z\}$. The split form has six associative types with three continuous families, the Lie algebra $\mathfrak{gl}(2,\mathbb{R})$ whose simple part has signature $(2,1)$, and the Jordan algebra $M_2(\mathbb{R})^{+}$ whose lattice is a Grassmannian with an indefinite form. The compact form has four associative types with a sphere of copies of $\mathbb{C}$, the Lie algebra $\mathfrak u(2)$ with a negative semidefinite form, and the Jordan algebra $\mathbb{H}^{+}$ whose lattice is the same Grassmannian with a definite form. The involutions inside the two forms are the transpose and the quaternion conjugation, and the intersections with the six subspaces are $1,3,2,2,3,1$ and $1,3,4,0,1,3$. The Lie groups are collected in two tables, with the centre, the discrete central subgroups and the fundamental groups, and they are the application of the general correspondence to these algebras.

**Forward pointers.**

- **The complex form of $\mathbb{B}_{\mathbb{R}}$.** The complexification $M_2(\mathbb{C})\oplus M_2(\mathbb{C})$, its two central idempotents, the scalar extension of the operations treated here, and the Galois descent that recovers the two real forms from the complex one: these are the subject of the companion article on the complex form. The present article uses the complexification only to say what it is not.
- **The general Lie correspondence.** The three Lie theorems, the Baker–Campbell–Hausdorff formula, the surjectivity of the exponential map, the identification $\ker(\operatorname{Ad})=Z(G)$ and the general classification of the central quotients are in [The Lie Correspondence and the Adjoint Representation](the-lie-correspondence-and-the-adjoint-representation.html). This article cited the correspondence once, in the tenth section, and applied it.
- **The real forms of a general algebra.** The general theory of the real structures of a complex algebra, of which the two maps of the second section are the example of smallest dimension, is in [Real Forms and the Descent of an Algebra](real-forms-and-the-descent-of-an-algebra.html) and in [The Split Real Form: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$](the-split-real-form-mnr-inside-mnc.html).
- **The operator level.** The endomorphism algebras, the double centralizer and the description of $\mathbb{B}$ as an algebra of operators belong to a separate series and are not used here.

**Closing.** The rotation groups, the Lorentz group and the conformal group are all read off from algebras of the shape treated here, and the reason the reading is unambiguous is that the algebra, the real form, the discrete central subgroup and the real structure are each named separately. The algebraic foundation is what makes those applications well defined, and the two tables of the tenth section are the record of the choices involved.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra over $\mathbb{C}$, complex dimension four |
| $\mathbb{B}_{\mathbb{R}}$ | the same multiplication read over $\mathbb{R}$, real dimension eight |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the base, with $\vec e_k^{\,2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$ |
| $\sigma_{\mathrm{comp}}$ | the coefficient conjugation, fixed set $\mathbb{H}$ |
| $\sigma_{\mathrm{split}}$ | the inner twist by $\vec e_y$, fixed set $M_2(\mathbb{R})$ |
| $M_2(\mathbb{R})$ | $\operatorname{span}_{\mathbb{R}}\{e_t,\vec e_y,i\vec e_x,i\vec e_z\}$, the split form |
| $\mathbb{H}$ | $\operatorname{span}_{\mathbb{R}}\{e_t,\vec e_x,\vec e_y,\vec e_z\}=\mathbb{B}_H$, the compact form |
| $I,J,\sigma_1,\sigma_3$ | the images of $e_t,\vec e_y,i\vec e_x,i\vec e_z$ in the Pauli dictionary |
| $\mathfrak{gl}(2,\mathbb{R})$, $\mathfrak{sl}(2,\mathbb{R})$ | the Lie algebra of the split form and its traceless part |
| $\mathfrak u(2)$, $\mathfrak{su}(2)$ | the Lie algebra of the compact form and its traceless part |
| $\mathfrak{b}_0$, $\mathfrak{b}$, $\mathfrak{h}$ | the Borel of $\mathfrak{sl}(2,\mathbb{R})$, the Borel of $\mathfrak{gl}(2,\mathbb{R})$, the Cartan subalgebra |
| $\mathfrak{so}(2)$ | the line $\mathbb{R}\vec e_y$ |
| $N$ | the nilpotent $\tfrac12(i\vec e_x-\vec e_y)$; the two-dimensional Borel is $\mathfrak{b}_0=\operatorname{span}\{H',N\}$ |
| $H'$, $J'$ | hyperbolic and elliptic generators, $H'$ conjugate to $\sigma_3$ up to scale, $J'$ a complex structure conjugate to $J$ |
| $\tilde X\circ\tilde Y$ | $\tfrac12(\tilde X\tilde Y+\tilde Y\tilde X)$, the Jordan product |
| $Q(U)$ | $\tfrac12\operatorname{tr}(U^2)$, the trace form on the traceless part |
| $K(X,Y)$ | the Killing form, computed in the algebra itself |
| $S^2$ | the pure units of $\mathbb{H}$, the parameter space of the copies of $\mathbb{C}$ |
| $\widetilde{G}$, $\Gamma$ | the simply connected cover and a discrete central subgroup |
| $\pi_1$ | the fundamental group, equal to $\Gamma$ for $G=\widetilde{G}/\Gamma$ |

## Further Reading

- Nicolas Bourbaki, *Algèbre*, chapters II and III (Hermann, 1962), and *Groupes et algèbres de Lie*, chapters I and II, for the structure of matrix algebras and division algebras and for the correspondence between Lie algebras and Lie groups.
- Ferdinand Georg Frobenius, *Über lineare Substitutionen und bilineare Formen*, Journal für die reine und angewandte Mathematik 84 (1878), for the classification of the real division algebras.
- Joseph Henry Maclagan Wedderburn, *On hypercomplex numbers*, Proceedings of the London Mathematical Society 6 (1908), for the structure theorem for finite-dimensional algebras.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for the involutions of the first and second kind, the transpose and the quaternion conjugation as the two classical cases, and the real forms of a central simple algebra.
- Arkadij L. Onishchik and Ernest B. Vinberg, *Lie Groups and Algebraic Groups* (Springer, 1990), for the subalgebras and closed subgroups of the classical groups, including the complete lists for $SL(2,\mathbb{R})$ and $SU(2)$.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (American Mathematical Society, 2001), for the Cartan decomposition, the Killing form and its signature, and the twofold covers of the classical groups.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, second edition, 2001), for the theorem of Frobenius and the arithmetic of the quaternions.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras*, American Mathematical Society Colloquium Publications 39 (1968), for the Jordan product, the identity $XY+YX=\operatorname{tr}(XY)I$ in degree two, and the formally real algebras.
