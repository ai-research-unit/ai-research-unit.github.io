# __The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure__

## Introduction

An algebra acts on itself in two ways at once: from the left, $z\mapsto xz$, and from the right, $z\mapsto zy$. The corpus studies the two families of operators in *One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* and *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*, and it uses their commuting product in *The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint*. What the corpus does not yet carry is the **algebra** in which the pair of actions naturally lives. That algebra is the **enveloping algebra**

$$
\mathbb B^{\mathrm e} = \mathbb B\otimes_{\mathbb C}\mathbb B^{\mathrm{op}},
$$

the tensor product of the algebra with its opposite, and the pair of actions is the single left action of $\mathbb B^{\mathrm e}$ on $\mathbb B$,

$$
(x\otimes y^{\mathrm{op}})\cdot z = x\,z\,y .
$$

This article develops that algebra for the biquaternion algebra. There are two results. The first is that the enveloping algebra is the **whole endomorphism algebra** of the biquaternion algebra as a complex vector space,

$$
\mathbb B^{\mathrm e}\cong \operatorname{End}_{\mathbb C}(\mathbb B)\cong M_4(\mathbb C),
$$

so that the left action of $\mathbb B^{\mathrm e}$ on $\mathbb B$ is faithful and exhausts the linear operators. The second is the reading that follows: the left multiplications $L_x=x\otimes\mathbb 1^{\mathrm{op}}$ and the right multiplications $R_y=\mathbb 1\otimes y^{\mathrm{op}}$ are **two commuting copies of $\mathbb B$ and $\mathbb B^{\mathrm{op}}$ inside one endomorphism algebra**, of the same algebraic type, and the biquaternion algebra is a **bi-module** over the pair. The corpus's recorded question of which of the two actions is the physical matter representation then has a precise algebraic location: the question is not about the existence of one action or the other, since both are present and of the same type, but about which factor of the enveloping algebra a given physical degree of freedom uses.

The article is pure algebra. The one-sided and two-sided operators are *One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* and *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*; the general operator theory of an algebra is *The Operators on an Algebra*, whose left and right multiplications and whose double centraliser are the starting point here; the modules and the standard bi-module $_{\mathbb B}S_{\mathbb C}$ are *Modules over the Biquaternion Algebra*; and the spectral consequences of the Kronecker-product form of the two actions are *The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint*.

## The Two Regular Representations

The ground is the pair of regular representations, recalled with the corpus's notation.

**Definition.** For $a\in\mathbb B$ let

$$
L_a\colon \mathbb B\to\mathbb B,\quad L_a(z)=az,\qquad
R_a\colon \mathbb B\to\mathbb B,\quad R_a(z)=za .
$$

Both are $\mathbb C$-linear, and both assignments are injective, because $L_a(\mathbb 1)=a$ and $R_a(\mathbb 1)=a$.

**Proposition (the composition laws).** For all $a,b\in\mathbb B$,

$$
L_aL_b=L_{ab},\qquad R_aR_b=R_{ba},\qquad L_aR_b=R_bL_a .
$$

*Proof.* $(L_aL_b)(z)=a(bz)=(ab)z=L_{ab}(z)$; $(R_aR_b)(z)=(zb)a=z(ba)=R_{ba}(z)$; and $(L_aR_b)(z)=a(zb)=(az)b=(R_bL_a)(z)$. The last identity is associativity and needs no commutativity.

So the map $L\colon a\mapsto L_a$ is an algebra **homomorphism** of $\mathbb B$ into $\operatorname{End}_{\mathbb C}(\mathbb B)$, while $R\colon a\mapsto R_a$ is an algebra **anti**-homomorphism, whose image is therefore a copy of the opposite algebra $\mathbb B^{\mathrm{op}}$. The two families commute elementwise. This is the whole content of the two-sided operator $\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde{Q}^{*}}$ of the corpus, decomposed into its two factors.

**Theorem (the double centraliser).** The commutant of the left multiplications is exactly the right multiplications, and likewise with the roles exchanged:

$$
\{T\in\operatorname{End}_{\mathbb C}(\mathbb B) : T\,L_a=L_a\,T\ \ \forall a\}=\{R_b\}_{b\in\mathbb B},\qquad
\{T : T\,R_b=R_b\,T\ \ \forall b\}=\{L_a\}_{a\in\mathbb B},
$$

and the bicommutant is the centre, $\{T: T\,\text{commutes with all }L_a\text{ and all }R_b\}=\mathbb C_{\mathbb B}=\mathbb C\cdot\mathbb 1$. Consequently $L_{\mathbb B}$ and $R_{\mathbb B}$ are mutual commutants, each of complex dimension four.

*Proof.* This is the double centraliser of *Modules over the Biquaternion Algebra* and *The Operators on an Algebra*, specialised to the regular module: $\operatorname{End}_{\mathbb B}(\mathbb B)=R_{\mathbb B}\cong\mathbb B^{\mathrm{op}}$, and the commutant of $R_{\mathbb B}$ is $\operatorname{End}_{\mathbb B^{\mathrm{op}}}(\mathbb B)=L_{\mathbb B}$; the operators commuting with both are the $\mathbb B$-$\mathbb B$-linear endomorphisms of $\mathbb B$, which are the scalars, since $\mathbb B$ is a simple algebra with centre $\mathbb C$. Verified on the four basis elements and on random elements.

The double centraliser theorem says that $\{L_a\}$ and $\{R_b\}$ are as large as two families can be while commuting. It does **not** yet say that together they generate every linear operator; that is the enveloping-algebra statement of the next section.

## The Enveloping Algebra

**Definition.** The **enveloping algebra** of $\mathbb B$ over $\mathbb C$ is

$$
\mathbb B^{\mathrm e} = \mathbb B\otimes_{\mathbb C}\mathbb B^{\mathrm{op}},
$$

with multiplication the tensor product of the multiplications, $(x\otimes y^{\mathrm{op}})(x'\otimes y'^{\mathrm{op}})=xx'\otimes(y y')^{\mathrm{op}}$, and unit $\mathbb 1\otimes\mathbb 1^{\mathrm{op}}$. It has complex dimension $16$.

**Definition (the action).** The algebra $\mathbb B^{\mathrm e}$ acts on $\mathbb B$ by the **sandwich action**

$$
(x\otimes y^{\mathrm{op}})\cdot z = x\,z\,y .
$$

**Proposition (the action is a left action).** The sandwich action is $\mathbb C$-linear in $z$, and

$$
\bigl((x\otimes y^{\mathrm{op}})(x'\otimes y'^{\mathrm{op}})\bigr)\cdot z = (x\otimes y^{\mathrm{op}})\cdot\bigl((x'\otimes y'^{\mathrm{op}})\cdot z\bigr),\qquad
(\mathbb 1\otimes\mathbb 1^{\mathrm{op}})\cdot z = z .
$$

*Proof.* The right-hand side is $x(x'zy')y=x x'\,z\,y'y=((xx')\otimes(yy')^{\mathrm{op}})\cdot z$, the left-hand side by the definition of the product in $\mathbb B^{\mathrm e}$. The unit is immediate. Verified on the basis.

**Proposition (the two regular representations inside $\mathbb B^{\mathrm e}$).** Under the sandwich action,

$$
(x\otimes\mathbb 1^{\mathrm{op}})\cdot z = xz = L_x(z),\qquad
(\mathbb 1\otimes y^{\mathrm{op}})\cdot z = zy = R_y(z).
$$

So the left and right multiplications are the two "one-sided" elements of the enveloping algebra, obtained by putting the unit in the unused factor. In particular the assignment $a\mapsto a\otimes\mathbb 1^{\mathrm{op}}$ is an algebra homomorphism $\mathbb B\to\mathbb B^{\mathrm e}$, and $a\mapsto\mathbb 1\otimes a^{\mathrm{op}}$ is one $\mathbb B^{\mathrm{op}}\to\mathbb B^{\mathrm e}$, and their images commute — the abstract form of $L_aR_b=R_bL_a$.

**Theorem (the enveloping algebra is the endomorphism algebra).** The sandwich action defines an isomorphism of $\mathbb C$-algebras

$$
\mathbb B^{\mathrm e}=\mathbb B\otimes_{\mathbb C}\mathbb B^{\mathrm{op}}\longrightarrow\operatorname{End}_{\mathbb C}(\mathbb B),\qquad x\otimes y^{\mathrm{op}}\mapsto\bigl(z\mapsto xzy\bigr),
$$

so that $\mathbb B^{\mathrm e}\cong M_4(\mathbb C)$ and the left action of $\mathbb B^{\mathrm e}$ on $\mathbb B$ is faithful and exhausts all $\mathbb C$-linear operators on $\mathbb B$.

*Proof.* Both sides have complex dimension $16$, so it suffices that the map is injective. Let $\sum_i x_i\otimes y_i^{\mathrm{op}}$ act as zero: $\sum_i x_i z y_i=0$ for all $z\in\mathbb B$. Taking $z$ running over a basis of matrix units $E_{ab}$ of $\mathbb B\cong M_2(\mathbb C)$ and using the independence of the $E_{ab}$ gives $\sum_i x_i\otimes y_i^{\mathrm{op}}=0$, so the kernel is trivial. A linear injection between spaces of equal finite dimension is an isomorphism. The endomorphism algebra of the four-dimensional complex space $\mathbb B$ is $M_4(\mathbb C)$. Verified numerically: the $\mathbb R$-span of the $64$ operators $L_xR_y$ with $x,y$ running over a real basis of $\mathbb B$ has real dimension $32$, which is $\dim_{\mathbb R}\operatorname{End}_{\mathbb C}(\mathbb B)=2\cdot 16$, and the $64$ elements $x_i\otimes y_j^{\mathrm{op}}$ on a $\mathbb C$-basis are linearly independent.

**Corollary (the two-sided operators are the elementary tensors).** The two-sided operator $\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde{Q}^{*}}$ is the image of the elementary tensor $\tilde Q\otimes(\tilde{Q}^{*})^{\mathrm{op}}$, and the mixed operators $L_aR_b$ are the images of $a\otimes b^{\mathrm{op}}$. The corpus's two-sided family is therefore the set of **rank-one** (elementary) elements of the enveloping algebra, a small subset of it.

## The Conway Operator Basis

The isomorphism $\mathbb B^{\mathrm e}\cong\operatorname{End}_{\mathbb C}(\mathbb B)$ is abstract: it manufactures operators from tensors without exhibiting a basis of the operator space. The basis is classical, and it is what makes the isomorphism usable in coordinates. Following Hamilton, write $e_n[\,]e_m$ for the elementary operator that puts the argument between the two units,

$$
(e_n[\,]e_m)(z)=e_n\,z\,e_m ,
$$

the empty brackets marking the slot; Conway and Synge named the calculus that uses it. In the sandwich picture $e_n[\,]e_m$ is the image of the elementary tensor $e_n\otimes e_m^{\mathrm{op}}$, so the sixteen operators are the images of a tensor basis and the main theorem gives at once:

**Proposition (the Conway operators are a basis).** The sixteen operators $e_n[\,]e_m$, $n,m\in\{0,1,2,3\}$, are a $\mathbb C$-basis of $\operatorname{End}_{\mathbb C}(\mathbb B)$: every $\mathbb C$-linear function is uniquely

$$
F( )=\sum_{n,m=0}^{3}z_{nm}\,e_n[\,]e_m ,
\qquad z_{nm}\in\mathbb C .
$$

*Proof.* The elementary tensors $e_n\otimes e_m^{\mathrm{op}}$ are a basis of $\mathbb B\otimes_{\mathbb C}\mathbb B^{\mathrm{op}}$ and the sandwich map is an isomorphism, so their images are a basis. Verified numerically: the $16\times16$ matrix of the sixteen operators in the coordinate basis of $\mathbb B$ has rank $16$.

In this notation the two regular representations are the two **edge rows** of the basis, the ones that carry the unit in the unused slot,

$$
L_a=\sum_{n=0}^{3}a_n\,e_n[\,]e_0,\qquad R_b=\sum_{m=0}^{3}b_m\,e_0[\,]e_m ,
$$

which is the coordinate form of $L_a=a\otimes\mathbb 1^{\mathrm{op}}$ and $R_b=\mathbb 1\otimes b^{\mathrm{op}}$.

**Proposition (the composition rule).** For all $a,b,c,d\in\mathbb B$,

$$
(a[\,]b)\circ(c[\,]d)=(ac)[\,](db) .
$$

*Proof.* $\bigl(a[\,]b\bigr)\bigl((c[\,]d)(z)\bigr)=a\,c\,z\,d\,b=(ac)z(db)$. Verified on random operators to $10^{-13}$. In the unit basis the rule expands as $e_n[\,]e_m\circ e_p[\,]e_q=(e_ne_p)[\,](e_qe_m)$, whose right-hand side is a linear combination of basis operators through the multiplication table of the imaginary units.

**Remark (the regular matrices).** In the coordinate basis of $\mathbb B$ the operator $e_n[\,]e_m$ is the matrix product $\rho_L(e_n)\rho_R(e_m)$ of the left and right regular matrices of *Biquaternion 4×4 Regular Matrix Element Representation*, and those sixteen products are an orthogonal basis of $M_4(\mathbb C)$ there. The Conway basis and that matrix basis are the same sixteen operators; the one is written as a linear function, the other as a matrix.

### The Three Classical Functions and Their Matrices

Three linear functions carry the classical matrix types. In the coordinate order $(e_1,e_2,e_3,e_0)$ — vector part first, scalar last — they are, with $t_1=s_2s_3$, $t_2=s_1s_3$ and $t_3=s_1s_2$,

$$
A\{a\}=\tfrac12\bigl(a[\,]-[\,]a\bigr)\ \longleftrightarrow\
\begin{pmatrix}0&-a_3&a_2&0\\a_3&0&-a_1&0\\-a_2&a_1&0&0\\0&0&0&0\end{pmatrix},
$$

$$
D\{d\}=\tfrac12\bigl(d_1e_1[\,]e_1+d_2e_2[\,]e_2+d_3e_3[\,]e_3\bigr)
\ \longleftrightarrow\
\tfrac12\begin{pmatrix}-d_1+d_2+d_3&0&0&0\\0&d_1-d_2+d_3&0&0\\0&0&d_1+d_2-d_3&0\\0&0&0&-(d_1+d_2+d_3)\end{pmatrix},
$$

$$
S\{s\}=D\{s_1^2,s_2^2,s_3^2\}-\tfrac12\,s[\,]s
\ \longleftrightarrow\
\begin{pmatrix}0&t_3&t_2&0\\t_3&0&t_1&0\\t_2&t_1&0&0\\0&0&0&0\end{pmatrix}.
$$

**Proposition (the matrix dictionary).** In the order $(e_1,e_2,e_3,e_0)$ the function $A\{a\}$ is the antisymmetric $3\times3$ block, $D\{d\}$ the traceless diagonal and $S\{s\}$ the diagonal-less symmetric $3\times3$ block, each with a vanishing fourth row and column, and the three families together span the traceless part of $M_3(\mathbb C)$.

*Proof.* Direct computation of the sixteen operator matrices and comparison with the displays. The coordinate order is a genuine trap: the corpus's basis order is $(e_0,e_1,e_2,e_3)$, whereas the matrix displays put the scalar last, and in the corpus's order the same matrices appear shifted by one. Verified numerically: exact in the order $(e_1,e_2,e_3,e_0)$, and not in the order $(e_0,e_1,e_2,e_3)$.

**Remark (the source's sign).** The source writes the symmetric function with the two terms in the opposite order, $S\{s\}=\tfrac12 s[\,]s-D\{s_1^2,s_2^2,s_3^2\}$; its two displays of $S$ then differ by an overall sign. The corpus fixes the sign by the printed matrix, the one written here. $A\{a\}$ and $D\{d\}$ reproduce the source's displays exactly, with zero residual.

### Function Association and the Adjoint

The operator picture has a second involution besides the dagger, and it is the one that makes a linear function transposable.

**Definition (function association).** Let $\mathrm{Sc}$ be the scalar part and $B(X,Y)=\mathrm{Sc}(XY)$ the scalar bilinear form. The **associate** $F^{\approx}$ of a linear function $F$ is defined by

$$
\mathrm{Sc}\bigl(F(X)\,Y\bigr)=\mathrm{Sc}\bigl(X\,F^{\approx}(Y)\bigr)
\qquad\text{for all }X,Y\in\mathbb B ,
$$

equivalently $B(FX,Y)=B(X,F^{\approx}Y)$.

**Proposition (association reverses the factors).** On the Conway basis

$$
\bigl(e_n[\,]e_m\bigr)^{\approx}=e_m[\,]e_n ,
\qquad\text{so}\qquad
\Bigl(\sum_{n,m}z_{nm}\,e_n[\,]e_m\Bigr)^{\approx}=\sum_{n,m}z_{nm}\,e_m[\,]e_n ,
$$

and in particular $\bigl(a[\,]b\bigr)^{\approx}=b[\,]a$, so that $L_a^{\approx}=R_a$ and $R_b^{\approx}=L_b$. Association is the transpose with respect to $B$.

*Proof.* $B\bigl((a[\,]b)(X),Y\bigr)=\mathrm{Sc}(aXbY)=\mathrm{Sc}(XbYa)=B\bigl(X,(b[\,]a)(Y)\bigr)$ by the invariance of the scalar part under cyclic permutation, and $B$ is non-degenerate. Verified for all sixteen basis operators, residual $2\cdot10^{-15}$.

**Proposition (the form and its Gram matrix).** The scalar bilinear form is

$$
B(X,Y)=X_0Y_0-X_1Y_1-X_2Y_2-X_3Y_3 :
$$

symmetric, non-degenerate and **indefinite**, of signature $(1,3)$, with Gram matrix $D=\operatorname{diag}(1,-1,-1,-1)$ in the basis $e_0,e_1,e_2,e_3$. The transpose with respect to $B$ is therefore

$$
F^{\approx}=D\,F^{\mathsf T}D ,
$$

for $F^{\mathsf T}$ the plain matrix transpose, and the two agree exactly when $D$ acts trivially, in particular for the operators that fix $e_0$ and preserve the vector part. Verified on random operators, to machine precision.

**Proposition (coefficient conjugation and the Hermitian adjoint).** Let $\bar F( )=\sum\bar z_{nm}e_n[\,]e_m$ be the function obtained by conjugating the coefficients, and let $F^{*}$ be the adjoint of $F$ with respect to the Hermitian form $(\tilde X,\tilde Y)=\mathrm{Sc}(\tilde{X}^{*}\tilde Y)=\sum_\mu\tilde X_\bar{\mu}\tilde Y_\mu$ of *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*, $(\tilde F(X),Y)=(X,F^{*}(Y))$. Then

$$
\bar F^{\approx}=D\,F^{*}D .
$$

On the operators that fix $e_0$ and preserve the vector part — among them every $\mathrm{SU}(3)$ and $\mathrm{SU}(4)$ element of *Biquaternion Lie Group and Exponential Structure* — the matrix has no entries mixing the scalar slot with the vector slots, the conjugation by $D$ is invisible, and the identity collapses to

$$
\bar F^{\approx}=F^{*}=F^{-1}\qquad\text{for unitary }F ,
$$

which is the source's $G^{-1}=G^{+\approx}=G^{\dagger}$.

*Proof.* The Gram matrix of $(\cdot,\cdot)$ is the identity while that of $B$ is $D$, so the two transposes differ by a conjugation by $D$ on both sides, and conjugating the coefficients turns the transpose with respect to $B$ into the adjoint with respect to $(\cdot,\cdot)$, again up to $D$. For a unitary $F$ the adjoint is the inverse. Verified numerically: $F^{\approx}=DF^{\mathsf T}D$ on random operators, and $\bar F^{\approx}=F^{*}$ on the $\mathrm{SU}(3)$ elements, both to machine precision.

**Remark (why the source's rule is safe there).** The source's group elements all fix the scalar unit and map the vector part to itself, so $D$ has no visible effect on their block form; this is why the source may use the plain transpose and the Hermitian adjoint interchangeably. For a general linear function the two involutions differ, and the corpus keeps them apart: association is the transpose for the **indefinite** scalar form, the dagger is the adjoint for the **positive Hermitian** form.

### The Limit of the Method

The quaternion formulation of the classical matrix types is complete in dimension three and incomplete in dimension four, and the reason is visible in the displays above.

**Remark (the method degrades from three to four dimensions).** The antisymmetric, diagonal and diagonal-less symmetric functions exhaust the traceless part of $M_3(\mathbb C)$ in the order $(e_1,e_2,e_3,e_0)$, since each acts on the vector part and fixes the scalar. For a general traceless $\mathbb C^4\to\mathbb C^4$ map the same three families no longer suffice: the symmetric part needs a function that mixes the scalar and vector parts, and the source records that the expression for it is cumbersome and not useful. The four-dimensional unitary groups are therefore assembled from two $SO(4)$ factors rather than from a single quaternion closed form — the same asymmetry that the Lie-group article reads as the clean three-dimensional and less clean four-dimensional parametrizations.

## The Base Field and the Real Dimension Count

The isomorphism of the theorem is over $\mathbb C$, and the choice matters.

**Remark (over $\mathbb R$ the action is not faithful).** Regard $\mathbb B$ as a **real** algebra, $\dim_{\mathbb R}\mathbb B=8$, so that $\mathbb B\otimes_{\mathbb R}\mathbb B^{\mathrm{op}}$ has real dimension $64$, the same as $\operatorname{End}_{\mathbb R}(\mathbb B)$. The sandwich map $\mathbb B\otimes_{\mathbb R}\mathbb B^{\mathrm{op}}\to\operatorname{End}_{\mathbb R}(\mathbb B)$, $x\otimes y\mapsto(z\mapsto xzy)$, is then **not** injective: its image is only the space of $\mathbb C$-linear operators, of real dimension $32$, and the kernel has real dimension $32$. The reason is that the central scalar $i$ is already in the algebra: the element $i\otimes\mathbb 1^{\mathrm{op}}-\mathbb 1\otimes i^{\mathrm{op}}$ acts as $z\mapsto iz-zi=0$, and the kernel is exactly the span of its image, that is the real $32$-dimensional space $\{ix\otimes y^{\mathrm{op}}-x\otimes(iy)^{\mathrm{op}}\}$. The complex base field removes exactly this redundancy, which is why the theorem above is stated over $\mathbb C$.

*Proof.* The image operators are $\mathbb C$-linear because $x$, $y$ commute with the scalar $i$, so the image is contained in $\operatorname{End}_{\mathbb C}(\mathbb B)$ of real dimension $32$, and $64-32=32$ is therefore an upper bound for the kernel; the element $i\otimes\mathbb 1^{\mathrm{op}}-\mathbb 1\otimes i^{\mathrm{op}}$ acts as zero, and the numerical rank computation below shows that the span of its image already has dimension $32$, so the bound is attained and the kernel is exactly that span.

**Remark (the general statement).** For $A=M_n(k)$ over a field $k$, the same proof gives $A^{\mathrm e}=A\otimes_kA^{\mathrm{op}}\cong\operatorname{End}_k(A)\cong M_{n^2}(k)$, and the enveloping action is faithful. The result is the matrix case of the general fact that a finite-dimensional **central simple** algebra is a faithful $A^{\mathrm e}$-module and $A^{\mathrm e}\cong\operatorname{End}_k(A)$; it fails for a commutative algebra with nilpotents, where $x\otimes\mathbb 1^{\mathrm{op}}-\mathbb 1\otimes x^{\mathrm{op}}$ can act as zero. The biquaternion algebra is central simple over $\mathbb C$, so the theorem applies with $n=2$.

## The Bi-module Structure

**Definition.** A $\mathbb B$-$\mathbb B$**-bi-module** is a complex vector space $M$ carrying a left $\mathbb B$-action and a right $\mathbb B$-action that commute: $(x\cdot m)\cdot y=x\cdot(m\cdot y)$ for all $x,y\in\mathbb B$, $m\in M$. The algebra $\mathbb B$ itself, with the left and right multiplications, is the **regular bi-module** ${}_{\mathbb B}\mathbb B_{\mathbb B}$, and it is the defining example.

**Proposition (the bi-module is the enveloping module).** A $\mathbb B$-$\mathbb B$-bi-module is the same thing as a left $\mathbb B^{\mathrm e}$-module, by $(x\otimes y^{\mathrm{op}})\cdot m=x\cdot m\cdot y$. In particular the regular bi-module ${}_{\mathbb B}\mathbb B_{\mathbb B}$ is the left regular module of the enveloping algebra, $\mathbb B^{\mathrm e}\cdot\mathbb B=\mathbb B$, and it is a **generator**: the enveloping algebra is recovered as $\operatorname{End}_{\mathbb C}(\mathbb B)$.

*Proof.* The correspondence is the definition of the enveloping algebra's action; the associativity of the two commuting actions is exactly the associativity of the multiplication in $\mathbb B^{\mathrm e}$. The last statement is the theorem of the previous section read as a statement about the module.

**Theorem (the left and the right actions are of the same type).** Under the isomorphism $\mathbb B^{\mathrm e}\cong\operatorname{End}_{\mathbb C}(\mathbb B)$, both the left multiplications and the right multiplications are **left multiplications in the enveloping algebra**: $L_a$ is left multiplication by $a\otimes\mathbb 1^{\mathrm{op}}$ and $R_b$ is left multiplication by $\mathbb 1\otimes b^{\mathrm{op}}$, and the two elements commute. The two actions are therefore not of different algebraic kinds; they are two commuting copies of the same construction, the one of $\mathbb B$ and the other of its opposite.

*Proof.* Immediate from the two propositions above. The distinction between $L_a$ and $R_b$ is the distinction between the tensor factors, not a distinction in the kind of action.

This is Fauser's observation on the Daviau equation, in its abstract form. An equation on an algebra that multiplies its unknown on the left and on the right at once, such as $\nabla\varphi\,i\sigma_1=m\varphi^{*}+qA\varphi$ of *The Daviau Map and the Space Clifford Formulation of the Dirac Equation*, is a single equation in the enveloping algebra; the two-sidedness is not an awkwardness of the formulation but the bi-module structure of the algebra acting on itself.

## The Left-versus-Right Question

The corpus records, in *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*, an open question of the **matter representation**: whether the physical Dirac field is the left action of the algebra on itself or the right action, the two being two consistent covariant constructions. The enveloping algebra gives the algebraic part of the answer.

**What the algebra says.** The bi-module ${}_{\mathbb B}\mathbb B_{\mathbb B}$ carries **both** actions, and they commute. A covariant construction that uses the left action and one that uses the right action are not two theories between which one must choose: they are two elements of one enveloping algebra, and any statement about one can be translated into a statement about the other. The choice of which action "is" the field is therefore not an algebraic choice; the algebra offers the pair.

**What the algebra does not say.** It does not say which physical degree of freedom is carried by which factor. The embedding of the left multiplications is $a\mapsto a\otimes\mathbb 1^{\mathrm{op}}$ and of the right multiplications is $b\mapsto\mathbb 1\otimes b^{\mathrm{op}}$; the two factors are algebraically distinct but no physical label attaches to either from the algebra alone. Fauser's caution on the same point is that the identification of the right multiplication with a specific internal symmetry — the iso-spin degree of freedom — is not warranted by the algebra. The corpus records the caution and leaves the physical assignment open.

**The precise form of the remaining question.** In the enveloping algebra the question becomes: for the physical Dirac field, which factor of $\mathbb B^{\mathrm e}$ carries the spin and which the internal quantum numbers, and is the split forced by the requirement that the current be conserved? The corpus's observation that the conserved current needs the Clifford-odd $\gamma_0$ of the full spacetime algebra is a constraint of exactly this kind, and it is the natural place to look for the answer. The algebra alone closes the existence half of the question and leaves the assignment half open.

## Worked Verification

The two structural statements were checked numerically on the biquaternion algebra.

**The bi-module generators.** With the real basis $E_{00},E_{01},E_{10},E_{11},iE_{00},\dots,iE_{11}$ of $\mathbb B\cong M_2(\mathbb C)$ and the operators $L_xR_y(z)=xzy$ written as $8\times8$ real matrices, the $\mathbb R$-span of the $64$ operators has rank $32$. This is $\dim_{\mathbb R}\operatorname{End}_{\mathbb C}(\mathbb B)$, confirming that the two-sided family spans all $\mathbb C$-linear operators and that the missing $32$ real dimensions are exactly the $\mathbb R$-linear operators that fail to be $\mathbb C$-linear.

**The composition laws and the commutativity.** On the same basis, $L_aL_b-L_{ab}=0$, $R_aR_b-R_{ba}=0$ and $L_aR_b-R_bL_a=0$ hold identically, with no residual.

**The kernel over $\mathbb R$.** The $64\times64$ matrix of the element $i\otimes\mathbb 1^{\mathrm{op}}-\mathbb 1\otimes i^{\mathrm{op}}$ acting on $\mathbb B\otimes_{\mathbb R}\mathbb B$ has rank $32$; equivalently, the real span of $\{ix\otimes y^{\mathrm{op}}-x\otimes(iy)^{\mathrm{op}}\}$ has dimension $32$, which is the kernel of the real sandwich map, confirming both the non-faithfulness of the real enveloping action and the role of the complex base field.

## Open Questions

1. **The physical assignment.** Which tensor factor of $\mathbb B^{\mathrm e}$ carries the spin and which the internal quantum numbers of the physical Dirac field? The algebra settles the existence of both actions; the assignment is the remaining physical question, and the conserved-current constraint of *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism* is the natural tool.

2. **The two-sided operators as rank-one elements.** The corpus's two-sided operators $\Theta_{\tilde Q}$ are the elementary tensors $\tilde Q\otimes(\tilde{Q}^{*})^{\mathrm{op}}$. Does the corpus's classification of the two-sided operators (self-adjoint, unitary, and the rest) become the classification of elementary tensors by their factors, and does the enveloping algebra give the general operator a decomposition into such elementary pieces?

3. **The enveloping algebra and the trace.** The trace form $\operatorname{Tr}(\tilde Q_1\tilde Q_2)=2\operatorname{Sc}(\tilde Q_1\tilde Q_2)$ is the algebra's $\mathbb C$-bilinear pairing. Does it extend to a trace on $\mathbb B^{\mathrm e}\cong M_4(\mathbb C)$, and is the resulting trace the one the corpus's spectral article uses on the operators?

4. **The higher enveloping algebras.** The construction iterates: $(\mathbb B^{\mathrm e})^{\mathrm e}$ is the algebra acting on the operators on $\mathbb B$. Does the iteration terminate at the scalar matrices, and is there a chain of "enveloping" algebras with a limit that the corpus's operator theory would recognise?

5. **Comparison with the universal enveloping algebra.** The corpus's *Universal Enveloping Algebras* is the Lie-theoretic $U(\mathfrak g)$ of a Lie algebra. The two "enveloping algebras" are different constructions sharing a name; the corpus should keep them apart and cross-link them, which this article does.

## Summary

The biquaternion algebra acts on itself from the left and from the right, and the algebra in which the pair of actions lives is the **enveloping algebra** $\mathbb B^{\mathrm e}=\mathbb B\otimes_{\mathbb C}\mathbb B^{\mathrm{op}}$, with the sandwich action $(x\otimes y^{\mathrm{op}})\cdot z=xzy$. The enveloping algebra is isomorphic to the full endomorphism algebra, $\mathbb B^{\mathrm e}\cong\operatorname{End}_{\mathbb C}(\mathbb B)\cong M_4(\mathbb C)$, so the action is faithful and exhausts the $\mathbb C$-linear operators; the two-sided operators of the corpus are the elementary tensors of the enveloping algebra. The isomorphism has an explicit basis, the sixteen **Conway operators** $e_n[\,]e_m$, with $(e_n[\,]e_m)(z)=e_nze_m$ and the composition rule $(a[\,]b)\circ(c[\,]d)=(ac)[\,](db)$; the classical antisymmetric, diagonal and diagonal-less symmetric functions $A\{a\}$, $D\{d\}$ and $S\{s\}$ are the basis elements of the three matrix types, and a linear function carries a second involution, **association**, which is the transpose for the indefinite scalar form $\mathrm{Sc}(XY)$ of signature $(1,3)$ and which combines with the conjugation of the coefficients to give the Hermitian adjoint on the group elements. The left multiplications $L_a=a\otimes\mathbb 1^{\mathrm{op}}$ and the right multiplications $R_b=\mathbb 1\otimes b^{\mathrm{op}}$ are two commuting copies, in the enveloping algebra, of $\mathbb B$ and of $\mathbb B^{\mathrm{op}}$; they are of the **same** algebraic type, and the biquaternion algebra is a **bi-module** over the pair, equivalently a left module of the enveloping algebra. The corpus's left-versus-right matter-representation question is thereby split into an algebraic half, which the enveloping algebra closes — both actions are present, of the same type, and commuting — and a physical half, which is the assignment of spin and internal quantum numbers to the two tensor factors and which the algebra does not decide. The result is over $\mathbb C$; over $\mathbb R$ the sandwich map has a $32$-dimensional kernel, exactly the redundancy of the central $i$, and this confirms that the complex base field is the natural one. The construction is the abstract form of Fauser's reading of the Daviau equation, whose unknown is multiplied from both sides at once.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb B=\mathbb C\otimes_\mathbb R\mathbb H$ | Biquaternion algebra, $\cong M_2(\mathbb C)$, complex dimension $4$ |
| $L_a(z)=az$, $R_b(z)=zb$ | Left and right multiplication |
| $e_n[\,]e_m$, $(e_n[\,]e_m)(z)=e_nze_m$ | Conway operator; a basis of $\operatorname{End}_{\mathbb C}(\mathbb B)$ |
| $(a[\,]b)\circ(c[\,]d)=(ac)[\,](db)$ | The composition rule |
| $A\{a\}$, $D\{d\}$, $S\{s\}$ | The antisymmetric, diagonal and diagonal-less symmetric linear functions |
| $B(X,Y)=\mathrm{Sc}(XY)$, $D=\operatorname{diag}(1,-1,-1,-1)$ | The scalar bilinear form, indefinite of signature $(1,3)$, and its Gram matrix |
| $F^{\approx}$ | The associate of $F$; the transpose for $B$, $F^{\approx}=DF^{\mathsf T}D$ |
| $\bar F^{\approx}=DF^{*}D$; $=F^{\dagger}$ on the group elements | Association combined with conjugation, against the Hermitian adjoint |
| $L_aL_b=L_{ab}$, $R_aR_b=R_{ba}$, $L_aR_b=R_bL_a$ | The composition laws |
| $\{L_a\}'=\{R_b\}$, $\{R_b\}'=\{L_a\}$ | The double centraliser |
| $\mathbb B^{\mathrm{op}}$ | The opposite algebra |
| $\mathbb B^{\mathrm e}=\mathbb B\otimes_{\mathbb C}\mathbb B^{\mathrm{op}}$ | The enveloping algebra; $\cong M_4(\mathbb C)$ |
| $(x\otimes y^{\mathrm{op}})\cdot z=xzy$ | The sandwich action |
| $\mathbb B^{\mathrm e}\cong\operatorname{End}_{\mathbb C}(\mathbb B)$ | The main theorem |
| ${}_{\mathbb B}\mathbb B_{\mathbb B}$ | The regular bi-module; a left $\mathbb B^{\mathrm e}$-module |
| $\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde{Q}^{*}}$ | The two-sided operator; the elementary tensor $\tilde Q\otimes(\tilde{Q}^{*})^{\mathrm{op}}$ |

## Further Reading

- A. Gsponer, "Explicit closed-form parametrization of SU(3) and SU(4) in terms of complex quaternions and elementary functions," arXiv:math-ph/0211056v2, 2002, §2–4, for the Conway operators $e_n[\,]e_m$, the composition and association rules, the functions $A\{a\}$, $D\{d\}$, $S\{s\}$ and their $4\times4$ matrix displays (10′)–(13′), the rule $G^{-1}=G^{+\approx}=G^{\dagger}$ for the group elements, and the remark that the quaternion method loses power from three to four dimensions.
- A. W. Conway, "Quaternions and matrices," *Proceedings of the Royal Irish Academy* **A 50** (1945) 98–130, and J. L. Synge, "Quaternions, Lorentz transformations, and the Conway–Dirac–Eddington matrices," *Communications of the Dublin Institute for Advanced Studies* **A 21** (1972), for the Conway operator calculus in its original form.
- B. Fauser, "On the equivalence of Daviau's space Clifford algebraic, Hestenes' and Parra's formulations of (real) Dirac theory," arXiv:hep-th/9908200, 1999, §1–2, for the enveloping algebra $P^{\mathrm e}\cong P\otimes P^{\mathrm T}$, the sandwich action, the statement that the left and right actions are of the same type, and the caution on the iso-spin reading.
- The companion articles of this series: *The Operators on an Algebra*, *Modules over the Biquaternion Algebra*, *Biquaternion 4×4 Regular Matrix Element Representation*, *One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*, *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*, *The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint*, and *Universal Enveloping Algebras* (the Lie-theoretic construction, distinct from this one).
- The physics articles that use the reading: *The Daviau Map and the Space Clifford Formulation of the Dirac Equation*, *Parra's Four Options of the Dirac Equation and the Discrete Symmetries*, and *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*.
