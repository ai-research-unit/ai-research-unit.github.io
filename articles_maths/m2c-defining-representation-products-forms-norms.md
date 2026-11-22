# __$M_2(\mathbb{C})$ Defining Representation : Products, Forms and Norms__

## Introduction

**The subject.** Every quantity of the pair that involves two objects, and every one of them is a matrix of size two: the three pairings of two columns, the two pairings of two operators, the determinant as a quadratic form and the four norms of an operator. *$M_2(\mathbb{C})$ Defining Representation* writes the carrier, its basis and the five bases of the operator space; this article writes the pair; the third article, *$M_2(\mathbb{C})$ Defining Representation : Operators*, writes the two-sided family.

**The result in one line.** The three pairings of two columns have the three Gram matrices $I_2$, $J_2$ and $I_2$, and each of them is the trace of a rank-one operator,
$$
B(u,v)=\operatorname{tr}(uv^{\mathsf T}),\qquad
H(u,v)=\operatorname{tr}(uv^{\dagger}),\qquad
\omega(u,v)=B(u,J_2v).
$$

**Three pairings and not one.** There is no canonical isomorphism $V\cong V^{*}$, so a pairing of two columns is a choice; the carrier carries three, and the complex structure prefers none of them. The article keeps the three separate and gives each its Gram matrix, its isometry group and its isotropic set.

**Every object here is a $2\times2$ complex matrix.** The carrier is a complex space of dimension two, an operator is a $2\times2$ complex matrix, a pairing is a $2\times2$ Gram matrix, and a norm is a quadratic function of the four entries. **No object of the article has size four**: the four entries $w_{11},w_{12},w_{21},w_{22}$ are the four coordinates that the whole computation uses, and nothing is read as a quadruple of real numbers.

**The concrete setting.** The carrier is $V=\mathbb{C}^{2}$ with the basis columns
$$
e_1=\begin{pmatrix}1\\0\end{pmatrix},\qquad e_2=\begin{pmatrix}0\\1\end{pmatrix},
\qquad
u=\begin{pmatrix}u_{\blacktriangle}\\ u_{\blacktriangledown}\end{pmatrix},
\qquad
v=\begin{pmatrix}v_{\blacktriangle}\\ v_{\blacktriangledown}\end{pmatrix},
$$
and the operator space is $M_2(\mathbb{C})$ with the matrix units $E_{jk}=e_je_k^{\mathsf T}$.

**The order of the article.** The three pairings and their Gram matrices come first (§*The Three Pairings and Their Gram Matrices*), then the effect of conjugating one argument (§*The Pairings with a Conjugated Argument*) and the table of what each form sees (§*What Each Form Sees*). The pairings of two operators follow (§*The Pairings of Two Operators*), then the determinant as a quadratic form (§*The Determinant as a Quadratic Form*) and the four norms (§*The Four Norms*). The last two sections read the column pairings as traces of rank-one operators (§*The Factors*) and record what the size two buys (§*What the Module Size Gives*).

**Boundaries.** The carrier, the bases and the five bases of the operator space are *$M_2(\mathbb{C})$ Defining Representation*; the properties of $H$, $B$ and $\omega$, their isometry groups and their isotropic sets are *The Three Canonical Forms on $\mathbb{C}^2$*; the two-sided family, its rank and its fibres are *$M_2(\mathbb{C})$ Defining Representation : Operators*. On the algebra side, *$M_2(\mathbb{C})$ Pauli Representation : Products, Forms and Norms* carries the same four norms with the product inside.

**Conventions.** The pairing $H$ is linear in the first slot and conjugate-linear in the second, the convention of the whole corpus; $B$ and $\omega$ are complex bilinear, with **no conjugation**. The transpose is $M^{\mathsf T}$, the dagger is $M^{\dagger}=\overline{M}^{\mathsf T}$, and $J_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ is the alternating matrix.

## The Three Pairings and Their Gram Matrices

**Three pairings, three matrices, and the matrices are the whole content.**

**Definition.** The three canonical pairings of two columns are
$$
B(u,v)=u^{\mathsf T}v=u_{\blacktriangle}v_{\blacktriangle}+u_{\blacktriangledown}v_{\blacktriangledown},
\qquad
\omega(u,v)=u^{\mathsf T}J_2v=u_{\blacktriangle}v_{\blacktriangledown}-u_{\blacktriangledown}v_{\blacktriangle},
\qquad
J_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
$$
$$
H(u,v)=u^{\mathsf T}\overline{v}=u_{\blacktriangle}\overline{v_{\blacktriangle}}+u_{\blacktriangledown}\overline{v_{\blacktriangledown}} .
$$
**The first two are complex bilinear, the third is linear in the first slot and conjugate-linear in the second**, which is the convention of the whole corpus.

**Proposition (the Gram matrices).** In the basis $(e_1,e_2)$,
$$
G_B=\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad
G_\omega=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
G_H=\begin{pmatrix}1&0\\0&1\end{pmatrix},
$$
and each is invertible, of determinant $1$.

*Proof.* Read the pairings at the basis vectors: $B(e_j,e_k)=\delta_{jk}$ because $e_j^{\mathsf T}e_k$ is the product of the two coordinate columns; $\omega(e_1,e_2)=1$ and $\omega(e_2,e_1)=-1$ by the display; $H(e_j,e_k)=\delta_{jk}$ because $e_j^{\dagger}e_k$ is the same product with a conjugate that does nothing on the entries of the basis. ∎

**Remark (the same matrix twice, and the difference is elsewhere).** The Gram matrices of $B$ and of $H$ are the same array. **The two pairings differ only in the conjugation of the second argument, and the difference shows in the isotropic set and in the isometry group and nowhere in the Gram matrix.** The matrix of $B$ is symmetric and that of $\omega$ is alternating, and those are the two symmetry types that a complex bilinear form can have.

**Proposition (the three identifications with the dual).** Each nondegenerate pairing identifies $V$ with $V^{*}$, and the three identifications are
$$
u\longmapsto u^{\mathsf T},\qquad
u\longmapsto u^{\mathsf T}J_2=(-u_{\blacktriangledown},\ u_{\blacktriangle}),\qquad
u\longmapsto u^{\dagger}=(\overline{u_{\blacktriangle}},\ \overline{u_{\blacktriangledown}}),
$$
with the values $u^{\mathsf T}v$, $u^{\mathsf T}J_2v$ and $\overline{u^{\dagger}v}$. The first two are $\mathbb{C}$-linear and the third is conjugate-linear; **the second is the first rotated by a quarter turn in the coefficient plane.**

*Proof.* The row $u^{\mathsf T}G$ is the functional $v\mapsto u^{\mathsf T}Gv$; with $G=I_2$ and $G=J_2$ it gives the first two rows. The third is the conjugate of the plain product, $u_{\blacktriangle}\overline{v_{\blacktriangle}}+u_{\blacktriangledown}\overline{v_{\blacktriangledown}}=\overline{u^{\dagger}v}$, and $u\mapsto u^{\dagger}$ is conjugate-linear because it conjugates the coordinates. ∎

**The three matrices are the three ways of reading a $2\times2$ matrix as a form**: $I_2$ twice, once without conjugation and once with it, and $J_2$ once. **The alternating one is the determinant of the pair**, $\omega(u,v)=u_{\blacktriangle}v_{\blacktriangledown}-u_{\blacktriangledown}v_{\blacktriangle}$, the $2\times2$ determinant of the two columns.

## The Pairings with a Conjugated Argument

**Conjugating one argument exchanges two of the three pairings up to conjugation, and conjugating both conjugates the value.**

**Proposition (the exchange).** For all $u,v$,
$$
B(\bar u,v)=\overline{H(u,v)},\qquad
H(\bar u,v)=\overline{B(u,v)},\qquad
B(\bar u,\bar v)=\overline{B(u,v)},\qquad
H(\bar u,\bar v)=\overline{H(u,v)},\qquad
\omega(\bar u,\bar v)=\overline{\omega(u,v)}.
$$

*Proof.* Entrywise, $B(\bar u,v)=\sum_j\bar u_jv_j=\overline{H(u,v)}$ because $H(u,v)=\sum_j u_j\overline{v_j}$; $H(\bar u,v)=\sum_j\bar u_j\overline{v_j}=\overline{B(u,v)}$; conjugating $B(u,v)=\sum_j u_jv_j$ gives $\sum_j\bar u_j\bar v_j=B(\bar u,\bar v)$, and the same line gives the fourth identity; the fifth is the fourth read on $\omega$, whose coefficients are the same products in the other order. ∎

**Remark (why the two readings of the pair use two forms).** The conjugation is an anti-linear map of the carrier, and it carries $B$ to the conjugate of $H$ and back. **The bilinear cone of the pair uses $B$ and the qubit reading uses $H$, and the two are exchanged by the conjugation**, at the price of conjugating the value.

**Remark (the pairs of arguments).** The three pairings and the two choices of conjugated argument give six bilinear objects; the proposition shows that they are the three and their three conjugates. **There is no seventh object, and no pairing of the carrier is missing from the list.**

## What Each Form Sees

**One table, and the three readings of the pair are one line each of it.**

| Form | Isometry group | Isotropic set | The reading |
|---|---|---|---|
| $H$ | $\mathrm{U}(2)$ | $\{0\}$ | the qubit, with the pure states as the rank-one projectors |
| $B$ | $\mathrm{O}(2,\mathbb{C})$ | two complex lines | the bilinear cone $u\phi^{\mathsf T}$ |
| $\omega$ | $\mathrm{SL}_2(\mathbb{C})$ | every complex line | the spinor and the Lorentz group |

**The three groups are not the same group and the three geometries are not the same geometry.** The first is compact, the second is the complex orthogonal group $\mathrm{O}(2,\mathbb{C})$, and the third is the double cover of the Lorentz group. **The same carrier carries a compact geometry, a split geometry and a symplectic geometry, and the three pairings are what separates them.**

**The isotropic sets separate the forms without any computation.** $H$ has no isotropic vector but $0$, $B$ has the two lines $u_{\blacktriangle}=\pm iu_{\blacktriangledown}$, and $\omega$ has every line because it is alternating in dimension two. **The Gram matrix sees none of this and the isotropic set sees all of it.**

## The Pairings of Two Operators

**The operator space has two pairings, one bilinear and one Hermitian, and both are read on the four entries of the matrices.**

**Definition.** For $X,Y\in M_2(\mathbb{C})$,
$$
\langle X,Y\rangle=\operatorname{tr}(X^{\mathsf T}Y),\qquad
\langle X,Y\rangle_{H}=\operatorname{tr}(X^{\dagger}Y).
$$

**Proposition (the two pairings in entries).** For $X=\begin{pmatrix}w_{11}&w_{12}\\w_{21}&w_{22}\end{pmatrix}$ and $Y=\begin{pmatrix}z_{11}&z_{12}\\z_{21}&z_{22}\end{pmatrix}$,
$$
\langle X,Y\rangle=w_{11}z_{11}+w_{12}z_{12}+w_{21}z_{21}+w_{22}z_{22},\qquad
\langle X,Y\rangle_{H}=\overline{w_{11}}z_{11}+\overline{w_{12}}z_{12}+\overline{w_{21}}z_{21}+\overline{w_{22}}z_{22},
$$
and on the matrix units
$$
\langle E_{jk},E_{lm}\rangle=\delta_{jl}\delta_{km}=\langle E_{jk},E_{lm}\rangle_{H}.
$$
**Each pairing is the sum of the products of the four entries, taken without conjugation in the first case and with the conjugate of the first factor in the second**, so the two agree exactly when the entries of $X$ are real.

*Proof.* For the first, $E_{jk}^{\mathsf T}E_{lm}=E_{kj}E_{lm}=\delta_{jl}E_{km}$, whose trace is $\delta_{jl}\delta_{km}$; the expansion of $\operatorname{tr}(X^{\mathsf T}Y)$ is the sum of the four products, because the transpose puts $w_{jk}$ against $z_{jk}$. For the second, the entries of the units are real, so the dagger does nothing on them, and $\operatorname{tr}(X^{\dagger}Y)$ conjugates the first factor entry by entry. ∎

**Proposition (the two properties).** The bilinear pairing is symmetric, complex bilinear and nondegenerate. The Hermitian pairing is conjugate-symmetric in the two slots and positive definite,
$$
\langle X,X\rangle_{H}=\lvert w_{11}\rvert^{2}+\lvert w_{12}\rvert^{2}+\lvert w_{21}\rvert^{2}+\lvert w_{22}\rvert^{2}>0\quad(X\neq0).
$$

*Proof.* The symmetry of the first is the identity $\operatorname{tr}(X^{\mathsf T}Y)=\operatorname{tr}(Y^{\mathsf T}X)$, read on the entries above, which are four products in the same order in the two arguments. The nondegeneracy: if $\langle X,Y\rangle=0$ for all $Y$ then the four entries of $X$ vanish, because each of the four products appears alone at one of the four units. The conjugate symmetry of the second is $\overline{\langle Y,X\rangle_{H}}=\langle X,Y\rangle_{H}$, entry by entry, and the positivity is the displayed sum of four moduli. ∎

**Remark (the two pairings are not the same pairing).** Both are nondegenerate and both have the four units as an orthogonal family, and **the first is complex bilinear with an isotropic set and the second is positive definite with no isotropic vector but $0$.** The first is the pairing a complex-bilinear computation uses, and the second is the one a Hilbert space uses.

**Remark (the isotropic set of the bilinear pairing).** Since $\langle X,X\rangle=\sum_{jk}w_{jk}^{2}$, the isotropic set is the cone $\sum_{jk}w_{jk}^{2}=0$ in the four coefficients. **It is not the rank-one cone** $\det X=0$, which is the isotropic set of the polar form of the determinant (§*The Determinant as a Quadratic Form*); the two cones meet: the matrix $\begin{pmatrix}1&i\\0&0\end{pmatrix}$ lies on both and is of rank one, while $E_{11}+iE_{22}$ lies on the first only.

## The Determinant as a Quadratic Form

**The determinant is the second quadratic invariant of an operator, and its polar form is nondegenerate.**

**Definition.** The **polar form** of the determinant is
$$
b(X,Y)=\tfrac12\bigl(\det(X+Y)-\det X-\det Y\bigr).
$$

**Proposition (the polar form).** For $X=(w_{jk})$ and $Y=(z_{jk})$,
$$
b(X,Y)=\tfrac12\bigl(w_{11}z_{22}+z_{11}w_{22}-w_{12}z_{21}-z_{12}w_{21}\bigr),
$$
so the four products $w_{11}z_{22}$, $w_{22}z_{11}$, $-w_{12}z_{21}$ and $-w_{21}z_{12}$ are the whole form. **It is symmetric and complex bilinear, and the cone $\mathcal{C}=\{\det=0\}$ is its isotropic set.**

*Proof.* Expand $\det(X+Y)=(w_{11}+z_{11})(w_{22}+z_{22})-(w_{12}+z_{12})(w_{21}+z_{21})$, subtract $\det X$ and $\det Y$, and halve: the two linear terms and the four cross terms are exactly the display. The symmetry is the symmetry of the four products under $X\leftrightarrow Y$, and the isotropy is $\det X=b(X,X)=0$. ∎

**Proposition (nondegeneracy, read on four functionals).** The form $b$ is nondegenerate, and the four functionals $b(I_2,\cdot)$, $b(E_{11}-E_{22},\cdot)$, $b(E_{12},\cdot)$ and $b(E_{21},\cdot)$ are independent and read
$$
\tfrac12\operatorname{tr}X,\qquad
\tfrac12\bigl(w_{22}-w_{11}\bigr),\qquad
-\tfrac12 w_{21},\qquad
-\tfrac12 w_{12}.
$$

*Proof.* With $Y$ the four operators in turn, the display gives the four functionals; their common kernel is the set of $X$ with $w_{jk}=0$ for all four entries, because $\operatorname{tr}X$, $w_{22}-w_{11}$, $w_{21}$ and $w_{12}$ determine the four entries. ∎

**Remark (the cone is not a linear subspace and it is not the pairing cone).** $\mathcal{C}$ is the set of operators of rank at most one, a cone of complex dimension three in the four-dimensional operator space, and it is the isotropic set of $b$. **The bilinear pairing of §*The Pairings of Two Operators* has a different isotropic cone**, $\sum_{jk}w_{jk}^{2}=0$, and the two are distinct: $E_{11}+iE_{22}$ lies on the second and has determinant $i\neq0$.

**Remark (the polar form and the adjugate).** On the two diagonal entries the form pairs $w_{11}$ with $w_{22}$, and on the two off-diagonal entries it pairs $w_{12}$ with $w_{21}$ and inserts a minus sign, which is the sign pattern of the adjugate $\operatorname{adj}X=\begin{pmatrix}w_{22}&-w_{12}\\-w_{21}&w_{11}\end{pmatrix}$. **The trace of $X\operatorname{adj}Y$ is twice the polar form**, $\operatorname{tr}(X\operatorname{adj}Y)=2b(X,Y)$, and that is the whole of the form.

## The Four Norms

**An operator carries four quadratic invariants, and a column carries two.**

**Proposition (the four norms of an operator).** For $X=\begin{pmatrix}w_{11}&w_{12}\\w_{21}&w_{22}\end{pmatrix}$ and $\operatorname{adj}X=\begin{pmatrix}w_{22}&-w_{12}\\-w_{21}&w_{11}\end{pmatrix}$,
$$
\tfrac12\operatorname{tr}(X^{2})=\tfrac12\bigl(w_{11}^{2}+2w_{12}w_{21}+w_{22}^{2}\bigr),
\qquad
\det X=w_{11}w_{22}-w_{12}w_{21},
$$
$$
\tfrac12\operatorname{tr}(X^{\dagger}X)=\tfrac12\sum_{j,k}\lvert w_{jk}\rvert^{2},
\qquad
\tfrac12\operatorname{tr}(\operatorname{adj}X\,X^{\dagger})=\operatorname{Re}\bigl(w_{11}\overline{w_{22}}\bigr)-\tfrac12\bigl(\lvert w_{12}\rvert^{2}+\lvert w_{21}\rvert^{2}\bigr).
$$

| Norm | Formula | Values in | Definite |
|---|---|---|---|
| the plain norm | $\tfrac12\operatorname{tr}(X^{2})$ | $\mathbb{C}$ | no |
| the determinant | $\det X$ | $\mathbb{C}$ | no |
| the Hilbert–Schmidt norm | $\tfrac12\operatorname{tr}(X^{\dagger}X)$ | $\mathbb{R}$ | yes |
| the Krein-type form | $\tfrac12\operatorname{tr}(\operatorname{adj}X\,X^{\dagger})$ | $\mathbb{R}$ | no |

*Proof.* The first is the square of $X$ read on the entries, the second is the definition, the third is $\operatorname{tr}(X^{\dagger}X)=\sum_{j,k}\lvert w_{jk}\rvert^{2}$, and the fourth is the trace of $\operatorname{adj}X\,X^{\dagger}$, whose diagonal entries are $w_{22}\overline{w_{11}}-\lvert w_{12}\rvert^{2}$ and $w_{11}\overline{w_{22}}-\lvert w_{21}\rvert^{2}$. ∎

**Remark (only one is positive).** The Hilbert–Schmidt norm is the only one of the four that is positive definite; the plain norm and the determinant are complex-valued, and the Krein-type form is real and indefinite, taking the value $1$ at $I_2$ and the value $-\tfrac12$ at $E_{12}$. **The four are distinct functions of the four entries, and the table is the whole list.**

**The two norms of a column.** For a column $u$ the two invariants are
$$
H(u,u)=\lvert u_{\blacktriangle}\rvert^{2}+\lvert u_{\blacktriangledown}\rvert^{2},\qquad
B(u,u)=u_{\blacktriangle}^{2}+u_{\blacktriangledown}^{2},
$$
of which the first is definite and the second has the isotropic lines $u_{\blacktriangle}=\pm iu_{\blacktriangledown}$. **The column has two and the operator has four**, and the extra two of the operator are the two off-diagonal invariants.

## The Factors

**The pairings of the columns are the traces of the rank-one operators, and the two levels are one level.**

**Proposition (the three pairings as traces).** For all $u,v$,
$$
B(u,v)=\operatorname{tr}(uv^{\mathsf T}),\qquad
H(u,v)=\operatorname{tr}(uv^{\dagger}),\qquad
\omega(u,v)=B(u,J_2v)=\operatorname{tr}\bigl(u\,(J_2v)^{\mathsf T}\bigr).
$$

*Proof.* The matrix $uv^{\mathsf T}$ has entries $u_jv_k$, and its trace is $\sum_j u_jv_j=B(u,v)$. The matrix $uv^{\dagger}$ has entries $u_j\bar v_k$, and its trace is $\sum_j u_j\bar v_j=H(u,v)$. The third is the definition of $\omega$ together with the first identity applied to $J_2v$. ∎

**Remark (the level of the object and the level of the pair).** The operator pairings of §*The Pairings of Two Operators* are forms on the space of operators; the three pairings here are the same construction read on the rank-one members. **The carrier's forms are the traces of the cone**, and a pairing of two columns is a pairing of two rank-one operators with the trace taken.

## What the Module Size Gives

**Four statements, each with its shape at this size and its shape at the algebra's size.**

| Statement | Here | In the algebra pair |
|---|---|---|
| the determinant of a rank-one member | $0$, identically | the quaternionic norm, nonzero |
| the trace of a rank-one member | $\phi(u)$, a product of two coordinates | $2Q_t$ |
| the four norms on one element | the plain, the determinant, the Hilbert–Schmidt and the Krein-type forms | the same four, with the algebra product inside |
| the two pairings of two elements | $\operatorname{tr}(uv^{\mathsf T})$ and $\operatorname{tr}(uv^{\dagger})$ | the four forms $\tfrac12\operatorname{tr}(A_1A_2)$ and its three variants |

**The trace and the determinant of a member of the cone are the two elementary symmetric functions of the pair $(u,\phi)$**, and this is exact at this size only: at the size four the determinant of a two-sided operator is a quartic in the coordinates. **The module reading is the one in which the rank is one by construction**, and the algebra reading is the one in which the rank is a condition.

## Summary

The carrier carries three pairings — the symmetric $B$, the alternating $\omega$ and the Hermitian $H$ — with the Gram matrices $I_2$, $J_2$ and $I_2$ in the basis $(e_1,e_2)$; $B$ and $H$ have the same array and differ in the conjugation of the second argument, which separates them by their isotropic sets, $\{0\}$ for $H$ and two lines for $B$. Every one of the objects is a $2\times2$ complex matrix or a quadratic function of its four entries.

The operator space carries the bilinear pairing $\operatorname{tr}(X^{\mathsf T}Y)$ and the Hermitian pairing $\operatorname{tr}(X^{\dagger}Y)$, both read as sums of the four products of entries, the second with the conjugate of the first factor; the first is nondegenerate with the isotropic cone $\sum w_{jk}^{2}=0$, and the second is positive definite.

An operator carries four quadratic invariants, of which only the Hilbert–Schmidt norm is positive definite; a column carries two, of which only $H$ is definite. The column pairings are the traces of the rank-one operators, $B(u,v)=\operatorname{tr}(uv^{\mathsf T})$ and $H(u,v)=\operatorname{tr}(uv^{\dagger})$, and the determinant's polar form has the cone of rank-one operators as its isotropic set.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $B(u,v)=u^{\mathsf T}v$ | the symmetric bilinear pairing, Gram $I_2$ |
| $\omega(u,v)=u^{\mathsf T}J_2v$ | the alternating pairing, Gram $J_2$ |
| $H(u,v)=u^{\mathsf T}\overline{v}$ | the Hermitian pairing, Gram $I_2$, conjugate-linear in the second slot |
| $J_2$ | the alternating matrix $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ |
| $\langle X,Y\rangle=\operatorname{tr}(X^{\mathsf T}Y)$ | the bilinear pairing of two operators |
| $\langle X,Y\rangle_{H}=\operatorname{tr}(X^{\dagger}Y)$ | the Hermitian pairing of two operators |
| $b(X,Y)$ | the polar form of the determinant |
| $w_{jk}$, $z_{jk}$ | the entries of $X$ and of $Y$ |
| $\operatorname{adj}X$ | the adjugate $\begin{pmatrix}w_{22}&-w_{12}\\-w_{21}&w_{11}\end{pmatrix}$ |
| $E_{jk}=e_je_k^{\mathsf T}$ | the matrix units |

## Further Reading

*$M_2(\mathbb{C})$ Defining Representation* is the first article of the trio: the two basis vectors, the two generators, the five bases of the operator space and the four readings. *$M_2(\mathbb{C})$ Defining Representation : Operators* is the third: the two-sided family $u\phi^{\mathsf T}$, its rank and its fibres.

*The Three Canonical Forms on $\mathbb{C}^2$* proves the properties of $H$, $B$ and $\omega$, their isometry groups and their isotropic sets. *Duo-Complex Numbers* fixes the space, its two scalar structures, the complex structure and the norm, and is the article of the category that this trio reads through matrices.

On the algebra side, *$M_2(\mathbb{C})$ Pauli Representation : Products, Forms and Norms* carries the same four norms and the same four forms on the algebra $\mathbb{B}\cong M_2(\mathbb{C})$, with the product inside.

On the general theory, *Bilinear Forms* and *The Sesquilinear Form and the Conjugation* carry the Gram matrix and the classification, *The Determinant and Alternating Forms* carries the determinant as a form, and *Product and Form Conventions* the glyphs and the conventions of the corpus.
