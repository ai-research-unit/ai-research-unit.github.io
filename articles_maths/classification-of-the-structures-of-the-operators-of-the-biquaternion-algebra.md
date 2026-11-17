# __Classification of the Structures of the Operators of the Biquaternion Algebra__

## Introduction and Scope

The article [Classification of the Structures of the Biquaternion Algebra](classification-of-the-structures-of-the-biquaternion-algebra.html) classifies the structures that change the ground field of the algebra $\mathbb{B}$ itself. It proves that the complex algebra carries exactly two real structures, with fixed sets $M_2(\mathbb{R})$ and $\mathbb{H}$, and that the real algebra carries exactly one complex structure, whose complex form is $\mathbb{B}$. This article asks the same two questions one level up, for the **operator algebras** attached to $\mathbb{B}$,

$$
\mathcal{E}_{\mathbb{C}}=\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_4(\mathbb{C}),
\qquad
\mathcal{E}_{\mathbb{R}}=\operatorname{End}_{\mathbb{R}}(\mathbb{B})\cong M_8(\mathbb{R}).
$$

The operator algebras are not the element-level algebra under another name. The complex one has complex dimension sixteen against four, the real one has real dimension sixty-four against eight, and their centres are one-dimensional against the two-dimensional centre of $\mathbb{B}_{\mathbb{R}}$. The element-level real forms do not become operator-level real forms either: they enter as four-dimensional real subalgebras of $\mathcal{E}_{\mathbb{C}}$, in a position that the eighth section computes.

**The two questions.** A real structure on $\mathcal{E}_{\mathbb{C}}$ is a conjugate-linear multiplicative involution, and its fixed set is a real form of the complex operator algebra. A complex structure on $\mathcal{E}_{\mathbb{R}}$, in the technical sense of the element-level series, would be a unital $\mathbb{R}$-algebra map $\mathbb{C}\to Z(\mathcal{E}_{\mathbb{R}})$; since $Z(\mathcal{E}_{\mathbb{R}})=\mathbb{R}\cdot\mathrm{I}$, no such map exists, and the operator-level question in the ascending direction is not a complex structure but the **complexification** $\mathcal{E}_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C}\cong M_8(\mathbb{C})$. The two answers are short: two real forms of $M_4(\mathbb{C})$, namely $M_4(\mathbb{R})$ and $M_2(\mathbb{H})$, and two real forms of $M_8(\mathbb{C})$, namely $M_8(\mathbb{R})$ and $M_4(\mathbb{H})$.

**Scope.** This article states the two operator algebras, the two form notions at operator level, the real-form classification of $\mathcal{E}_{\mathbb{C}}$, the complexification of $\mathcal{E}_{\mathbb{R}}$, the double centralizer theorem with its distinguished subalgebras $L(\mathbb{B})$, $R(\mathbb{B})$ and $\mathfrak{m}$, the Jordan layer as a statement, and the relation between the operator-level and the element-level structures, including the one-sided and two-sided spans that a real form of $\mathbb{B}$ generates. It does **not** develop the subalgebra lattices, the Killing forms, the Jordan lattices or the Lie-group tables of the two real forms $M_4(\mathbb{R})$ and $M_2(\mathbb{H})$; those belong to the operator-level companions *Classification of the Real Structures of the Operators of the Biquaternion Algebra* and *Classification of the Complex Structures of the Operators of the Biquaternion Algebra*. It cites [Classification of the Structures of the Biquaternion Algebra](classification-of-the-structures-of-the-biquaternion-algebra.html) for the classification of $\mathbb{B}$ itself, [Real Forms and the Descent of an Algebra](real-forms-and-the-descent-of-an-algebra.html) for the general theory of descent, and [The Lie Correspondence and the Adjoint Representation](the-lie-correspondence-and-the-adjoint-representation.html) for the group layer.

**The order of the argument.** The second section fixes the two operator algebras and their dimensions. The third states the two form notions and separates them, and records the three corrections that the present article applies to the terminology of the source paper. The fourth proves the two real forms of $\mathcal{E}_{\mathbb{C}}$ and states the corresponding Lie-algebra count. The fifth treats the complexification of $\mathcal{E}_{\mathbb{R}}$ and compares it with the complexification of $\mathcal{E}_{\mathbb{C}}$. The sixth proves the double centralizer theorem and describes the distinguished subalgebras and the six-subspace analogue. The seventh records the Jordan layer. The eighth relates the operator level to the element level through the two embeddings and the two-sided span. The ninth states what the operator level does and does not determine, and the tenth hands off.

## The Two Operator Algebras

**The carrier.** The algebra $\mathbb{B}$ is the complex matrix algebra $M_2(\mathbb{C})$ read with the base $e_t=\mathrm{I}_2$, $\vec e_x=-i\sigma_1$, $\vec e_y=-i\sigma_2$, $\vec e_z=-i\sigma_3$, as in [The Biquaternion Algebra](the-biquaternion-algebra.html). It has complex dimension four and real dimension eight, and the four units are a complex basis of the first and a real basis of the second. An element is written $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ with complex coefficients, and its coordinate column in the order $(e_t,\vec e_x,\vec e_y,\vec e_z)$ is the object on which every operator of this article acts.

**Definition (the two operator algebras).** The complex operator algebra is

$$
\mathcal{E}_{\mathbb{C}}:=\operatorname{End}_{\mathbb{C}}(\mathbb{B}),
$$

the $\mathbb{C}$-linear maps $\mathbb{B}\to\mathbb{B}$ with composition, of complex dimension sixteen and real dimension thirty-two. The real operator algebra is

$$
\mathcal{E}_{\mathbb{R}}:=\operatorname{End}_{\mathbb{R}}(\mathbb{B}),
$$

the $\mathbb{R}$-linear maps, of real dimension sixty-four. The article [The Endomorphisms of the Biquaternion Algebra](the-endomorphisms-of-the-biquaternion-algebra.html) fixes the carrier and the two readings; this article takes that fixing as given and works with both algebras side by side.

**Proposition (the centres).** $Z(\mathcal{E}_{\mathbb{C}})=\mathbb{C}\cdot\mathrm{I}_4$ and $Z(\mathcal{E}_{\mathbb{R}})=\mathbb{R}\cdot\mathrm{I}_8$. Both algebras are simple.

*Proof.* A choice of complex basis of $\mathbb{B}$ identifies $\mathcal{E}_{\mathbb{C}}$ with $M_4(\mathbb{C})$, and a choice of real basis identifies $\mathcal{E}_{\mathbb{R}}$ with $M_8(\mathbb{R})$. A full matrix algebra over a field $F$ has centre $F$ and no two-sided ideal other than $0$ and the algebra itself. Both statements are invariant under the identification, so they hold for $\mathcal{E}_{\mathbb{C}}$ and for $\mathcal{E}_{\mathbb{R}}$. ∎

**Proposition (the complex-linear algebra inside the real one).** Let $J\in\mathcal{E}_{\mathbb{R}}$ be the multiplication by $i$, that is $J(\tilde X)=i\tilde X$. Then

$$
\mathcal{E}_{\mathbb{C}}=\{F\in\mathcal{E}_{\mathbb{R}}:FJ=JF\},
$$

a real subalgebra of $\mathcal{E}_{\mathbb{R}}$ of real dimension thirty-two.

*Proof.* A real-linear map is complex-linear exactly when it commutes with multiplication by $i$. The real dimension is half of sixty-four because $J^2=-\mathrm{I}$ gives $\mathcal{E}_{\mathbb{R}}=\mathcal{E}_{\mathbb{C}}\oplus\mathcal{E}_{\mathbb{C}}J$ as real spaces. ∎

**Remark (why the two algebras must be kept apart).** The two readings of one carrier give two algebras, and neither is a scalar multiple of the other: $\mathcal{E}_{\mathbb{C}}$ is a real subalgebra of $\mathcal{E}_{\mathbb{R}}$ and not an ideal, and the quotient $\mathcal{E}_{\mathbb{R}}/\mathcal{E}_{\mathbb{C}}$ is a real vector space and not an algebra. Every statement below names the algebra it belongs to, and no statement is carried from one to the other by a formula.

**The two tensor embeddings, stated.** Write

$$
L_{\tilde Q}(\tilde X)=\tilde Q\tilde X,\qquad R_{\tilde Q}(\tilde X)=\tilde X\tilde Q,
$$

and put $L(\mathbb{B})=\{L_{\tilde Q}\}$ and $R(\mathbb{B})=\{R_{\tilde Q}\}$, following [Operators Acting on One Side](operators-acting-on-one-side.html). Both assignments are injective, since $L_{\tilde Q}(e_t)=\tilde Q=R_{\tilde Q}(e_t)$, and both are algebra maps, the second reversing the order. Under a complex basis of $\mathbb{B}$ they become

$$
L(\mathbb{B})\cong M_2(\mathbb{C})\otimes\mathrm{I}_2,\qquad
R(\mathbb{B})\cong \mathrm{I}_2\otimes M_2(\mathbb{C})^{\mathsf T},
$$

the transpose recording that the right action multiplies the second index on the right; this is the tensor form of the double centralizer theorem proved in the sixth section.

**The master table.** The four algebras of the article, with their ground fields, dimensions and centres.

| algebra | ground field | dimension | centre |
|---|---|---|---|
| $\mathcal{E}_{\mathbb{C}}\cong M_4(\mathbb{C})$ | $\mathbb{C}$ | $16$ complex, $32$ real | $\mathbb{C}\cdot\mathrm{I}_4$ |
| $\mathcal{E}_{\mathbb{R}}\cong M_8(\mathbb{R})$ | $\mathbb{R}$ | $64$ real | $\mathbb{R}\cdot\mathrm{I}_8$ |
| $\mathcal{E}_{\mathbb{R},\mathbb{C}}=\mathcal{E}_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C}\cong M_8(\mathbb{C})$ | $\mathbb{C}$ | $64$ complex | $\mathbb{C}\cdot\mathrm{I}_8$ |
| $\mathcal{E}^{\oplus 2}_{\mathbb{C}}=\mathcal{E}_{\mathbb{C}}\otimes_{\mathbb{R}}\mathbb{C}\cong M_4(\mathbb{C})\oplus M_4(\mathbb{C})$ | $\mathbb{C}$ | $32$ complex | $\mathbb{C}\oplus\mathbb{C}$ |

The last two rows are the two different scalar extensions, and they are distinguished in the fifth section. The glyphs follow the element-level series, where $\mathbb{B}^{\oplus 2}_{\mathbb{C}}$ denotes the complexification of $\mathbb{B}_{\mathbb{R}}$: the subscript records the ground field of the algebra that is extended, and the superscript records the shape of the result.

## The Two Form Notions at Operator Level

### Real Structures of the Complex Operator Algebra

**Definition (real structure on the operator algebra).** A **real structure** on $\mathcal{E}_{\mathbb{C}}$ is a map $\tau:\mathcal{E}_{\mathbb{C}}\to\mathcal{E}_{\mathbb{C}}$ that is conjugate-linear, multiplicative and involutive:

$$
\tau(X+\lambda Y)=\tau(X)+\bar\lambda\,\tau(Y),\qquad \tau(XY)=\tau(X)\tau(Y),\qquad \tau^2=\mathrm{id}.
$$

**Notation.** Real structures of the element algebra $\mathbb{B}$ are written $\sigma$; real structures of the operator algebra $\mathcal{E}_{\mathbb{C}}$ are written $\tau$. A real structure $\sigma$ of $\mathbb{B}$ acts on operators by conjugation, $T\mapsto\sigma\circ T\circ\sigma^{-1}$; that induced map is written $\tau_{\sigma}$, and it is a real structure of $\mathcal{E}_{\mathbb{C}}$ only when it is checked to be conjugate-linear and involutive, which is a separate statement proved in the ninth section.

**Proposition (the fixed set is a real form).** Let $\tau$ be a real structure on $\mathcal{E}_{\mathbb{C}}$ and let

$$
\mathcal{E}^{\tau}=\{X\in\mathcal{E}_{\mathbb{C}}:\tau(X)=X\}.
$$

Then $\mathcal{E}^{\tau}$ is a real subalgebra of real dimension sixteen, and the multiplication map

$$
\mu:\mathcal{E}^{\tau}\otimes_{\mathbb{R}}\mathbb{C}\longrightarrow\mathcal{E}_{\mathbb{C}},\qquad X\otimes\lambda\longmapsto\lambda X
$$

is an isomorphism of $\mathbb{C}$-algebras.

*Proof.* Conjugate-linearity gives $\tau(\lambda X)=\bar\lambda\tau(X)$, so the fixed set is closed under addition and under real scalars and is a real subspace. Multiplicativity makes it a subalgebra. Every $X$ splits as

$$
X=\tfrac12\bigl(X+\tau(X)\bigr)+\tfrac12\bigl(X-\tau(X)\bigr),
$$

and the second summand is $i$ times the fixed element $\tfrac{1}{2i}(X-\tau(X))$, so $\mathcal{E}_{\mathbb{C}}=\mathcal{E}^{\tau}\oplus i\mathcal{E}^{\tau}$ as real spaces and the real dimension is sixteen. The multiplication map is surjective by that splitting and injective on dimensions. ∎

**The two concrete real structures.** Fix a matrix frame, that is an identification $\mathcal{E}_{\mathbb{C}}\cong M_4(\mathbb{C})$. The **entrywise conjugation**

$$
\tau_{\mathbb{R}}(X)=\bar X
$$

is a real structure, whose fixed set is $M_4(\mathbb{R})$. The **quaternionic conjugation**

$$
\tau_{\mathbb{H}}(X)=J_0\bar XJ_0^{-1},\qquad J_0=\begin{pmatrix}0&\mathrm{I}_2\\-\mathrm{I}_2&0\end{pmatrix},
$$

is a real structure, because $J_0$ is skew and $\bar J_0=-J_0$ give $\tau_{\mathbb{H}}^2=\mathrm{id}$. Its fixed set consists of the matrices

$$
X=\begin{pmatrix}A&B\\-\bar B&\bar A\end{pmatrix},\qquad A,B\in M_2(\mathbb{C}),
$$

which is the standard model of $M_2(\mathbb{H})$: the pair $(A,B)$ comprises the sixteen real parameters of four quaternionic entries, and the block rule is the rule of quaternionic multiplication.

**Warning (a real structure on the operators is not a real structure on the algebra).** A real structure on $\mathbb{B}$ is a conjugate-linear multiplicative involution of $\mathbb{B}$; a real structure on $\mathcal{E}_{\mathbb{C}}$ is a conjugate-linear multiplicative involution of the operators. The two are different maps on different algebras. The only bridge is the action on the regular families: a real structure $\sigma$ of $\mathbb{B}$ carries $L_{\tilde Q}$ to $L_{\sigma(\tilde Q)}$ and $R_{\tilde Q}$ to $R_{\sigma(\tilde Q)}$ when it is extended by conjugation, and the extension is a real structure of the operator algebra only after it is checked to be conjugate-linear on operators, which is a separate statement and is not automatic.

### Complexification of the Real Operator Algebra

**Definition (the scalar extension).** The complexification of the real operator algebra is

$$
\mathcal{E}_{\mathbb{R},\mathbb{C}}:=\mathcal{E}_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C},
$$

with the product $(X\otimes\lambda)(Y\otimes\mu)=XY\otimes\lambda\mu$.

**Proposition (the scalar extension is a full matrix algebra).** A real basis of $\mathbb{B}$ identifies $\mathcal{E}_{\mathbb{R}}$ with $M_8(\mathbb{R})$, and the same basis identifies

$$
\mathcal{E}_{\mathbb{R},\mathbb{C}}\cong M_8(\mathbb{R})\otimes_{\mathbb{R}}\mathbb{C}\cong M_8(\mathbb{C}),
$$

an algebra of complex dimension sixty-four and centre $\mathbb{C}\cdot\mathrm{I}_8$.

*Proof.* The identification of $\mathcal{E}_{\mathbb{R}}$ with $M_8(\mathbb{R})$ is the choice of a real basis. Entrywise extension of scalars gives $M_8(\mathbb{R})\otimes_{\mathbb{R}}\mathbb{C}\cong M_8(\mathbb{C})$, and the identification carries the centre to the centre. ∎

**Proposition (the real operator algebra has no complex structure).** The algebra $\mathcal{E}_{\mathbb{R}}$ admits no complex structure in the sense of [Classification of the Structures of the Biquaternion Algebra](classification-of-the-structures-of-the-biquaternion-algebra.html), that is, no unital $\mathbb{R}$-algebra map $\kappa:\mathbb{C}\to Z(\mathcal{E}_{\mathbb{R}})$.

*Proof.* A unital map of fields $\mathbb{C}\to\mathbb{R}$ is injective, so its image would be a subfield of $\mathbb{R}$ isomorphic to $\mathbb{C}$. No such subfield exists: every real $x$ satisfies $x^2\ge 0$, while the image of $i$ would satisfy $x^2=-1$. Since $Z(\mathcal{E}_{\mathbb{R}})=\mathbb{R}\cdot\mathrm{I}_8$ is a copy of $\mathbb{R}$, there is no such map. ∎

**Remark (non-central copies of $\mathbb{C}$ do not count).** The algebra $M_8(\mathbb{R})$ does contain subfields isomorphic to $\mathbb{C}$: four copies of the block $\begin{pmatrix}a&b\\-b&a\end{pmatrix}$ on the diagonal give a unital ring map $\mathbb{C}\to M_8(\mathbb{R})$ whose image is not central. Such a map makes $M_8(\mathbb{R})$ a complex algebra, but not by scalar extension: the complex scalars do not act through the centre. The definition asks for the centre for exactly this reason, and the next warning draws the consequence.

**Warning (no complex structure, only a complexification).** The phrase "complex form of $M_8(\mathbb{R})$" names no object. What exists is the complexification $M_8(\mathbb{C})$, obtained by extending scalars, and its two real forms, $M_8(\mathbb{R})$ and $M_4(\mathbb{H})$. Every occurrence of "complex form of the operator algebra" in the source paper is read in this article as "complexification and its real forms".

### The Two Questions Are Not Inverse

The two notions run in opposite directions and are not inverse to one another. A real structure descends from a complex algebra to a real one; a complexification ascends from a real algebra to a complex one. The first asks for a map on a given complex algebra, the second constructs a new complex algebra from a given real one.

| question | input | output |
|---|---|---|
| real forms of $\mathcal{E}_{\mathbb{C}}\cong M_4(\mathbb{C})$ | a complex algebra | real algebras of real dimension $16$ |
| real forms of $\mathcal{E}_{\mathbb{R},\mathbb{C}}\cong M_8(\mathbb{C})$ | a complex algebra | real algebras of real dimension $64$ |
| complexification of $\mathcal{E}_{\mathbb{R}}\cong M_8(\mathbb{R})$ | a real algebra | a complex algebra of complex dimension $64$ |
| complexification of $\mathcal{E}_{\mathbb{C}}$ read over $\mathbb{R}$ | a real algebra | a complex algebra of complex dimension $32$ |

**Warning (equal counts, different objects).** The two real-form counts are $2$ and $2$, and the coincidence is an accident of the two sizes. The objects classified in the two rows are different: the first row classifies the real algebras whose scalar extension is $M_4(\mathbb{C})$, the second the real algebras whose scalar extension is $M_8(\mathbb{C})$. Nothing follows from the equality of the counts, and no real form of $M_4(\mathbb{C})$ is a real form of $M_8(\mathbb{C})$.

### The Corrections of the Source Paper

Three statements of the source paper are corrected here, and the corrected forms are used throughout. They are recorded together so that a reader who compares the two texts finds the whole list in one place.

**Correction one (paper §3.3, heading "Real forms of $M_8(\mathbb{R})$").** The real algebra $M_8(\mathbb{R})$ has no real forms in the technical sense, because a real form is the fixed set of a real structure on a complex algebra and $M_8(\mathbb{R})$ is not complex. The correct statement is: *the complex algebra $M_8(\mathbb{C})=\mathcal{E}_{\mathbb{R},\mathbb{C}}$ has exactly two real forms, $M_8(\mathbb{R})$ and $M_4(\mathbb{H})$*. The heading names the wrong algebra, and the list it introduces is the list of real forms of the complexification.

**Correction two (paper §3.4, heading "Real forms of $\mathfrak{gl}(8,\mathbb{R})$").** The same slip in the Lie layer. The algebra $\mathfrak{gl}(8,\mathbb{R})$ is a real Lie algebra and has no real forms; the list belongs to the complex Lie algebra $\mathfrak{gl}(8,\mathbb{C})$, whose real forms are more numerous than the paper records. The corrected statement and its count are in the fourth section.

**Correction three (paper §4.2, the complexification read as a complex form).** The paper reads the tensor product $\operatorname{End}_{\mathbb{R}}(\mathbb{B})\otimes\mathbb{C}$ as a "complex form" of the endomorphism algebra. A complex form in the corpus's sense is an algebra with a complex structure, that is a central action of $\mathbb{C}$; the tensor product is a complexification, an ascent, and a complexification is not the fixed set of a real structure. The count that separates the two operations runs as follows. A real form of a complex algebra of complex dimension $n$ is a real algebra of real dimension $n$; a complexification $\mathcal{E}_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C}$ is a complex algebra of complex dimension sixty-four, hence a real algebra of real dimension one hundred and twenty-eight, twice the dimension that a real form of the ambient algebra can have. A form and an extension are objects of different sizes, and an extension is not a form of anything. The correct statement is: *$\mathcal{E}_{\mathbb{R},\mathbb{C}}\cong M_8(\mathbb{C})$ is the complexification of $\mathcal{E}_{\mathbb{R}}$, and its real forms are $M_8(\mathbb{R})$ and $M_4(\mathbb{H})$*.

**Remark (why the three come together).** All three corrections have one cause: the source paper uses the word "form" for the result of a scalar extension. The element-level article keeps the two words apart, and the separation is repeated here because the operator algebras have larger centres and the confusion is easier to make. A form is a subalgebra; an extension is a tensor product.

## The Real Forms of the Complex Operator Algebra

### The Two Forms

**Theorem (the real forms of the complex operator algebra).** Up to isomorphism, the algebra $\mathcal{E}_{\mathbb{C}}\cong M_4(\mathbb{C})$ has exactly two real forms:

$$
M_4(\mathbb{R})\quad\text{(split)},\qquad M_2(\mathbb{H})\quad\text{(quaternionic)}.
$$

*Proof.* Let $D$ be a real form, that is a real subalgebra of $\mathcal{E}_{\mathbb{C}}$ with $D\otimes_{\mathbb{R}}\mathbb{C}\cong\mathcal{E}_{\mathbb{C}}$. Then $D$ has real dimension sixteen. Its centre satisfies $Z(D)\otimes_{\mathbb{R}}\mathbb{C}\cong Z(\mathcal{E}_{\mathbb{C}})=\mathbb{C}$, so $Z(D)$ is a real form of $\mathbb{C}$ and is $\mathbb{R}$; and an ideal of $D$ complexifies to an ideal of $\mathcal{E}_{\mathbb{C}}$, which has none but $0$ and the whole, so $D$ is simple. Hence $D$ is a central simple $\mathbb{R}$-algebra of dimension sixteen. By Wedderburn's theorem $D\cong M_k(K)$ with $K$ a division algebra with centre $\mathbb{R}$, and by Frobenius the only such division algebras are $\mathbb{R}$ and $\mathbb{H}$. The dimension is $k^2$ in the first case and $4k^2$ in the second, so the possibilities are $k=4$ with $K=\mathbb{R}$ and $k=2$ with $K=\mathbb{H}$. ∎

**Remark (the two directions of the same theorem).** The proof is the proof of the element-level theorem with $4$ in place of $2$. The two real forms of $M_n(\mathbb{C})$ are $M_n(\mathbb{R})$ and $M_{n/2}(\mathbb{H})$ for even $n$; at $n=4$ the list reads $M_4(\mathbb{R})$ and $M_2(\mathbb{H})$, and at $n=2$ it reads $M_2(\mathbb{R})$ and $M_1(\mathbb{H})=\mathbb{H}$, which is the element-level statement. The general form, with the descent of the ideal lattice, of the automorphisms and of the derivations, is [Real Forms and the Descent of an Algebra](real-forms-and-the-descent-of-an-algebra.html).

**The two real structures, explicitly.** In a fixed matrix frame, the entrywise conjugation $\tau_{\mathbb{R}}(X)=\bar X$ has fixed set $M_4(\mathbb{R})$ and the quaternionic conjugation $\tau_{\mathbb{H}}(X)=J_0\bar XJ_0^{-1}$ has fixed set the block model of $M_2(\mathbb{H})$ of the previous section. The two real structures are not conjugate: if they were, their fixed algebras would be isomorphic, and the next proposition separates them by an invariant of the algebras.

### A Separating Invariant

**Proposition (the trace form).** On $\mathcal{E}_{\mathbb{C}}$ consider the symmetric bilinear form

$$
(X,Y)\longmapsto\operatorname{tr}(XY).
$$

Its restriction to $M_4(\mathbb{R})$ has inertia $(10,6)$, and its restriction to $M_2(\mathbb{H})$, in the block model, has inertia $(6,10)$.

*Proof.* On $M_4(\mathbb{R})$ decompose $X=S+K$ into symmetric and skew parts. Then $\operatorname{tr}(XY)$ pairs the symmetric part with the symmetric part and the skew part with the skew part, because the two subspaces are orthogonal under the trace; $\operatorname{tr}(S^2)=\sum_{ij}s_{ij}^2$ is positive definite on the ten-dimensional space of symmetric matrices, and $\operatorname{tr}(K^2)=-\sum_{ij}k_{ij}^2$ is negative definite on the six-dimensional space of skew matrices. On $M_2(\mathbb{H})$ use the quaternionic conjugation $X\mapsto X^{*}=\bar X^{\mathsf T}$, which preserves $M_2(\mathbb{H})$ and is the conjugate transpose in the block model. A matrix splits as $X=H+S$ with $H$ quaternionic Hermitian and $S$ quaternionic skew-Hermitian, and the two spaces are orthogonal under the trace: for $H$ Hermitian and $S$ skew the product $HS$ is skew-Hermitian, so $\operatorname{tr}(HS)$ is a pure imaginary quaternion and its real part vanishes. On the Hermitian space $\operatorname{tr}(X^{2})=\sum_k\lambda_k^{2}>0$ by the quaternionic spectral theorem, which writes a Hermitian matrix as a sum $\sum_k\lambda_kv_kv_k^{*}$ of rank-one Hermitian terms with real $\lambda_k$, and $\operatorname{tr}(X^{2})=\sum_k\lambda_k^{2}(v_k^{*}v_k)^{2}$; on the skew space $\operatorname{tr}(X^{2})<0$ by the same expansion applied to $iS$, which is Hermitian. The Hermitian space has real dimension $6$, from the two real diagonal entries and the one free quaternion off the diagonal, and the skew space has real dimension $10$, from the six real parameters on the diagonal and the same off-diagonal quaternion; the two add to $16$, and the inertia is $(6,10)$. ∎

**Corollary (the two real forms are not isomorphic).** $M_4(\mathbb{R})$ and $M_2(\mathbb{H})$ are not isomorphic as real algebras, so $\tau_{\mathbb{R}}$ and $\tau_{\mathbb{H}}$ are not conjugate by an automorphism of $\mathcal{E}_{\mathbb{C}}$.

**Remark (the inertia is an invariant of the algebra and not of the frame).** The trace form is defined without a basis, since the trace is, and a change of frame conjugates the form and preserves its inertia. The two inertias therefore separate the two real forms without a computation in coordinates beyond the one displayed. The same two inertias are the ones that the operator-level companion computes from the Killing form of the Lie layer: on the traceless part of $M_n(F)$ the Killing form is a positive multiple of the trace form, $K(X,Y)=2n\operatorname{tr}(XY)$, and on the centre the two forms are both positive, so the inertias of the two forms agree on each real form.

**Remark (the word "compact" is a misnomer at the operator level).** The element-level pair is called compact and split because the compact one is a division algebra and the group $SU(2)$ attached to it is compact. At the operator level no such statement survives. The compact real form of the Lie algebra $\mathfrak{gl}(4,\mathbb{C})$ is $\mathfrak{u}(4)$, and $\mathfrak{u}(4)$ is not the Lie algebra of any real form of the associative algebra $M_4(\mathbb{C})$: a real form of an algebra is closed under products, while the product of two skew-Hermitian matrices is skew-Hermitian only when the two commute. The real form $M_2(\mathbb{H})$ contains zero divisors, its Lie algebra $\mathfrak{gl}(2,\mathbb{H})$ contains a noncompact simple part, and the correct pair of words is **split** and **quaternionic**. The article uses those two words from here on.

### The Lie Algebra Has More Real Forms Than the Algebra

**Theorem (the real forms of $\mathfrak{gl}(4,\mathbb{C})$).** Up to isomorphism the complex Lie algebra $\mathfrak{gl}(4,\mathbb{C})$ has exactly six real forms:

$$
\mathfrak{gl}(4,\mathbb{R}),\quad
\mathfrak{u}(4),\quad
\mathfrak{u}(3,1),\quad
\mathfrak{u}(2,2),\quad
\mathfrak{gl}(2,\mathbb{H}),\quad
\mathfrak{gl}(4,\mathbb{C})_{\mathbb{R}}.
$$

Only two of them, $\mathfrak{gl}(4,\mathbb{R})$ and $\mathfrak{gl}(2,\mathbb{H})$, are the Lie algebras of real forms of the associative algebra $M_4(\mathbb{C})$.

*Proof.* The real forms of $\mathfrak{sl}(n,\mathbb{C})$ are the split form $\mathfrak{sl}(n,\mathbb{R})$, the unitary forms $\mathfrak{su}(p,q)$ with $p+q=n$ and $p\ge q$, the quaternionic form $\mathfrak{su}^{*}(n)$ for even $n$, and the realification $\mathfrak{sl}(n,\mathbb{C})_{\mathbb{R}}$. At $n=4$ this gives $\mathfrak{sl}(4,\mathbb{R})$, $\mathfrak{su}(4)$, $\mathfrak{su}(3,1)$, $\mathfrak{su}(2,2)$, $\mathfrak{su}^{*}(4)=\mathfrak{sl}(2,\mathbb{H})$ and $\mathfrak{sl}(4,\mathbb{C})_{\mathbb{R}}$, six forms in all. Adding the one-dimensional centre gives the six forms of the statement. The last sentence is the observation that $\mathfrak{u}(4)=\mathfrak{su}(4)\oplus\mathbb{R}i\mathrm{I}$ and the indefinite unitary forms are not closed under products. ∎

**The six forms in a table.** The invariants that separate them, with $\mathfrak{g}=\mathfrak{k}\oplus\mathfrak{p}$ the Cartan decomposition, $\dim_{\mathbb{R}}\mathfrak{g}=15$ throughout, and $\mathfrak{a}\subset\mathfrak{p}$ maximal abelian:

| real form | $\mathfrak{k}$ | $\dim_{\mathbb{R}}\mathfrak{k}$ | $\dim_{\mathbb{R}}\mathfrak{p}$ | real rank | restricted roots |
|---|---|---|---|---|---|
| $\mathfrak{sl}(4,\mathbb{R})$ | $\mathfrak{so}(4)$ | $6$ | $9$ | $3$ | $A_3$ |
| $\mathfrak{su}(4)$ | $\mathfrak{su}(4)$ | $15$ | $0$ | $0$ | none |
| $\mathfrak{su}(3,1)$ | $\mathfrak{s}(\mathfrak{u}(3)\oplus\mathfrak{u}(1))$ | $9$ | $6$ | $1$ | $BC_1$ |
| $\mathfrak{su}(2,2)$ | $\mathfrak{s}(\mathfrak{u}(2)\oplus\mathfrak{u}(2))$ | $7$ | $8$ | $2$ | $C_2$ |
| $\mathfrak{su}^{*}(4)\cong\mathfrak{so}(5,1)$ | $\mathfrak{sp}(2)$ | $10$ | $5$ | $1$ | $A_1$ |
| $\mathfrak{sl}(4,\mathbb{C})_{\mathbb{R}}$ | $\mathfrak{su}(4)$ | $15$ | $15$ | $3$ | $A_3$, multiplicity two |

The first and the last row have the same real rank and the same underlying restricted root system; they are separated by the size of the compact part, $\mathfrak{so}(4)$ of real dimension six in one case and $\mathfrak{su}(4)$ of real dimension fifteen in the other, and by the multiplicity of the restricted roots, one against two.

**Corollary (the count for $n=8$).** The complex Lie algebra $\mathfrak{gl}(8,\mathbb{C})$ has eight real forms: $\mathfrak{gl}(8,\mathbb{R})$; the five unitary forms $\mathfrak{u}(8)$, $\mathfrak{u}(7,1)$, $\mathfrak{u}(6,2)$, $\mathfrak{u}(5,3)$, $\mathfrak{u}(4,4)$; the quaternionic form $\mathfrak{gl}(4,\mathbb{H})$; and the realification $\mathfrak{gl}(8,\mathbb{C})_{\mathbb{R}}$. Only two of them are Lie algebras of real forms of $M_8(\mathbb{C})$.

**Remark (the corrected form of paper §3.4).** The source paper lists three real forms of $\mathfrak{gl}(8,\mathbb{C})$ under the heading "real forms of $\mathfrak{gl}(8,\mathbb{R})$", and the list omits the indefinite unitary forms and the quaternionic form. The heading and the count are both corrected above: the algebra with eight real forms is the complex one, and the two that come from real forms of the associative algebra are $\mathfrak{gl}(8,\mathbb{R})$ and $\mathfrak{gl}(4,\mathbb{H})$.

**Warning (a Lie-algebra real form is not an algebra real form).** The six forms of $\mathfrak{gl}(4,\mathbb{C})$ are six real Lie algebras with the same complexification, and two of them are algebras under a product. A real form of the Lie algebra is a subspace closed under the bracket; a real form of the associative algebra is a subalgebra closed under the product, and the second condition is stronger. The passage from the algebra to its Lie algebra therefore loses forms: the four forms $\mathfrak{u}(4)$, $\mathfrak{u}(3,1)$, $\mathfrak{u}(2,2)$ and $\mathfrak{gl}(4,\mathbb{C})_{\mathbb{R}}$ have no associative model inside $M_4(\mathbb{C})$ as a real form, and the compact one is the extreme case, being a subspace on which the product leaves at once.

## The Complexification of the Real Operator Algebra

### The Scalar Extension and Its Real Forms

**Theorem (the real forms of $\mathcal{E}_{\mathbb{R},\mathbb{C}}$).** The complex algebra $\mathcal{E}_{\mathbb{R},\mathbb{C}}\cong M_8(\mathbb{C})$ has exactly two real forms up to isomorphism, namely $M_8(\mathbb{R})$ and $M_4(\mathbb{H})$.

*Proof.* The argument of the fourth section with $8$ in place of $4$: a real form is a central simple $\mathbb{R}$-algebra of dimension $64$ whose scalar extension is $M_8(\mathbb{C})$, and Wedderburn with Frobenius leaves $M_8(\mathbb{R})$ and $M_4(\mathbb{H})$. ∎

**Remark (the two forms and the two structures).** The entrywise conjugation of $M_8(\mathbb{C})$ has fixed set $M_8(\mathbb{R})$, and the quaternionic conjugation $X\mapsto J_1\bar XJ_1^{-1}$, with $J_1$ the block skew matrix of size eight, has fixed set $M_4(\mathbb{H})$ in its block model. The two are separated by the trace form exactly as before, with the inertias $(36,28)$ for $M_8(\mathbb{R})$, from $36$ symmetric and $28$ skew directions, and $(28,36)$ for $M_4(\mathbb{H})$ in the block model.

### The Complexification of the Complex Operator Algebra

**Proposition (the scalar extension of the complex operator algebra).** The complexification of $\mathcal{E}_{\mathbb{C}}$ read over $\mathbb{R}$ is

$$
\mathcal{E}^{\oplus 2}_{\mathbb{C}}=\mathcal{E}_{\mathbb{C}}\otimes_{\mathbb{R}}\mathbb{C}\cong M_4(\mathbb{C})\oplus M_4(\mathbb{C}),
$$

of complex dimension thirty-two, with centre $\mathbb{C}\oplus\mathbb{C}$ and the two central idempotents $E_1=(\mathrm{I}_4,0)$ and $E_2=(0,\mathrm{I}_4)$.

*Proof.* The rules $\Phi(X\otimes1)=(X,\bar X)$ and $\Phi(X\otimes i)=(iX,i\bar X)$, with the bar taken entrywise in a fixed frame, define an isomorphism onto the direct sum: they are $\mathbb{R}$-bilinear, multiplicative, and they carry $X\otimes\lambda$ for complex $\lambda$ to $\lambda$ times the pair. The centre of the direct sum is the direct sum of the centres, and the two idempotents are the identities of the two summands. ∎

**Warning (the two complexifications are different objects).** The algebras

$$
\mathcal{E}_{\mathbb{R},\mathbb{C}}\cong M_8(\mathbb{C})\quad(\text{complex dimension }64)
\qquad\text{and}\qquad
\mathcal{E}^{\oplus 2}_{\mathbb{C}}=M_4(\mathbb{C})\oplus M_4(\mathbb{C})\quad(\text{complex dimension }32)
$$

are both scalar extensions, and neither is a complex form of the other. The first extends the real operator algebra, the second extends the complex operator algebra read over $\mathbb{R}$. They have different dimensions, different centres, and different real-form lattices: the first is simple with two real forms, the second is a direct sum whose real structures number five and whose real forms number four, in the pattern computed for the element-level complexification in [Classification of the Complex Structures of the Biquaternion Algebra, including Lie Algebras and Lie Groups](classification-of-the-complex-structures-of-the-biquaternion-algebra.html).

**Remark (which complexification belongs to which question).** A statement about **all** real-linear operators on the carrier, without a complex structure, belongs to $\mathcal{E}_{\mathbb{R}}$ and to its complexification $M_8(\mathbb{C})$. A statement about complex-linear operators whose complex structure is itself allowed to vary belongs to $\mathcal{E}_{\mathbb{C}}$ and to its complexification $M_4(\mathbb{C})\oplus M_4(\mathbb{C})$. The first is the operator-level analogue of $\mathbb{B}_{\mathbb{R}}$ and the second of $\mathbb{B}$, and the correspondence is exact: the carrier $\mathbb{B}$ gives the algebra $\mathcal{E}_{\mathbb{C}}$ and the carrier read over $\mathbb{R}$ gives $\mathcal{E}_{\mathbb{R}}$.

**Forward pointer.** The two real forms of $M_4(\mathbb{C})\oplus M_4(\mathbb{C})$, the five real structures that produce the four isomorphism classes, the two central idempotents and the Peirce decomposition at operator level are developed in *Classification of the Complex Structures of the Operators of the Biquaternion Algebra*. This article states only that the pattern is the one of the element-level complexification, with $M_4$ in place of $M_2$.

## The Double Centralizer and the Distinguished Subalgebras

### The Double Centralizer Theorem

**Theorem (double centralizer).** In $\mathcal{E}_{\mathbb{C}}$, with $L(\mathbb{B})$ and $R(\mathbb{B})$ the regular families,

$$
L(\mathbb{B})'=R(\mathbb{B}),\qquad R(\mathbb{B})'=L(\mathbb{B}),\qquad
\bigl(L(\mathbb{B})\cup R(\mathbb{B})\bigr)'=\mathbb{C}\cdot\mathrm{I}_4 .
$$

Moreover $L(\mathbb{B})\cap R(\mathbb{B})=\mathbb{C}\cdot\mathrm{I}_4$, and $L(\mathbb{B})$ and $R(\mathbb{B})$ are commuting copies of $M_2(\mathbb{C})$, the second with the reversed product.

*Proof.* Let $T\in\mathcal{E}_{\mathbb{C}}$ commute with every $R_{\tilde Q}$. Evaluating at the unit and using $R_{\tilde X}(e_t)=\tilde X$,

$$
T(\tilde X)=T\bigl(R_{\tilde X}(e_t)\bigr)=R_{\tilde X}\bigl(T(e_t)\bigr)=T(e_t)\tilde X,
$$

so $T=L_{T(e_t)}$ and $T\in L(\mathbb{B})$; the other inclusion is the identity $L_{\tilde Q}R_{\tilde X}=R_{\tilde X}L_{\tilde Q}$. The same computation with $L$ and $R$ exchanged gives the second equality. An operator commuting with both families commutes in particular with every $L_{\tilde Q}$, hence is some $R_{\tilde P}$, and it also commutes with every $R_{\tilde X}$, hence $\tilde P$ is central in $\mathbb{B}$, that is $\tilde P\in\mathbb{C}e_t$: the common centralizer is $\mathbb{C}\cdot\mathrm{I}_4$. Finally, if $L_{\tilde Q}=R_{\tilde P}$ then evaluating at $e_t$ gives $\tilde Q=\tilde P$, and then $\tilde Q\tilde X=\tilde X\tilde Q$ for all $\tilde X$, so $\tilde Q$ is central. ∎

**Corollary (the tensor form).** The multiplication map

$$
L(\mathbb{B})\otimes_{\mathbb{C}}R(\mathbb{B})\longrightarrow\mathcal{E}_{\mathbb{C}},\qquad L_{\tilde Q}\otimes R_{\tilde P}\longmapsto T_{\tilde Q,\tilde P},
$$

with $T_{\tilde Q,\tilde P}(\tilde X)=\tilde Q\tilde X\tilde P$, is an isomorphism of algebras. In a complex basis of $\mathbb{B}$ it reads $M_2(\mathbb{C})\otimes M_2(\mathbb{C})\cong M_4(\mathbb{C})$, with $L(\mathbb{B})=M_2(\mathbb{C})\otimes\mathrm{I}_2$ and $R(\mathbb{B})=\mathrm{I}_2\otimes M_2(\mathbb{C})^{\mathsf T}$.

*Proof.* The map is an algebra map, since $T_{\tilde Q,\tilde P}T_{\tilde R,\tilde S}=T_{\tilde Q\tilde R,\tilde S\tilde P}$ and the product in the tensor is taken with the reversed factor. Its image contains $L(\mathbb{B})$ and $R(\mathbb{B})$, hence contains their products, and the products span $\mathcal{E}_{\mathbb{C}}$ because every operator is a sum of two-sided ones. Both sides have complex dimension sixteen, so the surjection is an isomorphism. ∎

**Remark (the double centralizer is the bimodule statement).** The theorem says that the algebra $\mathbb{B}$ acts on itself on both sides with no waste: nothing commutes with the left action but the right action, and the two together exhaust the operators. That is the content of [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), where the enveloping algebra is identified with $\mathcal{E}_{\mathbb{C}}$ and the two regular families are its two tensor factors.

### The Complement

**Definition (the off-diagonal part).** Let $\mathfrak{sl}_2\subset\mathbb{B}$ be the traceless part, of complex dimension three, and put

$$
\mathfrak{m}:=\{T_{\tilde Q,\tilde P}:2\,\mathrm{Sc}\,\tilde Q=2\,\mathrm{Sc}\,\tilde P=0\}=\mathfrak{sl}_2\otimes_{\mathbb{C}}\mathfrak{sl}_2 .
$$

**Proposition (the decomposition).** The space $\mathfrak{m}$ has complex dimension nine, and

$$
\mathcal{E}_{\mathbb{C}}=(L(\mathbb{B})+R(\mathbb{B}))\oplus\mathfrak{m},
$$

where $L(\mathbb{B})+R(\mathbb{B})$ has complex dimension seven. Both assertions are equalities of vector spaces.

*Proof.* The dimension of $\mathfrak{m}$ is $3\cdot 3=9$. The sum $L+R$ has dimension $4+4-1=7$ by the intersection computed above. For the vanishing of the intersection, note first that $\mathbb{B}=\mathbb{C}e_t\oplus\mathfrak{sl}_2$ and that every two-sided operator splits by bilinearity as

$$
T_{\tilde Q,\tilde P}=T_{Q_0e_t,P_0e_t}+T_{Q_0e_t,P_1}+T_{Q_1,P_0e_t}+T_{Q_1,P_1},
$$

with $Q_1,P_1$ scalar-free; the first term is a scalar, the second lies in $R(\mathbb{B})$, the third in $L(\mathbb{B})$ and the fourth in $\mathfrak{m}$. Hence $\mathcal{E}_{\mathbb{C}}=L(\mathbb{B})+R(\mathbb{B})+\mathfrak{m}$, and the dimensions give $7+9=16$, so the sum is direct. ∎

**Warning (the sum $L+R$ is not direct, and $\mathfrak{m}$ is not a subalgebra).** The sum $L(\mathbb{B})+R(\mathbb{B})$ is a sum of two four-dimensional spaces meeting in the line $\mathbb{C}\cdot\mathrm{I}_4$; it is not direct, and it is not closed under products, since $L_{\tilde Q}R_{\tilde P}=T_{\tilde Q,\tilde P}$ leaves it whenever both factors are non-scalar. It is a Lie subalgebra, because $[L,L]\subset L$, $[R,R]\subset R$ and $[L,R]=0$. The complement $\mathfrak{m}$ is neither an associative nor a Lie subalgebra. For scalar-free parameters the product is $T_{\tilde Q,\tilde P}T_{\tilde R,\tilde S}=T_{\tilde Q\tilde R,\tilde S\tilde P}$, and $\tilde Q\tilde R$ is scalar-free only when $2\,\mathrm{Sc}(\tilde Q\tilde R)=0$, so the product leaves $\mathfrak{m}$; the witness is $(T_{\vec e_x,\vec e_x})^{2}=T_{\vec e_x^2,\vec e_x^2}=\mathrm{I}_4$, using $\vec e_x^2=-e_t$. The bracket is no better: $[T_{\vec e_x,\vec e_y},T_{\vec e_x,\vec e_z}]$ lies in $L(\mathbb{B})+R(\mathbb{B})$ and not in $\mathfrak{m}$. What does hold is stability under the scalar-free parts of the two regular families: $L_{\tilde Q}\mathfrak{m}R_{\tilde P}\subset\mathfrak{m}$ and $[L_{\tilde Q},\mathfrak{m}]\subset\mathfrak{m}$, $[R_{\tilde P},\mathfrak{m}]\subset\mathfrak{m}$ for $\tilde Q,\tilde P\in\mathfrak{sl}_2$, with $L_{\tilde Q}T_{\tilde R,\tilde S}R_{\tilde P}=T_{\tilde Q\tilde R,\tilde S\tilde P}$. The complement is a module over $L(\mathfrak{sl}_2)\oplus R(\mathfrak{sl}_2)$ and not over $L(\mathbb{B})\oplus R(\mathbb{B})$: $L_{\vec e_x}T_{\vec e_x,\vec e_y}R_{\vec e_y}=\mathrm{I}_4$ leaves $\mathfrak{m}$.

**Remark (why nine).** The number nine is the dimension of the space of traceless $2\times2$ matrices squared, $\mathfrak{m}=\mathfrak{sl}_2\otimes_{\mathbb{C}}\mathfrak{sl}_2$, and it is also $16-7$. Two readings of the same count: the operators that are neither a left multiplication, nor a right one, nor a scalar multiple of either, form a nine-dimensional space, and they are exactly the two-sided operators with both parameters scalar-free. The two factors explain the module structure: $[L_{\tilde Q},T_{\tilde R,\tilde S}]=T_{[\tilde Q,\tilde R],\tilde S}$ stays in $\mathfrak{m}$ for traceless $\tilde Q,\tilde R$, so $L(\mathfrak{sl}_2)$ acts on the first tensor factor and $R(\mathfrak{sl}_2)$ on the second, while $L(\mathbb{B})$ and $R(\mathbb{B})$ do not act at all.

### The Real Forms of the Distinguished Subalgebras

**Proposition (real forms of $L$ and $R$).** The algebra $L(\mathbb{B})$ is a copy of $M_2(\mathbb{C})$, and its real forms are

$$
L(\mathbb{H})\cong\mathbb{H},\qquad L(M_2(\mathbb{R}))\cong M_2(\mathbb{R}),
$$

of real dimension four each. The same holds for $R(\mathbb{B})$, with $R(\mathbb{H})\cong\mathbb{H}^{\mathrm{opp}}$ and $R(M_2(\mathbb{R}))\cong M_2(\mathbb{R})^{\mathrm{opp}}$.

*Proof.* $L$ is an injective algebra map, so it carries a real form of $\mathbb{B}$ to a real form of $L(\mathbb{B})$: the image has real dimension four and its complex span is $L(\mathbb{B})$. The isomorphisms are the restrictions of $L$ and the fact that $\mathbb{H}$ and $M_2(\mathbb{R})$ are the two real forms of $M_2(\mathbb{C})$. For $R$ the product is reversed, which is the opposite algebra. ∎

**Remark (the Lie layer of the same statement).** Read as Lie algebras, the real forms of $\mathfrak{gl}(2,\mathbb{C})$ number three: $\mathfrak{gl}(2,\mathbb{R})$, $\mathfrak{u}(2)$ and $\mathfrak{gl}(2,\mathbb{C})_{\mathbb{R}}$, exactly as in the fourth section with $2$ in place of $4$. The two that come from real forms of the associative algebra are $\mathfrak{gl}(2,\mathbb{R})$ and $\mathfrak{gl}(2,\mathbb{H})$, and the second is $\mathfrak{u}^{*}(2)$ in this size, which is $\mathfrak{u}(2)$: at $n=2$ the quaternionic form and the compact form are both $\mathfrak{su}(2)\oplus\mathbb{R}$ and coincide by dimension count. The coincidence does not survive to $n=4$, where $\mathfrak{gl}(2,\mathbb{H})$ is $\mathfrak{u}^{*}(4)$ and is not isomorphic to $\mathfrak{u}(4)$.

### The Six-Subspace Analogue

**Definition (the images of the six subspaces).** For each of the six remarkable subspaces $B_j$ of [Subspaces and Decompositions of the Biquaternion Algebra](subspaces-and-decompositions-of-the-biquaternion-algebra.html), put

$$
L(B_j)=\{L_{\tilde Q}:\tilde Q\in B_j\},\qquad R(B_j)=\{R_{\tilde Q}:\tilde Q\in B_j\}.
$$

Each is a real subspace of $\mathcal{E}_{\mathbb{C}}$ of the same real dimension as $B_j$, because $L$ and $R$ are injective and real-linear. The definitions of the six are recalled in [Classification of the Structures of the Biquaternion Algebra](classification-of-the-structures-of-the-biquaternion-algebra.html), §*The Six Subspaces and the Structures*: $\mathbb{B}_C$ is the centre, of real dimension two, $\mathbb{B}_V$ the pure part, of real dimension six, and $\mathbb{B}_H$, $\mathbb{B}_{iH}$, $\mathbb{B}_{\Psi}$, $\mathbb{B}_{\Phi}$ the four fixed and anti-fixed spaces of the three involutions, of real dimension four each.

| subspace | $\dim_{\mathbb{R}}$ | $\dim_{\mathbb{R}}L(B_j)$ | associative subalgebra | Lie subalgebra |
|---|---|---|---|---|
| $\mathbb{B}_C$ | $2$ | $2$ | yes, $\mathbb{C}\cdot\mathrm{I}_4$ | yes |
| $\mathbb{B}_V$ | $6$ | $6$ | no | yes |
| $\mathbb{B}_H$ | $4$ | $4$ | yes, $\cong\mathbb{H}$ | yes |
| $\mathbb{B}_{iH}$ | $4$ | $4$ | no | no |
| $\mathbb{B}_{\Psi}$ | $4$ | $4$ | no | no |
| $\mathbb{B}_{\Phi}$ | $4$ | $4$ | no | yes, $\cong\mathfrak{u}(2)$ |

**The two rows that are subalgebras.** $L(\mathbb{B}_C)=\mathbb{C}\cdot\mathrm{I}_4$ is the scalars, a subalgebra and a Lie subalgebra. $L(\mathbb{B}_H)$ is a subalgebra because $\mathbb{B}_H=\mathbb{H}$ is one, and it is a real form of $L(\mathbb{B})$ by the previous proposition.

**The two rows that are Lie subalgebras only.** $L(\mathbb{B}_V)$ is closed under the bracket, since the commutator of two pure elements is pure, and it is not closed under the product, since $\vec e_x^2=-e_t$ leaves $\mathbb{B}_V$: the witness is $L_{\vec e_x}^2=-L_{e_t}=-\mathrm{I}_4$. $L(\mathbb{B}_{\Phi})$ is closed under the bracket, because $\mathbb{B}_{\Phi}=\mathfrak{u}(2)$ is, and it is not closed under the product, since $\vec e_x\vec e_x=-e_t$ leaves $\mathbb{B}_{\Phi}$ as well.

**The two rows that are neither.** $L(\mathbb{B}_{iH})$ is not closed under the bracket: the elements $i\vec e_x$ and $i\vec e_y$ lie in $i\mathbb{B}_H$, and their bracket is $-[\vec e_x,\vec e_y]$, a nonzero multiple of $\vec e_z$; the element $\vec e_z$ lies outside $i\mathbb{B}_H$, whose intersection with $\mathbb{B}_V$ is spanned by $i\vec e_x,i\vec e_y,i\vec e_z$. $L(\mathbb{B}_{\Psi})$ is not closed under the bracket either. The elements $i\vec e_x$ and $i\vec e_y$ are Hermitian, hence lie in $\mathbb{B}_{\Psi}$, and $[i\vec e_x,i\vec e_y]=-2\vec e_z$. The element $\vec e_z$ is anti-Hermitian, $\vec e_z^{*}=-\vec e_z\neq\vec e_z$, so it lies outside $\mathbb{B}_{\Psi}$ and the bracket leaves the space. The two rows have the same cause: the bracket of two Hermitian matrices is anti-Hermitian, and $\mathbb{B}_{\Psi}$ is the Hermitian space.

**Warning (the six images are not all subalgebras).** The six subspaces $L(B_j)$ are complex subspaces of the operator algebra, and a complex subspace is a subalgebra only when the corresponding $B_j$ is a subalgebra of $\mathbb{B}$. Of the six, only $\mathbb{B}_C$ and $\mathbb{B}_H$ are subalgebras of $\mathbb{B}$; of the other four, $\mathbb{B}_V$ and $\mathbb{B}_{\Phi}$ are Lie subalgebras and $\mathbb{B}_{iH}$ and $\mathbb{B}_{\Psi}$ are neither. The same list holds for the $R$-images, and for a reason that can be stated once. The map $R$ is an anti-isomorphism onto its image, $R_{\tilde Q}R_{\tilde P}=R_{\tilde P\tilde Q}$, so $R(B_j)$ is closed under the product exactly when $B_j$ is; and $[R_{\tilde Q},R_{\tilde P}]=R_{[\tilde Q,\tilde P]}$, so the bracket on the image is the bracket of the parameters and $R(B_j)$ is a Lie subalgebra exactly when $B_j$ is. Reversing the product and keeping the bracket leave the six statuses unchanged.

## The Jordan Layer

**Definition (the symmetrized product).** Put

$$
X\circ Y=\tfrac12\bigl(XY+YX\bigr).
$$

This product is commutative and satisfies the Jordan identity $(X\circ Y)\circ(X\circ X)=X\circ\bigl(Y\circ(X\circ X)\bigr)$, and the complex algebra so obtained is written $\mathcal{E}_{\mathbb{C}}^{+}=M_4(\mathbb{C})^{+}$.

**Proposition (the Jordan real forms).** The complex Jordan algebra $\mathcal{E}_{\mathbb{C}}^{+}$ has at least the three real forms

$$
M_4(\mathbb{R})^{+},\qquad M_2(\mathbb{H})^{+},\qquad H_4(\mathbb{C}),
$$

of real dimension sixteen each, where $X^{*}$ is the conjugate transpose and $H_4(\mathbb{C})=\{X:X^{*}=X\}$ is the space of Hermitian matrices.

*Proof.* The first two are the Jordan algebras of the two real forms of the associative algebra, since the symmetrized product is invariant under the real structure. For the third: the adjoint of $X\mapsto X\circ Y$ for the trace form is $X\mapsto X\circ Y^{*}$, so $(X\circ Y)^{*}=X^{*}\circ Y^{*}$ and the Hermitian space is closed under $\circ$; its real dimension is $4+2\cdot 6=16$, counting the four real diagonal entries and the six complex off-diagonal entries; and its complex span is all of $\mathcal{E}_{\mathbb{C}}$, since every $X$ is the sum of the two Hermitian matrices $\tfrac12(X+X^{*})$ and $i\cdot\tfrac{1}{2i}(X-X^{*})$. The three are pairwise non-isomorphic: the trace form $\operatorname{tr}(X^{2})$ has inertia $(16,0)$ on $H_4(\mathbb{C})$, $(10,6)$ on $M_4(\mathbb{R})^{+}$ and $(6,10)$ on $M_2(\mathbb{H})^{+}$. ∎

**Warning (three Jordan structures over one associative algebra).** The three real forms of the Jordan algebra, the two real forms of the associative algebra and the six real forms of the Lie algebra are three different lattices over the same complex object,

$$
\mathcal{E}_{\mathbb{C}},\qquad
\mathcal{E}_{\mathbb{C}}^{+},\qquad
\mathcal{E}_{\mathbb{C}}^{\mathrm{Lie}}=\mathfrak{gl}(4,\mathbb{C}),
$$

with the last two obtained from the first by the identities

$$
XY=X\circ Y+\tfrac12[X,Y],\qquad X\circ Y=\tfrac12\bigl((X+Y)^{2}-X^{2}-Y^{2}\bigr).
$$

The associative lattice is the finest: a real form of $\mathcal{E}_{\mathbb{C}}$ gives one of each of the other two, and neither of the other two can be lifted back to an associative form in general. $H_4(\mathbb{C})$ is the witness: it is a real form of the Jordan algebra with no associative real form above it, since an associative real form of $M_4(\mathbb{C})$ is closed under products and $H_4(\mathbb{C})$ is not.

**Remark (the element-level observables act by self-adjoint operators).** Two forms on $\mathcal{E}_{\mathbb{C}}$ must be kept apart: the complex-bilinear trace form $(X,Y)\mapsto\operatorname{tr}(XY)$, which is the one whose inertias are computed above and which is not a Hermitian form, and the Hermitian form $(X,Y)\mapsto\operatorname{tr}(X^{*}Y)$, with $X^{*}$ the conjugate transpose. For $\tilde Q\in\mathbb{B}_{\Psi}=\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\}_{\mathbb{R}}$ the operator $L_{\tilde Q}$ is self-adjoint for the Hermitian form, since

$$
\operatorname{tr}\bigl((L_{\tilde Q}\tilde X)^{*}\tilde Y\bigr)=\operatorname{tr}\bigl(\tilde X^{*}L_{\tilde Q}\tilde Y\bigr)
$$

holds for $\tilde Q$ Hermitian, both sides reducing to $2\,\mathrm{Sc}(\tilde X^{*}\tilde Q\tilde Y)$, and the identity extends by linearity to the whole four-dimensional space. Hence

$$
L(\mathbb{B}_{\Psi})\subset H_4(\mathbb{C}),
$$

a real subspace of real dimension four and not a subalgebra, since the product of two Hermitian operators is Hermitian only when they commute. The statement is the operator-level shadow of the element-level one that $\mathbb{B}_{\Psi}$ is the observable space of $\mathbb{B}$.

**Forward pointer.** The Jordan lattice of $M_4(\mathbb{R})^{+}$ and of $M_2(\mathbb{H})^{+}$, the Peirce decompositions, the idempotents and the attached symmetric spaces are developed in the two operator-level companions. Here the Jordan layer is recorded only as a third structure that the real-form question produces.

## The Relation to the Element-Level Structures

### The Two Embeddings

The algebra $\mathbb{B}$ enters the operator algebra twice, on the left and on the right, and both entries are algebra maps of the same kind: an injective complex-linear map whose image is a four-dimensional subspace and a real-form-carrying map. For a real form $A_0$ of $\mathbb{B}$, with complexification $\mathbb{B}=A_0\otimes_{\mathbb{R}}\mathbb{C}$, the images are

$$
\iota_L(A_0)=L(A_0),\qquad \iota_R(A_0)=R(A_0),
$$

and both are real forms of $L(\mathbb{B})$ and of $R(\mathbb{B})$, of real dimension four. The two embeddings are isomorphisms onto their images, and the images are subalgebras: this is the statement of the sixth section, and it is the only statement of the element level that carries over without a change.

**Warning (the embedding does not carry the element-level classification).** The map $A_0\mapsto L(A_0)$ carries the two element-level real forms to two non-isomorphic four-dimensional subalgebras of $\mathcal{E}_{\mathbb{C}}$, namely $\mathbb{H}$ and $M_2(\mathbb{R})$; the map $A_0\mapsto R(A_0)$ carries them to the opposite algebras. Neither map classifies the real forms of the operator algebra, because both images have dimension four and the operator algebra has dimension sixteen: a real form of $\mathcal{E}_{\mathbb{C}}$ is a sixteen-dimensional object, and a four-dimensional image cannot be one.

### The Two-Sided Span

**Theorem (the span generated by a real form).** Let $A_0$ be a real form of $\mathbb{B}$ and put

$$
\mathcal{E}(A_0)=\operatorname{span}_{\mathbb{R}}\{T_{\tilde Q,\tilde P}:\tilde Q,\tilde P\in A_0\},
$$

the real span of the two-sided operators with both parameters in $A_0$. Then:

1. $\mathcal{E}(A_0)$ is a real subalgebra of $\mathcal{E}_{\mathbb{C}}$, generated as an algebra by $L(A_0)\cup R(A_0)$, of real dimension sixteen;
2. $\mathcal{E}(A_0)\otimes_{\mathbb{R}}\mathbb{C}=\mathcal{E}_{\mathbb{C}}$, so $\mathcal{E}(A_0)$ is a real form of $\mathcal{E}_{\mathbb{C}}$;
3. $\mathcal{E}(A_0)\cong A_0\otimes_{\mathbb{R}}A_0^{\mathrm{op}}$, an isomorphism of real algebras.

*Proof.* The set is closed under products because $T_{\tilde Q,\tilde P}T_{\tilde R,\tilde S}=T_{\tilde Q\tilde R,\tilde S\tilde P}$ and $A_0$ is a subalgebra, so it is a real subalgebra, and it contains $L(A_0)=T_{A_0,e_t}$ and $R(A_0)=T_{e_t,A_0}$, which generate it. The map $\tilde Q\otimes\tilde P\mapsto T_{\tilde Q,\tilde P}$ from $A_0\otimes_{\mathbb{R}}A_0^{\mathrm{op}}$ is an algebra map by the same product rule, and it is injective because $A_0$ is simple with centre $\mathbb{R}$, so its image has real dimension sixteen, which is also the dimension of the space spanned. Complexifying gives $A_0\otimes\mathbb{C}\otimes A_0^{\mathrm{op}}\otimes\mathbb{C}=\mathbb{B}\otimes\mathbb{B}^{\mathrm{op}}$, which is $\mathcal{E}_{\mathbb{C}}$ by the tensor form of the double centralizer. ∎

**Corollary (both element-level forms give the split operator form).** For $A_0=\mathbb{H}$ and for $A_0=M_2(\mathbb{R})$,

$$
\mathcal{E}(\mathbb{H})\cong\mathbb{H}\otimes_{\mathbb{R}}\mathbb{H}^{\mathrm{op}}\cong M_4(\mathbb{R}),
\qquad
\mathcal{E}(M_2(\mathbb{R}))\cong M_2(\mathbb{R})\otimes_{\mathbb{R}}M_2(\mathbb{R})^{\mathrm{op}}\cong M_4(\mathbb{R}).
$$

Both isomorphisms hold because a division algebra $D$ of real dimension $n$ satisfies $D\otimes_{\mathbb{R}}D^{\mathrm{op}}\cong\operatorname{End}_{\mathbb{R}}(D)\cong M_n(\mathbb{R})$, with $n=4$ for $\mathbb{H}$ and $n=2$ for $M_2(\mathbb{R})$, and $M_2(\mathbb{R})^{\mathrm{op}}\cong M_2(\mathbb{R})$ by the transpose.

**Lemma (the two-sided span is the fixed set of the induced real structure).** Let $\sigma$ be a real structure of $\mathbb{B}$ and let $\tau_{\sigma}(T)=\sigma\circ T\circ\sigma^{-1}$ be the induced map on $\mathcal{E}_{\mathbb{C}}$. Then $\tau_{\sigma}$ is a real structure of $\mathcal{E}_{\mathbb{C}}$, and its fixed set is $\mathcal{E}(A_0)$ for $A_0$ the fixed set of $\sigma$.

*Proof.* The map is conjugate-linear and multiplicative in $T$ and involutive, since $\sigma$ is. For $\tilde Q,\tilde P\in A_0$ one has $\tau_\sigma(T_{\tilde Q,\tilde P})=T_{\tilde Q,\tilde P}$, so $\mathcal{E}(A_0)$ is contained in the fixed set. Both sides have real dimension sixteen, the first by the theorem and the second by the proposition on the fixed set of a real structure, so they are equal. ∎

**Proposition (the two spans are distinct and conjugate).** The subalgebras $\mathcal{E}(\mathbb{H})$ and $\mathcal{E}(M_2(\mathbb{R}))$ are different subspaces of $\mathcal{E}_{\mathbb{C}}$; their intersection has real dimension eight. They are carried to one another by an automorphism of $\mathcal{E}_{\mathbb{C}}$.

*Proof.* By the lemma it suffices to exhibit one operator fixed by the first induced structure and not by the second. Take $R_{\vec e_x}$. With the coefficient conjugation as the reference conjugation of $\mathbb{B}$, which is the compact real structure $\sigma_{\mathrm{comp}}(\tilde Q)=\overline{\tilde Q}$, the element $\vec e_x$ has real coordinates and is fixed; hence $\tau_{\sigma_{\mathrm{comp}}}(R_{\vec e_x})=R_{\vec e_x}$ and $R_{\vec e_x}\in\mathcal{E}(\mathbb{H})$. The split real structure is $\sigma_{\mathrm{split}}(\tilde Q)=-\vec e_y\overline{\tilde Q}\vec e_y$, and $\sigma_{\mathrm{split}}(\vec e_x)=-\vec e_y\vec e_x\vec e_y=-\vec e_z\vec e_y=-\vec e_x$, using $\vec e_y\vec e_x=\vec e_z$ and $\vec e_z\vec e_y=\vec e_x$; hence $\tau_{\sigma_{\mathrm{split}}}(R_{\vec e_x})=R_{-\vec e_x}=-R_{\vec e_x}$ and $R_{\vec e_x}\notin\mathcal{E}(M_2(\mathbb{R}))$. The intersection is eight-dimensional by the direct computation of the rank of the two bases. For the conjugacy, choose an isomorphism $\alpha:\mathbb{H}\to M_2(\mathbb{R})$ of real algebras and extend $a\otimes b\mapsto\alpha(a)\otimes\alpha^{\mathrm{op}}(b)$ by complex linearity; the extension is an automorphism of $\mathcal{E}_{\mathbb{C}}=\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}$ that carries $\mathcal{E}(\mathbb{H})=\mathbb{H}\otimes_{\mathbb{R}}\mathbb{H}^{\mathrm{op}}$ onto $\mathcal{E}(M_2(\mathbb{R}))$. ∎

### The Quaternionic Real Form Is Not of This Shape

**Theorem (the endomorphisms of the quaternionic module).** Let

$$
\mathcal{E}^{\mathbb{H}}=\{F\in\mathcal{E}_{\mathbb{R}}:F(\tilde X\tilde Q)=F(\tilde X)\tilde Q\ \text{for all}\ \tilde Q\in\mathbb{H}\}
$$

be the real-linear maps that are right $\mathbb{H}$-linear. Then $\mathcal{E}^{\mathbb{H}}$ is a real subalgebra of $\mathcal{E}_{\mathbb{R}}$ of real dimension sixteen, $\mathcal{E}^{\mathbb{H}}\cong M_2(\mathbb{H})$, and $\mathcal{E}^{\mathbb{H}}$ is a real form of $\mathcal{E}_{\mathbb{C}}$ in the sense that $\mathcal{E}^{\mathbb{H}}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathcal{E}_{\mathbb{C}}$.

*Proof.* The algebra $\mathbb{B}$ is a free right $\mathbb{H}$-module of rank two, with the classes of $e_t$ and of $i\vec e_x$ as a basis, because $\mathbb{B}=\mathbb{H}\oplus i\mathbb{H}$. A right $\mathbb{H}$-linear map is therefore determined by its values on the two generators, which are eight real parameters each, so the dimension is sixteen; the endomorphism ring of a free module of rank two over a division ring is $M_2(\mathbb{H})$. The scalar extension is $M_2(\mathbb{H})\otimes_{\mathbb{R}}\mathbb{C}\cong M_4(\mathbb{C})$. ∎

**Corollary (the complex-linear part).** $\mathcal{E}^{\mathbb{H}}\cap\mathcal{E}_{\mathbb{C}}=L(\mathbb{B})$.

*Proof.* A complex-linear right $\mathbb{H}$-linear map $F$ satisfies $F(\tilde Q\tilde X)=F(\tilde Q)\tilde X$ and $F(i\tilde X)=iF(\tilde X)$. Writing $\tilde X=\tilde Q_1+i\tilde Q_2$ with $\tilde Q_j\in\mathbb{H}$ gives $F(\tilde X)=F(\tilde Q_1)+iF(\tilde Q_2)=F(e_t)\tilde Q_1+iF(e_t)\tilde Q_2=F(e_t)\tilde X$, so $F=L_{F(e_t)}$, and conversely every left multiplication is right $\mathbb{H}$-linear. ∎

**Warning (the element level does not determine the operator level).** The quaternionic real form $\mathcal{E}^{\mathbb{H}}$ is not generated by a real form of $\mathbb{B}$ through the two-sided action: both real forms of $\mathbb{B}$ generate the **split** operator form $M_4(\mathbb{R})$, as the previous subsection proves, and no choice of a four-dimensional real subalgebra can generate $M_2(\mathbb{H})$ this way. Moreover the one-sided images do not separate the two operator forms, because

$$
L(\mathbb{H})\subset\mathcal{E}(\mathbb{H})
\qquad\text{and}\qquad
L(\mathbb{H})\subset\mathcal{E}^{\mathbb{H}},
$$

so the presence of $\mathbb{H}$ among the left multiplications says nothing about which operator-level form is intended. The element-level choice selects a four-dimensional subalgebra; the operator-level form is a sixteen-dimensional object and is selected by a different piece of data, the module structure of $\mathbb{B}$ over a four-dimensional real subalgebra.

**Remark (which construction gives which form).** The rule that survives is a rule of dimension and of sidedness, not a rule of compactness. A one-sided action of a real form $A_0$ gives a four-dimensional subalgebra of $L(\mathbb{B})$ and of $R(\mathbb{B})$, and its Lie algebra is a real form of $\mathfrak{gl}(2,\mathbb{C})$; a two-sided action gives the sixteen-dimensional algebra $A_0\otimes A_0^{\mathrm{op}}$, and its Lie algebra is a real form of $\mathfrak{gl}(4,\mathbb{C})$. The compactness of the element-level form is not transmitted in either case: the compact form $\mathbb{H}$ generates the split algebra $M_4(\mathbb{R})$, and the compact real form $\mathfrak{u}(4)$ of the Lie layer is not the Lie algebra of a real form of the associative algebra at all.

## What the Operator-Level Structures Determine

The classification of the real forms of $\mathcal{E}_{\mathbb{C}}$ is complete and it is a classification by one invariant. What it decides, and what it leaves to other data, is worth stating separately.

**Determined by the operator-level real form.**
- The isomorphism class of the real algebra: split or quaternionic, separated by the inertia of the trace form, $(10,6)$ or $(6,10)$.
- The isomorphism class of the attached real Lie algebra, $\mathfrak{gl}(4,\mathbb{R})$ or $\mathfrak{gl}(2,\mathbb{H})$, and hence the lattice of its Lie subalgebras and its Killing form.
- The spectrum type of an element: a generic element of $M_4(\mathbb{R})$ has real or conjugate-pair eigenvalues, while an element of $M_2(\mathbb{H})$ has eigenvalues in classes of the quaternionic involution $\lambda\mapsto\bar\lambda$, so that the two algebras differ already in their elementary linear algebra.

**Not determined by the operator-level real form.**
- Which element-level form generated it. Both $\mathbb{H}$ and $M_2(\mathbb{R})$ generate the split form, so the element-level data is lost in the two-sided passage.
- The complex structure of the carrier. The operator algebra knows $\mathbb{B}$ as a complex vector space of dimension four; it does not know whether the carrier is read over $\mathbb{R}$ or over $\mathbb{C}$, and that choice is the choice between $\mathcal{E}_{\mathbb{C}}$ and $\mathcal{E}_{\mathbb{R}}$.
- The compactness of any group attached to the Lie layer, for the reason recorded in the fourth section: the compact real form $\mathfrak{u}(4)$ has no associative model, and the quaternionic form is not compact as a Lie algebra.
- The unitary representation theory, the harmonic analysis and the physical interpretation, which depend on the real form of the element algebra and on the global topology of the group, in the pattern of [Classification of the Real Structures of the Biquaternion Algebra, including Lie Algebras and Lie Groups](classification-of-the-real-structures-of-the-biquaternion-algebra.html).

**Warning (no operator-level statement follows from an element-level one alone).** The passage from a real form of $\mathbb{B}$ to a real form of $\mathcal{E}_{\mathbb{C}}$ is not injective: two non-isomorphic element-level forms give one operator-level form. A statement about the operator algebra therefore needs its own proof, and the operator-level classification is not a corollary of the element-level one. The two classifications are related by the dimension and by the sidedness of the action, and by nothing else that this article establishes.

**Remark (what a classification of operator structures is).** Two real structures of $\mathcal{E}_{\mathbb{C}}$ are classified up to isomorphism when their fixed algebras are isomorphic, and two real structures are conjugate when an automorphism of $\mathcal{E}_{\mathbb{C}}$ carries one to the other. The two notions agree here, because an isomorphism of the fixed algebras extends by complex linearity to an automorphism of the ambient algebra. The count is two in each case, the invariant is the inertia of the trace form, and the whole content of the classification is the theorem of Wedderburn and Frobenius applied at dimension sixteen.

## Hand-Off

The chain of the operator level is

$$
\mathcal{E}_{\mathbb{C}}\cong M_4(\mathbb{C})
\ \longleftrightarrow\
\{M_4(\mathbb{R}),\ M_2(\mathbb{H})\},
\qquad
\mathcal{E}_{\mathbb{R},\mathbb{C}}\cong M_8(\mathbb{C})
\ \longleftrightarrow\
\{M_8(\mathbb{R}),\ M_4(\mathbb{H})\}.
$$

The complex operator algebra fixes its two real forms; the real operator algebra has no complex structure and its complexification fixes its two real forms; and the two complexifications are different objects, of complex dimensions thirty-two and sixty-four. The distinguished subalgebras $L(\mathbb{B})$ and $R(\mathbb{B})$ are commuting copies of $M_2(\mathbb{C})$, their common centralizer is the scalars, and the two-sided operators split as $L+R$ plus a nine-dimensional complement. The Jordan layer adds a third lattice over the same complex algebra, with the Hermitian space $H_4(\mathbb{C})$ as the real form that has no associative model. The element level enters through the two embeddings, and a real form of $\mathbb{B}$ generates, by the two-sided action, the split operator form whichever of the two element-level forms is chosen.

Three texts follow. *Classification of the Real Structures of the Operators of the Biquaternion Algebra* develops the two real forms $M_4(\mathbb{R})$ and $M_2(\mathbb{H})$ layer by layer, with the subalgebras, the Lie algebras, the Killing forms and the Lie groups. *Classification of the Complex Structures of the Operators of the Biquaternion Algebra* develops the complexification $\mathcal{E}^{\oplus 2}_{\mathbb{C}}\cong M_4(\mathbb{C})\oplus M_4(\mathbb{C})$, its five real structures and its four isomorphism classes, counted by the pattern of the element-level complexification with $M_4$ in place of $M_2$ and checked there, and with the Peirce decomposition at operator level. *The Endomorphisms of the Biquaternion Algebra*, [Operators Acting on One Side](operators-acting-on-one-side.html) and [Operators Acting on Two Sides](operators-acting-on-two-sides.html) collect the operators of the corpus, the regular families, the transposition, the involutions and the two-sided operators, in the operator-level dictionary. The element-level background is [Classification of the Structures of the Biquaternion Algebra](classification-of-the-structures-of-the-biquaternion-algebra.html), and the general theory of descent is [Real Forms and the Descent of an Algebra](real-forms-and-the-descent-of-an-algebra.html).

## Summary

The two operator algebras of $\mathbb{B}$ are $\mathcal{E}_{\mathbb{C}}=\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_4(\mathbb{C})$, of complex dimension sixteen, and $\mathcal{E}_{\mathbb{R}}=\operatorname{End}_{\mathbb{R}}(\mathbb{B})\cong M_8(\mathbb{R})$, of real dimension sixty-four; the first is the complex-linear part of the second.

The complex operator algebra has exactly two real forms up to isomorphism, the split $M_4(\mathbb{R})$ and the quaternionic $M_2(\mathbb{H})$, obtained as the fixed sets of the entrywise conjugation and of the quaternionic conjugation, and separated by the inertia of the trace form, $(10,6)$ and $(6,10)$. The real operator algebra has no complex structure, because its centre is $\mathbb{R}$ and there is no unital map $\mathbb{C}\to\mathbb{R}$; its complexification is $M_8(\mathbb{C})$, whose real forms are $M_8(\mathbb{R})$ and $M_4(\mathbb{H})$. The complexification of the complex operator algebra read over $\mathbb{R}$ is $M_4(\mathbb{C})\oplus M_4(\mathbb{C})$, of complex dimension thirty-two, and the two complexifications are different objects with different real-form lattices.

The Lie algebra of the complex operator algebra has six real forms, $\mathfrak{gl}(4,\mathbb{R})$, $\mathfrak{u}(4)$, $\mathfrak{u}(3,1)$, $\mathfrak{u}(2,2)$, $\mathfrak{gl}(2,\mathbb{H})$ and $\mathfrak{gl}(4,\mathbb{C})_{\mathbb{R}}$, of which only the first and the fifth are Lie algebras of real forms of the associative algebra; the compact form $\mathfrak{u}(4)$ is not closed under products and has no associative model. The word "compact" is therefore a misnomer at the operator level, and the pair of words used is split and quaternionic.

The double centralizer theorem identifies $L(\mathbb{B})$ and $R(\mathbb{B})$ as the mutual centralizers, their common centralizer as the scalars, and the algebra as generated by the two families; $L+R$ has complex dimension seven, its complement $\mathfrak{m}=\mathfrak{sl}_2\otimes\mathfrak{sl}_2$ is the nine-dimensional space of two-sided operators with both parameters traceless, and $\mathfrak{m}$ is a module over $L(\mathfrak{sl}_2)\oplus R(\mathfrak{sl}_2)$ and neither an associative nor a Lie subalgebra. The images of the six remarkable subspaces under $L$ have the same dimensions and the same algebra-statuses as the subspaces themselves: two subalgebras, two Lie subalgebras and two that are neither.

The Jordan layer is a third lattice, with the real forms $M_4(\mathbb{R})^{+}$, $M_2(\mathbb{H})^{+}$ and $H_4(\mathbb{C})$, the last with no associative real form above it, and with $L(\mathbb{B}_{\Psi})\subset H_4(\mathbb{C})$ the operator-level shadow of the observables.

The element level enters through two embeddings of dimension four, and a real form of $\mathbb{B}$ generates by the two-sided action the split operator form: $\mathcal{E}(\mathbb{H})\cong\mathcal{E}(M_2(\mathbb{R}))\cong M_4(\mathbb{R})$, while the quaternionic operator form is the algebra of right $\mathbb{H}$-linear maps and is selected by the module structure, not by the subalgebra. The operator-level classification therefore is not a corollary of the element-level one, and the passage between them loses information.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{E}_{\mathbb{C}}=\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ | The complex operator algebra, $M_4(\mathbb{C})$, complex dimension $16$ |
| $\mathcal{E}_{\mathbb{R}}=\operatorname{End}_{\mathbb{R}}(\mathbb{B})$ | The real operator algebra, $M_8(\mathbb{R})$, real dimension $64$ |
| $\mathcal{E}_{\mathbb{R},\mathbb{C}}=\mathcal{E}_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C}$ | The complexification of the real operator algebra, $M_8(\mathbb{C})$ |
| $\mathcal{E}^{\oplus 2}_{\mathbb{C}}=\mathcal{E}_{\mathbb{C}}\otimes_{\mathbb{R}}\mathbb{C}$ | The complexification of the complex operator algebra read over $\mathbb{R}$, $M_4(\mathbb{C})\oplus M_4(\mathbb{C})$ |
| $\mathcal{E}^{\tau}$ | The real form of $\mathcal{E}_{\mathbb{C}}$ fixed by the real structure $\tau$ |
| $\tau_{\mathbb{R}}(X)=\bar X$ | The entrywise conjugation; fixed set $M_4(\mathbb{R})$ |
| $\tau_{\mathbb{H}}(X)=J_0\bar XJ_0^{-1}$ | The quaternionic conjugation; fixed set $M_2(\mathbb{H})$ |
| $H_4(\mathbb{C})$ | The Hermitian matrices for the trace form; real dimension $16$ |
| $L_{\tilde Q}(\tilde X)=\tilde Q\tilde X$, $R_{\tilde Q}(\tilde X)=\tilde X\tilde Q$ | The left and right multiplications |
| $L(\mathbb{B})$, $R(\mathbb{B})$ | The regular families, mutually centralizing copies of $M_2(\mathbb{C})$ |
| $T_{\tilde Q,\tilde P}(\tilde X)=\tilde Q\tilde X\tilde P$ | The two-sided operator |
| $\mathfrak{m}=\{T_{\tilde Q,\tilde P}:2\,\mathrm{Sc}\,\tilde Q=2\,\mathrm{Sc}\,\tilde P=0\}$ | The complement of $L+R$ in $\mathcal{E}_{\mathbb{C}}$, complex dimension $9$ |
| $X\circ Y=\tfrac12(XY+YX)$ | The symmetrized product; the Jordan layer |
| $\mathcal{E}(A_0)=\operatorname{span}_{\mathbb{R}}\{T_{\tilde Q,\tilde P}:\tilde Q,\tilde P\in A_0\}$ | The two-sided span of a real form $A_0$ of $\mathbb{B}$ |
| $\mathcal{E}^{\mathbb{H}}$ | The right $\mathbb{H}$-linear maps; $\cong M_2(\mathbb{H})$ |

## Further Reading

- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, second edition, 2001), for the theorem of Wedderburn, the theorem of Frobenius and the classification of the central simple algebras over $\mathbb{R}$.
- Israel Nathan Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the Skolem–Noether theorem and the conjugacy of the real structures.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the involutions of the first and second kind and their fixed algebras at the operator level.
- Nicolas Bourbaki, *Algebra II* (Springer, 2003), for the scalar extension and the descent by a quadratic extension.
- Nathan Jacobson, *Lectures on Quadratic Jordan Algebras* (Tata Institute, 1969), and Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the Jordan layer and the Hermitian real forms $H_n(\mathbb{C})$.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), and Arkady L. Onishchik and Ernest B. Vinberg, *Lie Groups and Algebraic Groups* (Springer, 1990), for the real forms of the classical Lie algebras and the Lie groups attached to the operator real forms.
- Stephen J. Sangwine, Todd A. Ell and Nicolas Le Bihan, *Fundamental Representations and Algebraic Properties of Biquaternions or Complexified Quaternions* (Advances in Applied Clifford Algebras 21, 2011), for the matrix representations and the two readings of the carrier.
