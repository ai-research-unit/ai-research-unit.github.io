# __The Transposition of the Two Sides__

## The Question

Every element of the biquaternion algebra can be multiplied on the left or on the right, and the two operators that result are different: for a general element $\tilde Q$ the operators $X\mapsto\tilde QX$ and $X\mapsto X\tilde Q$ disagree, and they disagree already on the unit. Yet the two families they form are not independent. The algebra carries a symmetry that turns every left multiplication into a right multiplication, and the purpose of this article is to find that symmetry, to compute exactly what it does to the element that parametrizes the operator, and to explain why the element cannot be left untouched.

The article proceeds in the order in which the facts are needed. The two families and their laws come first, because everything later is a statement about them. The symmetry comes next, with a proof of the one property it contributes, namely that it reverses products. Then the composite is computed on an arbitrary element, and the identity is read off the computation rather than assumed: the computation is what proves it, so it comes first. Only after that does the article turn to the equation that the notation invites and that is false, and it says exactly which elements make it true.

No step uses a basis, a matrix, a topology, a distance or a limit. Every object below is an operator on the algebra, and every proof is a computation on an arbitrary element.

## The Two Families

**Definition.** For $\tilde Q$ in $\mathbb{B}$, the **left multiplication** and the **right multiplication** by $\tilde Q$ are the operators

$$
L_{\tilde Q}(X)=\tilde Q X,
\qquad\qquad
R_{\tilde Q}(X)=X\tilde Q,
$$

defined for every $X$ in $\mathbb{B}$.

Both are $\mathbb{C}$-linear, because the product of the algebra is bilinear over $\mathbb{C}$. The element $\tilde Q$ is called the **parameter** of the operator.

**Proposition (the three laws).** For all elements,

$$
L_{\tilde Q}L_{\tilde P}=L_{\tilde Q\tilde P},
\qquad
R_{\tilde Q}R_{\tilde P}=R_{\tilde P\tilde Q},
\qquad
L_{\tilde Q}R_{\tilde P}=R_{\tilde P}L_{\tilde Q}.
$$

*Proof.* Let $X$ be arbitrary. Each identity is a chain of equalities in which the only ingredient is the associativity of the product.

$$
L_{\tilde Q}\bigl(L_{\tilde P}(X)\bigr)=\tilde Q\bigl(\tilde PX\bigr)=\bigl(\tilde Q\tilde P\bigr)X=L_{\tilde Q\tilde P}(X),
$$
$$
R_{\tilde Q}\bigl(R_{\tilde P}(X)\bigr)=\bigl(X\tilde P\bigr)\tilde Q=X\bigl(\tilde P\tilde Q\bigr)=R_{\tilde P\tilde Q}(X),
$$
$$
L_{\tilde Q}\bigl(R_{\tilde P}(X)\bigr)=\tilde Q X\tilde P=R_{\tilde P}\bigl(L_{\tilde Q}(X)\bigr).
$$

Since $X$ was arbitrary, the operators agree.

The second law deserves a word. It says that the map $\tilde Q\mapsto R_{\tilde Q}$ does not preserve the order of the parameters but exchanges them, and such a map is called an **anti-representation**. The first law says that the map $\tilde Q\mapsto L_{\tilde Q}$ is a representation. The third says that the two families commute element by element, so a product $L_{\tilde Q}R_{\tilde P}$ may be written with the factors in either order.

**Proposition (the unit reads the parameter).** Let $e_t$ be the unit of the algebra. Then

$$
L_{\tilde Q}(e_t)=\tilde Q=R_{\tilde Q}(e_t),
$$

and consequently $L_{\tilde Q}=L_{\tilde P}$ exactly when $\tilde Q=\tilde P$, and $R_{\tilde Q}=R_{\tilde P}$ exactly when $\tilde Q=\tilde P$.

*Proof.* Multiplying by the unit changes nothing, so both operators return $\tilde Q$ at $e_t$. If two such operators are equal then their values at $e_t$ are equal, which gives $\tilde Q=\tilde P$; and if the parameters are equal the operators are equal by definition.

This little proposition carries a large share of the article. It does two jobs. Applied to an identity between operators it produces an identity between parameters, because the unit evaluates a parameter directly. Applied in the other direction it says that a family written with a parameter is written uniquely: two right multiplications that agree are the same right multiplication, so the parameter in a display can be read off and cannot be silently changed. Both jobs are used below.

**Proposition (a left multiplication is a right one only at the centre).** $L_{\tilde Q}=R_{\tilde Q}$ exactly when $\tilde Q$ commutes with every element of $\mathbb{B}$, and the elements with that property are the scalar multiples of the unit.

*Proof.* The equality $L_{\tilde Q}=R_{\tilde Q}$ says $\tilde QX=X\tilde Q$ for every $X$, which is the definition of commuting with everything. For the second claim, let $\tilde Q=q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$ commute with every element; it is enough to test the three vector units. From $\tilde Q\vec e_x=\vec e_x\tilde Q$ the two sides are

$$
q_te_t\vec e_x+q_x\vec e_x^2+q_y\vec e_y\vec e_x+q_z\vec e_z\vec e_x
=q_te_t\vec e_x+q_x\vec e_x^2+q_y\vec e_x\vec e_y+q_z\vec e_x\vec e_z,
$$

and cancelling the common terms leaves $q_y\bigl(\vec e_y\vec e_x-\vec e_x\vec e_y\bigr)+q_z\bigl(\vec e_z\vec e_x-\vec e_x\vec e_z\bigr)=0$, that is $-2q_y\vec e_z+2q_z\vec e_y=0$, so $q_y=q_z=0$. The same test with $\vec e_y$ gives $q_x=0$. Hence $\tilde Q=q_te_t$.

So the two families meet only over the centre, and there the left multiplication and the right multiplication are one operator, the multiplication by a scalar. Everywhere else they are different operators, and the question of the article is how far apart they are.

## The Quaternion Conjugation

**Definition.** The **quaternion conjugation** is the map

$$
\natural\bigl(q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z\bigr)
=q_te_t-q_x\vec e_x-q_y\vec e_y-q_z\vec e_z .
$$

It fixes the scalar part and negates the vector part. It is $\mathbb{C}$-linear by construction, since the coefficients are untouched.

**Proposition (the two properties).**

1. $\natural$ is an involution: $\natural\bigl(\natural(X)\bigr)=X$ for every $X$.
2. $\natural$ reverses every product: $\natural(XY)=\natural(Y)\natural(X)$ for all $X,Y$.

*Proof.* The first property is immediate, because negating the vector part twice restores it. For the second, write $\varepsilon_t=1$ and $\varepsilon_x=\varepsilon_y=\varepsilon_z=-1$, so that $\natural(e_\mu)=\varepsilon_\mu e_\mu$ on the four units. Every product of two units is again a unit up to a sign, and it is enough to check the three possible shapes, because both sides of the identity are $\mathbb{C}$-bilinear in the pair and a bilinear identity that holds on the units holds everywhere.

- If one factor is the unit, say $e_t e_\nu=e_\nu$, then $\natural(e_te_\nu)=\varepsilon_\nu e_\nu$ and $\natural(e_\nu)\natural(e_t)=\varepsilon_\nu e_\nu e_t=\varepsilon_\nu e_\nu$; they agree, and the same holds with the factors exchanged.
- If the two factors are the same vector unit, $e_j^2=-e_t$, then $\natural(e_je_j)=-e_t$ and $\natural(e_j)\natural(e_j)=(-\vec e_j)(-\vec e_j)=e_je_j=-e_t$; they agree.
- If the two factors are distinct vector units, $e_je_k=\epsilon e_l$ with $\epsilon=\pm1$ and $l$ the third vector index, then $\natural(e_je_k)=\epsilon\,\varepsilon_l e_l=-\epsilon e_l$, because $l$ is a vector index; and $\natural(e_k)\natural(e_j)=(-\vec e_k)(-\vec e_j)=e_ke_j=-\epsilon e_l$, because distinct vector units anticommute. They agree.

In every case the two sides coincide, so the identity holds on the units and therefore on all pairs.

The two properties together say that $\natural$ is a bijection of the algebra with $\natural^{-1}=\natural$, and that it reverses the order of every product. The reversal is the whole engine of the article, and it is worth stating in words what reversal does to a product: it moves the factor that stood on the left to the right, and the factor that stood on the right to the left, and it applies the map to each of them on the way.

## The Computation

The symmetry we want is $\natural$, and the operator we want to understand is the composite $\natural L_{\tilde Q}\natural$. It is written with $\natural$ on both sides of the left multiplication because conjugating an operator $F$ means forming $\natural F\natural^{-1}$, and here $\natural^{-1}=\natural$. So the composite acts in three steps: conjugate the input, multiply by $\tilde Q$ on the left, conjugate the result.

Let $X$ be an arbitrary element and compute. Reading the composite from the inside out,

$$
\bigl(\natural L_{\tilde Q}\natural\bigr)(X)
=\natural\Bigl(L_{\tilde Q}\bigl(\natural(X)\bigr)\Bigr)
=\natural\Bigl(\tilde Q\,\natural(X)\Bigr).
$$

The first equality is the definition of composition, and the second is the definition of the left multiplication, which multiplies its parameter on the left of its argument. The argument of the outer $\natural$ is now a product of two elements, namely $\tilde Q$ and $\natural(X)$. Apply the reversal property to that product, and the two factors change places while $\natural$ is applied to each:

$$
\natural\Bigl(\tilde Q\,\natural(X)\Bigr)
=\natural\bigl(\natural(X)\bigr)\,\natural(\tilde Q)
=X\,\natural(\tilde Q).
$$

The last equality is the involution property, which returns $\natural(X)$ to $X$. Combining the two displays, and recalling that right multiplication by an element is the operator that multiplies that element on the right of its argument,

$$
\bigl(\natural L_{\tilde Q}\natural\bigr)(X)=X\,\natural(\tilde Q)=R_{\natural(\tilde Q)}(X).
$$

The element $X$ was arbitrary, so the composite and the right multiplication agree as operators.

This is the whole proof, and it used three things and no more: that $\natural$ is $\mathbb{C}$-linear, so that the composite is defined and composition may be read as above; that $\natural$ is an involution; and that $\natural$ reverses products. Nothing was assumed about $\tilde Q$.

## The Identity

The computation of the preceding section has a single conclusion, and it is the theorem of the article.

**Theorem (conjugation by the quaternion conjugation).** For every element $\tilde Q$ of the algebra,

$$
\natural\,L_{\tilde Q}\,\natural=R_{\natural(\tilde Q)}=R_{\tilde Q^{\natural}} .
$$

Equivalently, for every $X$,

$$
\natural\bigl(\tilde Q\,\natural(X)\bigr)=X\,\tilde Q^{\natural}.
$$

*Proof.* The computation of §*The Computation* establishes the second display for an arbitrary $X$, and the first display is the same statement written with the notation of right multiplication.

Three readings of the theorem are worth separating, because they answer three different questions.

**Which side.** The composite lands in the right family. Its parameter is multiplied on the right of the input, and that is why the conjugation is described as a transposition of the two sides: it moves a multiplication from the left side of its argument to the right side.

**Which parameter.** The parameter of the resulting right multiplication is $\natural(\tilde Q)$ and not $\tilde Q$. It is not chosen; it is produced. In the middle step of the computation the reversal moved $\tilde Q$ across the other factor, and the outer $\natural$ applied the conjugation to it while it was there. An element that is moved by a reversal is carried, and $\natural$ is what carries it.

**How sharp.** No other parameter gives the same operator, because a right multiplication determines its parameter at the unit. So the theorem is not one way of writing the right multiplication by $\natural(\tilde Q)$ among many; it is the only way of writing it as a conjugate of a left multiplication, and the element that must be conjugated on the left is forced.

**Consistency at the unit.** The cheapest check is to evaluate both sides at $e_t$, which is what the proposition of §*The Two Families* recommends. On the right, $R_{\natural(\tilde Q)}(e_t)=\natural(\tilde Q)$. On the left, the composite sends $e_t$ first to $\natural(e_t)=e_t$, then to $\tilde Qe_t=\tilde Q$, then to $\natural(\tilde Q)$. The two agree, as they must.

## The Same Identity Read the Other Way

The theorem holds for every element, so it holds for the element $\natural(\tilde Q)$. Applying it there, and using the involution property twice,

$$
\natural\,L_{\natural(\tilde Q)}\,\natural
=R_{\natural(\natural(\tilde Q))}
=R_{\tilde Q}.
$$

Since $L_{\natural(\tilde Q)}=L_{\tilde Q^{\natural}}$, this reads

$$
\natural\,L_{\tilde Q^{\natural}}\,\natural=R_{\tilde Q}.
$$

The two displays are one theorem read at two elements. The first says what the conjugation does to the left multiplication by an element: it produces the right multiplication by the image of that element. The second says the same thing from the side of the right family: to obtain the right multiplication by $\tilde Q$ as a conjugate of a left multiplication, conjugate the left multiplication by $\tilde Q^{\natural}$. Neither display is a shorthand, and neither restricts $\tilde Q$.

The second display is the form the article is named after, because its left-hand side names the operator and its right-hand side names the parameter without a conjugation. The first display is the form that explains why the parameter moves. Both are used below, and the choice between them is a choice of what to make visible.

## Why the Sides Exchange

The theorem was proved by computing, but the computation contains one step that decides everything, and the article would be incomplete without isolating it. Take any bijection $\Theta$ of the algebra that reverses products, $\Theta(XY)=\Theta(Y)\Theta(X)$ for all $X,Y$, and ask what its conjugation does to a left multiplication. The same three steps give

$$
\bigl(\Theta L_{\tilde Q}\Theta^{-1}\bigr)(X)
=\Theta\Bigl(\tilde Q\,\Theta^{-1}(X)\Bigr)
=\Theta\bigl(\Theta^{-1}(X)\bigr)\,\Theta(\tilde Q)
=X\,\Theta(\tilde Q)
=R_{\Theta(\tilde Q)}(X),
$$

so that $\Theta L_{\tilde Q}\Theta^{-1}=R_{\Theta(\tilde Q)}$. Now take instead a bijection $\sigma$ that **preserves** products, $\sigma(XY)=\sigma(X)\sigma(Y)$, and run the same three steps:

$$
\bigl(\sigma L_{\tilde Q}\sigma^{-1}\bigr)(X)
=\sigma\Bigl(\tilde Q\,\sigma^{-1}(X)\Bigr)
=\sigma(\tilde Q)\,\sigma\bigl(\sigma^{-1}(X)\bigr)
=\sigma(\tilde Q)\,X
=L_{\sigma(\tilde Q)}(X).
$$

The contrast is exact. In the first computation the two factors change places, so the parameter ends on the right of the input and the operator becomes a right multiplication. In the second computation the two factors keep their places, so the parameter stays on the left and the operator remains a left multiplication. The exchange of the sides is precisely the reversal of the two factors, and nothing else in the computation can produce it.

That observation can be turned around, and the result is the sharpest statement of the section.

**Proposition (exchange forces reversal).** Let $\Theta$ be a bijection of the algebra such that $\Theta L_{\tilde Q}\Theta^{-1}=R_{\Theta(\tilde Q)}$ for every $\tilde Q$. Then $\Theta$ reverses products.

*Proof.* Let $X$ be arbitrary and write $Y=\Theta^{-1}(X)$, so that $X=\Theta(Y)$. Evaluating the hypothesis at $X$,

$$
\Theta\bigl(\tilde Q\,Y\bigr)
=\bigl(\Theta L_{\tilde Q}\Theta^{-1}\bigr)(X)
=R_{\Theta(\tilde Q)}(X)
=X\,\Theta(\tilde Q)
=\Theta(Y)\,\Theta(\tilde Q).
$$

Since this holds for all $\tilde Q$ and $Y$, the map $\Theta$ reverses products.

Together with the computation above, the proposition says that the bijections which transpose the two families are exactly the bijections which reverse products. There are therefore two descriptions of one class of maps, and the class is not empty: $\natural$ is a member.

The proposition also settles a question of principle. A bijection that exchanges the families carries the parameter to its image, by the first computation; and it must reverse products, by the proposition. So no bijection can exchange the families and leave the parameter in place. The equation that keeps the parameter is not merely unproved here; it is impossible for any symmetry of this kind, and the next section shows the impossibility directly, on one element.

## The Equation the Notation Invites

The theorem writes the right multiplication by $\natural(\tilde Q)$ as a conjugated left multiplication. Read quickly, and with the muscle memory of the transpose, it suggests the simpler display

$$
R_{\tilde Q}=\natural\,L_{\tilde Q}\,\natural,
$$

in which the same element stands on both sides. That display is false, and the cheapest way to see it is to evaluate at the unit, which reads a parameter directly by the proposition of §*The Two Families*.

**Proposition (when the display with one parameter holds).** $R_{\tilde Q}=\natural L_{\tilde Q}\natural$ exactly when $\tilde Q$ is a scalar multiple of the unit.

*Proof.* Suppose the two operators are equal and evaluate at $e_t$. The right multiplication gives $e_t\tilde Q=\tilde Q$. The composite, by the computation of §*The Computation*, gives $e_t\natural(\tilde Q)=\natural(\tilde Q)$. Hence $\tilde Q=\natural(\tilde Q)$, that is

$$
q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z=q_te_t-q_x\vec e_x-q_y\vec e_y-q_z\vec e_z,
$$

so $q_x=q_y=q_z=0$ and $\tilde Q=q_te_t$. Conversely, if $\tilde Q=q_te_t$ then $\natural(\tilde Q)=\tilde Q$, and the theorem gives $\natural L_{\tilde Q}\natural=R_{\natural(\tilde Q)}=R_{\tilde Q}$.

**Proposition (the size of the failure).** For every element, the two operators differ by the right multiplication by twice the vector part:

$$
R_{\tilde Q}-\natural\,L_{\tilde Q}\,\natural=R_{2\vec Q},
\qquad\text{where } \vec Q=\tilde Q-q_te_t .
$$

*Proof.* The theorem gives $\natural L_{\tilde Q}\natural=R_{\natural(\tilde Q)}$, and the right multiplication is additive in its parameter, $R_{\tilde P}+R_{\tilde P'}=R_{\tilde P+\tilde P'}$, because the product is additive. Hence the difference is $R_{\tilde Q-\natural(\tilde Q)}$, and $\tilde Q-\natural(\tilde Q)=2\vec Q$.

The proposition is the honest form of the failure. The false display is not wrong by an arbitrary amount: it is wrong by a right multiplication, and the parameter of that right multiplication is twice the vector part, which vanishes exactly at the centre and nowhere else.

**Example.** Take $\tilde Q=e_t+2\vec e_x$, so that $\natural(\tilde Q)=e_t-2\vec e_x$ and $\tilde Q-\natural(\tilde Q)=4\vec e_x$. On the input $e_t$ the right multiplication gives $e_t+2\vec e_x$ and the composite gives $e_t-2\vec e_x$; the gap is $4\vec e_x$. The two operators disagree on the unit alone, before any other input is tried.

**Proposition (which parameter does work).** Fix $\tilde Q$ and let $\tilde P$ vary. Then $\natural L_{\tilde P}\natural=R_{\tilde Q}$ exactly when $\tilde P=\natural(\tilde Q)$.

*Proof.* By the theorem the left side is $R_{\natural(\tilde P)}$, and by the unit this equals $R_{\tilde Q}$ exactly when $\natural(\tilde P)=\tilde Q$. Applying the involution gives $\tilde P=\natural(\tilde Q)$.

So the false display is not repaired by any choice of a different reading; it is repaired by moving the parameter through the conjugation, and the element that must stand under $L$ is the image of the element that stands under $R$. That is the content of the amended display $\natural L_{\tilde Q^{\natural}}\natural=R_{\tilde Q}$.

## The Genuine Transposition

The article calls the conjugation a transposition of the two sides. The name is borrowed, and it should be earned, because the algebra also carries a genuine transposition: the adjoint of its plain bilinear form. The two operations move a multiplication to the other side, and comparing them shows exactly what each one does to the parameter.

**The plain form.** Put

$$
\langle X,Y\rangle=\mathrm{Sc}(XY),
$$

the scalar part of the product. It is symmetric, because the scalar part is invariant under the exchange of the two factors. It is non-degenerate, because the four units read the four coefficients: for $X=x_te_t+x_x\vec e_x+x_y\vec e_y+x_z\vec e_z$ one has $\langle X,e_t\rangle=x_t$ and $\langle X,\vec e_k\rangle=-x_k$ for the three vector units. So an element whose pairing with every element vanishes is the zero element.

**Definition (the transpose).** For a $\mathbb{C}$-linear operator $F$ of the algebra, the **transpose** for the plain form is the operator $F^{\approx}$ with

$$
\bigl\langle F(X),Y\bigr\rangle=\bigl\langle X,F^{\approx}(Y)\bigr\rangle
\qquad\text{for all } X,Y .
$$

It exists and it is unique: the relation determines $F^{\approx}(Y)$ by its pairings with all elements, and the form is non-degenerate. The corpus names this operator the **associate**, and the mark $\approx$ is the one used for it.

**Proposition (the transpose exchanges the sides and keeps the parameter).**

$$
L_{\tilde Q}^{\approx}=R_{\tilde Q},
\qquad\qquad
R_{\tilde Q}^{\approx}=L_{\tilde Q}.
$$

*Proof.* By the definition of the transpose, the left side of the defining relation for $F=L_{\tilde Q}$ is $\bigl\langle \tilde QX,Y\bigr\rangle=\mathrm{Sc}\bigl(\tilde QXY\bigr)$. The scalar part is invariant under the cyclic permutation of the three factors, so

$$
\mathrm{Sc}\bigl(\tilde QXY\bigr)=\mathrm{Sc}\bigl(XY\tilde Q\bigr)=\bigl\langle X,R_{\tilde Q}(Y)\bigr\rangle,
$$

which is the defining relation for $R_{\tilde Q}$; the transpose is unique, so $L_{\tilde Q}^{\approx}=R_{\tilde Q}$. The second identity is the same computation with the cyclic permutation run the other way.

The comparison is now immediate, and it is the point of the section. The two operators $F\mapsto F^{\approx}$ and $F\mapsto\natural F\natural$ both exchange the two families, and they both send $L_{\tilde Q}$ to a right multiplication by $\tilde Q$:

$$
L_{\tilde Q}^{\approx}=R_{\tilde Q}=\natural\,L_{\tilde Q^{\natural}}\,\natural .
$$

They agree as operators and they differ in what they do to the parameter. The transpose keeps the parameter of the left multiplication and reaches the right family; the conjugation carries the parameter and reaches the right family; and the two are reconciled only by giving the conjugation the parameter $\tilde Q^{\natural}$, which is the parameter that the transpose would have used had it conjugated. An article that writes $R_{\tilde Q}=\natural L_{\tilde Q}\natural$ takes the parameter from the transpose and the map from the conjugation, and loses the difference between them.

## Consequences

Two facts follow at once from the theorem, and both are used elsewhere in the corpus.

**The two-sided family is generated by the left family and the conjugation.** By the theorem applied to $\tilde P$,

$$
L_{\tilde Q}R_{\tilde P}=L_{\tilde Q}\,\natural\,L_{\tilde P^{\natural}}\,\natural .
$$

*Proof.* Compose the theorem, in the form $R_{\tilde P}=\natural L_{\tilde P^{\natural}}\natural$, on the left with $L_{\tilde Q}$.

So a two-sided operator, which naively requires two different kinds of multiplication, is a product of three left multiplications separated by conjugations. The right family adds nothing new to the left family except the one symmetry $\natural$.

**The anti-representation of the right family is the reversal of $\natural$.** The law $R_{\tilde Q}R_{\tilde P}=R_{\tilde P\tilde Q}$ was proved from associativity in §*The Two Families*. It can also be read as the reversal property in disguise: conjugating the law of the left family gives the law of the right family with the parameters exchanged, because $\natural\bigl(\tilde Q\tilde P\bigr)=\natural(\tilde P)\natural(\tilde Q)$. The two proofs are the same proof seen on the two families, which is what the theorem asserts.

## Summary

For every element $\tilde Q$, conjugating the left multiplication by $\tilde Q$ with the quaternion conjugation gives the right multiplication by $\natural(\tilde Q)$, and conjugating the left multiplication by $\natural(\tilde Q)$ gives the right multiplication by $\tilde Q$: the two displays $\natural L_{\tilde Q}\natural=R_{\natural(\tilde Q)}$ and $\natural L_{\tilde Q^{\natural}}\natural=R_{\tilde Q}$ are one theorem read at two elements.

The theorem was obtained by computing the composite on an arbitrary element, and the computation shows why the parameter moves. The composite conjugates the input, multiplies by $\tilde Q$ on the left, and conjugates the result; the outer conjugation meets the product $\tilde Q\natural(X)$, reverses it, and therefore moves $\tilde Q$ to the right while applying $\natural$ to it. The parameter lands on the right of the input, which is what makes the operator a right multiplication, and it lands there as $\natural(\tilde Q)$, which is what makes the display exact for every element rather than only at the centre.

The display $R_{\tilde Q}=\natural L_{\tilde Q}\natural$, with one element on both sides, is exact only when that element is a scalar multiple of the unit, and its failure is quantitative: the two operators differ by the right multiplication by twice the vector part. The element that does work is $\natural(\tilde Q)$, and it is unique, because a right multiplication determines its parameter at the unit.

The name of the article is earned by comparison with the genuine transpose, the associate of the plain form, which exchanges the two families and keeps the parameter. The associate and the conjugation reach the same operator $R_{\tilde Q}$ from the same left multiplication, and they differ exactly in whether the parameter is carried through $\natural$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{\tilde Q}(X)=\tilde QX$, $R_{\tilde Q}(X)=X\tilde Q$ | the left and the right multiplication by $\tilde Q$ |
| $L_{\tilde Q}L_{\tilde P}=L_{\tilde Q\tilde P}$, $R_{\tilde Q}R_{\tilde P}=R_{\tilde P\tilde Q}$, $L_{\tilde Q}R_{\tilde P}=R_{\tilde P}L_{\tilde Q}$ | the three laws, from associativity alone |
| $L_{\tilde Q}(e_t)=\tilde Q=R_{\tilde Q}(e_t)$ | the unit reads the parameter, and separates two operators |
| $\natural(\tilde Q)=q_te_t-q_x\vec e_x-q_y\vec e_y-q_z\vec e_z$ | the quaternion conjugation: involutive and antimultiplicative |
| $\natural L_{\tilde Q}\natural=R_{\natural(\tilde Q)}$ | the theorem: the parameter is carried to its image |
| $\natural L_{\tilde Q^{\natural}}\natural=R_{\tilde Q}$ | the same theorem at the element $\natural(\tilde Q)$ |
| $R_{\tilde Q}-\natural L_{\tilde Q}\natural=R_{2\vec Q}$ | the failure of the display with one parameter, measured |
| $\langle X,Y\rangle=\mathrm{Sc}(XY)$ | the plain bilinear form, symmetric and non-degenerate |
| $L_{\tilde Q}^{\approx}=R_{\tilde Q}$, $R_{\tilde Q}^{\approx}=L_{\tilde Q}$ | the associate, the transpose for the plain form, which keeps the parameter |
| $L_{\tilde Q}R_{\tilde P}=L_{\tilde Q}\natural L_{\tilde P^{\natural}}\natural$ | a two-sided operator as three left multiplications |

## Further Reading

- [Operators Acting on One Side](operators-acting-on-one-side.html), for the two families, their images, their commutants and the laws used here
- [Operators Acting on Two Sides](operators-acting-on-two-sides.html), for the products $L_{\tilde Q}R_{\tilde P}$, their adjoints and their isometries
- [Adjoint Pair of $L$ and $R$ Operators](adjoint-pair-of-l-and-r-operators.html), for the associate $L_{\tilde Q}^{\approx}=R_{\tilde Q}$ as the first of the four adjoints, and for the other three
- [Operator Chirality on the Biquaternion Algebra](operator-chirality-on-the-biquaternion-algebra.html), for the exchange of the sides as the corpus records it, and for its difference from the swap of the two slots
- [The Hermitian Pair of Operators Acting on One Side](the-hermitian-pair-of-operators-acting-on-one-side.html), for the same transposition with $\ast$ in place of $\natural$, and for the pair whose adjoints stay on one side
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for the generation of the endomorphism algebra by the two families
- [The Group of Involutions](the-group-of-involutions.html), for $\natural$, $\ast$ and the coefficient conjugation, their linearity and their grades
- [Bilinear Forms](bilinear-forms.html), §*Isometries*, for the transpose of a bilinear form, of which the associate is the biquaternion case
