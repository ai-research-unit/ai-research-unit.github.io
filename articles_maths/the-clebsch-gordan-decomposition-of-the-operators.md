# __The Clebsch–Gordan Decomposition of the Operators__

## Introduction

**The subject.** The operator space is the tensor square of the module, and the tensor square of the highest weight $\tfrac32$ decomposes into four summands of labels three, two, one and zero. The article proves the rule, computes the dimensions, identifies the highest weight of each summand, checks the multiplicity one, and reads the four summands as the four carriers of the space. It then names the two bases of the space, the products and the coupled states, defines the coefficients of the change of basis, and states their orthogonality and their symmetry. It then derives the recurrence of the coefficients from the ladder operators. It next takes the four summands one at a time, fixes for each its dimension, its weight string, its Casimir, its identity as an operator and its projector, and compares the rule with the rule of the row of the elements.

**The notation.** Every symbol used below, including the symmetric square $\operatorname{Sym}^{2}$, the alternating square $\Lambda^{2}$ and the Casimir $C$, is defined in *Notation*, which follows the introduction.

**The order of the article.** The tensor square and the rule come first; the highest weights and the dimensions second. The multiplicity one follows, then the two bases, the coefficients and their recurrence, then the four carriers one at a time, and the comparison closes the article.

**It assumes** *The Spin Group: the Principal Copy, $\operatorname{Sym}^{3}$ and the Kernel $\{\pm\mathrm I\}$*, *The Four Weights of the Module and the Half Angle* and *The Spin Decomposition: Four Carriers and the Weight Multiset*. **The row of the elements is** where the rule is $\tfrac12\otimes\tfrac12=V_1\oplus V_0$; here the same rule is applied to the doubled label and produces four summands.

**The result in one line.** $\tfrac32\otimes\tfrac32=V_3\oplus V_2\oplus V_1\oplus V_0$ with dimensions $7+5+3+1=16$, each summand occurring once, so the decomposition is canonical.

**Boundaries.** The weight multiset of the sixteen is *The Spin Decomposition: Four Carriers and the Weight Multiset*; the products of the carriers are *The Truncated Rule: the Product of Two Carriers Is Not a Carrier*; the squares of the module are *The Parity Rule*.

## Notation

Every symbol used below is fixed here, once, so that no display later in the article rests on an undefined letter.

**The algebra and its operators.** $\mathbb{B}$ is the biquaternion algebra, of complex dimension four, with unit $e_t$ and vector part spanned by $\vec e_x,\vec e_y,\vec e_z$, each of square $-e_t$. $\operatorname{End}(\mathbb{B})$ is the complex vector space of the linear maps of the algebra into itself, of complex dimension sixteen, and $\mathrm{I}$ is its identity map, the operator that fixes every element.

**The two one-sided operators.** For an element $a$ of the algebra, $L_a$ is the operator $X\mapsto aX$ and $R_a$ is the operator $X\mapsto Xa$. Both are linear maps of the algebra, so both are elements of $\operatorname{End}(\mathbb{B})$.

**The copy.** $\mathfrak{g}$ is the three-dimensional complex Lie algebra spanned by the operators $\xi_x=L_{i\vec e_x}$, $\xi_y=L_{i\vec e_y}$ and $\xi_z=L_{i\vec e_z}$, with brackets $[\xi_x,\xi_y]=-2\xi_z$ and its cyclic images. It is a copy of $\mathfrak{sl}_2(\mathbb{C})$, and the article calls it **the copy** throughout.

**Weights.** A vector $v$ of a module for the copy has **weight** $m$ when $\xi_z v=mv$. The **weight string** of a carrier is the list of the weights of a basis of weight vectors of that carrier, each weight written once for each vector that carries it. A **highest weight vector** is a vector of weight $m$ killed by the raising part of the copy, that is by the operator of the copy that raises the weight.

**The labels and the carriers.** For a non-negative half-integer $k$, $V_k$ is the simple module of **label** $k$: the module of complex dimension $2k+1$ whose weights are $k,k-1,\dots,-k$, each once, with a highest weight vector of weight $k$. The label $k$ is also called the **spin** of the carrier. The **Casimir operator** $C$ is the central element of the copy. The copy is simple, so a central element is unique up to a scalar; the scalar is fixed by the requirement that $C$ act on $V_k$ by $k(k+1)$, equivalently by $C|_{V_1}=2$ on the adjoint triplet. The four values are then $0,2,6,12$ at $k=0,1,2,3$. For an invariant subspace $V$ the symbol $C|_{V}$ means $C$ read only on $V$, and an equation $C|_{V}=c$ means that $C$ acts on $V$ by the scalar $c$.

**Uniqueness and the lattice of labels.** For each $j$ in the lattice
$$
j\in\{0,\tfrac12,1,\tfrac32,2,\dots\}
$$
there is exactly one simple module up to isomorphism, the one of dimension $2j+1$ and highest weight $j$; it is written $V_j$. The labels form a half-integer lattice: the sum and the difference of two labels are again labels, which is why a tensor product decomposes into labels and not into other objects. The same family is the family of irreducible representations of the compact group $\mathrm{SU}(2)$: the algebra and the group have the same labels, and a representation of the algebra integrates to a representation of the group. The integer labels are the representations that descend to the rotation group $\mathrm{SO}(3)$; the half-integer labels are the spin representations, which are representations of $\mathrm{SU}(2)$ and not of $\mathrm{SO}(3)$, because the passage from the sphere $S^3$ to the rotation group is two to one and the half-integer labels change sign along the antipodal pair.

**Two independent systems.** The tensor product is the joint state space of two independent systems. If the first system carries $V_{j_1}$ and the second carries $V_{j_2}$, the pair carries $V_{j_1}\otimes V_{j_2}$, the observables of the first act on the first factor and those of the second on the second, and the sixteen-dimensional square of this article is the case in which both systems carry the same module. The decomposition then says what the pair carries as a single system: a direct sum of carriers, each an irreducible module for the copy acting on the pair at once.

**The ladder.** The copy contains the Cartan element $H$ and two operators $E$ and $F$ with
$$
[H,E]=E,\qquad [H,F]=-F,\qquad [E,F]=2H ,
$$
so that $E$ raises the weight by one, $F$ lowers it by one — the factor two of the last bracket is the normalisation that matches the matrix elements displayed next — and the weight string of $V_j$ is generated from the highest weight vector by repeated application of $F$. In the standard normalisation the states obey
$$
E\,\lvert j,m\rangle=\sqrt{(j-m)(j+m+1)}\,\lvert j,m+1\rangle,\qquad
F\,\lvert j,m\rangle=\sqrt{(j+m)(j-m+1)}\,\lvert j,m-1\rangle ,
$$
with $H\lvert j,m\rangle=m\lvert j,m\rangle$. A finite weight string must end: at the top $E$ annihilates the highest weight vector, and at the bottom $F$ annihilates the lowest, and the two conditions force $j$ to be a half-integer and the string to have $2j+1$ members. The copy of the previous section is a rescaling of this normalisation, and the labels, the dimension and the Casimir are unchanged by the rescaling; the recurrences below are written in the standard one.

**The module.** $V_{3/2}$ is the four-dimensional carrier on which the copy acts in this row, so that $2\cdot\tfrac32+1=4$. $S$ is the two-dimensional spinor space, and $\operatorname{Sym}^{3}S$ is its third symmetric power, of dimension four.

**The tensor product and the direct sum.** $\otimes$ is the tensor product over $\mathbb{C}$ and $\oplus$ the direct sum; $\cong$ is an isomorphism of modules for the copy. The **tensor square** of a module $V$ is $V\otimes V$.

**The two squares of a module.** Let $V$ be a complex vector space of dimension $n$. The **symmetric square** $\operatorname{Sym}^{2}V$ is the quotient of $V\otimes V$ by the subspace spanned by the differences $v\otimes w-w\otimes v$; it has dimension $n(n+1)/2$. The **alternating square** $\Lambda^{2}V$, also written $\bigwedge^{2}V$ and read *lambda squared*, is the quotient of $V\otimes V$ by the subspace spanned by the sums $v\otimes w+w\otimes v$; it has dimension $n(n-1)/2$. At $n=4$ the two dimensions are $10=4\cdot5/2$ and $6=4\cdot3/2$, and they sum to the sixteen of the tensor square.

**The kets.** $\lvert j,m\rangle$ is a name for the weight vector of weight $m$ in the carrier $V_j$, so that $m$ runs over $j,j-1,\dots,-j$ and the $2j+1$ kets are a basis of $V_j$. The two factors of the tensor square are distinguished by their order, and the sixteen products are written $\lvert j_1,m_1\rangle\otimes\lvert j_2,m_2\rangle$; a vector of the coupled basis is written $\lvert J,M\rangle$. The ket is a name and not a new object: every ket is a vector of the space, and the symbol $\langle j_1,m_1;j_2,m_2\vert J,M\rangle$ is the coefficient of the product in the state, a number.

**The coefficients.** The **Clebsch–Gordan coefficients** are the numbers $\langle j_1,m_1;j_2,m_2\vert J,M\rangle$ of the change of basis between the products and the coupled states. The **Condon–Shortley phase** is the convention that fixes each highest weight vector $\lvert J,J\rangle$ by the requirement that its coefficient on the product $\lvert j_1,j_1\rangle\otimes\lvert j_2,J-j_1\rangle$ be positive; with that convention the coefficients are real.

**The $3$-$j$ symbol.** $\begin{pmatrix}j_1&j_2&J\\ m_1&m_2&-M\end{pmatrix}$ is the Wigner $3$-$j$ symbol, defined from the coefficients by
$$
\langle j_1,m_1;j_2,m_2\vert J,M\rangle=(-1)^{j_1-j_2+M}\sqrt{2J+1}\,\begin{pmatrix}j_1&j_2&J\\ m_1&m_2&-M\end{pmatrix}.
$$
It vanishes unless $m_1+m_2=M$ and unless the three labels satisfy the triangle condition $\lvert j_1-j_2\rvert\le J\le j_1+j_2$.

**The symbol $\subset$.** The statement $V\subset W$ means that $V$ is a linear subspace of $W$. In this article it is applied only to carriers: $V_3\subset\operatorname{Sym}^{2}V_{3/2}$ means that the carrier of label three lies inside the symmetric square of the module, as one of its two summands; and $V_2\subset\Lambda^{2}V_{3/2}$ means the same for the carrier of label two inside the alternating square.

**Dimensions.** $\dim_{\mathbb{C}}$ is the dimension over the complex numbers.

## The Tensor Square

**Scope.** The theorem below is a statement about the abstract tensor square $V_{3/2}\otimes V_{3/2}$ and holds for any module of label $\tfrac32$. Whether the operator space of the algebra is that square is a separate question, and it is not settled here. With the copy generated by the left multiplications $L_{i\vec e_k}$, the algebra carries $V_{1/2}\oplus V_{1/2}$, of weights $\pm\tfrac12$ twice, and the square is then four copies of $V_1\oplus V_0$; the series $7+5+3+1$ belongs to $V_{3/2}\otimes V_{3/2}$ and to any row where the module has the weights $\pm\tfrac32,\pm\tfrac12$ each once. Every statement below is read on the tensor square, and the carrier names are names of its four summands.

**Theorem.** The operator algebra, as a module for the copy by left multiplication on the first factor and right multiplication on the second, is the tensor square of the module:
$$
\operatorname{End}(\mathbb{B})=\mathbb{B}\otimes\mathbb{B}^{*}\cong V_{3/2}\otimes V_{3/2},
$$
the last isomorphism by the self-duality of the module.

*Proof.* The operators are the linear maps of the module into itself, and the space of linear maps is the tensor product of the module with its dual; the module is self-dual, so the dual is the module again.

**Corollary.** The dimension of the operator space is the square of the dimension of the module, $16=4\cdot4$.

*Proof.* The tensor product of two four-dimensional spaces.

**Corollary.** The weights of the operator space are the sums of a weight and the negative of a weight of the module, that is, the sixteen differences.

*Proof.* The weight of a tensor product is the sum of the weights of the factors, and the dual carries the negative weights.

**The reading.** The operator space is the square of the module, and its weights are the differences of the weights of the module. Everything below follows from that single identification.

## The Rule

**The general rule.** For two labels $j_1$ and $j_2$, the tensor product decomposes over every label from the difference to the sum,
$$
V_{j_1}\otimes V_{j_2}=\bigoplus_{J=\lvert j_1-j_2\rvert}^{j_1+j_2}V_J,
\qquad
\sum_{J=\lvert j_1-j_2\rvert}^{j_1+j_2}(2J+1)=(2j_1+1)(2j_2+1),
$$
each label once, with the weight of a product the sum of the weights, $M=m_1+m_2$. The square case $j_1=j_2=j$ is the instance $J=2j,2j-1,\dots,0$.

**Theorem.** The tensor square decomposes as
$$
V_{3/2}\otimes V_{3/2}=V_3\oplus V_2\oplus V_1\oplus V_0,
$$
where $V_k$ is the simple module of label $k$, and the four summands have complex dimensions $7,5,3,1$.

*Proof.* The Clebsch–Gordan rule for the tensor square of the highest weight $j$ reads $V_j\otimes V_j=\bigoplus_{k=0}^{2j}V_k$, each summand once; with $j=\tfrac32$ the labels are $3,2,1,0$. The dimension of $V_k$ is $2k+1$, giving $7,5,3,1$.

**Corollary.** The dimensions sum to sixteen, and the count is the check of the rule at this row.

*Proof.* $7+5+3+1=16$, the dimension of the tensor square.

**Corollary.** No further summand occurs, since a fifth simple module would raise the dimension above sixteen.

*Proof.* The smallest unused label would contribute at least one dimension, and the sum is already exact.

**The reading.** The rule is the addition of the weights: each summand of label $k$ has a highest weight $k$, obtained by adding two weights of the module. The four labels are all the integers from zero to three, and this is the arithmetic of the doubled string.

## The Highest Weights

**Proposition.** The highest weight of $V_k$ in the tensor square is the product of the highest weight vector of the module with the lowest weight vector, of total weight $k$, or the sum of two weights adding to $k$.

*Proof.* The highest weight of the tensor square is $\tfrac32+\tfrac32=3$, and the lowering steps produce the weights $2,1,0$ for the other summands, each realised by a pair of a weight and the negative of a weight.

**Corollary.** The four highest weight vectors are $s^{3}\otimes t^{3}$, $s^{3}\otimes s^{2}t$, $s^{3}\otimes st^{2}$ and $s^{3}\otimes s^{3}$ up to the choice of pairing.

*Proof.* The monomials of the module have the weights $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$, and the pairings displayed give the four highest weights.

**Corollary.** The highest weight vector of each summand is annihilated by the raising operator of the diagonal copy.

*Proof.* A vector of highest weight is annihilated by the raising part of the diagonal copy by definition.

**The reading.** The four highest weights are read on four products of monomials, and their weights are three, two, one, zero. The lowest weight of the module, $t^{3}$, plays the role of the dual and is what makes the differences appear.

## The Two Bases

**Definition (the uncoupled basis).** The **uncoupled** basis of the tensor square is the sixteen products
$$
\lvert j_1,m_1\rangle\otimes\lvert j_2,m_2\rangle,\qquad m_1=j_1,j_1-1,\dots,-j_1,\quad m_2=j_2,j_2-1,\dots,-j_2 .
$$
Each product is a weight vector of the copy, of weight $m_1+m_2$.

**Definition (the coupled basis).** The **coupled** basis is the sixteen states
$$
\lvert J,M\rangle,\qquad J=0,1,2,3,\quad M=J,J-1,\dots,-J ,
$$
where $\lvert J,M\rangle$ is a weight vector of weight $M$ lying in the carrier $V_J$.

**Theorem.** Both families are orthonormal bases of the tensor square, with respect to the same form, and the weight of a state is additive: a product of weights $m_1$ and $m_2$ has weight $m_1+m_2$, and a coupled state $\lvert J,M\rangle$ has weight $M$.

*Proof.* The products of two bases are a basis of the tensor product, and the weight of a tensor product is the sum of the weights. The coupled states are, by construction, one basis of each carrier taken together, and the carriers span the space by the decomposition; orthonormality holds because each carrier carries an orthonormal basis and the carriers are mutually orthogonal for the invariant form.

**Proposition (the selection rule).** A coefficient $\langle j_1,m_1;j_2,m_2\vert J,M\rangle$ vanishes unless $m_1+m_2=M$.

*Proof.* A state of weight $M$ is a sum of products of weight $M$ only, and the products of weight different from $M$ are independent of it.

**Theorem (the change of basis).** Every coupled state expands in the products as
$$
\lvert J,M\rangle=\sum_{m_1+m_2=M}\langle j_1,m_1;j_2,m_2\vert J,M\rangle\;\lvert j_1,m_1\rangle\otimes\lvert j_2,m_2\rangle ,
$$
the sum running over the pairs of weights that add to $M$, and the numbers of the expansion are the Clebsch–Gordan coefficients.

*Proof.* Both families are bases, so one expands in the other; the selection rule restricts the sum to the pairs of weight $M$, and the coefficients are by definition the coordinates of the state in the products.

**Proposition (the count at each weight).** The space of weight $M$ has dimension $4-\lvert M\rvert$, and the number of coupled states of weight $M$ is the same, because a carrier of label $J$ contributes a state of weight $M$ exactly when $J\ge\lvert M\rvert$.

*Proof.* The products of weight $M$ are the pairs with $m_1+m_2=M$, and there are $4-\lvert M\rvert$ of them. The labels $J=0,1,2,3$ that satisfy $J\ge\lvert M\rvert$ are also $4-\lvert M\rvert$ in number, and each contributes exactly one state $\lvert J,M\rangle$. The two counts agree at every weight, which is the dimension check of the change of basis.

**The four states of highest weight.** With the phase convention of the notation, the four highest weight vectors read
$$
\lvert 3,3\rangle=\lvert\tfrac32,\tfrac32\rangle\otimes\lvert\tfrac32,\tfrac32\rangle,
$$
$$
\lvert 2,2\rangle=\tfrac{1}{\sqrt2}\Bigl(\lvert\tfrac32,\tfrac32\rangle\otimes\lvert\tfrac32,\tfrac12\rangle-\lvert\tfrac32,\tfrac12\rangle\otimes\lvert\tfrac32,\tfrac32\rangle\Bigr),
$$
$$
\lvert 1,1\rangle=\sqrt{\tfrac{3}{10}}\Bigl(\lvert\tfrac32,\tfrac32\rangle\otimes\lvert\tfrac32,-\tfrac12\rangle+\lvert\tfrac32,-\tfrac12\rangle\otimes\lvert\tfrac32,\tfrac32\rangle\Bigr)-\sqrt{\tfrac{2}{5}}\,\lvert\tfrac32,\tfrac12\rangle\otimes\lvert\tfrac32,\tfrac12\rangle,
$$
$$
\lvert 0,0\rangle=\tfrac12\Bigl(\lvert\tfrac32,\tfrac32\rangle\otimes\lvert\tfrac32,-\tfrac32\rangle-\lvert\tfrac32,\tfrac12\rangle\otimes\lvert\tfrac32,-\tfrac12\rangle+\lvert\tfrac32,-\tfrac12\rangle\otimes\lvert\tfrac32,\tfrac12\rangle-\lvert\tfrac32,-\tfrac32\rangle\otimes\lvert\tfrac32,\tfrac32\rangle\Bigr).
$$
The first is the product of the two highest weight vectors of the module; the second alternates two products; the third is symmetric in the two factors and the fourth alternates all four. The coefficients are $\pm1$, $\pm\tfrac{1}{\sqrt2}$, $\sqrt{\tfrac{3}{10}},\sqrt{\tfrac{2}{5}}$ and $\pm\tfrac12$, and every one of them is real.

**Proposition (a state of the top carrier).** The state of weight $1$ in the top carrier reads
$$
\lvert 3,1\rangle=\tfrac{1}{\sqrt5}\Bigl(\lvert\tfrac32,\tfrac32\rangle\otimes\lvert\tfrac32,-\tfrac12\rangle+\sqrt3\,\lvert\tfrac32,\tfrac12\rangle\otimes\lvert\tfrac32,\tfrac12\rangle+\lvert\tfrac32,-\tfrac12\rangle\otimes\lvert\tfrac32,\tfrac32\rangle\Bigr),
$$
so that the top carrier is spread over the three products of weight $1$ with the coefficients $\tfrac{1}{\sqrt5},\sqrt{\tfrac35},\tfrac{1}{\sqrt5}$.

**Corollary (the two routes agree).** The sum $\sum_{M}\lvert J,M\rangle\langle J,M\rvert$ over the $2J+1$ states of a carrier is the projector onto that carrier, and it equals the Lagrange polynomial of the Casimir at $k(k+1)$ with $k=J$.

*Proof.* The $2J+1$ states are an orthonormal basis of $V_J$, so the sum of their rank-one projectors is the projector onto $V_J$. The Lagrange polynomial is the projector onto the eigenspace of the Casimir with eigenvalue $J(J+1)$, and that eigenspace is $V_J$; two projectors with the same image are equal.

**The reading.** The two bases answer two different questions. The products answer *what the two factors are*; the coupled states answer *what the whole is*. Neither is preferred, and the passage between them is a single orthogonal matrix of sixteen rows, whose entries are the coefficients. The rank-one sums of the coupled states reproduce, without any computation of a Casimir, the four projectors of the previous section.

## The Coefficients

**Theorem (orthogonality of the rows).** The coefficients of a fixed pair of labels are orthonormal,
$$
\sum_{m_1,m_2}\langle j_1,m_1;j_2,m_2\vert J,M\rangle\;\langle j_1,m_1;j_2,m_2\vert J',M'\rangle=\delta_{JJ'}\delta_{MM'} .
$$

*Proof.* Both bases are orthonormal for the same form, so the matrix of the change of basis is orthogonal; its rows are the expansions of the coupled states in the products, and orthonormality of those states is the displayed relation.

**Theorem (orthogonality of the columns).** The coefficients of a fixed pair of weights are orthonormal the other way,
$$
\sum_{J,M}\langle j_1,m_1;j_2,m_2\vert J,M\rangle\;\langle j_1,m_1';j_2,m_2'\vert J,M\rangle=\delta_{m_1m_1'}\delta_{m_2m_2'} .
$$

*Proof.* The same matrix is orthogonal, so its columns are orthonormal; the columns are indexed by the pairs of weights.

**Corollary (the matrix).** At $\tfrac32\otimes\tfrac32$ the coefficients form a $16\times16$ orthogonal matrix, and each of its rows has at most four nonzero entries, one for each pair of weights adding to $M$.

*Proof.* Sixteen rows for the coupled states, sixteen columns for the products; the largest weight space has dimension four.

**Corollary (reality).** The coefficients are real: no complex number occurs in the change of basis.

*Proof.* The highest weight vectors are fixed by the phase convention, the lowering operator has real matrix elements in the products, and the two together produce real coordinates.

**Proposition (symmetry in the two factors).** The two factors may be exchanged at the cost of a sign,
$$
\langle j_1,m_1;j_2,m_2\vert J,M\rangle=(-1)^{j_1+j_2-J}\langle j_2,m_2;j_1,m_1\vert J,M\rangle .
$$
For the square, $j_1=j_2=\tfrac32$, the sign is $(-1)^{J+1}$, so the coefficients of $V_3$ and $V_1$ are symmetric in the two factors and those of $V_2$ and $V_0$ alternate.

*Proof.* The exchange of the two factors is an odd permutation of the three labels of the $3$-$j$ symbol, which multiplies it by $(-1)^{j_1+j_2+J}$; the definition of the symbol carries the factor $\sqrt{2J+1}$, unchanged. Since $(-1)^{j_1+j_2-J}=(-1)^{j_1+j_2+J}$, the displayed relation follows. At $j_1=j_2=\tfrac32$ the exponent is $3-J$, which is odd exactly at $J=2$ and $J=0$.

**Theorem (the $3$-$j$ form).** In the $3$-$j$ symbol the coefficients become symmetric in the three labels: an even permutation of the three columns leaves the symbol unchanged, an odd permutation multiplies it by $(-1)^{j_1+j_2+J}$, and the reversal of all three lower entries multiplies it by the same sign.

*Proof.* Each property is read from the definition and from the symmetries of the coefficients; the permutation of two columns exchanges a factor and a coupled label, which is the exchange used in the previous proposition.

**Corollary (orthogonality of the $3$-$j$ symbol).** The row orthogonality of the coefficients becomes
$$
\sum_{m_1,m_2}(2J+1)\begin{pmatrix}j_1&j_2&J\\ m_1&m_2&-M\end{pmatrix}^{2}=1 ,
$$
so the symbol is normalised at each $J$ and $M$.

*Proof.* Substitute the definition into the row orthogonality and use $\delta_{JJ'}$ at $J=J'$.

**The reading.** The coefficients are one orthogonal matrix, read by rows or by columns. The rows say that the coupled states are orthonormal; the columns say that the products are. The $3$-$j$ symbol makes the three labels enter alike, and it is the form in which the permutation symmetry of the three angular momenta is visible: the decomposition singles out no factor and no label.

## The Recurrence

**Theorem (the recurrence).** The coefficients of a fixed label obey the two recursions obtained by applying the ladder to the state and to the two products:
$$
\sqrt{(J-M)(J+M+1)}\,\langle j_1,m_1;j_2,m_2\vert J,M+1\rangle
=\sqrt{(j_1-m_1+1)(j_1+m_1)}\,\langle j_1,m_1-1;j_2,m_2\vert J,M\rangle
+\sqrt{(j_2-m_2+1)(j_2+m_2)}\,\langle j_1,m_1;j_2,m_2-1\vert J,M\rangle ,
$$
and the same with $E$ replaced by $F$, which lowers $\lvert J,M\rangle$ to $\lvert J,M-1\rangle$ and each product to the product of the lowered factors.

*Proof.* Apply the raising operator $E=E^{(1)}+E^{(2)}$ to the expansion of $\lvert J,M\rangle$. On the left the ladder gives the factor $\sqrt{(J-M)(J+M+1)}$ and the state $\lvert J,M+1\rangle$. On the right the same operator acts on each factor of each product, and the two terms are the two displays of the statement.

**Corollary (the highest weight vector is determined).** The state $\lvert J,J\rangle$ is annihilated by $E$, and the coefficient of the product $\lvert j_1,j_1\rangle\otimes\lvert j_2,J-j_1\rangle$ is the first nonzero one; all the others follow from it by the recurrence and by normalisation.

*Proof.* The state of highest weight is annihilated by the raising operator, so the left side vanishes and the right side is the recursion that determines the coefficients of weight $J$ from those of weight $J$ with a shifted index; iterating from the top produces every coefficient of the string, and normalisation fixes the overall sign and scale.

**Proposition (the count of the steps).** The recurrence lowers the weight by one at each step, so a string of length $2J+1$ is produced in $2J$ steps, and the four labels of the square are reached in $6$, $4$, $2$ and $0$ steps from their highest weight vectors.

*Proof.* The length of the string of $V_J$ is $2J+1$ and each step of $F$ shortens the remaining run by one; the labels are $3,2,1,0$.

**Corollary (the ladder and the Casimir agree).** The four states produced from the four highest weight vectors are annihilated by $F$ at the bottom, and the Casimir of each string is the value $J(J+1)$ of its label.

*Proof.* A string of length $2J+1$ with the weights $J$ down to $-J$, each once, is the module $V_J$, and the Casimir acts on a simple module by a scalar fixed by the label. The two descriptions agree in dimension, $2J+1$, and the four dimensions $7,5,3,1$ sum to sixteen, so the four strings are the whole space and the Casimir takes on them the four values $12,6,2,0$.

**The reading.** The recurrence is the third route to the same sixteen numbers: the Casimir route gives the four projectors, the orthogonality route gives the matrix, and the ladder route gives each coefficient from its neighbours. All three agree, and the ladder route is the one that shows why the labels must be half-integers: a string that can be raised must end, and the ending is a half-integer.

## The Multiplicity One

**Theorem.** Each summand occurs exactly once in the tensor square, so the decomposition is canonical and no choice of a projector is needed.

*Proof.* The Clebsch–Gordan rule for the square of one module gives each label at most once; the dimension count then forces exactness.

**Corollary.** The four summands are the eigenspaces of the Casimir operator with the four distinct eigenvalues $12,6,2,0$.

*Proof.* The Casimir acts on $V_k$ by $k(k+1)$, giving $12,6,2,0$; distinct eigenvalues give the eigenspaces directly.

**Corollary.** A canonical projector onto $V_k$ is the Lagrange interpolation of the Casimir at the value $k(k+1)$.

*Proof.* The interpolation polynomial in the Casimir is the identity on the eigenspace of that eigenvalue and zero on the other three.

**The reading.** Multiplicity one is what makes the decomposition usable: the summands are the eigenspaces of one operator, and the projectors are polynomials in it. No frame and no choice of basis enters.

## The Four Carriers, One at a Time

**The table.** The four summands, with the four numbers that distinguish them: the label, the dimension, the weight string and the Casimir.

| carrier | label $k$ | dimension $2k+1$ | weight string | Casimir $k(k+1)$ | square | trace of the projector |
|---|---|---|---|---|---|---|
| $V_0$ | $0$ | $1$ | $0$ | $0$ | alternating | $1$ |
| $V_1$ | $1$ | $3$ | $1,0,-1$ | $2$ | symmetric | $3$ |
| $V_2$ | $2$ | $5$ | $2,1,0,-1,-2$ | $6$ | alternating | $5$ |
| $V_3$ | $3$ | $7$ | $3,2,1,0,-1,-2,-3$ | $12$ | symmetric | $7$ |

**The four readings of one table.** The dimension is the number of weights in the string, the label is the largest weight in it, and the Casimir is fixed by the label alone. The last two columns are theorems about a square and about a trace, not new data.

**The mechanism of the peel.** At weight $m$ the tensor square has multiplicity $4-\lvert m\rvert$, and a carrier of label $k$ contributes one vector at weight $m$ exactly when $k\ge\lvert m\rvert$. The counts agree at every weight, which is why the peel of the previous section terminates exactly after four steps: $V_3$ takes one vector at each of the seven weights, $V_2$ takes one at the five weights of modulus at most two, and so on to $V_0$, which takes only the weight zero.

## The Carrier $V_0$: the Scalars

**Definition.** The carrier of label zero is the set of operators of the operator space that commute with every element of the copy.

**Theorem.** The carrier is the complex line of the multiples of the identity,
$$
V_0=\mathbb{C}\,\mathrm{I},\qquad \dim_{\mathbb{C}}V_0=1,
$$
and it is the common intersection of the left and right one-sided families, $V_0=L_{\mathbb{B}}\cap R_{\mathbb{B}}$.

*Proof.* An operator commuting with every left multiplication by the copy is a right multiplication by an element of the commutant of the algebra, and the algebra is central simple, so the commutant is the scalars. The same argument on the other side gives the same line, and the intersection of the two families is that line.

**Corollary.** The carrier contributes one dimension to the sum $16=7+5+3+1$, and it is the smallest of the four.

*Proof.* The dimension is that of a line; the other three are $3,5,7$.

**Proposition.** As a real space of operators the carrier has dimension two, and it splits into the real line spanned by the identity and the imaginary line spanned by the multiplication by $i$.

*Proof.* The line is a complex line inside a complex space, so it is a real plane; its real and imaginary parts are the two lines displayed.

**Corollary (weight string and Casimir).** The weight string of $V_0$ is the single weight $0$, and the Casimir vanishes on it.

*Proof.* A scalar multiple of the identity is fixed by the copy, so every generator annihilates it and its weight is zero; the Casimir of the label zero is $0\cdot1=0$.

**Corollary (the projector).** The projector onto $V_0$ is the Lagrange polynomial of the Casimir at the value $0$, that is the product $\prod_{k=1}^{3}\bigl(C-k(k+1)\bigr)\big/\prod_{k=1}^{3}\bigl(0-k(k+1)\bigr)$.

*Proof.* The interpolation polynomial is the identity on the eigenspace of the value $0$ and zero on the other three eigenspaces, and the four eigenspaces span the space.

**The reading.** The smallest carrier is the one that carries no weight. It is the centre of the operator space, the line that every action of the copy fixes, and the reason the four carriers have a common point of departure: each of the other three also contains a weight-zero line, and the four lines together span the kernel of the Cartan generator, of dimension four.

## The Carrier $V_1$: the Adjoint Triplet

**Definition.** The three operators
$$
J_k:=\tfrac12\bigl(L_{\vec e_k}-R_{\vec e_k}\bigr),\qquad k=x,y,z,
$$
are the commutator maps $X\mapsto\tfrac12[\vec e_k,X]$, and their span is a second copy of the Lie algebra of the copy inside the operator space.

**Theorem.** The carrier of label one is the span of the three commutator maps,
$$
V_1=\operatorname{span}_{\mathbb{C}}\{J_x,J_y,J_z\},\qquad \dim_{\mathbb{C}}V_1=3,
$$
with weight string $1,0,-1$ and Casimir $2$.

*Proof.* The three are independent, since each sends the identity to zero and acts nontrivially on the vector part. A commutator map is a derivation of the algebra, so the bracket of two of them is again a commutator map, and the three satisfy the brackets of the angular momentum algebra. Under the Cartan generator the highest one has weight $1$, the lowest weight $-1$, and the middle one weight $0$, so the string is $1,0,-1$; the Casimir is $1\cdot2=2$.

**Corollary.** The carrier $V_1$ is the adjoint module: the copy acting on itself.

*Proof.* The commutator maps are the operators of the adjoint action of the copy, and the space they span is the copy.

**Corollary.** The carrier $V_1$ is the only carrier of positive label that is closed under the commutator of operators.

*Proof.* A carrier closed under the commutator is a Lie subalgebra of the operator algebra and a module for the copy of dimension at most three; the carriers of label two and three have dimensions five and seven and are not closed, as the truncated rule shows.

**Corollary (parity).** The carrier lies in the symmetric square, since its label is odd.

*Proof.* The parity rule $\operatorname{Sym}^{2}V_{3/2}=V_3\oplus V_1$.

**Corollary (the projector).** The projector onto $V_1$ is the Lagrange polynomial of the Casimir at the value $2$, and its trace is $3$.

*Proof.* The interpolation at $2$, and the trace of a projector is the dimension of its image.

**The reading.** The second carrier is the one that is already a Lie algebra. It is the copy inside the operators, and it is the only carrier that the copy can multiply by itself: the other three are modules and not algebras.

## The Carrier $V_2$: the Alternating Five

**Definition.** The carrier of label two is the five-dimensional summand of the operator space that lies in the alternating square of the module.

**Theorem.** The carrier has weight string $2,1,0,-1,-2$, complex dimension $5$ and Casimir $6$:
$$
V_2\subset\Lambda^{2}V_{3/2},\qquad \dim_{\mathbb{C}}V_2=5,\qquad C|_{V_2}=6.
$$

*Proof.* By the peel, the carrier takes one vector at each of the five weights of modulus at most two, so its string is $2,1,0,-1,-2$ and its dimension is five. The label is $2$ and the Casimir is $2\cdot3=6$. The parity rule places the even label in the alternating square.

**Proposition (its highest weight vector).** At weight $2$ the tensor square has multiplicity two; one vector of that weight lies in $V_3$, in the string of the top carrier, and the other is the highest weight vector of $V_2$.

*Proof.* The multiplicity at weight $2$ is $4-\lvert2\rvert=2$. The top carrier occupies one vector at every weight from $3$ down to $-3$, so it occupies one of the two at weight $2$; the remaining one is annihilated by the raising operator, since a further raise would give a weight-three vector, and the weight-three space is already spanned by the highest vector of $V_3$.

**Corollary.** The carrier is of real type: it admits a real form of five real dimensions.

*Proof.* The module is self-dual and quaternionic in the sense of the module article, so its alternating square is of real type; the real form has the dimension of the complex carrier.

**Corollary (the projector).** The projector onto $V_2$ is the Lagrange polynomial of the Casimir at the value $6$, and its trace is $5$.

*Proof.* The interpolation at $6$, and the trace is the dimension.

**The reading.** The label suggests symmetric tensors and the space is alternating, and the reason is the parity rule: the symmetric square carries the odd labels and the alternating square the even ones. The carrier of label two is the first one that exists only on the operators: the algebra itself stops at labels zero and one, and the module at label $\tfrac32$, so a carrier of label two has no counterpart in either.

## The Carrier $V_3$: the Symmetric Seven

**Definition.** The carrier of label three is the traceless part of the symmetric square of the module, and it is the largest summand of the operator space.

**Theorem.** The carrier has weight string $3,2,1,0,-1,-2,-3$, complex dimension $7$ and Casimir $12$:
$$
V_3\subset\operatorname{Sym}^{2}V_{3/2},\qquad \dim_{\mathbb{C}}V_3=7,\qquad C|_{V_3}=12.
$$

*Proof.* The peel gives one vector at each of the seven weights of modulus at most three, so the string is $3,2,1,0,-1,-2,-3$ and the dimension is seven. The label is the highest weight of the tensor square, $3$, and the Casimir is $3\cdot4=12$. The parity rule places the odd label in the symmetric square, and the trace part is removed because the identity operator lies in $V_0$.

**Corollary (no higher carrier).** No carrier of label four or more occurs.

*Proof.* A carrier of label four would contain a weight of modulus four, and the tensor square has none: the largest weight is $3$.

**Corollary.** The highest weight vector of $V_3$ is the product of the two highest weight vectors of the module, of total weight $3$.

*Proof.* The highest weight of the tensor product is the sum of the highest weights of the factors.

**Corollary (the projector).** The projector onto $V_3$ is the Lagrange polynomial of the Casimir at the value $12$, and its trace is $7$.

*Proof.* The interpolation at $12$, and the trace is the dimension.

**The reading.** The top carrier is the largest and the one furthest from the centre: it carries the extreme weights $\pm3$, it exists only on the operators, and the chain of closures of a weight vector runs from it down to $V_0$.

## The Comparison of the Four

**Proposition (the sum of the four projectors).** The four projectors sum to the identity of the operator space, and their traces sum to sixteen.

*Proof.* The four eigenspaces of the Casimir span the space, since the Casimir is diagonalisable with the four values $0,2,6,12$ and the space has dimension $1+3+5+7=16$. The traces are the dimensions.

**Corollary (one operator, four labels).** The four carriers are separated by the Casimir alone: no frame, no basis and no choice of axis enters.

*Proof.* A projector is a polynomial in the Casimir, and the Casimir is built from the copy.

**Corollary (two carriers per square).** Each square of the module splits into exactly two carriers, the symmetric into the odd labels and the alternating into the even ones:
$$
\operatorname{Sym}^{2}V_{3/2}=V_3\oplus V_1,\qquad \Lambda^{2}V_{3/2}=V_2\oplus V_0,
$$
with $10=7+3$ and $6=5+1$.

*Proof.* The parity rule and the dimensions of the four carriers.

**Corollary (the row of the elements).** The rule of the row of the elements is $\tfrac12\otimes\tfrac12=V_1\oplus V_0$, with dimensions $3+1=4$, and on the operators the same rule at $j=\tfrac32$ runs over every label from $0$ to $2j=3$, which is why four carriers appear instead of two.

*Proof.* The same Clebsch–Gordan rule at $j=\tfrac12$ gives $V_1\oplus V_0$; at $j=\tfrac32$ it gives the four carriers. The label of the module is doubled and the intermediate labels appear, because the square of a module of label $j$ runs over every label from $0$ to $2j$.

**The reading.** One rule, two rows, and the difference is the label of the module: two terms on the algebra, four on the operators. The four carriers of the operators are the four terms of one sum, and the terms are distinguished by the Casimir alone.

## Further Reading

- [The Spin Group: the Principal Copy, $\operatorname{Sym}^{3}$ and the Kernel $\{\pm\mathrm I\}$](the-spin-group-the-principal-copy-and-the-kernel.html), for the module and the copy.
- [The Spin Decomposition: Four Carriers and the Weight Multiset](the-spin-decomposition-four-carriers-and-the-weight-multiset.html), for the weights of the sixteen.
- [The Parity Rule: $\operatorname{Sym}^{2}=V_3\oplus V_1$ and $\Lambda^{2}=V_2\oplus V_0$](the-parity-rule-the-two-squares-of-the-module.html), for the split of the four carriers into the two squares.
- [The Truncated Rule: the Product of Two Carriers Is Not a Carrier](the-truncated-rule-the-product-of-two-carriers-is-not-a-carrier.html), for the failure of the carriers to be closed under the product.
