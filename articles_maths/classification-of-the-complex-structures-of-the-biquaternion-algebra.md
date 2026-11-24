# __Classification of the Complex Structures of the Biquaternion Algebra, including Lie Algebras and Lie Groups__

## Introduction and Scope

The companion article [Classification of the Structures of the Biquaternion Algebra](classification-of-the-structures-of-the-biquaternion-algebra.html) classifies the structures that change the ground field. It proves that the complex algebra $\mathbb{B}=M_2(\mathbb{C})$ carries exactly two real structures, that their fixed sets $M_2(\mathbb{R})$ and $\mathbb{H}$ are the only two real forms, and that the complexification $\mathbb{B}_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C}$ is $M_2(\mathbb{C})\oplus M_2(\mathbb{C})$, an algebra of complex dimension eight. The companion article [Classification of the Real Structures of the Biquaternion Algebra, including Lie Algebras and Lie Groups](classification-of-the-real-structures-of-the-biquaternion-algebra.html) then develops the two real forms in three layers, associative, Lie and Jordan, with the Lie groups that the Lie layer determines.

This article develops the third object: the complexification. It is written in the same three layers, at the same level of detail, with the same conventions, and it takes $M_2(\mathbb{C})\oplus M_2(\mathbb{C})$ as its object of study in place of the pair $\{M_2(\mathbb{R}),\mathbb{H}\}$.

**The structural novelty, stated first.** Each real form is a **simple** algebra, so its subalgebra lattice is one connected object. The complexification is not simple: two central idempotents cut it into two commuting simple ideals, and every subalgebra of it projects onto subalgebras of the two factors in a way that need not respect the cut. A subalgebra may be a product of one subalgebra of each factor, the diagonal copy of one subalgebra, the graph of an isomorphism between two of them, or the fibre product of two onto a common quotient. The last two families have no counterpart in either real form, and they are what makes the complex case richer.

**The finding, stated as a contrast.** Within one factor the complex lattice is *smaller* than the real one. The unital subalgebras of $M_2(\mathbb{C})$ fall into five conjugacy classes, against six in $M_2(\mathbb{R})$, and the three continuous families of the real case collapse to single classes, because over $\mathbb{C}$ every nonzero number is a square and the projective line of complex structures is one orbit. The Jordan layer follows the same rule, six types against eight. The richness of the complex case is therefore not in the factors. It is in the product, and the sections that follow locate it there: the three families of subalgebras of the direct sum, the four real algebras rather than two, and the larger centre of the simply connected covers.

**Scope.** This article develops the complex form $\mathbb{B}^{\oplus 2}_{\mathbb{C}}=\mathbb{B}_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C}=M_2(\mathbb{C})\oplus M_2(\mathbb{C})$ in three layers, associative, Lie and Jordan, together with the two central idempotents, the Peirce decomposition, the Killing forms, the real-form lattice inside the complexification, the involutions and the six-subspace intersections, the Lie groups attached to each Lie subalgebra, and the comparison with the real case. It recaps the real-form results from the companion article without re-deriving them, and it cites [The Lie Correspondence and the Adjoint Representation](the-lie-correspondence-and-the-adjoint-representation.html) once for the general group theory.

The order is as follows. The next section fixes the complexification and the isomorphism that identifies it with the direct sum. The third section treats the two central idempotents and the Peirce decomposition, and states why that decomposition has no off-diagonal pieces. The fourth, fifth and sixth sections treat the associative, Lie and Jordan layers. The seventh computes the Killing forms and their ranks. The eighth gives the five real structures of the complexification, the four real algebras that they produce, and the diagonal correspondence with the two real forms of $\mathbb{B}$. The ninth treats the involutions and the intersections with the six remarkable subspaces. The tenth gives the Lie groups. The eleventh compares with the real case, the twelfth states what the complex form does and does not determine, and the thirteenth hands off.

## The Complex Form and the Complexification

**The complex form.** The algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has complex dimension four and is $M_2(\mathbb{C})$; the article [Classification of the Structures of the Biquaternion Algebra](classification-of-the-structures-of-the-biquaternion-algebra.html), §*The One Complex Structure*, proves that any complex form of $\mathbb{B}_{\mathbb{R}}$ is a central simple $\mathbb{C}$-algebra of dimension four, hence is $M_2(\mathbb{C})$, and that there is one isomorphism class. The real algebra $\mathbb{B}_{\mathbb{R}}$ is the same ring read with real scalars, of real dimension eight.

**Definition (the complexification).** The complexification is

$$
\mathbb{B}^{\oplus 2}_{\mathbb{C}}:=\mathbb{B}_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C},
$$

an algebra of complex dimension eight and real dimension sixteen. The superscript records the result of the next proposition: the complexification is two copies of the complex form. The glyph $\mathbb{B}_{\mathbb{C}}$ alone is not used in this article, neither for the complex form, which is written $\mathbb{B}$, nor for the complexification, which is written $\mathbb{B}^{\oplus 2}_{\mathbb{C}}$.

**Proposition (the complexification is a direct sum).** The rules

$$
\Phi(x\otimes 1)=(x,\bar x),\qquad \Phi(x\otimes i)=(ix,i\bar x)
$$

define an isomorphism of $\mathbb{C}$-algebras

$$
\Phi:\mathbb{B}_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C}\longrightarrow \mathbb{B}\oplus\mathbb{B},
$$

where $\bar x$ is the coefficient conjugation of $\mathbb{B}$.

*Proof.* The rule is $\mathbb{R}$-bilinear in the two slots of the tensor and $\mathbb{C}$-linear in the second, so it extends to a $\mathbb{C}$-linear map. It is multiplicative on the generators $x\otimes1$ and $x\otimes i$: the four cases reduce to

$$
(x,\bar x)(y,\bar y)=(xy,\overline{xy}),\qquad (ix,i\bar x)(y,\bar y)=(ixy,i\overline{xy}),
$$

and the two remaining products follow from these by the commutation $x\otimes i=i(x\otimes1)$. A $\mathbb{C}$-linear multiplicative map of algebras is a homomorphism. For surjectivity, let $(u,v)$ be given and put $y=i(\bar v-u)/2$ and $x=u-iy$; then $x+iy=u$ and $\bar x+i\bar y=v$, so $(u,v)=\Phi(x\otimes1)+\Phi(y\otimes i)$. The two sides have complex dimension eight, so the surjective homomorphism is an isomorphism. ∎

**The two copies.** Write

$$
\iota_1(M)=(M,0),\qquad \iota_2(M)=(0,M)
$$

for the two embeddings of the complex form. They are the inclusions of the two summands, each is injective, and their images commute elementwise: $\iota_1(M)\iota_2(N)=0$ for all $M,N$.

**Remark (the canonical real copy is slanted).** The first rule of $\Phi$ gives $\Phi(x\otimes1)=(x,\bar x)$, so the image of the real algebra itself in its complexification is the **slanted** copy $\{(x,\bar x):x\in\mathbb{B}\}$, not the diagonal $\{(x,x)\}$ and not a summand. That copy is a real form of the complexification, and the eighth section identifies it with the slanted form. Its existence is general: the complexification of a real algebra always contains the algebra, slanted by the conjugation of the scalars.

**Warning (the complex form is not the complexification).** The complex form of $\mathbb{B}_{\mathbb{R}}$ is $\mathbb{B}=M_2(\mathbb{C})$, of complex dimension four. The complexification is $M_2(\mathbb{C})\oplus M_2(\mathbb{C})$, of complex dimension eight. The two objects are different, their subalgebra lattices are different, and a statement about one is not a statement about the other. This article develops the second. The first enters only through its two copies $\iota_1(\mathbb{B})$ and $\iota_2(\mathbb{B})$ inside the second.

**Remark (one ideal against two).** The complex form is simple: its only two-sided ideals are $0$ and the algebra. The complexification has the four ideals $0$, $\mathbb{B}\oplus0$, $0\oplus\mathbb{B}$ and the whole algebra, and the two middle ones are simple. Every structural difference between this article and the companion article follows from that one difference, and the next section states its cause.

## The Two Central Idempotents and the Peirce Decomposition

**The two idempotents.** Write

$$
\Pi_1=(I,0),\qquad \Pi_2=(0,I).
$$

The notation of the corpus is used here: $e$ carries the base, $e_t$ and $\vec e_x,\vec e_y,\vec e_z$, and $e_1,e_2$ are the basis of $\mathbb{C}^2$ and of the reduced biquaternion layer, so the two central idempotents take the idempotent glyph $\Pi$ with the numeric Peirce subscripts of [Special Element and Peirce Conventions](special-element-and-peirce-conventions.html).

**Proposition (the two idempotents).** The elements $\Pi_1$ and $\Pi_2$ are idempotent, orthogonal, sum to the identity, are central, and are the only nonzero central idempotents of $\mathbb{B}^{\oplus 2}_{\mathbb{C}}$.

*Proof.* The products are computed slot by slot: $\Pi_1^2=(I^2,0)=\Pi_1$, $\Pi_2^2=\Pi_2$, and $\Pi_1\Pi_2=(I\cdot0,0\cdot I)=0=\Pi_2\Pi_1$. The sum is $(I,I)$, the identity of the direct sum. For centrality, let $(M,N)$ be any element; then

$$
\Pi_1(M,N)=(M,0)=(M,N)\Pi_1,\qquad \Pi_2(M,N)=(0,N)=(M,N)\Pi_2 .
$$

For uniqueness, let $P=(P_1,P_2)$ be a central idempotent. Centrality gives $P_1\in Z(\mathbb{B})=\mathbb{C}I$ and $P_2\in\mathbb{C}I$, and idempotence gives $P_k^2=P_k$ in $\mathbb{C}$, so each $P_k$ is $0$ or $I$. The four choices are $0$, $\Pi_1$, $\Pi_2$ and $(I,I)$, and $\Pi_1$ and $\Pi_2$ are the two that are neither. ∎

**The Peirce decomposition.** Relative to the family $\Pi_1,\Pi_2$, the Peirce components are $A_{ij}=\Pi_i A\Pi_j$ with $A=\mathbb{B}^{\oplus 2}_{\mathbb{C}}$, and

$$
A=\Pi_1A\Pi_1\oplus\Pi_1A\Pi_2\oplus\Pi_2A\Pi_1\oplus\Pi_2A\Pi_2 .
$$

**Proposition (the off-diagonal components vanish).** For every $(M,N)$,

$$
\Pi_1(M,N)\Pi_2=(0,0)=\Pi_2(M,N)\Pi_1 ,
$$

so $A_{12}=A_{21}=0$ and the decomposition reads

$$
\mathbb{B}^{\oplus 2}_{\mathbb{C}}=A_{11}\oplus A_{22},\qquad A_{11}=\mathbb{B}\oplus 0=\iota_1(\mathbb{B}),\qquad A_{22}=0\oplus\mathbb{B}=\iota_2(\mathbb{B}).
$$

*Proof.* The first display is the product of a general element with the two idempotents, computed slot by slot: $\Pi_1(M,N)\Pi_2=(M,0)(0,N)=(M\cdot0,0\cdot N)=(0,0)$, and symmetrically. The diagonal components are $\Pi_1(M,N)\Pi_1=(M,0)$ and $\Pi_2(M,N)\Pi_2=(0,N)$, which run over the two summands as $(M,N)$ runs over the algebra. ∎

**Remark (a Peirce decomposition without off-diagonal lines).** A Peirce decomposition is trivial in the technical sense when its off-diagonal components vanish, and this one is trivial for one reason: the family is central. The general Peirce cut of the corpus is the cut of a **non-central** pair, and inside each factor such a pair exists. The standard pair of $\mathbb{B}$ is $\tilde\Pi_{\mathrm{id},\pm}=\tfrac12(e_t\pm i\vec e_z)$, and it gives the four lines

$$
\mathbb{B}_{st}=\tilde\Pi_{\mathrm{id},s}\mathbb{B}\tilde\Pi_{\mathrm{id},t},\qquad s,t\in\{+,-\},
$$

each a complex line, with the mixed lines spanned by $\vec\Pi_{\mathrm{nil},1}=\tfrac12(i\vec e_x-\vec e_y)$ and $\vec\Pi_{\mathrm{nil},2}=\tfrac12(i\vec e_x+\vec e_y)$ and the products $\vec\Pi_{\mathrm{nil},1}\vec\Pi_{\mathrm{nil},2}=\tilde\Pi_{\mathrm{id},+}$ and $\vec\Pi_{\mathrm{nil},2}\vec\Pi_{\mathrm{nil},1}=\tilde\Pi_{\mathrm{id},-}$. That decomposition is [Peirce Decompositions of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), and it is repeated in each factor of the complexification. The contrast is the point of this section: the central pair cuts the algebra into two blocks and nothing more, while a non-central pair cuts one factor into four lines.

**Warning (why the vanishing of the off-diagonal components creates the new families).** The vanishing of $A_{12}$ and $A_{21}$ does not mean that a subalgebra of the complexification is a product of one subalgebra of each factor. It means only that the *algebra* is such a product. A subalgebra $S$ carries two projections $p_1(S)\subset\mathbb{B}$ and $p_2(S)\subset\mathbb{B}$, and it need not contain the pair of them: it may hold only the pairs $(u,v)$ that satisfy a relation. Whether the relation is trivial, an isomorphism, or a quotient map is decided in the fourth section, and that decision is the classification.

## Associative Subalgebras of the Complexification

**Theorem (Goursat, for algebras).** Let $A_1,A_2$ be unital $\mathbb{C}$-algebras, let $S\subset A_1\oplus A_2$ be a unital subalgebra, and let $p_i$ be the two projections. Put $S_i=p_i(S)$ and

$$
J_1=\{a\in S_1:(a,0)\in S\},\qquad J_2=\{b\in S_2:(0,b)\in S\}.
$$

Then $J_i$ is a two-sided ideal of $S_i$, the quotients $S_1/J_1$ and $S_2/J_2$ are isomorphic, and

$$
S=\{(x,y)\in S_1\oplus S_2:\ \digamma_{\mathrm{map}}(x+J_1)=y+J_2\}
$$

for the isomorphism $\digamma_{\mathrm{map}}:S_1/J_1\to S_2/J_2$ that sends $x+J_1$ to $y+J_2$ whenever $(x,y)\in S$.

*Proof.* For the ideal property, let $x\in S_1$ and $a\in J_1$, so that $(a,0)\in S$ by the definition of $J_1$. Choose $y$ with $(x,y)\in S$; then $(x,y)(a,0)=(xa,0)$ lies in $S$ and has zero second slot, so $xa\in J_1$, and the same product on the other side gives $ax\in J_1$. The computation in the second slot gives the ideal property of $J_2$. For well-definedness of $\digamma_{\mathrm{map}}$, suppose $(x,y)$ and $(x,y')$ lie in $S$; then $(0,y-y')=(x,y)-(x,y')\in S$ has zero first slot, so $y-y'\in J_2$ and the two images agree. The map is additive and multiplicative because products in the direct sum are computed slot by slot; it is surjective because every $y\in S_2$ occurs in a pair; it is injective because $y\in J_2$ forces $(0,y)\in S$ and hence $(x,0)=(x,y)-(0,y)\in S$, that is $x\in J_1$. For the display, the inclusion from left to right is the definition of $\digamma_{\mathrm{map}}$, and for the other inclusion let $\digamma_{\mathrm{map}}(x+J_1)=y+J_2$; choose $(x,y')\in S$ with $y'-y\in J_2$; then $(0,y-y')\in S$ and $(x,y)=(x,y')+(0,y-y')\in S$. ∎

**Corollary (the three families).** With the notation of the theorem, exactly one of the following holds:

- **product**: $J_1=S_1$ and $J_2=S_2$, so $S=S_1\oplus S_2$;
- **graph**: $J_1=0$ and $J_2=0$, so $S=\{(x,\digamma_{\mathrm{map}}(x)):x\in S_1\}$ is the graph of an isomorphism $\digamma_{\mathrm{map}}:S_1\to S_2$;
- **fibre product**: $J_1$ and $J_2$ are both nonzero proper, so $S$ is the fibre product of $S_1$ and $S_2$ over a proper common quotient.

*Proof.* If $J_1=S_1$ then $S_1/J_1=0$, so $S_2/J_2=0$ and $J_2=S_2$; the case is a product, and symmetrically. If $J_1=J_2=0$ the theorem gives a graph. The remaining case is the third. ∎

**Theorem (five unital subalgebras of $M_2(\mathbb{C})$).** Up to conjugacy by $GL_2(\mathbb{C})$ there are five unital subalgebras of $\mathbb{B}=M_2(\mathbb{C})$, namely

$$
\mathbb{C}I,\qquad \mathbb{C}\oplus\mathbb{C},\qquad \mathbb{C}[\epsilon],\qquad \mathfrak{b}_0,\qquad M_2(\mathbb{C}),
$$

of complex dimensions $1,2,2,3,4$, where $\mathbb{C}\oplus\mathbb{C}$ is $\mathbb{C}P\oplus\mathbb{C}P'$ for a projection $P$ of rank one, $\mathbb{C}[\epsilon]$ is $\mathbb{C}I\oplus\mathbb{C}N$ with $N\ne0$ and $N^2=0$, and $\mathfrak{b}_0$ is the algebra of upper triangular matrices, the Borel of $\mathfrak{gl}_2$; the subscript distinguishes it from the Borel $\operatorname{span}\{H,N\}$ of the traceless part.

*Proof.* A unital subalgebra $S$ of a four-dimensional algebra has dimension one to four. At dimension four it is the whole algebra, and at dimension one it is $\mathbb{C}I$. At dimension two, let $M\in S$ be non-scalar and put $U=M-\tfrac12\operatorname{tr}(M)I$; then $U$ is traceless and nonzero, and $S=\mathbb{C}I\oplus\mathbb{C}U$. Cayley–Hamilton for a traceless $2\times2$ matrix reads $U^2=-\det(U)I$, so $U^2=\mu I$ with $\mu=-\det U$, and closure imposes no further condition. If $\mu=0$ then $U$ is a nonzero nilpotent and $S=\mathbb{C}[\epsilon]$. If $\mu\ne0$, write $\mu=\nu^2$, which is possible because $\mathbb{C}$ is closed under square roots, and put $P=\tfrac12(I+U/\nu)$; then $P^2=P$, $P\ne I$, $P\ne0$, and $S=\mathbb{C}P\oplus\mathbb{C}(I-P)$, which is $\mathbb{C}\oplus\mathbb{C}$. At dimension three, let $V=S\cap\mathfrak{sl}_2(\mathbb{C})$, of dimension two. Since $S$ is an algebra, $V$ is closed under commutators, so it is a two-dimensional Lie subalgebra of $\mathfrak{sl}_2(\mathbb{C})$. It is not abelian: two commuting traceless matrices are simultaneously triangularizable, so they lie in a Borel, whose traceless part is spanned by $H=\operatorname{diag}(1,-1)$ and $N=E_{12}$ with $[H,N]=2N$; and two elements $aH+bN$ and $cH+dN$ of that part commute exactly when $ad-bc=0$, that is exactly when they are proportional. A two-dimensional nonabelian Lie algebra has a one-dimensional derived algebra, and after rescaling its basis it reads $\operatorname{span}\{H,N\}$ with $[H,N]=N$; inside $\mathfrak{sl}_2(\mathbb{C})$ the derived line is spanned by a nonzero element, semisimple or nilpotent, which conjugacy moves to a fixed one, and the second generator is then determined up to a multiple of the first. So all such $V$ are conjugate, and $S$ is conjugate to $\mathbb{C}I\oplus\operatorname{span}\{H,N\}=\mathfrak{b}_0$. ∎

**Remark (the three families of the real case collapse).** The real theorem of the companion article lists six classes and three continuous families: the copies of $\mathbb{C}$ form a hyperboloid of complex structures modulo $J'\mapsto-J'$, the rank-one projections a sphere, and the nilpotent lines a quadric. Over $\mathbb{C}$ each of the three is a single orbit, and the reason is the same in all three cases: $GL_2(\mathbb{C})$ is transitive on the objects of a fixed type, because every nonzero complex number is a square and a semisimple eigenvalue carries no sign. The step $\mu=\nu^2$ is where the closure under square roots enters, and it is the only step of the proof that differs from the real one.

**Theorem (graphs are diagonals).** Let $S_1,S_2$ be isomorphic unital subalgebras of $M_2(\mathbb{C})$ and let $S=\{(x,\digamma_{\mathrm{map}}(x)):x\in S_1\}$ be the graph of an isomorphism $\digamma_{\mathrm{map}}$. Then $S$ is conjugate in $GL_2(\mathbb{C})\times GL_2(\mathbb{C})$ to the diagonal $\{(x,x):x\in S_1\}$.

*Proof.* It is enough to show that every isomorphism between two of the five blocks is realised by conjugation with an element of $GL_2(\mathbb{C})$, because then $\digamma_{\mathrm{map}}=\operatorname{Ad}_g$ on $S_1$ and the element $(1,g^{-1})$ conjugates $(x,\operatorname{Ad}_g x)$ to $(x,x)$. For $\mathbb{C}I$ the statement is trivial. For $\mathbb{C}\oplus\mathbb{C}=\mathbb{C}P\oplus\mathbb{C}P'$ the only nontrivial automorphism exchanges $P$ and $P'$, and in the frame where $P=\operatorname{diag}(1,0)$ it is conjugation by $\sigma_1$. For $\mathbb{C}[\epsilon]$ an automorphism fixes $I$ and sends $N$ to $\lambda N$ with $\lambda\ne0$, and conjugation by $\operatorname{diag}(1,\lambda)$ does that. For $\mathfrak{b}_0$ an automorphism preserves the derived algebra $[S,S]=\mathbb{C}N$ and fixes $H$ modulo $\mathbb{C}N$, so it reads $H\mapsto H+\gamma N$, $N\mapsto\beta N$; conjugation by $\begin{pmatrix}a&b\\0&d\end{pmatrix}$ acts by $\beta=a/d$ and $\gamma=2b/d$, and $a,b,d$ are free with $a,d\ne0$, so every pair $(\beta,\gamma)$ occurs. For $M_2(\mathbb{C})$ the statement is Skolem–Noether. ∎

**Remark (what survives as new).** The theorem removes the graph family from the list of new classes whenever the two blocks are conjugate, and the real case of the companion article has the same property. Two subfamilies survive:

- **graphs across types**, such as the line spanned by $(N,H)$ with $N$ nilpotent and $H$ semisimple, which is the graph of an isomorphism $\mathbb{C}N\to\mathbb{C}H$ of one-dimensional algebras and is conjugate to no diagonal, since the two slots have different projective types;
- **fibre products**, which are not graphs at all.

**Proposition (a fibre product with a nilpotent quotient).** The set

$$
F=\{(A,B)\in\mathfrak{b}_0\oplus\mathfrak{b}_0:\ A-B\in\mathbb{C}N\},\qquad N=E_{12},
$$

is a unital subalgebra of dimension four. It contains neither $\Pi_1$ nor $\Pi_2$, and it is neither a product nor a graph.

*Proof.* Closure: write $A=B+\lambda N$ and $A'=B'+\lambda'N$ with $B,B'\in\mathfrak{b}_0$; then $AA'=BB'+\lambda BN+\lambda'NB+\lambda\lambda'NN$, and $BN$, $NB$ and $NN$ lie in the ideal $\mathbb{C}N$ of $\mathfrak{b}_0$, so $AA'-BB'\in\mathbb{C}N$. Dimension: the condition is $A_{11}=B_{11}$ and $A_{22}=B_{22}$, two linear conditions on a six-dimensional space. The identity $(I,I)$ satisfies them. Neither $\Pi_1$ nor $\Pi_2$ lies in $F$, because $I\notin\mathbb{C}N$; a product of unital subalgebras contains both, so $F$ is not a product. A graph contains no element with a zero slot and no element with the other slot zero, while $F$ contains $(N,0)$ and $(0,N)$; so $F$ is not a graph. ∎

**The table of the associative layer.** The rows give the families and their subfamilies, one witness each, its dimension, and the criterion that places the witness.

| family | witness | $\dim_{\mathbb{C}}$ | criterion |
|---|---|---|---|
| product | $\mathfrak{b}_0\oplus\mathbb{C}I$ | $4$ | contains $\Pi_1$ and $\Pi_2$ |
| diagonal | $\{(M,M)\}\cong M_2(\mathbb{C})$ | $4$ | graph of the identity |
| graph across types | $\mathbb{C}(N,H)$ | $1$ | graph, not conjugate to a diagonal |
| fibre product | $\{(A,B)\in\mathfrak{b}_0^2:A-B\in\mathbb{C}N\}$ | $4$ | no $\Pi_1$, no $\Pi_2$, not a graph |

**Remark (the non-unital subalgebras are not classified here).** A subalgebra without identity escapes the Goursat theorem as stated, because the projections need not be onto algebras with identity. Examples are $\mathbb{C}N\oplus0$ inside $\mathfrak{b}_0\oplus\mathfrak{b}_0$, the nilpotent radical of one factor; the graph of the zero map $\mathbb{C}N\to0$; and the strictly upper triangular line of one factor. Their classification is a separate problem, it is not needed below, and it is not undertaken here.

**Warning (the lattice of the product is not the product of the lattices).** The associative lattice of $M_2(\mathbb{C})\oplus M_2(\mathbb{C})$ is **not** the product of two copies of the lattice of $M_2(\mathbb{C})$. The diagonal, the graphs across types and the fibre products are new, and a subalgebra of the sum can have a dimension that no product of two subalgebras has. The count makes the point: five blocks give twenty-five products and five diagonals, and the fibre products add further classes, among them the four-dimensional witness above, whose dimension agrees with a product and with a diagonal and whose structure agrees with neither.

## Lie Subalgebras of the Complexification

**The Lie algebra.** The commutator turns $\mathbb{B}^{\oplus 2}_{\mathbb{C}}$ into a complex Lie algebra $\mathfrak{gl}(2,\mathbb{C})\oplus\mathfrak{gl}(2,\mathbb{C})$ of complex dimension eight. Its centre is $\mathbb{C}\Pi_1\oplus\mathbb{C}\Pi_2$, of dimension two, and its derived algebra is $\mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C})$, of dimension six. The algebra is neither simple nor semisimple: it is the direct sum of two simple ideals, and the centre is the two-dimensional abelian algebra of scalars.

**Theorem (Goursat, for Lie algebras).** Let $\mathfrak a_1,\mathfrak a_2$ be Lie algebras over $\mathbb{C}$, let $\mathfrak s\subset\mathfrak a_1\oplus\mathfrak a_2$ be a Lie subalgebra, and put $\mathfrak s_i=p_i(\mathfrak s)$, $\mathfrak j_1=\{x\in\mathfrak s_1:(x,0)\in\mathfrak s\}$ and $\mathfrak j_2=\{y\in\mathfrak s_2:(0,y)\in\mathfrak s\}$. Then $\mathfrak j_i$ is an ideal of $\mathfrak s_i$, the quotients are isomorphic, and $\mathfrak s$ is the fibre product of the $\mathfrak s_i$ over them.

*Proof.* The proof of the associative theorem repeats word for word, with the bracket in place of the product, because the bracket in a direct sum is computed slot by slot and the ideal property is the same computation: $[(x,y),(a,0)]=([x,a],0)$. ∎

**The blocks: Lie subalgebras of $\mathfrak{gl}(2,\mathbb{C})$.** Up to conjugacy by $GL_2(\mathbb{C})$ the Lie subalgebras of $\mathfrak{gl}(2,\mathbb{C})$ begin with the following list, ordered by dimension.

| dimension | algebra | normal form |
|---|---|---|
| $0$ | $0$ | — |
| $1$ | the centre | $\mathbb{C}I$ |
| $1$ | semisimple line | $\mathbb{C}\operatorname{diag}(1,0)$ |
| $1$ | one eigenvalue, Jordan part | $\mathbb{C}(I+\mu N)$, $\mu\ne0$ |
| $1$ | nilpotent line | $\mathbb{C}N$ |
| $2$ | abelian plane, semisimple | $\mathbb{C}I\oplus\mathbb{C}\operatorname{diag}(1,0)$ |
| $2$ | abelian plane, Jordan | $\mathbb{C}I\oplus\mathbb{C}N$ |
| $2$ | Borel | $\operatorname{span}\{H,N\}$, $[H,N]=N$ |
| $3$ | Borel with centre | $\mathfrak{b}_0=\mathbb{C}I\oplus\operatorname{span}\{H,N\}$ |
| $3$ | traceless part | $\mathfrak{sl}(2,\mathbb{C})$ |
| $4$ | the whole algebra | $\mathfrak{gl}(2,\mathbb{C})$ |

**Remark (four projective types of a line).** The four one-dimensional rows are the four projective Jordan types of a matrix over $\mathbb{C}$: the scalar type, the semisimple type with two distinct eigenvalues, the type with a single eigenvalue and a nontrivial Jordan part, and the nilpotent type, which is the member $\mu=0$ of the third family. Over $\mathbb{R}$ the count is five, because the semisimple type splits into the split and the complex cases according to the sign of the discriminant; that is the list of the companion article, §*Lie Subalgebras of the Split Form*. The parameter $\mu$ carries no invariant: conjugation by $\operatorname{diag}(1,t)$ sends $I+\mu N$ to $I+t\mu N$, and the line spanned by $I+t\mu N$ is the line spanned by $(1/(t\mu))I+N$, so all $\mu\ne0$ give one class. Over $\mathbb{R}$ the same computation leaves the sign of $\mu$, which is why the real list separates the Jordan block from its negative.

**Remark (the blocks in the biquaternion base).** The dictionary turns the standard matrices into corpus elements:

$$
H=\operatorname{diag}(1,-1)=i\vec e_z,\qquad E_{12}=\tfrac12(i\vec e_x-\vec e_y)=\vec\Pi_{\mathrm{nil},1},\qquad E_{21}=\tfrac12(i\vec e_x+\vec e_y)=\vec\Pi_{\mathrm{nil},2},\qquad E_{12}+E_{21}=i\vec e_x .
$$

Hence

$$
\mathfrak b_0=\operatorname{span}_{\mathbb{C}}\{e_t,\ i\vec e_z,\ \vec\Pi_{\mathrm{nil},1}\},\qquad \mathfrak{sl}_2(\mathbb{C})=\operatorname{span}_{\mathbb{C}}\{i\vec e_z,\ \vec\Pi_{\mathrm{nil},1},\ \vec\Pi_{\mathrm{nil},2}\},
$$

and the Cartan subalgebra is the line $\mathbb{C}\,i\vec e_z$. The three elements $(i\vec e_z,\vec\Pi_{\mathrm{nil},1},\vec\Pi_{\mathrm{nil},2})$ are the standard triple:

$$
[i\vec e_z,\vec\Pi_{\mathrm{nil},1}]=2\vec\Pi_{\mathrm{nil},1},\qquad [i\vec e_z,\vec\Pi_{\mathrm{nil},2}]=-2\vec\Pi_{\mathrm{nil},2},\qquad [\vec\Pi_{\mathrm{nil},1},\vec\Pi_{\mathrm{nil},2}]=i\vec e_z .
$$

The Cartan direction is one of the Hermitian units, and the two nilpotent directions are the two mixed Peirce lines, $\vec\Pi_{\mathrm{nil},1}$ spanning $\mathbb{B}_{+-}$ and $\vec\Pi_{\mathrm{nil},2}$ spanning $\mathbb{B}_{-+}$ in the Peirce decomposition of [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), where $\vec\Pi_{\mathrm{nil},1}\vec\Pi_{\mathrm{nil},2}=\tilde\Pi_{\mathrm{id},+}$ and $\vec\Pi_{\mathrm{nil},2}\vec\Pi_{\mathrm{nil},1}=\tilde\Pi_{\mathrm{id},-}$. So the abstract triple $(H,E,F)$ is, in this algebra, the diagonal unit and the two off-diagonal Peirce lines, and the Borel is spanned by the identity, the diagonal unit and one of the two off-diagonal lines. The same reading holds on the real side: all three elements have real matrices, so $\mathfrak b_0$ and $\mathfrak{sl}_2(\mathbb{C})$ are the complexifications of the real upper triangular and traceless matrices.

**Remark (why the complex algebra carries both real forms at once).** The two real forms are the traceless parts of the two real forms of $\mathbb{B}$: the compact form $\mathbb{H}$ has scalar-free part $\mathfrak{su}(2)=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$, and the split form has traceless part $\operatorname{span}_{\mathbb{R}}\{i\vec e_x,\vec e_y,i\vec e_z\}=\mathfrak{sl}(2,\mathbb{R})$. Because the three units $\vec e_x,\vec e_y,\vec e_z$ are already a $\mathbb{C}$-basis of the traceless part, the complex algebra is the complex span of each: the equations

$$
\mathfrak{sl}(2,\mathbb{C})=\mathfrak{su}(2)\otimes_{\mathbb{R}}\mathbb{C}=\mathfrak{sl}(2,\mathbb{R})\otimes_{\mathbb{R}}\mathbb{C}
$$

say that the complexification is the two slices glued by the coefficient field. What keeps the slices distinct is the star, which is conjugate-linear: no $\mathbb{C}$-linear operation can separate the anti-Hermitian units from the Hermitian ones. The two slices are exchanged by no complex-linear map, and that is the precise sense in which the complex algebra is one algebra with two real readings.

**The three families in the direct sum.** The Goursat theorem gives, for Lie subalgebras of $\mathfrak{gl}(2,\mathbb{C})\oplus\mathfrak{gl}(2,\mathbb{C})$, the same three families: products $\mathfrak s_1\oplus\mathfrak s_2$, graphs of isomorphisms, and fibre products over proper common quotients. The diagonal cases are the graphs of the identity, and they are the ones that lie inside one simple summand:

$$
\{(M,M):M\in\mathfrak{sl}(2,\mathbb{C})\}\cong\mathfrak{sl}(2,\mathbb{C}),\qquad \{(M,M):M\in\mathfrak b_0\}\cong\mathfrak b_0 .
$$

**Proposition (the Lie graphs are diagonals).** Every graph of an isomorphism between two isomorphic blocks of the list is conjugate to the diagonal of its block.

*Proof.* The claim is the associative theorem applied block by block. The automorphisms of the blocks are the same in the two structures: $\operatorname{Aut}(\mathfrak b_0)$ is the group computed in that proof, $\operatorname{Aut}(\mathfrak{sl}_2)=PGL_2$ is inner, and the abelian blocks carry the scalings and the exchange of their two lines, all realised by conjugation in $GL_2(\mathbb{C})$. ∎

**Proposition (the ideals).** An ideal of $\mathfrak{gl}(2,\mathbb{C})\oplus\mathfrak{gl}(2,\mathbb{C})$ is a subspace $\mathfrak j\oplus\Lambda$, where $\mathfrak j$ is one of the four ideals of $\mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C})$ and $\Lambda$ is an arbitrary subspace of the centre. The ideals are therefore not finitely many: the lines of the two-dimensional centre form a projective line.

*Proof.* A subspace of the centre is an ideal, the centre being abelian and central. Conversely, let $\mathfrak a$ be an ideal and let $(x,y,\lambda)\in\mathfrak a$ with $x\ne0$. Then $[(N,0,0),(x,y,\lambda)]=([N,x],0,0)$ lies in $\mathfrak a$ for every $N$, and as $N$ runs over $\mathfrak{sl}_2$ the elements $[N,x]$ run over the hyperplane orthogonal to $x$ under the Killing form; bracketing that hyperplane with $\mathfrak{sl}_2$ gives the whole algebra, so $\mathfrak{sl}\oplus0\subset\mathfrak a$. The same argument in the second slot gives $0\oplus\mathfrak{sl}\subset\mathfrak a$ when $y\ne0$. So the semisimple part of $\mathfrak a$ is the sum of the simple summands that it meets, and the remainder lies in the centre. ∎

**Proposition (a fibre product by the trace).** The set

$$
F=\{(A,B)\in\mathfrak{gl}(2,\mathbb{C})\oplus\mathfrak{gl}(2,\mathbb{C}):\ \operatorname{tr}A=\operatorname{tr}B\}
$$

is a Lie subalgebra of dimension seven, and it is neither a product nor a graph.

*Proof.* For closure, $\operatorname{tr}[A,A']=0$ for every pair, so both traces of a bracket vanish and the difference of the two traces stays zero. The dimension is eight minus one. Neither $\Pi_1$ nor $\Pi_2$ lies in $F$, so $F$ is not a product of unital subalgebras. A graph of an isomorphism $\mathfrak s_1\to\mathfrak s_2$ has dimension $\dim\mathfrak s_1=\dim\mathfrak s_2$, while both projections of $F$ are onto $\mathfrak{gl}(2,\mathbb{C})$, of dimension four, and $\dim F=7$; so $F$ is not a graph. ∎

**Remark (a Lie subalgebra is not an associative subalgebra).** The two lattices are different, and one example shows it: the diagonal matrices $\mathbb{C}\operatorname{diag}(1,0)$ are a Lie subalgebra and not an associative one, while $\mathfrak b_0$ is both. The companion article makes the same warning for the real case, and it holds here without change.

## Jordan Subalgebras of the Complexification

**The Jordan product.** The symmetrisation

$$
A\circ B=\tfrac12(AB+BA)
$$

turns $\mathbb{B}^{\oplus 2}_{\mathbb{C}}$ into a complex Jordan algebra, of the same dimension eight, with the same identity. The circle is the product written in the companion article; the corpus writes the Jordan product with a bullet, $\bullet$, and the two glyphs denote the same operation, the circle being used here so that the two articles read alike. The product is computed slot by slot, so the Jordan algebra of the direct sum is the direct sum of the two Jordan algebras:

$$
(\mathbb{B}\oplus\mathbb{B})^{+}=\mathbb{B}^{+}\oplus\mathbb{B}^{+}.
$$

**Lemma (the traceless identity).** For traceless $2\times2$ matrices $U_1,U_2$,

$$
U_1U_2+U_2U_1=\operatorname{tr}(U_1U_2)I,
$$

so the Jordan product of two traceless elements is a scalar.

*Proof.* Both sides are bilinear, so it is enough to check the claim on a basis of $\mathfrak{sl}_2(\mathbb{C})$, for instance $H=\operatorname{diag}(1,-1)$, $S=E_{12}+E_{21}$ and $N=E_{12}$. On that basis $H^2=S^2=I$, $N^2=0$, $HS+SH=0$, $HN+NH=0$, $SN+NS=I$, and the traces are $\operatorname{tr}(H^2)=\operatorname{tr}(S^2)=2$, $\operatorname{tr}(HS)=\operatorname{tr}(HN)=\operatorname{tr}(SN)=\operatorname{tr}(N^2)=0$; all nine cases agree. ∎

**Corollary (the traceless part is Jordan nilpotent).** For $U_1,U_2$ traceless, $U_1\circ U_2\in\mathbb{C}I$, and hence $U_1\circ U_2\circ U_3=0$ for traceless $U_3$. The traceless part is therefore a subspace on which the Jordan product vanishes modulo the scalars, and every subspace of it is closed under the Jordan product up to scalars.

**Remark (the traceless identity is the Euclidean scalar product).** For real coefficients,

$$
\Bigl(\sum_k u_k\vec e_k\Bigr)\Bigl(\sum_k v_k\vec e_k\Bigr)+\Bigl(\sum_k v_k\vec e_k\Bigr)\Bigl(\sum_k u_k\vec e_k\Bigr)=-2\langle u,v\rangle e_t,\qquad \operatorname{tr}(UV)=-2\langle u,v\rangle ,
$$

because distinct units anticommute and each unit squares to $-e_t$. So the lemma $U_1U_2+U_2U_1=\operatorname{tr}(U_1U_2)I$ on the traceless part says, in the biquaternion base, that the traceless part is Euclidean three-space and that the Jordan product of two of its elements is minus their scalar product, times the identity. The proof above uses the basis $i\vec e_z,i\vec e_x,\vec\Pi_{\mathrm{nil},1}$, which is the biquaternion form of $H,S,N$. The form $q$ of the theorem is the complexification of minus that Euclidean form, so a complex line on which $q$ vanishes is a complex line isotropic for the Euclidean form in the complex sense, as $\vec e_x+i\vec e_y$ is: $(\vec e_x+i\vec e_y)^2=-e_t+i\vec e_z-i\vec e_z+e_t=0$, of trace zero. The six Jordan types are the complex subspaces of a three-dimensional space, classified by dimension and by the rank of the restriction of $q$.

**Theorem (the six Jordan types).** The unital Jordan subalgebras of $\mathbb{B}^{+}=M_2(\mathbb{C})^{+}$ are exactly the spaces $\mathbb{C}I\oplus V$ with $V$ a complex subspace of the traceless part $\mathfrak{sl}_2(\mathbb{C})$. Two of them are conjugate if and only if the restrictions of the trace form $q(U_1,U_2)=\operatorname{tr}(U_1U_2)$ to $V$ are equivalent, and the possible types are six.

*Proof.* Closure: for $U_1,U_2\in V$ traceless, $U_1\circ U_2=\tfrac12\operatorname{tr}(U_1U_2)I$ lies in $\mathbb{C}I$ by the lemma, so $\mathbb{C}I\oplus V$ is closed under $\circ$ for every subspace $V$; conversely a unital Jordan subalgebra $J$ is $\mathbb{C}I\oplus V$ with $V=J\cap\mathfrak{sl}_2$, because every element splits as its scalar part plus its traceless part and both parts lie in $J$ when the element does. Conjugacy: an invertible $g$ sends $J$ to $\mathbb{C}I\oplus gVg^{-1}$, and $\operatorname{tr}((gUg^{-1})^2)=\operatorname{tr}(U^2)$ and $\operatorname{tr}(gUg^{-1}\,gU'g^{-1})=\operatorname{tr}(UU')$, so $q$ is preserved; the conjugating group acts on $\mathfrak{sl}_2$ as the orthogonal group of $q$, hence preserves the function $V\mapsto q|_V$. Conversely, two subspaces with equivalent restrictions are carried to each other by an isometry of $q$ on $\mathfrak{sl}_2$, by the extension theorem of Witt, and every isometry is realised by a conjugation: $PGL_2(\mathbb{C})$ acts on $\mathfrak{sl}_2$ as the rotation group of $q$, and the full orthogonal group is obtained from it by adjoining $-1$, which is itself a conjugation in the second slot up to sign. The enumeration is by dimension and by the rank of $q|_V$, and is recorded in the table below. ∎

**The table of the six types.** The rank is that of $q|_V$, and the last column names a witness in the basis $H,S,N$.

| type | $\dim_{\mathbb{C}}J$ | $\dim V$ | rank | algebra | witness $V$ |
|---|---|---|---|---|---|
| scalar | $1$ | $0$ | $0$ | $\mathbb{C}$ | $0$ |
| dual numbers | $2$ | $1$ | $0$ | $\mathbb{C}[\epsilon]$ | $\mathbb{C}N$ |
| split | $2$ | $1$ | $1$ | $\mathbb{C}\oplus\mathbb{C}$ | $\mathbb{C}H$ |
| symmetric | $3$ | $2$ | $2$ | $\operatorname{Sym}_2(\mathbb{C})$ | $\operatorname{span}\{H,S\}$ |
| degenerate | $3$ | $2$ | $1$ | $\mathbb{C}I\oplus\mathbb{C}H\oplus\mathbb{C}N$ | $\operatorname{span}\{H,N\}$ |
| whole | $4$ | $3$ | $3$ | $M_2(\mathbb{C})^{+}$ | $\mathfrak{sl}_2(\mathbb{C})$ |

**Remark (why the count is six).** The rank of a quadratic form on $V$ can be $0$, $1$, $2$ or $3$, and it is bounded by $\dim V$. At $\dim V=0$ there is one type; at $\dim V=1$ the ranks $0$ and $1$ give two; at $\dim V=2$ the ranks cannot be $0$, because a two-dimensional totally isotropic subspace would have to equal its own orthogonal complement in a space of rank three, which is impossible for a nondegenerate form of odd rank; so the ranks $1$ and $2$ give two; at $\dim V=3$ the form is the whole form, of rank $3$. The total is six. Over $\mathbb{C}$ this is the whole classification; over $\mathbb{R}$ each rank is refined by an inertia, and that refinement is what makes the real lists longer.

**Remark (the Jordan types against the real ones).** The companion article lists eight types for the split form and four for the compact one. The complex list is shorter than the real one for the same reason as in the associative layer: over $\mathbb{R}$ the rank of $q|_V$ is not enough, because the inertia of a nondegenerate form is an invariant, while over $\mathbb{C}$ only the rank is. The symmetric type is the complex analogue of $H_2(\mathbb{R})$; the degenerate type is the complex analogue of the degenerate three-dimensional algebra that the companion article records; and there is no complex analogue of the formally real type, because formality is a property of the real slice.

**Remark (the three families in the Jordan layer).** The Goursat theorem holds for Jordan algebras, with the same proof, since the Jordan product in a direct sum is computed slot by slot and $\{xyx\}$-type identities play no role. The families are products, graphs and fibre products as before. Two examples suffice to show that the families differ from the associative ones: the diagonal of the whole algebra $\{(M,M)\}$, which is a graph of the identity; and the fibre product

$$
F=\{(x,y)\in\mathbb{C}[\epsilon]^2:\ x_0=y_0\},
$$

where $x_0$ is the scalar part of $x$, of dimension three over $\mathbb{C}$, which is a Jordan subalgebra because the scalar part of a Jordan product is the product of the scalar parts, and which contains neither $\Pi_1$ nor $\Pi_2$. In the Jordan layer the fibre products are fewer than in the associative layer, because most of the six types are simple: the scalar type, the split type, the symmetric type and the whole algebra have no proper ideals, the dual numbers have the ideal $\mathbb{C}N$, and the degenerate type has the radical $\mathbb{C}N$. Only the last two types admit a proper quotient, and the fibre products over them are the only ones beyond the diagonal and the product families.

**Warning (a Jordan subalgebra is not an associative one).** The symmetric matrices $\operatorname{Sym}_2(\mathbb{C})$ are a Jordan subalgebra of $M_2(\mathbb{C})^{+}$ and not an associative one, since the product of two symmetric matrices need not be symmetric. The converse inclusion holds: every associative subalgebra is a Jordan subalgebra. The two lattices therefore stand in a strict inclusion, and the Jordan lattice is the coarser of the two.

## The Killing Forms and Their Ranks

**The formula.** The Killing form of a matrix Lie algebra is $K(X,Y)=\operatorname{tr}(\operatorname{ad}_X\operatorname{ad}_Y)$, and on $\mathfrak{gl}(2,\mathbb{C})\oplus\mathfrak{gl}(2,\mathbb{C})$ it is the sum of the two Killing forms of the factors, because the adjoint action of a pair acts slot by slot. A direct computation in the four-dimensional factor gives

$$
K_{\mathfrak{gl}_2}(X,Y)=4\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y).
$$

*Proof.* Take the basis $E_{11},E_{12},E_{21},E_{22}$ and compute $\operatorname{ad}_X$ and $\operatorname{ad}_Y$ as $4\times4$ matrices; the trace of their product is the right-hand side. The identity is the one used in the companion article for the real algebra, and it holds over $\mathbb{C}$ without change. ∎

**Consequences.** Two evaluations fix most of the structure: $K(I,I)=8-8=0$ and $K(I,X)=4\operatorname{tr}X-4\operatorname{tr}X=0$, so the scalar line is isotropic and orthogonal to everything. On the traceless part the formula collapses to $K(U_1,U_2)=4\operatorname{tr}(U_1U_2)=4q(U_1,U_2)$, which is the same form as the $q$ of the Jordan layer, rescaled.

**Remark (the inertia is the shadow of the star).** A real slice of a complex algebra is cut out by a conjugate-linear involution, and the star is the one that preserves the form:

$$
K(\tilde X^{*},\tilde Y^{*})=\overline{K(\tilde X,\tilde Y)} .
$$

On the anti-fixed space $\mathbb{B}_{\Phi}=\mathfrak u(2)$ the form vanishes on the central direction $i e_t$ and equals $-8$ on each of $\vec e_x,\vec e_y,\vec e_z$; on the fixed space $\mathbb{B}_{\Psi}$ it vanishes on $e_t$ and equals $+8$ on each of $i\vec e_x,i\vec e_y,i\vec e_z$. The two real slices of the scalar-free part therefore take opposite counts: $\mathfrak{su}(2)$ takes three negative values and the inertia $(0,3)$, and $\operatorname{span}_{\mathbb{R}}\{i\vec e_x,\vec e_y,i\vec e_z\}$ takes two positive and one negative and the inertia $(2,1)$. The complex algebra sees neither count, and the reason is the biquaternion reason: the star is conjugate-linear, so it is not an operation of the complex structure, and the signs it produces are invisible over $\mathbb{C}$.

**The table of the ambient restrictions.** The radical and the rank are those of the restriction of $K_{\mathfrak{gl}\oplus\mathfrak{gl}}$ to the subalgebra named. The last column compares the intrinsic Killing form, that of the subalgebra read as an abstract Lie algebra, with the ambient restriction: "itself" means that the two coincide, and a numerical entry gives the intrinsic value where it differs.

| algebra | $\dim_{\mathbb{C}}$ | radical of the restriction | rank | intrinsic form |
|---|---|---|---|---|
| $\mathfrak{gl}(2,\mathbb{C})$ | $4$ | $\mathbb{C}I$ | $3$ | itself |
| $\mathfrak{sl}(2,\mathbb{C})$ | $3$ | $0$ | $3$ | itself |
| $\mathfrak b_0$ | $3$ | $\mathbb{C}I\oplus\mathbb{C}N$ | $1$ | $K(H,H)=4$, not $8$ |
| abelian plane $\mathbb{C}I\oplus\mathbb{C}H$ | $2$ | $\mathbb{C}I$ | $1$ | zero |
| $\mathfrak{gl}\oplus\mathfrak{gl}$ | $8$ | $\mathbb{C}\Pi_1\oplus\mathbb{C}\Pi_2$ | $6$ | itself |
| $\mathfrak{sl}\oplus\mathfrak{sl}$ | $6$ | $0$ | $6$ | itself |

**Remark (the ambient form is not the intrinsic one on the Borel).** The two forms agree on $\mathfrak{gl}_2$ and on $\mathfrak{sl}_2$, because $\mathfrak{sl}_2$ is an ideal of $\mathfrak{gl}_2$ and the adjoint action on the extra scalar direction is zero, but they differ on the Borel by a factor two: the ambient adjoint action of $H$ has the eigenvalues $0,0,2,-2$ on $\mathfrak{gl}_2$ and only $0,0,2$ on $\mathfrak b_0$, so $K(H,H)$ is $8$ in the first case and $4$ in the second. The ranks and radicals agree, and every statement above uses the ambient form.

**Warning (the inertia is not a complex invariant).** Over $\mathbb{R}$ the Killing form is a real symmetric bilinear form, and a real symmetric form is classified by its inertia. Over $\mathbb{C}$ a symmetric bilinear form is classified by its **rank** alone: every nondegenerate symmetric form over $\mathbb{C}$ is equivalent to the standard one, because every nonzero complex number is a square. So the table above records ranks and radicals, and the inertias $(2,1)$ and $(0,3)$ of the companion article are the inertias of the **real forms** of these algebras, not of the complex algebras. The same complex algebra can carry both inertias: $\mathfrak{sl}(2,\mathbb{C})$ has rank three as a complex form, and its two real forms realize the inertias $(2,1)$ and $(0,3)$, which is the cleanest illustration of the rule.

**Remark (the Killing form as a test of semisimplicity).** The criterion of Cartan holds over $\mathbb{C}$: a Lie algebra is semisimple if and only if its Killing form is nondegenerate. On the complexification the form is degenerate, with radical the two-dimensional centre, and the derived algebra $\mathfrak{sl}\oplus\mathfrak{sl}$ is the semisimple part. The decomposition

$$
\mathfrak{gl}\oplus\mathfrak{gl}=\mathfrak{sl}\oplus\mathfrak{sl}\oplus\mathbb{C}\Pi_1\oplus\mathbb{C}\Pi_2
$$

is the decomposition into the semisimple part and the radical, and it is read off the Killing form as its nondegenerate part and its radical.

## The Real-Form Lattice Inside the Complexification

**The classification of real structures.** A real structure on $\mathbb{B}^{\oplus 2}_{\mathbb{C}}=A\oplus A$, with $A=\mathbb{B}=M_2(\mathbb{C})$, is a conjugate-linear multiplicative involution $\theta$. In this section the coefficient conjugation is written $\sigma_1$, to keep the glyph of the real-structure classification; it is the map $\bar{}$ of the ninth section. It either preserves the two simple summands or exchanges them, and the two cases give the following list.

**Theorem (the real structures).** Let $A=M_2(\mathbb{C})$.

- If $\theta$ preserves the summands, then $\theta=\theta_1\times\theta_2$ with each $\theta_i$ a real structure of $A$, and there are four such maps.
- If $\theta$ exchanges the summands, then $\theta(x,y)=(\digamma_{\mathrm{map}}(y),\digamma_{\mathrm{map}}^{-1}(x))$ for a conjugate-linear automorphism $\digamma_{\mathrm{map}}$ of $A$; the fixed algebra is $\{(x,\digamma_{\mathrm{map}}^{-1}x):x\in A\}\cong A_{\mathbb{R}}$, and all such $\theta$ are conjugate, so they give one class.

Hence there are five real structures, falling into four classes under conjugation by $\operatorname{Aut}(A\oplus A)$, and four real algebras up to isomorphism: $\mathbb{H}\oplus\mathbb{H}$, $\mathbb{H}\oplus M_2(\mathbb{R})$, $M_2(\mathbb{R})\oplus M_2(\mathbb{R})$ and $M_2(\mathbb{C})_{\mathbb{R}}$. The two mixed structures are exchanged by the swap, and that is why five structures give four classes.

*Proof.* The summands are the two simple ideals, and a conjugate-linear automorphism permutes the two-element set of them, so it preserves or exchanges. In the preserving case each component is a conjugate-linear multiplicative involution of $A$, and by the companion article there are exactly two of those, the coefficient conjugation $\sigma_1$ and its inner twist $\sigma_{\mathrm{split}}$. In the exchanging case write $\theta(x,y)=(\digamma_{\mathrm{map}}(y),Ξ_{\mathrm{wfn}}(x))$; multiplicativity forces $\digamma_{\mathrm{map}}$ and $Ξ_{\mathrm{wfn}}$ to be multiplicative, and $\theta^2=1$ forces $Ξ_{\mathrm{wfn}}=\digamma_{\mathrm{map}}^{-1}$. A conjugate-linear automorphism of $A$ is $\digamma_{\mathrm{map}}=\operatorname{Ad}_g\circ\sigma_1$ for some $g\in GL_2(\mathbb{C})$, by the Skolem–Noether theorem applied to the automorphism $\digamma_{\mathrm{map}}\circ\sigma_1^{-1}$, which is $\mathbb{C}$-linear. Two such structures are conjugate: conjugation by $(1,u)$ on $A\oplus A$ replaces $\operatorname{Ad}_g$ by $\operatorname{Ad}_{g\bar u}$, and $g\bar u$ runs over $GL_2(\mathbb{C})$ as $u$ does. The fixed algebra of the exchanging case is read off from $\theta(x,y)=(x,y)$, which is $y=\digamma_{\mathrm{map}}^{-1}(x)$ and $x=\digamma_{\mathrm{map}}(y)$, one condition, of real dimension eight. The four preserving fixed algebras are the products of the two fixed algebras of $A$, that is $\mathbb{B}_H=\mathbb{H}$ and $M_2(\mathbb{R})$, in the four orders, and the two mixed orders give the same algebra in two inequivalent positions. ∎

**Remark (the swap exchanges the two mixed structures).** The swap $s(u,v)=(v,u)$ is a $\mathbb{C}$-algebra automorphism of $A\oplus A$, and

$$
s\circ(\sigma_1\times\sigma_{\mathrm{split}})\circ s^{-1}=\sigma_{\mathrm{split}}\times\sigma_1,
$$

so the two mixed structures are conjugate and give isomorphic algebras. The distinction between them is the position of the two summands, not the isomorphism class of the fixed algebra, and it is a distinction that only the pair $(A\oplus A,\theta)$ records.

**The table of the real forms.** The first four rows are the pair forms, the fifth the slanted form. The two mixed rows are distinct structures and isomorphic algebras, exchanged by the swap.

| real structure | fixed algebra | $\dim_{\mathbb{R}}$ | type |
|---|---|---|---|
| $\sigma_1\times\sigma_1$ | $\mathbb{H}\oplus\mathbb{H}$ | $8$ | pair, division $\oplus$ division |
| $\sigma_1\times\sigma_{\mathrm{split}}$ | $\mathbb{H}\oplus M_2(\mathbb{R})$ | $8$ | pair, mixed |
| $\sigma_{\mathrm{split}}\times\sigma_1$ | $M_2(\mathbb{R})\oplus\mathbb{H}$ | $8$ | pair, mixed, other order |
| $\sigma_{\mathrm{split}}\times\sigma_{\mathrm{split}}$ | $M_2(\mathbb{R})\oplus M_2(\mathbb{R})$ | $8$ | pair, matrices $\oplus$ matrices |
| $\tau$, and its twists | $\{(x,\digamma_{\mathrm{map}}^{-1}x)\}\cong\mathbb{B}_{\mathbb{R}}$ | $8$ | slanted |

**Remark (a commonly quoted list of four, corrected).** A commonly quoted list names four real forms, $\mathbb{H}\oplus\mathbb{H}$, $M_2(\mathbb{R})\oplus M_2(\mathbb{R})$, $M_2(\mathbb{C})$ and $\mathbb{B}\oplus\bar{\mathbb{B}}$. The list omits the mixed pair $\mathbb{H}\oplus M_2(\mathbb{R})$ and counts the slanted form twice, since $\mathbb{B}\oplus\bar{\mathbb{B}}=\{(u,\bar u)\}$ is the slanted form already listed as $M_2(\mathbb{C})$. The correct count is five structures, four conjugacy classes and four algebras, and the mixed pair is not exotic: it is the complexification of the two real forms taken separately, and it appears whenever the two summands are used for different purposes.

**Theorem (the diagonal correspondence).** For either real structure $\theta$ of $\mathbb{B}$, the map $x\mapsto\Phi(x\otimes1)=(x,\bar x)$ is an isomorphism of the real form $\mathbb{B}^{\theta}$ onto a copy of itself inside the pair form $\mathbb{B}^{\theta}\oplus\mathbb{B}^{\theta}$, and that copy lies inside the slanted form, which contains the two copies for the two choices of $\theta$.

*Proof.* Let $x\in\mathbb{B}^{\theta}$. Then $\theta(\bar x)=\overline{\theta(x)}=\bar x$, because the two real structures of $\mathbb{B}$ commute: $\sigma_{\mathrm{split}}=\operatorname{Ad}_{\vec e_y}\circ\sigma_1$ with $\sigma_1(\vec e_y)=\vec e_y$, and an inner automorphism by an element fixed by $\sigma_1$ commutes with $\sigma_1$. So $(x,\bar x)$ is fixed by $\theta\times\theta$. It is fixed by $\tau$ by construction. The map $x\mapsto(x,\bar x)$ is the restriction of the algebra isomorphism $\Phi$ and is therefore injective, and its image has real dimension four in each case. ∎

**Remark (the correspondence is diagonal, not bijective).** The two real forms of $\mathbb{B}$ give two of the five real structures of the complexification, and they give them twice: once inside their own pair form and once inside the slanted form, which contains both. The mixed pair form is not the image of anything in $\mathbb{B}$: it is the complexification of the two real forms used separately, and it has no counterpart in the classification of the real structures of $\mathbb{B}$. The direction of the correspondence is therefore one-way: every real form of $\mathbb{B}$ gives a real form of the complexification, and not every real form of the complexification comes from one.

**Remark (the algebras of the four types).** The four real algebras are pairwise non-isomorphic, and two invariants separate them. The algebra $M_2(\mathbb{C})_{\mathbb{R}}$ is simple over $\mathbb{R}$, while the other three are sums of two simple ideals; among the sums, the number of summands isomorphic to $\mathbb{H}$ is $0$, $1$ or $2$, and $\mathbb{H}$ is the only division algebra of the four. The count of idempotents shows the same separation from a different side: $\mathbb{H}\oplus\mathbb{H}$ has the four idempotents $0$, $\Pi_1$, $\Pi_2$ and the identity and no other, $\mathbb{H}\oplus M_2(\mathbb{R})$ has a circle of them in its second slot, and the two last algebras have a surface of them.

## The Involutions and the Six Remarkable Subspaces

**The involutions.** Four maps act on $\mathbb{B}=M_2(\mathbb{C})$ and extend to the complexification by acting on each slot.

| involution | action on the base | fixed subspace | $\dim_{\mathbb{R}}$ |
|---|---|---|---|
| coefficient conjugation $\bar{}$ | $e_t\mapsto e_t$, $\vec e_k\mapsto\vec e_k$ | $\mathbb{B}_H$ | $4$ |
| quaternion conjugation $\natural$ | $e_t\mapsto e_t$, $\vec e_k\mapsto-\vec e_k$ | $\mathbb{B}_C$ | $2$ |
| the star ${}^{*}=\natural\circ\bar{}$ | $e_t\mapsto e_t$, $\vec e_x\mapsto-\vec e_x$, $\vec e_y\mapsto-\vec e_y$, $\vec e_z\mapsto-\vec e_z$ | $\mathbb{B}_\Psi$ | $4$ |
| the transpose ${}^{T}$ | — | the symmetric matrices | $6$ |

The action on the base, together with the linearity or the conjugate-linearity, determines each of the first three maps; the transpose needs its action on the whole algebra. In the order of the table, the first is a conjugate-linear automorphism, the second and the fourth are $\mathbb{C}$-linear anti-automorphisms, and the third is a conjugate-linear anti-automorphism. In the order of the table, the fixed subspaces of the first three are the quaternion subspace $\mathbb{B}_H$, the centre $\mathbb{B}_C$ and the star-invariant $\mathbb{B}_\Psi$, and their anti-fixed subspaces are the anti-quaternion subspace $\mathbb{B}_{iH}$, of dimension four, the vector subspace $\mathbb{B}_V$, of dimension six, and the star-anti-invariant $\mathbb{B}_\Phi$, of dimension four. These six are the remarkable subspaces of the corpus:

| subspace | definition | $\dim_{\mathbb{R}}$ | closed under |
|---|---|---|---|
| $\mathbb{B}_C$ | fixed of $\natural$ | $2$ | products, Jordan, bracket |
| $\mathbb{B}_V$ | anti-fixed of $\natural$ | $6$ | bracket |
| $\mathbb{B}_H$ | fixed of $\bar{}$ | $4$ | products, Jordan, bracket |
| $\mathbb{B}_{iH}$ | anti-fixed of $\bar{}$ | $4$ | none |
| $\mathbb{B}_\Psi$ | fixed of ${}^{*}$ | $4$ | Jordan |
| $\mathbb{B}_\Phi$ | anti-fixed of ${}^{*}$ | $4$ | bracket |

Read with the layers, the table says that the two halves of the ambient algebra are the two halves of the two layers: $\mathbb{B}_{\Phi}$ is $\mathfrak u(2)$, the Lie algebra of the compact form, and $\mathbb{B}_{\Psi}$ is the Hermitian space on which the Jordan product closes. The row for $\mathbb{B}_V$ is the sum $\mathfrak{su}(2)\oplus i\,\mathfrak{su}(2)$ of the anti-Hermitian and Hermitian scalar-free parts, and together with $\mathbb{B}_{\Phi}$ it is one of the two rows closed under the bracket and under nothing else.

**The subspaces inside the complexification.** Each of the six sits in each slot, so the complexification carries the doubled subspaces $B_j\oplus B_j$, of complex dimension equal to the real dimension of $B_j$, and the slanted copies $\{(x,\bar x):x\in B_j\}$, of the same real dimension. The doubled copies are the ones that enter the lattice, and the slanted ones are the ones that descend.

**The intersection table.** The intersections of the six with the quaternion subspace, which is the compact real form, and with the anti-quaternion subspace, are

| $B_j$ | $\dim B_j$ | $\dim(B_j\cap\mathbb{B}_H)$ | $\dim(B_j\cap\mathbb{B}_{iH})$ | sum |
|---|---|---|---|---|
| $\mathbb{B}_C$ | $2$ | $1$ | $1$ | $2$ |
| $\mathbb{B}_V$ | $6$ | $3$ | $3$ | $6$ |
| $\mathbb{B}_H$ | $4$ | $4$ | $0$ | $4$ |
| $\mathbb{B}_{iH}$ | $4$ | $0$ | $4$ | $4$ |
| $\mathbb{B}_\Psi$ | $4$ | $1$ | $3$ | $4$ |
| $\mathbb{B}_\Phi$ | $4$ | $3$ | $1$ | $4$ |

The last column is the sum of the two intersections and equals the dimension, so each subspace is the direct sum of its intersections with the real form and with its anti-fixed part. That is the content of the fact that $\mathbb{B}_H$ is a real form: conjugation by $\bar{}$ splits every subspace into its fixed and anti-fixed parts.

**Remark (the identity with the compact column of the companion article).** The fourth column is exactly the compact column of the companion article, $1,3,4,0,1,3$. The reason is that the compact real form of $\mathbb{B}$ is $\mathbb{B}_H$, so the two tables record the same intersections. The complex article adds what the real one cannot see: the same numbers arise in each slot of the complexification, and the doubled subspaces $B_j\oplus B_j$ are complex subspaces of complex dimension $\dim_{\mathbb{R}}B_j$, while the six subspaces themselves are not complex subspaces of $\mathbb{B}$ but real ones.

**Remark (the star and the two real structures).** The star is the composition $\natural\circ\bar{}$ of the quaternion conjugation and the coefficient conjugation. The two real structures of $\mathbb{B}$ are the coefficient conjugation $\bar{}$ and its inner twist $\sigma_{\mathrm{split}}=\operatorname{Ad}_{\vec e_y}\circ\bar{}$, so the star is not a real structure but the product of two of them with a twist in between. Its fixed space $\mathbb{B}_\Psi$ is the fourth of the six subspaces and the one that is not a real form, because the star is an anti-automorphism and its fixed space is stable under the star and not under the product of two of its elements.

## The Lie Groups Attached to the Lie Subalgebras

**The correspondence, cited once.** The general theory is [The Lie Correspondence and the Adjoint Representation](the-lie-correspondence-and-the-adjoint-representation.html). Three statements are used below, and no others. First, every finite-dimensional complex Lie algebra has a simply connected Lie group $\widetilde G$, unique up to isomorphism. Second, every connected Lie group $G$ with that algebra is $\widetilde G/\Gamma$ for a discrete central subgroup $\Gamma\subset Z(\widetilde G)$, and conversely. Third, $\pi_1(G)\cong\Gamma$.

**The centres of the covers.** The covers that occur are $\mathbb{C}^3$, $\mathbb{C}^2$, $SL(2,\mathbb{C})$, $SL(2,\mathbb{C})\times\mathbb{C}$ and their products, and their centres are computed as follows.

**Lemma.** $Z(SL(2,\mathbb{C}))=\{\pm I\}$, of order two; $Z(\mathbb{C}^n)=\mathbb{C}^n$; $Z(SL(2,\mathbb{C})\times\mathbb{C})=(\mathbb{Z}/2)\times\mathbb{C}$; $Z(A\times A)=Z(A)\times Z(A)$ for a direct product.

*Proof.* The centre of $SL(2,\mathbb{C})$ is the set of scalar matrices $\lambda I$ of determinant one, that is $\lambda^2=1$. The centre of $\mathbb{C}^n$ is the whole group, $\mathbb{C}^n$ being abelian. The centre of a direct product is the product of the centres. ∎

**Lemma ($\mathfrak b_0$).** The group $B^+$ of invertible upper triangular matrices is $\mathbb{C}^\times\times\mathbb{C}^\times\times\mathbb{C}$ as a manifold, and its universal cover is $\widetilde{B^+}=\mathbb{C}^3$ with the law

$$
(x,y,z)(x',y',z')=(x+x',\,y+y',\,e^xz'+z),
$$

the covering map $\pi(x,y,z)=(e^x,\,e^y,\,e^xz)$, and the centre $Z(\widetilde{B^+})=\{(2\pi i k,y_0,0)\}\cong\mathbb{Z}\times\mathbb{C}$.

*Proof.* The product of $\begin{pmatrix}a&b\\0&d\end{pmatrix}$ and $\begin{pmatrix}a'&b'\\0&d'\end{pmatrix}$ is $\begin{pmatrix}aa'&ab'+bd'\\0&dd'\end{pmatrix}$; writing $a=e^x$, $d=e^y$, $b=e^xz$ turns it into the law of the display, which is associative, has the identity $(0,0,0)$, and has the inverse $(-x,-y,-e^{-x}z)$. The map $\pi$ is a homomorphism, is onto, and its kernel is $x\in2\pi i\mathbb{Z}$, $y\in2\pi i\mathbb{Z}$, $z=0$, a lattice isomorphic to $\mathbb{Z}^2$; the source is $\mathbb{C}^3$, which is simply connected, so $\pi$ is the universal covering. For the centre, compare the two products

$$
(X,Y,Z)(x,y,z)=(X+x,\,Y+y,\,e^Xz+Z),\qquad (x,y,z)(X,Y,Z)=(x+X,\,y+Y,\,e^xZ+z)
$$

The first two slots agree always. In the third slot, put $z=0$: the agreement reads $Z=e^xZ$ for all $x$, which forces $Z=0$; with $Z=0$ the third slot reads $e^Xz=z$ for all $z$, which forces $e^X=1$. So $(X,Y,Z)$ is central exactly when $X\in2\pi i\mathbb{Z}$ and $Z=0$, and $Y$ is free. ∎

**Remark (the centre is not discrete).** The centre $2\pi i\mathbb{Z}\times\mathbb{C}$ has a discrete part $2\pi i\mathbb{Z}$ and a continuous part $\mathbb{C}$, and only the discrete subgroups of the whole give quotients. These are not all of coordinate form. If $\Delta\subset2\pi i\mathbb{Z}\times\mathbb{C}$ is discrete, then $\Delta\cap(\{0\}\times\mathbb{C})=\{0\}\times\Lambda$ for a lattice $\Lambda$ of rank zero, one or two, and the image of $\Delta$ in $\mathbb{C}/\Lambda$ is discrete, so $\Delta$ sits in an extension

$$
0\longrightarrow\Lambda\longrightarrow\Delta\longrightarrow\Gamma\longrightarrow0
$$

with $\Gamma$ a discrete subgroup of the group $\mathbb{C}/\Lambda$, which is $\mathbb{C}$, $\mathbb{C}^\times$ or a torus according to the rank of $\Lambda$. The coordinate subgroups $2\pi i\mathbb{Z}\times\Lambda$ are the ones for which the extension splits at the class of $2\pi i$. The slanted subgroups are not of that form: for $\lambda\notin\Lambda$ the group generated by $(2\pi i,\lambda)$ is infinite cyclic and discrete, since the points $(2\pi i n,n\lambda)$ are separated, and it contains no element with zero second coordinate. The algebra $\mathfrak b_0$ therefore has infinitely many connected groups, in contrast with the semisimple algebras of the table below.

**The master table.** The rows give the Lie algebra, its complex dimension, the simply connected cover, the centre, the discrete central subgroups that occur, and the resulting quotients with their fundamental groups.

| Lie algebra | $\dim_{\mathbb{C}}$ | cover | centre | discrete $\Gamma$ | quotients and $\pi_1$ |
|---|---|---|---|---|---|
| $\mathfrak{sl}(2,\mathbb{C})$ | $3$ | $SL(2,\mathbb{C})$ | $\mathbb{Z}/2$ | $0$, $\mathbb{Z}/2$ | $SL(2,\mathbb{C})$, $\pi_1=0$; $PSL(2,\mathbb{C})$, $\pi_1=\mathbb{Z}/2$ |
| $\mathfrak{gl}(2,\mathbb{C})$ | $4$ | $SL(2,\mathbb{C})\times\mathbb{C}$ | $(\mathbb{Z}/2)\times\mathbb{C}$ | lattices in $\mathbb{C}$; $\langle(-I,\pi i)\rangle$ | $GL(2,\mathbb{C})$, $\pi_1=\mathbb{Z}$; $SL(2,\mathbb{C})\times\mathbb{C}^\times$; $PGL(2,\mathbb{C})$ |
| $\mathfrak{sl}\oplus\mathfrak{sl}$ | $6$ | $SL\times SL$ | $(\mathbb{Z}/2)^2$ | the five subgroups | five quotients, $\pi_1$ from $0$ to $(\mathbb{Z}/2)^2$ |
| diagonal $\mathfrak{sl}_2$ | $3$ | $SL(2,\mathbb{C})$ | $\mathbb{Z}/2$ | $0$, $\mathbb{Z}/2$ | $SL(2,\mathbb{C})$; $PSL(2,\mathbb{C})$ |
| $\mathfrak{sl}_2\oplus0$ | $3$ | $SL(2,\mathbb{C})$ | $\mathbb{Z}/2$ | $0$, $\mathbb{Z}/2$ | the same two |
| $\mathfrak h\oplus\mathfrak h$, $\mathfrak h$ diagonal | $2$ | $\mathbb{C}^2$ | $\mathbb{C}^2$ | lattices of rank $0$ to $4$ | $\mathbb{C}^2/\Lambda$, $\pi_1=\Lambda$ |
| $\mathfrak b_0$ | $3$ | $\mathbb{C}^3$ | $2\pi i\mathbb{Z}\times\mathbb{C}$ | the lattices $\Delta$ of that centre | $B^+$, $\pi_1=\mathbb{Z}^2$; $\mathbb{C}^3/\Delta$, $\pi_1=\Delta$ of rank $0$ to $3$ |
| $\mathfrak b_0\oplus\mathfrak b_0$ | $6$ | $\mathbb{C}^6$ | $(2\pi i\mathbb{Z}\times\mathbb{C})^2$ | products $\Delta_1\times\Delta_2$ | $B^+\times B^+$, $\pi_1=\mathbb{Z}^4$; quotients with $\pi_1$ of rank $0$ to $6$ |

**The entry for $\mathfrak{gl}(2,\mathbb{C})$, worked.** The map

$$
SL(2,\mathbb{C})\times\mathbb{C}\longrightarrow GL(2,\mathbb{C}),\qquad (A,t)\longmapsto e^tA
$$

is a surjective homomorphism onto $GL(2,\mathbb{C})$: every invertible matrix is a nonzero scalar times a matrix of determinant one, and every nonzero scalar is an exponential. Its kernel is the set of pairs with $e^tA=I$, that is $A=e^{-t}I$ and $\det A=1$, which forces $e^{2t}=1$, hence $t\in \pi i\mathbb{Z}$ and $A=(-1)^{t/(\pi i)}I\in\{\pm I\}$. The kernel is $\langle(-I,\pi i)\rangle\cong\mathbb{Z}$, discrete and central, so $GL(2,\mathbb{C})$ is the quotient of the simply connected group by a copy of $\mathbb{Z}$, and $\pi_1(GL(2,\mathbb{C}))\cong\mathbb{Z}$. The centre of $GL(2,\mathbb{C})$ is $\mathbb{C}^\times I\cong\mathbb{C}^\times$, connected, and the quotient by it is $PGL(2,\mathbb{C})$, whose same Lie algebra has the same cover.

**The entry for $\mathfrak b_0$, worked.** By the lemma the simply connected group is $\mathbb{C}^3$, the centre is $\mathbb{Z}\times\mathbb{C}$, the quotient by the lattice $(2\pi i\mathbb{Z})^2$ is $B^+$, of fundamental group $\mathbb{Z}^2$, and the quotient by a lattice $\Delta\cong\mathbb{Z}^r$ is a group with the same Lie algebra, fundamental group $\Delta$, and the homotopy type of the $r$-torus, the cover $\mathbb{C}^3$ being contractible. The point of the entry is that a solvable algebra has a continuous centre in its cover and therefore an infinite lattice of connected groups, while a semisimple algebra has a finite one.

**Warning (the centre of the cover is not the centre of the group).** The centre of $\widetilde{B^+}$ is $\mathbb{Z}\times\mathbb{C}$ and the centre of $B^+$ is $\{(1,c,0)\}\cong\mathbb{C}^\times$, connected. The quotient has lost the discrete part and kept the continuous one, and that is the general pattern: a discrete central subgroup of the cover is killed by the quotient and contributes to the fundamental group, not to the centre, while the image of the centre of the cover lies in the centre of the quotient. Confusing $Z(\widetilde G)$ with $Z(G)$ is one of the warning points of this article.

## The Comparison with the Real Case

**The two articles in one table.** The rows compare the object of this article with the object of the companion article.

| item | the two real forms | the complexification |
|---|---|---|
| the algebra | $M_2(\mathbb{R})$ and $\mathbb{H}$ | $M_2(\mathbb{C})\oplus M_2(\mathbb{C})$ |
| dimension | $4$ over $\mathbb{R}$ each | $8$ over $\mathbb{C}$, $16$ over $\mathbb{R}$ |
| centre | $\mathbb{R}e_t$ | $\mathbb{C}\Pi_1\oplus\mathbb{C}\Pi_2$ |
| simplicity | simple, both | two simple ideals |
| idempotents | the compact form has none beyond $0$ and $1$ | four central ones |
| associative unital types | six and four | five per factor, three families in the sum |
| continuous families | three | none per factor |
| Lie types of a line | five projective types | four projective types |
| Jordan types | eight and four | six |
| Killing form | inertias $(2,1)$ and $(0,3)$ | rank three per factor, radical two |
| real forms of the object | two | five real structures, four real algebras |
| subalgebra lattice | one lattice each | not the product of the two lattices |
| centres of the covers | $\mathbb{Z}$ for $\widetilde{SL}(2,\mathbb{R})$, $\mathbb{Z}/2$ for $SU(2)$ | $\mathbb{Z}/2$ for $\mathfrak{sl}_2$, $\mathbb{Z}\times\mathbb{C}$ for $\mathfrak b_0$ |
| fundamental groups of the quotients | $\mathbb{Z}$ for $SL(2,\mathbb{R})$, $\mathbb{Z}/2$ for $SO(3)$ | $\mathbb{Z}$ for $GL(2,\mathbb{C})$, $\mathbb{Z}^2$ for $B^+$ |

**The three differences and their sources.** Read down the table, three entries carry the information. The complexification is not simple, so its lattice has the three families. Its centre is two-dimensional, so its ideals are not finitely many and its real structures form four classes. Its factors are closed under square roots, so the continuous families of the real case collapse to single classes. The first two have one source: without the splitting into two ideals there would be no pair of summands to exchange, no graphs and no fibre products, and no second direction in the centre. The third is independent of the product and comes from the ground field.

**What the real case sees that the complex case does not.** The real article can speak of the inertia of the Killing form, of formally real Jordan algebras, of the compact and the split real form, and of the three families of complex structures as genuine parameters. The complex article can speak of none of these, and it gains instead the families of subalgebras of a direct sum. The two articles are therefore not translations of one another. Each sees a part of the structure that the other cannot express.

## What the Complex Form Does and Does Not Determine

**What it determines.** The complex algebra $M_2(\mathbb{C})\oplus M_2(\mathbb{C})$ determines the following, and the computations above show each one.

- The two simple ideals, as the minimal two-sided ideals, and hence the two central idempotents $\Pi_1$ and $\Pi_2$, as their identities.
- The centre, as the centre, and its dimension.
- The subalgebra lattice of each factor, in the three layers, up to conjugacy.
- The three families of subalgebras of the sum, as a description: every subalgebra is a product, a graph or a fibre product.
- The ranks of the Killing form on each block, and the radical of the ambient form.
- The Lie algebra of every subalgebra, and hence its simply connected cover.

**What it does not determine.** The following are extra data, and each is invisible to the complex algebra.

- **The real form.** The complex algebra has a compact real form and a split one, and it does not say which is meant. $\mathfrak{sl}(2,\mathbb{C})$ is the complexification of both $\mathfrak{su}(2)$ and $\mathfrak{sl}(2,\mathbb{R})$, and the two real algebras have different groups, different representation theory and different geometry. The same holds for the algebra of this article: $\mathbb{H}\oplus\mathbb{H}$ and $M_2(\mathbb{R})\oplus M_2(\mathbb{R})$ are both real forms, and the complex algebra does not choose.
- **The inertia.** Over $\mathbb{C}$ a symmetric bilinear form has a rank and no inertia, so the Killing form of the complexification records the rank and loses the information that separates the two real forms. The star of the ambient algebra is what would supply the signs, $K(\tilde X^{*},\tilde Y^{*})=\overline{K(\tilde X,\tilde Y)}$, and the star is conjugate-linear, so the complex structure cannot see them.
- **The position of the six subspaces.** The intersection table of the ninth section requires a real structure to be stated: it is an intersection with $\mathbb{B}_H$, which is the fixed set of one of the two. With the split real structure in place of the compact one the same computation gives the numbers $1,3,2,2,3,1$ of the companion article. The complex algebra alone does not decide which table applies.
- **The topology of the group.** The Lie algebra determines the cover, and the group is the cover modulo a discrete central subgroup. The complex algebra does not say which subgroup.
- **Unitary representation theory.** The complex algebra $\mathfrak{sl}(2,\mathbb{C})$ has the same finite-dimensional representations for both real forms, but the unitary representations of $SU(2)$ are all finite-dimensional while those of $\widetilde{SL}(2,\mathbb{R})$ are not, and the unitary structure lives on the real form.

**Warning (what the complex form does not determine).** The complex algebra fixes the factors, their lattices, the three families of subalgebras of the sum, and the ranks of the Killing form. It does not fix the real form, the inertia, the position of the real subspaces, the discrete central subgroup that gives the group, or the unitary representation theory. Those are the extra data, and they are supplied by the real structure, not by the complex one.

## Hand-off

**To the real article.** The companion article [Classification of the Real Structures of the Biquaternion Algebra, including Lie Algebras and Lie Groups](classification-of-the-real-structures-of-the-biquaternion-algebra.html) develops the two real forms at the same depth, and every statement there about the split and the compact form is a statement about a real slice of the object of this article. The reader who wants the inertias, the real Jordan types and the real projective families should read it with this one open beside it: the columns of its intersection table are the fourth column of the table of the ninth section here.

**To the structure article.** The article [Classification of the Structures of the Biquaternion Algebra](classification-of-the-structures-of-the-biquaternion-algebra.html) proves that there are exactly two real structures on $\mathbb{B}$ and one complex form, and that the complexification is the direct sum. This article takes the last statement as its starting point and develops what follows from it.

**To the operator series.** The operator articles treat left and right multiplication on $\mathbb{B}$ and the double centralizer theorem, $\operatorname{End}(\mathbb{B})=M_4(\mathbb{C})$. In the complexification each operator doubles: left multiplication by $(M,N)$ is the pair of left multiplications, the two-sided operators form the direct sum of the two cones, and the double centralizer statement holds slot by slot. The complexification is therefore the natural place where the two copies of the operator algebra are seen at once, and the operator articles carry the computation.

**To the Lie correspondence.** The group theory of the tenth section is quoted from [The Lie Correspondence and the Adjoint Representation](the-lie-correspondence-and-the-adjoint-representation.html), which proves the three statements used: the existence and uniqueness of the simply connected cover, the classification of the connected groups with a given algebra as quotients by discrete central subgroups, and the identification $\pi_1(G)\cong\Gamma$.

## Summary

**The complex form and the complexification.** The complex form of $\mathbb{B}_{\mathbb{R}}$ is $\mathbb{B}=M_2(\mathbb{C})$, of complex dimension four; the complexification is $\mathbb{B}_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C}=M_2(\mathbb{C})\oplus M_2(\mathbb{C})$, of complex dimension eight, identified with the direct sum by $\Phi(x\otimes1)=(x,\bar x)$ and $\Phi(x\otimes i)=(ix,i\bar x)$. The image of the real algebra itself is the slanted copy $\{(x,\bar x)\}$ and not a summand. The complex form is simple; the complexification has the four ideals $0$, $\Pi_1$, $\Pi_2$ and the whole, and the two middle ones are simple.

**The two central idempotents.** $\Pi_1=(I,0)$ and $\Pi_2=(0,I)$ are idempotent, orthogonal, central, sum to the identity, and are the only nonzero central idempotents. The Peirce decomposition relative to them has vanishing off-diagonal components, because the pair is central, so the algebra splits into the two blocks and nothing more; the non-central Peirce cut of each factor is the four-line decomposition of the companion article, and the contrast between the two cuts is the source of everything that follows.

**The associative layer.** Goursat's theorem for algebras states that a unital subalgebra $S$ of $A_1\oplus A_2$ is the fibre product of its two projections over isomorphic quotients, and the corollary gives the three families, product, graph and fibre product. The blocks of one factor are five up to conjugacy, $\mathbb{C}I$, $\mathbb{C}\oplus\mathbb{C}$, $\mathbb{C}[\epsilon]$, $\mathfrak b_0$ and $M_2(\mathbb{C})$, against six in the real case, and the three continuous families of the real case collapse because $\mathbb{C}$ is closed under square roots. Every graph of an isomorphism between conjugate blocks is a diagonal, so the new families are the graphs across types and the fibre products; the example is the four-dimensional fibre product over the nilpotent ideal of the Borel, which contains neither central idempotent.

**The Lie layer.** The algebra is $\mathfrak{gl}(2,\mathbb{C})\oplus\mathfrak{gl}(2,\mathbb{C})$, with a two-dimensional centre and a six-dimensional semisimple part. Goursat's theorem holds verbatim, the blocks of one factor are the four projective types of a line, the three types of a plane, the Borel, the traceless part and the whole algebra, and the graphs of isomorphisms between conjugate blocks are diagonals. The ideals are the spaces $\mathfrak j\oplus\Lambda$ with $\mathfrak j$ one of the four ideals of the semisimple part and $\Lambda$ an arbitrary subspace of the centre, so the lines of the centre form a projective line of ideals; the fibre product by the trace is a seven-dimensional subalgebra that is neither a product nor a graph. In the biquaternion base the Cartan direction is the Hermitian unit $i\vec e_z$ and the two nilpotent directions are the mixed Peirce lines $\vec\Pi_{\mathrm{nil},1},\vec\Pi_{\mathrm{nil},2}$, the two real forms are the traceless parts of $\mathbb{H}$ and of the split form, and the inertia of the Killing form is invisible over $\mathbb{C}$ because the star that would produce it is conjugate-linear.

**The Jordan layer.** The symmetrisation turns the complexification into the sum of two copies of $M_2(\mathbb{C})^{+}$. The identity $U_1U_2+U_2U_1=\operatorname{tr}(U_1U_2)I$ for traceless matrices makes the traceless part Jordan-nilpotent, so every space $\mathbb{C}I\oplus V$ with $V$ traceless is a Jordan subalgebra, and the types are six, indexed by the dimension of $V$ and the rank of the trace form on it: scalar, dual numbers, split, symmetric, degenerate, whole. The count is six against eight in the real case, and the reason is again that only the rank survives over $\mathbb{C}$.

**The Killing forms.** $K(X,Y)=4\operatorname{tr}(XY)-2\operatorname{tr}X\operatorname{tr}Y$ on each factor, the scalar line isotropic and orthogonal to everything, the restriction to the traceless part equal to four times the trace form of the Jordan layer. The ranks are three on $\mathfrak{gl}_2$, three on $\mathfrak{sl}_2$, one on the Borel, one on the abelian plane, six on the sum of the two traceless parts and six on the sum of the two full algebras with a two-dimensional radical. Over $\mathbb{C}$ the inertia is not an invariant, and the inertias of the companion article are those of the real slices.

**The real forms.** A real structure on the sum preserves or exchanges the two simple summands. The preserving case gives four maps, with fixed algebras $\mathbb{H}\oplus\mathbb{H}$, $\mathbb{H}\oplus M_2(\mathbb{R})$, $M_2(\mathbb{R})\oplus\mathbb{H}$ and $M_2(\mathbb{R})\oplus M_2(\mathbb{R})$; the exchanging case is determined by a conjugate-linear automorphism and gives one class, with fixed algebra $M_2(\mathbb{C})_{\mathbb{R}}$, the slanted form. A commonly quoted list omits the mixed pair and counts the slanted form twice. The two mixed structures are exchanged by the swap and give the same algebra, so the count is five structures and four classes. The map $x\mapsto(x,\bar x)$ carries each real form of $\mathbb{B}$ into its own pair form and into the slanted form, and the mixed pair is not the image of anything.

**The involutions and the six subspaces.** The coefficient conjugation, the quaternion conjugation, the star and the transpose have fixed spaces of real dimensions four, two, four and six, and the six remarkable subspaces have dimensions $2,6,4,4,4,4$. The intersection table with $\mathbb{B}_H$ and $\mathbb{B}_{iH}$ is $1,3,4,0,1,3$ with the sums equal to the dimensions, and its fourth column is the compact column of the companion article.

**The Lie groups.** The centres of the covers are $\{\pm I\}$ for $SL(2,\mathbb{C})$, $(\mathbb{Z}/2)\times\mathbb{C}$ for $SL(2,\mathbb{C})\times\mathbb{C}$, $\mathbb{C}^n$ for $\mathbb{C}^n$, and $2\pi i\mathbb{Z}\times\mathbb{C}$ for $\widetilde{B^+}=\mathbb{C}^3$. The quotient by $\langle(-I,\pi i)\rangle$ gives $GL(2,\mathbb{C})$ with fundamental group $\mathbb{Z}$; the quotients of $\mathbb{C}^3$ by a lattice $\Delta$ of that centre give $B^+$ with fundamental group $\mathbb{Z}^2$, and the slanted lattices give the further quotients with fundamental group $\Delta$. A semisimple algebra has finitely many connected groups; a solvable one with a continuous centre has infinitely many.

**The comparison and the verdict.** Within one factor the complex lattice is smaller than the real one; in the sum it is larger, by the three families. The complexification determines the factors, their lattices, the families of the sum and the ranks of the Killing form, and it does not determine the real form, the inertia, the position of the real subspaces, the discrete central subgroup or the unitary representation theory. The extra data are supplied by the real structure.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the complex form, $M_2(\mathbb{C})$ |
| $\mathbb{B}_{\mathbb{R}}$ | the same algebra with real scalars |
| $\mathbb{B}^{\oplus 2}_{\mathbb{C}}$ | the complexification, $\mathbb{B}_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C}$ |
| $\Phi$ | the isomorphism onto $\mathbb{B}\oplus\mathbb{B}$ |
| $\iota_1,\iota_2$ | the two inclusions of the complex form |
| $\Pi_1,\Pi_2$ | the two central idempotents $(I,0)$ and $(0,I)$ |
| $A_{ij}$ | the Peirce components $\Pi_iA\Pi_j$ |
| $\sigma_1,\sigma_{\mathrm{split}}$ | the coefficient conjugation, written $\bar{}$ in the ninth section, and its inner twist |
| $\tau$ | the exchange $(u,v)\mapsto(v,u)$ |
| $\bar{}$ | the coefficient conjugation |
| $\natural$ | the quaternion conjugation |
| ${}^{*}$ | the star, $\natural\circ\bar{}$ |
| $\circ$ | the Jordan product, the corpus's bullet |
| $q$ | the trace form $\operatorname{tr}(U_1U_2)$ on the traceless part |
| $\mathfrak b_0$ | the upper triangular matrices, a Lie subalgebra of dimension three |
| $B^+$ | the group of invertible upper triangular matrices |
| $H,N,S$ | $\operatorname{diag}(1,-1)$, $E_{12}$, $E_{12}+E_{21}$ |
| $\mathfrak h$ | the diagonal traceless matrices, a Cartan subalgebra |

## Further Reading

Bourbaki, *Algèbre*, chapters 8 and 9, for the semisimple algebras over a field and their forms; *Groupes et algèbres de Lie*, chapters 1 to 3, for the Lie correspondence and the exponential.

Goursat, *Sur les substitutions orthogonales et les divisions régulières de l'espace*, Annales scientifiques de l'École Normale Supérieure 6 (1889), for the lemma on subalgebras of a direct product.

Jacobson, *Structure of Rings*, chapter 4, for the central simple algebras and the Skolem–Noether theorem; *Lie Algebras*, for the Killing form and the Cartan criteria.

Pierce, *Associative Algebras*, for the classification of the low-dimensional subalgebras and the Peirce decomposition.

Springer and Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups*, for the Jordan algebras of a quadratic form and the six types of the sixth section.

Zhevlakov, Slin'ko, Shestakov and Shirshov, *Rings That Are Nearly Associative*, for the Jordan and alternative algebras and the identities used in the Jordan layer.

Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, chapter 2, for the Lie correspondence, the exponential map and the covering groups.

Onishchik and Vinberg, *Lie Groups and Algebraic Groups*, for the real forms and the table of the classical groups.
