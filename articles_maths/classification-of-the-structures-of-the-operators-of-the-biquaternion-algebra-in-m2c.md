# __Classification of the Structures of the Operators of the Biquaternion Algebra in $M_2(\mathbb{C})$__

## Introduction

**The question.** The operator algebra of the display is $\operatorname{End}_{\mathbb{C}}(M_2(\mathbb{C}))\cong M_4(\mathbb{C})$. This article asks which structures change its ground field. It classifies the real structures of $M_4(\mathbb{C})$, shows that $\operatorname{End}_{\mathbb{R}}(M_2(\mathbb{C}))\cong M_8(\mathbb{R})$ has no complex structure, and relates the answer to the element-level classification of $\mathbb{B}$.

**Why it is the same statement.** This is the in-depth matrix reading of [Classification of the Structures of the Operators of the Biquaternion Algebra](classification-of-the-structures-of-the-operators-of-the-biquaternion-algebra.html). The source states the operator algebras abstractly and proves the two real forms; the display identifies $\mathcal{E}_{\mathbb{C}}$ with $M_4(\mathbb{C})$, so every proof below is the source's proof written in Kronecker products. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. $\mathcal{E}_{\mathbb{C}}=M_4(\mathbb{C})$ has centre $\mathbb{C}\mathrm I_4$ and is simple. A real structure is a conjugate-linear multiplicative involution, and its fixed set is a real form. $M_4(\mathbb{C})$ has exactly two real forms, $M_4(\mathbb{R})$ and $M_2(\mathbb{H})$; they are separated by the inertia of the trace form, $(10,6)$ against $(6,10)$. $\mathcal{E}_{\mathbb{R}}=M_8(\mathbb{R})$ has no complex structure and its complexification is $M_8(\mathbb{C})$, with the two real forms $M_8(\mathbb{R})$ and $M_4(\mathbb{H})$. The double centralizer reads $M_2\otimes M_2^{\mathrm{op}}\cong M_4$, the regular families are the two tensor factors, and the complement $\mathfrak{sl}_2\otimes\mathfrak{sl}_2$ is nine-dimensional. The Jordan layer has three real forms over one complex algebra, and the Hermitian space $H_4(\mathbb{C})$ has no associative model.

**What the article does not do.** It does not develop the subalgebra lattices, Killing forms or group tables of $M_4(\mathbb{R})$ and $M_2(\mathbb{H})$; those are [Classification of the Real Structures of the Operators of the Biquaternion Algebra, including Lie Algebras and Lie Groups in $M_2(\mathbb{C})$](classification-of-the-real-structures-of-the-operators-of-the-biquaternion-algebra-in-m2c.html). It does not treat the two scalar extensions in detail; that is [Classification of the Complex Structures of the Operators of the Biquaternion Algebra, including Lie Algebras and Lie Groups in $M_2(\mathbb{C})$](classification-of-the-complex-structures-of-the-operators-of-the-biquaternion-algebra-in-m2c.html). It does not prove the element-level theorem, which is [Classification of the Structures of the Biquaternion Algebra](classification-of-the-structures-of-the-biquaternion-algebra.html).

**Conventions.** The display is $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$. The operator algebra is written $\mathcal{E}_{\mathbb{C}}=\operatorname{End}_{\mathbb{C}}(M_2(\mathbb{C}))$ and is identified with $M_4(\mathbb{C})$ along the basis $(E_t,E_x,E_y,E_z)$ with $E_t=\mathrm I_2$, $E_x=-i\sigma_1$, $E_y=-i\sigma_2$, $E_z=-i\sigma_3$. The left actor is $\mathrm I_2\otimes A$ and the right actor is $B^{\mathsf T}\otimes\mathrm I_2$, in the column convention of [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html).

**Boundaries.** The regular representation is [The Endomorphisms of the Biquaternion Algebra as an Algebra: the Regular Representation in $M_2(\mathbb{C})$](end-m2c-as-an-algebra-the-regular-representation.html). The two-sided operators and their cone are [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html). The enveloping algebra is [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure in $M_2(\mathbb{C})$](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure-in-m2c.html). The $n=2$ spine is [The Symmetric and Antisymmetric Parts of the Operator Space at $n=2$](the-symmetric-and-antisymmetric-parts-of-the-operator-space-at-n-2.html) and [The Length and the Two Ranks at $n=2$](the-length-and-the-two-ranks-at-n-2.html), and the display is [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html).

**Letters.** $\mathcal{E}_{\mathbb{C}}$ is $M_4(\mathbb{C})$ and $\mathcal{E}_{\mathbb{R}}$ is $M_8(\mathbb{R})$. Real structures are $\tau$; element-level real structures are $\sigma$. $\tau_{\mathbb{R}}$ is entrywise conjugation and $\tau_{\mathbb{H}}$ is quaternionic conjugation with $J_0=\begin{pmatrix}0&\mathrm I_2\\-\mathrm I_2&0\end{pmatrix}$. $\mathfrak{sl}_2\subset M_2(\mathbb{C})$ is the traceless part and $\mathfrak{m}=\mathfrak{sl}_2\otimes\mathfrak{sl}_2$.

## The Two Operator Algebras

**The carrier.** $M_2(\mathbb{C})$ has complex dimension four and real dimension eight, with the complex basis $(E_t,E_x,E_y,E_z)$ and the same four matrices as a real basis.

**The two algebras.**
$$
\mathcal{E}_{\mathbb{C}}=\operatorname{End}_{\mathbb{C}}(M_2(\mathbb{C}))\cong M_4(\mathbb{C}),\qquad
\mathcal{E}_{\mathbb{R}}=\operatorname{End}_{\mathbb{R}}(M_2(\mathbb{C}))\cong M_8(\mathbb{R}),
$$
of complex dimension sixteen and real dimension sixty-four. The first has real dimension thirty-two.

**The centres.** $Z(\mathcal{E}_{\mathbb{C}})=\mathbb{C}\mathrm I_4$ and $Z(\mathcal{E}_{\mathbb{R}})=\mathbb{R}\mathrm I_8$, and both algebras are simple, being full matrix algebras over a field.

**The complex-linear part of the real algebra.** Let $J(X)=iX$ be multiplication by $i$, of matrix $i\mathrm I_4$. Then
$$
\mathcal{E}_{\mathbb{C}}=\{F\in\mathcal{E}_{\mathbb{R}}:FJ=JF\},\qquad
\mathcal{E}_{\mathbb{R}}=\mathcal{E}_{\mathbb{C}}\oplus\mathcal{E}_{\mathbb{C}}J .
$$
The second identity is a direct sum of real spaces of dimensions $32+32=64$.

**The tensor forms.** $L_A=\mathrm I_2\otimes A$ and $R_B=B^{\mathsf T}\otimes\mathrm I_2$, and both assignments are injective algebra maps, the second reversing the order. The transpose records that the right actor multiplies the second index on the right.

**The master table.**

| algebra | ground field | dimension | centre |
|---|---|---|---|
| $\mathcal{E}_{\mathbb{C}}\cong M_4(\mathbb{C})$ | $\mathbb{C}$ | $16$ complex, $32$ real | $\mathbb{C}\mathrm I_4$ |
| $\mathcal{E}_{\mathbb{R}}\cong M_8(\mathbb{R})$ | $\mathbb{R}$ | $64$ real | $\mathbb{R}\mathrm I_8$ |
| $\mathcal{E}_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C}\cong M_8(\mathbb{C})$ | $\mathbb{C}$ | $64$ complex | $\mathbb{C}\mathrm I_8$ |
| $\mathcal{E}_{\mathbb{C}}\otimes_{\mathbb{R}}\mathbb{C}\cong M_4(\mathbb{C})\oplus M_4(\mathbb{C})$ | $\mathbb{C}$ | $32$ complex | $\mathbb{C}\oplus\mathbb{C}$ |

## The Two Form Notions

**Definition (real structure).** A real structure on $\mathcal{E}_{\mathbb{C}}$ is a conjugate-linear multiplicative involution $\tau$:
$$
\tau(X+\lambda Y)=\tau(X)+\bar\lambda\tau(Y),\qquad \tau(XY)=\tau(X)\tau(Y),\qquad \tau^{2}=\mathrm{id} .
$$

**Proposition (the fixed set is a real form).** $\mathcal{E}^{\tau}=\{X:\tau(X)=X\}$ is a real subalgebra of real dimension sixteen, and $\mathcal{E}^{\tau}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathcal{E}_{\mathbb{C}}$.

*Proof.* Every $X$ splits as $\tfrac12(X+\tau X)+\tfrac12(X-\tau X)$, and the second summand is $i$ times the fixed element $\tfrac1{2i}(X-\tau X)$.

**The two concrete structures.** In the frame $M_4(\mathbb{C})$,
$$
\tau_{\mathbb{R}}(X)=\bar X,\qquad \tau_{\mathbb{H}}(X)=J_0\bar XJ_0^{-1},\qquad J_0=\begin{pmatrix}0&\mathrm I_2\\-\mathrm I_2&0\end{pmatrix}.
$$
Both are verified as conjugate-linear, multiplicative and involutive, with residual $8\cdot10^{-16}$ and exact squares.

**The block model.** The fixed set of $\tau_{\mathbb{H}}$ is
$$
X=\begin{pmatrix}A&B\\-\bar B&\bar A\end{pmatrix},\qquad A,B\in M_2(\mathbb{C}),
$$
verified exactly on the projection $\tfrac12(X+J_0\bar XJ_0^{-1})$. The sixteen real parameters are the eight of $A$ and the eight of $B$, and the block rule is the rule of quaternionic multiplication. This is $M_2(\mathbb{H})$.

**The complexification of the real algebra.** A real basis identifies $\mathcal{E}_{\mathbb{R}}$ with $M_8(\mathbb{R})$ and $\mathcal{E}_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C}$ with $M_8(\mathbb{C})$, of complex dimension sixty-four.

**No complex structure on $\mathcal{E}_{\mathbb{R}}$.** A complex structure would be a unital map $\mathbb{C}\to Z(M_8(\mathbb{R}))=\mathbb{R}$, and no such map exists, since $i$ has no real square root of $-1$. What exists is the complexification $M_8(\mathbb{C})$, and its two real forms $M_8(\mathbb{R})$ and $M_4(\mathbb{H})$.

**The two questions are not inverse.** A real structure descends, a complexification ascends. The first is a map on a given complex algebra; the second builds a new complex algebra from a real one.

**Non-central copies of $\mathbb{C}$ do not count.** $M_8(\mathbb{R})$ contains $\mathbb{C}$ as the block $\begin{pmatrix}a&b\\-b&a\end{pmatrix}$, but the image is not central, so it is a complex structure of the module and not of the algebra.

## The Real Forms of the Complex Operator Algebra

**Theorem.** Up to isomorphism, $M_4(\mathbb{C})$ has exactly the two real forms
$$
M_4(\mathbb{R})\quad(\text{split}),\qquad M_2(\mathbb{H})\quad(\text{quaternionic}).
$$

*Proof.* A real form is a central simple real algebra of dimension sixteen. By Wedderburn it is $M_k(K)$ with $K$ a real division algebra, so $K=\mathbb{R}$ or $K=\mathbb{H}$ by Frobenius. The dimensions are $k^{2}$ and $4k^{2}$, giving $k=4$ with $\mathbb{R}$ and $k=2$ with $\mathbb{H}$.

**The same theorem at the size of the display.** The two real forms of $M_2(\mathbb{C})$ are $M_2(\mathbb{R})$ and $M_1(\mathbb{H})=\mathbb{H}$; that is the element-level statement. The operator-level list is the element-level list with $4$ in place of $2$.

**The separating invariant.** On $\mathcal{E}_{\mathbb{C}}$ the symmetric form $(X,Y)\mapsto\operatorname{tr}(XY)$ restricts to $M_4(\mathbb{R})$ with inertia $(10,6)$ and to $M_2(\mathbb{H})$ with inertia $(6,10)$, both computed from a real basis of sixteen elements.

*Proof.* In $M_4(\mathbb{R})$ the symmetric part is positive of dimension ten and the skew part negative of dimension six, and the two are orthogonal. In $M_2(\mathbb{H})$ the quaternionic Hermitian part is positive of real dimension six and the quaternionic skew part negative of real dimension ten.

**The corollary.** $M_4(\mathbb{R})$ and $M_2(\mathbb{H})$ are not isomorphic, so $\tau_{\mathbb{R}}$ and $\tau_{\mathbb{H}}$ are not conjugate.

**The word compact is a misnomer.** The compact real form of $\mathfrak{gl}(4,\mathbb{C})$ is $\mathfrak{u}(4)$, and $\mathfrak{u}(4)$ is not the Lie algebra of any real form of $M_4(\mathbb{C})$, since a real form of the algebra is closed under products and the product of two skew-Hermitian matrices is skew-Hermitian only when they commute. The pair of words is split and quaternionic.

**The Lie algebra has more forms.** $\mathfrak{gl}(4,\mathbb{C})$ has the six real forms $\mathfrak{gl}(4,\mathbb{R})$, $\mathfrak{u}(4)$, $\mathfrak{u}(3,1)$, $\mathfrak{u}(2,2)$, $\mathfrak{gl}(2,\mathbb{H})$ and $\mathfrak{gl}(4,\mathbb{C})_{\mathbb{R}}$, and only the first and the fifth are Lie algebras of real forms of the associative algebra. A real form of the Lie algebra is a bracket-closed subspace; a real form of the algebra is a product-closed one, and the second condition is stronger.

## The Complexification and the Two Scalar Extensions

**Two different extensions.** $\mathcal{E}_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C}$ is $M_8(\mathbb{C})$ of complex dimension sixty-four, and $\mathcal{E}_{\mathbb{C}}\otimes_{\mathbb{R}}\mathbb{C}$ is $M_4(\mathbb{C})\oplus M_4(\mathbb{C})$ of complex dimension thirty-two. The second is the complexification of the complex algebra read over the reals, and it splits because $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$.

**The two copies.** In the second extension the two copies of $M_4(\mathbb{C})$ are the projections onto the two factors of $\mathbb{C}\oplus\mathbb{C}$, and an operator $X$ corresponds to $(X,\bar X)$. The conjugation that swaps the two factors is the real structure of the complexification.

**The two real forms of $M_8(\mathbb{C})$.** $M_8(\mathbb{R})$ and $M_4(\mathbb{H})$, by the same Wedderburn and Frobenius argument at dimension sixty-four.

**The count of real structures of the split extension.** $M_4(\mathbb{C})\oplus M_4(\mathbb{C})$ has five real structures and four isomorphism classes, by the pattern of the element-level complexification with $M_4$ in place of $M_2$; the enumeration is [Classification of the Complex Structures of the Operators of the Biquaternion Algebra, including Lie Algebras and Lie Groups in $M_2(\mathbb{C})$](classification-of-the-complex-structures-of-the-operators-of-the-biquaternion-algebra-in-m2c.html).

## The Double Centralizer and the Distinguished Subalgebras

**Theorem (double centralizer in $M_4(\mathbb{C})$).**
$$
\{\mathrm I_2\otimes A\}'=\{B^{\mathsf T}\otimes\mathrm I_2\},\qquad
\{B^{\mathsf T}\otimes\mathrm I_2\}'=\{\mathrm I_2\otimes A\},\qquad
\bigl(L\cup R\bigr)'=\mathbb{C}\mathrm I_4 .
$$

*Proof.* Let $T$ commute with every $\mathrm I_2\otimes A$. Then $T(X)=T(X\mathrm I_2)=(\mathrm I_2\otimes X)T(\mathrm I_2)=T(\mathrm I_2)X$, so $T$ is a left actor. The other inclusion is $\mathrm I\otimes A$ commuting with $B^{\mathsf T}\otimes\mathrm I$, verified exactly. An operator commuting with both families is a left actor commuting with every right actor, hence $T(\mathrm I_2)$ is central, hence a scalar.

**Corollary (the tensor form).** The multiplication map
$$
M_2(\mathbb{C})\otimes_{\mathbb{C}}M_2(\mathbb{C})^{\mathrm{op}}\longrightarrow M_4(\mathbb{C}),\qquad A\otimes B\longmapsto \mathrm I_2\otimes A\cdot B^{\mathsf T}\otimes\mathrm I_2,
$$
is an isomorphism, and $L(M_2)=\mathrm I_2\otimes M_2$ while $R(M_2)=M_2^{\mathsf T}\otimes\mathrm I_2$.

**The complement.** With $\mathfrak{sl}_2$ the traceless part of $M_2(\mathbb{C})$,
$$
\mathfrak{m}=\mathfrak{sl}_2\otimes\mathfrak{sl}_2,\qquad \dim_{\mathbb{C}}\mathfrak{m}=9,\qquad
M_4(\mathbb{C})=\bigl(L+R\bigr)\oplus\mathfrak{m},\qquad \dim_{\mathbb{C}}(L+R)=7 .
$$
$7+9=16$, so the decomposition is an equality of vector spaces.

**Why nine.** The operators that are neither a left actor nor a right one nor a scalar multiple of either are the products $A\otimes B$ with both factors traceless, and there are nine complex parameters.

**The sum $L+R$ is not direct.** $L(M_2)$ and $R(M_2)$ meet in $\mathbb{C}\mathrm I_4$, and their sum is a Lie subalgebra but not an associative one, since $\mathrm I\otimes A\cdot B^{\mathsf T}\otimes\mathrm I$ leaves it for non-scalar factors.

**The complement is a module and not an algebra.** $\mathfrak{m}$ is stable under $[L_{\mathfrak{sl}_2},\cdot]$ and $[R_{\mathfrak{sl}_2},\cdot]$ and under multiplication by traceless left and right factors, but not under the full regular families: the witness is $(\vec e_x\otimes\vec e_x)^{2}=\mathrm I_4$, since $E_x^{2}=-\mathrm I_2$.

**The real forms of the distinguished subalgebras.** $L(M_2(\mathbb{C}))\cong M_2(\mathbb{C})$ has the real forms $L(\mathbb{H})\cong\mathbb{H}$ and $L(M_2(\mathbb{R}))\cong M_2(\mathbb{R})$, of real dimension four. The right family carries the reversed product, so its real forms are the opposite algebras.

**The six subspaces.** For each real subspace $B_j$ of $M_2(\mathbb{C})$, the image $L(B_j)$ has the same real dimension, and it is an associative subalgebra exactly when $B_j$ is. $\mathbb{B}_C$ and $\mathbb{B}_H$ are subalgebras; $\mathbb{B}_V$ and $\mathbb{B}_{\Phi}$ are Lie subalgebras only; $\mathbb{B}_{iH}$ and $\mathbb{B}_{\Psi}$ are neither. The reason is one line: the bracket of two Hermitian matrices is skew-Hermitian, and $\vec e_x^{2}=-\mathrm I_2$ leaves the pure part.

## The Jordan Layer

**The symmetrized product.** $X\circ Y=\tfrac12(XY+YX)$ is commutative and satisfies the Jordan identity, and the algebra is $M_4(\mathbb{C})^{+}$.

**The three real forms.**
$$
M_4(\mathbb{R})^{+},\qquad M_2(\mathbb{H})^{+},\qquad H_4(\mathbb{C})=\{X:X^{*}=X\},
$$
of real dimension sixteen each. The third is closed under $\circ$ because $(X\circ Y)^{*}=X^{*}\circ Y^{*}$, and its real dimension is $4+2\cdot6=16$, counting four real diagonal entries and six complex off-diagonal ones.

**The separating invariant.** The trace form $\operatorname{tr}(X^{2})$ has inertia $(16,0)$ on $H_4(\mathbb{C})$, $(10,6)$ on $M_4(\mathbb{R})^{+}$ and $(6,10)$ on $M_2(\mathbb{H})^{+}$, so the three are pairwise non-isomorphic.

**Three lattices over one complex algebra.** The associative, Jordan and Lie lattices of $M_4(\mathbb{C})$ are different, related by $XY=X\circ Y+\tfrac12[X,Y]$. A real form of the associative algebra gives one of each of the others, and $H_4(\mathbb{C})$ is the witness that the passage cannot be reversed: it is a Jordan real form with no associative real form above it.

**The Hermitian operators are self-adjoint.** For a Hermitian $A$, the left actor $\mathrm I_2\otimes A$ is self-adjoint for the Hermitian form $(X,Y)\mapsto\operatorname{tr}(X^{*}Y)$, so $L(\mathbb{B}_{\Psi})\subset H_4(\mathbb{C})$, a real subspace of dimension four and not a subalgebra.

## The Relation to the Element Level

**Theorem (the two-sided span).** Let $A_0$ be a real form of $M_2(\mathbb{C})$ and let
$$
\mathcal{E}(A_0)=\operatorname{span}_{\mathbb{R}}\{A\otimes B:A,B\in A_0\}.
$$
Then $\mathcal{E}(A_0)$ is a real subalgebra of real dimension sixteen, it complexifies to $M_4(\mathbb{C})$, and it is isomorphic to $A_0\otimes_{\mathbb{R}}A_0^{\mathrm{op}}$.

**Corollary (both element forms give the split form).**
$$
\mathbb{H}\otimes_{\mathbb{R}}\mathbb{H}^{\mathrm{op}}\cong M_4(\mathbb{R}),\qquad
M_2(\mathbb{R})\otimes_{\mathbb{R}}M_2(\mathbb{R})^{\mathrm{op}}\cong M_4(\mathbb{R}),
$$
because $D\otimes_{\mathbb{R}}D^{\mathrm{op}}\cong\operatorname{End}_{\mathbb{R}}(D)$ for a division algebra $D$, with $D=\mathbb{H}$ of real dimension four, and $M_2(\mathbb{R})$ is isomorphic to its opposite by the transpose.

**The passage loses information.** The two element-level forms give one operator-level form, so the operator classification is not a corollary of the element-level one. What the operator form determines is the isomorphism class of the real algebra, the attached Lie algebra and the spectrum type; what it does not determine is which element form generated it.

**The fixed set of an induced real structure.** For an element-level real structure $\sigma$, the map $T\mapsto\sigma T\sigma^{-1}$ has fixed set $\mathcal{E}(A_0)$, the two-sided span of the fixed algebra of $\sigma$, and both sides have real dimension sixteen.

**The two spans are distinct.** $\mathcal{E}(\mathbb{H})$ and $\mathcal{E}(M_2(\mathbb{R}))$ are different sixteen-dimensional subspaces meeting in real dimension eight, and an automorphism of $M_4(\mathbb{C})$ carries one to the other, since $\mathbb{H}$ and $M_2(\mathbb{R})$ are isomorphic over $\mathbb{R}$ as soon as a matrix frame is fixed for $\mathbb{H}$.

## Where $n=2$ Differs

**The size of the arrays.** The element algebra has size two, so $\operatorname{End}$ is $M_4(\mathbb{C})$ and the real endomorphism algebra is $M_8(\mathbb{R})$, and not larger. Every count above is the count at $n=2$: sixteen complex dimensions for the operator algebra against four for the element algebra, and sixty-four real dimensions against eight.

**The two real forms.** At $n=2$ the pair is $M_2(\mathbb{R})$ and $\mathbb{H}$, of real dimension four, and the element-level classification is the operator-level one at $n=2$ instead of $n=4$.

**The inertia.** The trace form on $M_2(\mathbb{C})$'s two real forms has inertia $(3,1)$ and $(1,3)$; the operator-level pair $(10,6)$, $(6,10)$ is the same arithmetic at dimension sixteen.

**The double centralizer.** $M_2\otimes M_2^{\mathrm{op}}\cong M_4$ is the display's own isomorphism, and the nine-dimensional complement is $3\times3$; at order $n$ it is $(n^{2}-1)^{2}$, which is nine only at $n=2$.

**Nothing else differs in kind.** The two real structures, the absence of a complex structure on the real operator algebra, the three Jordan forms and the loss of the element-level datum hold at every order.

## Summary

The complex operator algebra of the display is $M_4(\mathbb{C})$, with centre $\mathbb{C}\mathrm I_4$ and the two real forms $M_4(\mathbb{R})$ and $M_2(\mathbb{H})$. The forms are realised by entrywise conjugation $\tau_{\mathbb{R}}(X)=\bar X$ and by quaternionic conjugation $\tau_{\mathbb{H}}(X)=J_0\bar XJ_0^{-1}$, whose fixed set is the block model $\begin{pmatrix}A&B\\-\bar B&\bar A\end{pmatrix}$ verified exactly. The trace form separates them, with inertia $(10,6)$ on the split form and $(6,10)$ on the quaternionic one, and the separation is the Wedderburn and Frobenius count at dimension sixteen.

The real operator algebra is $M_8(\mathbb{R})$; it has no complex structure, because its centre is $\mathbb{R}$, and its complexification is $M_8(\mathbb{C})$ with the two real forms $M_8(\mathbb{R})$ and $M_4(\mathbb{H})$. The complexification of the complex algebra is instead $M_4(\mathbb{C})\oplus M_4(\mathbb{C})$, of complex dimension thirty-two, and the two extensions are different objects.

The double centralizer reads $M_2\otimes M_2^{\mathrm{op}}\cong M_4$ with the regular families as the two factors, $\mathrm I_2\otimes M_2$ and $M_2^{\mathsf T}\otimes\mathrm I_2$, and their common centralizer is the scalars. The two-sided operators split as $L+R$ of dimension seven plus the nine-dimensional complement $\mathfrak{sl}_2\otimes\mathfrak{sl}_2$, which is a module over the traceless regular families and neither an associative nor a Lie subalgebra.

The Jordan layer carries the three real forms $M_4(\mathbb{R})^{+}$, $M_2(\mathbb{H})^{+}$ and $H_4(\mathbb{C})$, separated by the inertia of the trace form, and $H_4(\mathbb{C})$ has no associative model. The element level enters through the two-sided span: both $\mathbb{H}$ and $M_2(\mathbb{R})$ generate the split form $M_4(\mathbb{R})$, so the operator-level classification is coarser than the element-level one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{E}_{\mathbb{C}}$ | $\operatorname{End}_{\mathbb{C}}(M_2(\mathbb{C}))\cong M_4(\mathbb{C})$ |
| $\mathcal{E}_{\mathbb{R}}$ | $\operatorname{End}_{\mathbb{R}}(M_2(\mathbb{C}))\cong M_8(\mathbb{R})$ |
| $\tau_{\mathbb{R}},\tau_{\mathbb{H}}$ | entrywise and quaternionic conjugation |
| $J_0$ | the quaternionic structure $\begin{pmatrix}0&\mathrm I_2\\-\mathrm I_2&0\end{pmatrix}$ |
| $\mathfrak{sl}_2$ | the traceless part of $M_2(\mathbb{C})$ |
| $\mathfrak{m}$ | $\mathfrak{sl}_2\otimes\mathfrak{sl}_2$ |
| $H_4(\mathbb{C})$ | the Hermitian matrices |
| $\mathcal{E}(A_0)$ | the two-sided span of a real form $A_0$ |

## Further Reading

- [Classification of the Structures of the Operators of the Biquaternion Algebra](classification-of-the-structures-of-the-operators-of-the-biquaternion-algebra.html), for the source statements and the corrections to the source paper.
- [Classification of the Real Structures of the Operators of the Biquaternion Algebra, including Lie Algebras and Lie Groups in $M_2(\mathbb{C})$](classification-of-the-real-structures-of-the-operators-of-the-biquaternion-algebra-in-m2c.html), for the two real forms layer by layer.
- [Classification of the Complex Structures of the Operators of the Biquaternion Algebra, including Lie Algebras and Lie Groups in $M_2(\mathbb{C})$](classification-of-the-complex-structures-of-the-operators-of-the-biquaternion-algebra-in-m2c.html), for the split extension and its five real structures.
- [The Endomorphisms of the Biquaternion Algebra as an Algebra: the Regular Representation in $M_2(\mathbb{C})$](end-m2c-as-an-algebra-the-regular-representation.html), for the two regular families as tensor factors.
- [Classification of the Structures of the Biquaternion Algebra](classification-of-the-structures-of-the-biquaternion-algebra.html), for the element-level theorem that this one lifts.
