# __The Transposition of the Two Sides__

## Introduction

Every element of the biquaternion algebra acts on the algebra in two ways, by multiplication on the left and by multiplication on the right, and for a general element the two actions are different operators. They are not, however, independent. The subject of this article is the pair of identities that converts one action into the other:

$$
L_{\tilde Q}=\natural\,R_{\natural(\tilde Q)}\,\natural,
\qquad\qquad
R_{\tilde Q}=\natural\,L_{\natural(\tilde Q)}\,\natural .
$$

In one sentence: every right multiplication is a conjugated left multiplication, and every left multiplication is a conjugated right multiplication. The second display says that a right multiplication is a left multiplication, conjugated on both sides by the quaternion conjugation: a reader who is given an equation written with right multiplications may rewrite it with left multiplications only, at the price of two conjugations for each converted operator and of the passage of the parameter through $\natural$. The first display says the same thing in the other direction, for a left multiplication replaced by a right one. The parameter is not free in either conversion. It is carried, and the carried value is $\natural(\tilde Q)$ and not $\tilde Q$.

The article proves the pair before it uses it. The two families and their laws come first, because every later statement is a statement about them. The quaternion conjugation comes next, with a proof that it reverses products, since that single property is the whole mechanism. The two displays are then proved one at a time, each by computing the composite on an arbitrary element, so that the reader sees where the carried parameter comes from rather than being told what it is. Once both are proved, they are recognised as two halves of one involution of the operator algebra, and that recognition is what makes the conversion a tool: the involution preserves products, so an equation may be transformed on both sides and remains equivalent.

The remaining sections put the tool to work. The rewriting rules are collected, a couple of one-sided operators is brought to a single side, and the law of the right family is re-derived from the law of the left family by the conversion alone, which shows the two laws are one law. Then comes the list of displays that resemble the pair and are false, with the exact size of their failure, because a conversion rule that is used carelessly is worse than none. Finally the mechanism is isolated, and the sense in which the operation deserves the name of a transposition is settled against the genuine transpose of the plain bilinear form.

No step uses a basis, a matrix, a topology, a distance or a limit. Every object is an operator on the algebra, and every proof is a computation on an arbitrary element.

## The Two Families

**Definition.** For $\tilde Q$ in $\mathbb{B}$, the **left multiplication** and the **right multiplication** by $\tilde Q$ are the operators

$$
L_{\tilde Q}(X)=\tilde Q X,
\qquad\qquad
R_{\tilde Q}(X)=X\tilde Q,
$$

defined for every $X$ in $\mathbb{B}$. Both are $\mathbb{C}$-linear, because the product of the algebra is bilinear over $\mathbb{C}$. The element $\tilde Q$ is called the **parameter** of the operator.

**Proposition (the three laws).** For all elements,

$$
L_{\tilde Q}L_{\tilde P}=L_{\tilde Q\tilde P},
\qquad
R_{\tilde Q}R_{\tilde P}=R_{\tilde P\tilde Q},
\qquad
L_{\tilde Q}R_{\tilde P}=R_{\tilde P}L_{\tilde Q}.
$$

*Proof.* Let $X$ be arbitrary. The only ingredient is the associativity of the product.

$$
L_{\tilde Q}\bigl(L_{\tilde P}(X)\bigr)=\tilde Q\bigl(\tilde PX\bigr)=\bigl(\tilde Q\tilde P\bigr)X=L_{\tilde Q\tilde P}(X),
$$
$$
R_{\tilde Q}\bigl(R_{\tilde P}(X)\bigr)=\bigl(X\tilde P\bigr)\tilde Q=X\bigl(\tilde P\tilde Q\bigr)=R_{\tilde P\tilde Q}(X),
$$
$$
L_{\tilde Q}\bigl(R_{\tilde P}(X)\bigr)=\tilde QX\tilde P=R_{\tilde P}\bigl(L_{\tilde Q}(X)\bigr).
$$

Since $X$ was arbitrary, the operators agree.

The second law says that the map $\tilde Q\mapsto R_{\tilde Q}$ exchanges the order of the parameters, and such a map is called an **anti-representation**; the first says that $\tilde Q\mapsto L_{\tilde Q}$ preserves it. The third says that the two families commute element by element, so a product of one operator from each may be written with the factors in either order.

**Proposition (the unit reads the parameter).** Let $e_t$ be the unit of the algebra. Then

$$
L_{\tilde Q}(e_t)=\tilde Q=R_{\tilde Q}(e_t),
$$

and consequently $L_{\tilde Q}=L_{\tilde P}$ exactly when $\tilde Q=\tilde P$, and $R_{\tilde Q}=R_{\tilde P}$ exactly when $\tilde Q=\tilde P$.

*Proof.* Multiplying by the unit changes nothing. If two such operators are equal, their values at $e_t$ are equal, which gives the equality of the parameters; if the parameters are equal, the operators are equal by definition.

This proposition is used twice in every section that follows. Applied to an identity between operators it turns that identity into an identity between parameters, because the unit evaluates a parameter directly. Applied in the other direction it says that a parameter written in a display is written uniquely, so it cannot be changed in silence.

**Proposition (a left multiplication is a right one only at the centre).** $L_{\tilde Q}=R_{\tilde Q}$ exactly when $\tilde Q$ commutes with every element, and those elements are the scalar multiples of the unit.

*Proof.* The equality says $\tilde QX=X\tilde Q$ for every $X$, which is the definition of commuting with everything. For the second claim, let $\tilde Q=q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$ commute with every element; it is enough to test the three vector units, because the scalar unit gives nothing. From $\tilde Q\vec e_x=\vec e_x\tilde Q$ the two sides are

$$
q_te_t\vec e_x+q_x\vec e_x^2+q_y\vec e_y\vec e_x+q_z\vec e_z\vec e_x
=q_te_t\vec e_x+q_x\vec e_x^2+q_y\vec e_x\vec e_y+q_z\vec e_x\vec e_z,
$$

and cancelling the common terms leaves $q_y\bigl(\vec e_y\vec e_x-\vec e_x\vec e_y\bigr)+q_z\bigl(\vec e_z\vec e_x-\vec e_x\vec e_z\bigr)=0$. Distinct vector units anticommute, so the left side is $-2q_y\vec e_z+2q_z\vec e_y$, which vanishes only for $q_y=q_z=0$. The same test with $\vec e_y$ gives $q_x=0$, hence $\tilde Q=q_te_t$.

So the two families meet only over the centre, and there both are the multiplication by a scalar. Everywhere else they are different operators, and the pair of the introduction is the exact measure of how they differ.

## The Quaternion Conjugation

**Definition.** The **quaternion conjugation** is the map

$$
\natural\bigl(q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z\bigr)
=q_te_t-q_x\vec e_x-q_y\vec e_y-q_z\vec e_z .
$$

It fixes the scalar part and negates the vector part, and it is $\mathbb{C}$-linear by construction, the coefficients being untouched.

**Proposition (the two properties).**

1. $\natural$ is an involution: $\natural\bigl(\natural(X)\bigr)=X$ for every $X$.
2. $\natural$ reverses every product: $\natural(XY)=\natural(Y)\natural(X)$ for all $X,Y$.

*Proof.* The first property is immediate, negating the vector part twice restoring it. For the second, put $\varepsilon_t=1$ and $\varepsilon_x=\varepsilon_y=\varepsilon_z=-1$, so that $\natural(e_\mu)=\varepsilon_\mu e_\mu$ on the four units. Both sides of the identity to be proved are $\mathbb{C}$-bilinear in the pair $(X,Y)$, so it is enough to check the products of two units, and there are three shapes.

- If one factor is the unit, say $e_te_\nu=e_\nu$, then $\natural(e_te_\nu)=\varepsilon_\nu e_\nu$ while $\natural(e_\nu)\natural(e_t)=\varepsilon_\nu e_\nu e_t=\varepsilon_\nu e_\nu$; the two agree, and exchanging the factors gives the same.
- If the two factors are the same vector unit, $e_je_j=-e_t$, then $\natural(e_je_j)=-e_t$ while $\natural(e_j)\natural(e_j)=\vec e_j\vec e_j=e_je_j=-e_t$; the two agree.
- If the two factors are distinct vector units, $e_je_k=\epsilon e_l$ with $\epsilon=\pm1$ and $l$ the third vector index, then $\natural(e_je_k)=\epsilon\,\varepsilon_l e_l=-\epsilon e_l$ because $l$ is a vector index; and $\natural(e_k)\natural(e_j)=\vec e_k\vec e_j=e_ke_j=-\epsilon e_l$ because distinct vector units anticommute. The two agree.

The identity holds on the units and both sides are bilinear, so it holds on all pairs.

The two properties together say that $\natural$ is a bijection with $\natural^{-1}=\natural$, and that it reverses the order of every product. Reversal is worth restating in words, because everything later is an application of it: it moves the factor that stood on the left to the right and the factor that stood on the right to the left, and it applies the map to each of them on the way.

## The First Identity

**Theorem.** For every element $\tilde Q$ of the algebra,

$$
\natural\,L_{\tilde Q}\,\natural=R_{\natural(\tilde Q)} .
$$

*Proof.* The composite is written with $\natural$ on both sides of the left multiplication because conjugating an operator $F$ means forming $\natural F\natural^{-1}$, and here $\natural^{-1}=\natural$. So the composite acts in three steps: conjugate the input, multiply the result by $\tilde Q$ on the left, conjugate again. Let $X$ be an arbitrary element and read the composite from the inside out:

$$
\bigl(\natural L_{\tilde Q}\natural\bigr)(X)
=\natural\Bigl(L_{\tilde Q}\bigl(\natural(X)\bigr)\Bigr)
=\natural\Bigl(\tilde Q\,\natural(X)\Bigr).
$$

The first equality is the definition of composition and the second is the definition of the left multiplication, which multiplies its parameter on the left of its argument.

The argument of the outer $\natural$ is now a product of two elements, namely $\tilde Q$ and $\natural(X)$. Apply the reversal property of §*The Quaternion Conjugation* to that product. The two factors change places and $\natural$ is applied to each:

$$
\natural\Bigl(\tilde Q\,\natural(X)\Bigr)
=\natural\bigl(\natural(X)\bigr)\,\natural(\tilde Q)
=X\,\natural(\tilde Q).
$$

The last equality is the involution property, which returns $\natural(X)$ to $X$. Right multiplication by an element is the operator that multiplies that element on the right of its argument, so the two displays together give

$$
\bigl(\natural L_{\tilde Q}\natural\bigr)(X)=X\,\natural(\tilde Q)=R_{\natural(\tilde Q)}(X).
$$

The element $X$ was arbitrary, so the composite and the right multiplication agree as operators.

Three things were used and no more: that $\natural$ is $\mathbb{C}$-linear, so that the composite is defined; that $\natural$ is an involution; and that $\natural$ reverses products. Nothing was assumed about $\tilde Q$, and no basis was chosen.

**The middle step, slowly.** The one step that decides the identity is the application of the reversal, and it is worth saying exactly what it does to the two factors. Before the step, the product stands as $\tilde Q$ on the left of $\natural(X)$. After the step, $\natural(X)$ stands on the left of $\natural(\tilde Q)$. So the factor $\tilde Q$ has crossed from the left of the other factor to its right, and while crossing it has been put through $\natural$. The parameter therefore ends on the right of the input, which is what makes the result a right multiplication, and it ends there as $\natural(\tilde Q)$, which is what makes the display exact for every element. Both facts come from the same step, and neither can be had without the other.

**Check at the unit.** Evaluate both sides at $e_t$. The composite sends $e_t$ first to $\natural(e_t)=e_t$, then to $\tilde Qe_t=\tilde Q$, then to $\natural(\tilde Q)$; the right multiplication sends $e_t$ to $\natural(\tilde Q)$. The two agree, as they must.

## The Second Identity

**Theorem.** For every element $\tilde Q$ of the algebra,

$$
\natural\,R_{\tilde Q}\,\natural=L_{\natural(\tilde Q)} .
$$

*Proof.* The composite again conjugates the input, multiplies by $\tilde Q$ on the right, and conjugates the result. For an arbitrary $X$,

$$
\bigl(\natural R_{\tilde Q}\natural\bigr)(X)
=\natural\Bigl(R_{\tilde Q}\bigl(\natural(X)\bigr)\Bigr)
=\natural\Bigl(\natural(X)\,\tilde Q\Bigr).
$$

The argument of the outer $\natural$ is now the product of $\natural(X)$ and $\tilde Q$. Reversal applies to it, and this time the two factors are found in the other order, so $\tilde Q$ moves to the left:

$$
\natural\Bigl(\natural(X)\,\tilde Q\Bigr)
=\natural(\tilde Q)\,\natural\bigl(\natural(X)\bigr)
=\natural(\tilde Q)\,X=L_{\natural(\tilde Q)}(X).
$$

Since $X$ was arbitrary, the composite and the left multiplication agree.

The two proofs are the same proof with the factors of one product written in the opposite order, and that is the whole difference between the two families. In the first proof the parameter stood on the left of the other factor and was carried to the right; in the second it stood on the right and was carried to the left. In both cases the reversal carried it across, and in both cases it arrived as its image.

**Check at the unit.** The composite sends $e_t$ to $\natural(\tilde Q)$, and so does $L_{\natural(\tilde Q)}$.

## The Symmetric Pair

The two theorems of the two preceding sections say what the conjugation does to each family. Both are stated with the conjugation on the left of the display and the family on the right. Solving each for the family gives the pair of the introduction, and the derivation is a single substitution in each case.

**Corollary (the pair).** For every element $\tilde Q$,

$$
L_{\tilde Q}=\natural\,R_{\natural(\tilde Q)}\,\natural,
\qquad\qquad
R_{\tilde Q}=\natural\,L_{\natural(\tilde Q)}\,\natural .
$$

*Proof.* For the first display, apply the second theorem to the element $\natural(\tilde Q)$ in place of $\tilde Q$: it gives $\natural R_{\natural(\tilde Q)}\natural=L_{\natural(\natural(\tilde Q))}=L_{\tilde Q}$, because $\natural$ is an involution. For the second display, apply the first theorem to the element $\natural(\tilde Q)$: it gives $\natural L_{\natural(\tilde Q)}\natural=R_{\natural(\natural(\tilde Q))}=R_{\tilde Q}$.

The corollary is the form in which the pair is used, and the theorems are the form in which it is proved. The difference is worth keeping in view: the theorems say what conjugation does to a family, and the corollary says that each family is the conjugate of the other. The corollary is what one applies to an equation, because it replaces one family by the other without leaving a conjugation outstanding.

**The pair is symmetric under the exchange of the two families.** The second display becomes the first if $L$ and $R$ are exchanged throughout, and the first becomes the second in the same way. That exchange is not a notational courtesy; it is an operation on operators, and it is the subject of the next section.

## The Single Involution

Both displays of the pair are statements about one map of the operator algebra, and naming that map makes the pair look like what it is: one involution with two-element orbits.

**Definition.** For a $\mathbb{C}$-linear operator $F$ of $\mathbb{B}$, put

$$
\mathsf K(F)=\natural\,F\,\natural .
$$

**Proposition (the four properties of $\mathsf K$).**

1. $\mathsf K$ is $\mathbb{C}$-linear.
2. $\mathsf K$ is an involution: $\mathsf K\bigl(\mathsf K(F)\bigr)=F$.
3. $\mathsf K$ preserves products: $\mathsf K(F)\mathsf K(G)=\mathsf K(FG)$.
4. $\mathsf K$ exchanges the two families: $\mathsf K(L_{\tilde Q})=R_{\natural(\tilde Q)}$ and $\mathsf K(R_{\tilde Q})=L_{\natural(\tilde Q)}$.

*Proof.* The first is the $\mathbb{C}$-linearity of $\natural$. The second is $\natural^4=\mathrm{id}$, which is the involution property applied twice. For the third, compose: applying $\mathsf K(G)$ and then $\mathsf K(F)$ gives

$$
\natural\Bigl(F\,\natural\bigl(\natural\,G\,\natural\bigr)\Bigr)\natural
=\natural\,F\,G\,\natural=\mathsf K(FG),
$$

the middle $\natural\natural$ being the identity. The fourth is the two theorems of the preceding sections.

The third property is the one that matters for equations, and it deserves a word of contrast. A conjugation by an involution of the algebra is an **automorphism** of the operator algebra, not an anti-automorphism, because the two inner conjugations cancel the reversal. So $\mathsf K$ may be applied to a product factor by factor, in the order the factors are written, and the result is the image of the product. That is what makes the conversion of a composite operator legitimate.

**Corollary (the orbits are the pairs).** For every $\tilde Q$ the set $\{L_{\tilde Q},R_{\natural(\tilde Q)}\}$ is carried into itself by $\mathsf K$, and the two elements are exchanged. The same holds for the set $\{R_{\tilde Q},L_{\natural(\tilde Q)}\}$.

*Proof.* By the fourth property, $\mathsf K(L_{\tilde Q})=R_{\natural(\tilde Q)}$, and applying $\mathsf K$ once more gives $\mathsf K(R_{\natural(\tilde Q)})=L_{\natural(\natural(\tilde Q))}=L_{\tilde Q}$. The second set is the same statement read from the right family.

So the pair of the introduction is one orbit of one involution, described from both of its ends. That is the precise sense in which the pair is symmetric: not two coincidences standing side by side, but a single two-element orbit, and the two displays are the orbit written starting from one member or from the other.

**Corollary (the orbit collapses exactly at the centre).** The two elements of the orbit coincide exactly when $\tilde Q$ is a scalar multiple of the unit, and then the orbit is a single operator, the multiplication by that scalar.

*Proof.* $L_{\tilde Q}=R_{\natural(\tilde Q)}$ at the unit reads $\tilde Q=\natural(\tilde Q)$, which by §*The Two Families* holds exactly at the centre; there both operators are the multiplication by the scalar.

Off the centre the orbit therefore has exactly two members, and the pair is a genuine exchange rather than a tautology.

**Remark (which operators the involution fixes).** An operator is fixed by $\mathsf K$ exactly when it commutes with $\natural$. Among the two-sided operators the products $L_{\tilde Q}R_{\natural(\tilde Q)}$ are fixed, since

$$
\mathsf K\bigl(L_{\tilde Q}R_{\natural(\tilde Q)}\bigr)
=R_{\natural(\tilde Q)}\,\mathsf K\bigl(R_{\natural(\tilde Q)}\bigr)
=R_{\natural(\tilde Q)}L_{\natural(\natural(\tilde Q))}
=R_{\natural(\tilde Q)}L_{\tilde Q}
=L_{\tilde Q}R_{\natural(\tilde Q)},
$$

the last equality being the commutation of the two families. The general criterion is one line longer.

**Proposition (the fixed two-sided operators).** Let $\tilde Q$ be invertible. Then $L_{\tilde Q}R_{\tilde P}$ is fixed by $\mathsf K$ exactly when the product $\tilde Q\tilde P$ is a scalar multiple of the unit; and for $\tilde P=\natural(\tilde Q)$ the product is the norm, so that case is always fixed.

*Proof.* Suppose first that the operator is fixed and evaluate at $e_t$. The operator gives $\tilde Q\tilde P$. Its image under $\mathsf K$ is $R_{\natural(\tilde Q)}L_{\natural(\tilde P)}$, which at $e_t$ gives $\natural(\tilde P)\natural(\tilde Q)=\natural(\tilde Q\tilde P)$ by the reversal property. So $\tilde Q\tilde P$ equals its own image under $\natural$, which is the centre. Conversely, let $\tilde Q\tilde P=\lambda e_t$. Then $\tilde P=\lambda\tilde Q^{-1}$, and since $\tilde Q\natural(\tilde Q)=N e_t$ with $N=q_t^2+q_x^2+q_y^2+q_z^2$ the scalar norm, one has $\tilde Q^{-1}=\natural(\tilde Q)/N$ and therefore $\natural(\tilde P)=\lambda\tilde Q/N$. Both operators then act by $X\mapsto\lambda\tilde QX\natural(\tilde Q)/N$, so they agree. For the last claim, $\tilde Q\natural(\tilde Q)=Ne_t$ is the displayed norm identity.

So the two-sided operators whose two parameters are related by the conjugation are the ones on which the transposition of the sides has no effect, and they are a special case of a broader family, the operators whose parameter product is central. The corpus studies the special case on its own account, under the name of the Hermitian pair.

## The Rewriting Rules

The pair converts one family into the other, and a composite operator is converted factor by factor, because $\mathsf K$ preserves products. The rules are therefore short.

| the operator | rewritten with the other family |
|---|---|
| $R_{\tilde Q}$ | $\natural\,L_{\natural(\tilde Q)}\,\natural$ |
| $L_{\tilde Q}$ | $\natural\,R_{\natural(\tilde Q)}\,\natural$ |
| $\natural\,R_{\tilde Q}\,\natural$ | $L_{\natural(\tilde Q)}$ |
| $\natural\,L_{\tilde Q}\,\natural$ | $R_{\natural(\tilde Q)}$ |

The first two rows are the pair. The last two are the two theorems, which are the same content read the other way: they say that a conjugated right multiplication *is* a left multiplication, with no conjugation left over.

**A couple of one-sided operators on a single side.** Let $L_{\tilde Q}$ and $R_{\tilde P}$ be given, the two operators of a couple, one from each family. Their product is converted to the left family by the first row:

$$
L_{\tilde Q}R_{\tilde P}
=L_{\tilde Q}\,\natural\,L_{\natural(\tilde P)}\,\natural .
$$

The right-hand side uses the left multiplication only. The two conjugations are operators in their own right, inserted where the right multiplication used to be, and the parameter $\tilde P$ has become $\natural(\tilde P)$. Read in the other direction, by the second row, the same product is a product of right multiplications only:

$$
L_{\tilde Q}R_{\tilde P}
=\natural\,R_{\natural(\tilde Q)}\,\natural\,R_{\tilde P},
$$

and the inner $\natural\natural$ of the two consecutive conversions combines when more factors are present. So a couple may be brought to whichever side is convenient, and the only trace of the move is the conjugation of the parameters and the presence of $\natural$ between the factors.

**The law of the right family follows from the law of the left family.** As a check that the conversion is consistent with the algebra and not merely a rewriting of symbols, derive the anti-representation of the right family from the representation of the left family. By the pair, $R_{\tilde Q}=\natural L_{\natural(\tilde Q)}\natural$ and $R_{\tilde P}=\natural L_{\natural(\tilde P)}\natural$, so

$$
R_{\tilde Q}R_{\tilde P}
=\natural\,L_{\natural(\tilde Q)}\,L_{\natural(\tilde P)}\,\natural
=\natural\,L_{\natural(\tilde Q)\natural(\tilde P)}\,\natural ,
$$

where the two inner conjugations have combined and the law of the left family has been used. Now $\natural(\tilde Q)\natural(\tilde P)=\natural\bigl(\tilde P\tilde Q\bigr)$, which is the reversal property read on two elements. Hence

$$
R_{\tilde Q}R_{\tilde P}=\natural\,L_{\natural(\tilde P\tilde Q)}\,\natural=R_{\tilde P\tilde Q},
$$

by the pair once more. The order of the parameters is exchanged, and the only ingredient beyond the pair is the reversal property of $\natural$. So the two laws are one law, seen on the two orbits of $\mathsf K$.

**Equations.** Let an equation between operators be written with the two families, and apply $\mathsf K$ to both sides. Because $\mathsf K$ is an involution it is injective, so the new equation is equivalent to the old one; because $\mathsf K$ preserves products, each side is transformed factor by factor; and because it exchanges the families, the transformed equation is written with the families exchanged and the parameters carried. An equation that is written mostly with right multiplications therefore becomes an equation written mostly with left multiplications, and conversely. This is the operation the pair exists to perform, and the four properties of $\mathsf K$ are exactly the four conditions that make it safe.

## The Pairings That Look Alike

The pair carries the parameter, and the conjugation is easy to drop, so the displays that omit it must be listed and refuted once, in one place. There are eight pairings of a family, a conjugation, and a parameter; four are true and four are false, and the rule that separates them is that the parameter written inside must be the conjugation of the parameter written outside.

| display | verdict |
|---|---|
| $L_{\tilde Q}=\natural\,R_{\natural(\tilde Q)}\,\natural$ | true |
| $R_{\tilde Q}=\natural\,L_{\natural(\tilde Q)}\,\natural$ | true |
| $\natural\,L_{\tilde Q}\,\natural=R_{\natural(\tilde Q)}$ | true |
| $\natural\,R_{\tilde Q}\,\natural=L_{\natural(\tilde Q)}$ | true |
| $L_{\tilde Q}=\natural\,R_{\tilde Q}\,\natural$ | false off the centre |
| $R_{\tilde Q}=\natural\,L_{\tilde Q}\,\natural$ | false off the centre |
| $\natural\,L_{\tilde Q}\,\natural=R_{\tilde Q}$ | false off the centre |
| $\natural\,R_{\tilde Q}\,\natural=L_{\tilde Q}$ | false off the centre |

The four false rows are the four true rows with the inner parameter replaced by the outer one. Each is refuted by the same one-element test.

**Proposition (the false rows fail at the centre and only there).** $\natural L_{\tilde Q}\natural=R_{\tilde Q}$ exactly when $\tilde Q$ is a scalar multiple of the unit.

*Proof.* Evaluate at $e_t$. The right multiplication gives $\tilde Q$; the composite gives $\natural(\tilde Q)$, as computed in §*The First Identity*. So the two agree exactly when $\tilde Q=\natural(\tilde Q)$, which by §*The Two Families* is the centre. The other three false rows are the same computation on the other pairing, or the same equation read from the other family.

**Proposition (the size of the failure).** For every element,

$$
R_{\tilde Q}-\natural\,L_{\tilde Q}\,\natural=R_{2\vec Q},
\qquad\text{where } \vec Q=\tilde Q-q_te_t .
$$

*Proof.* By the first theorem, $\natural L_{\tilde Q}\natural=R_{\natural(\tilde Q)}$. Right multiplication is additive in its parameter, because the product of the algebra is additive, so the difference of the two operators is the right multiplication by $\tilde Q-\natural(\tilde Q)$, and that element is $2\vec Q$.

So the false pairing is not wrong by an arbitrary amount. It is wrong by a right multiplication, and the parameter of that right multiplication is twice the vector part, which vanishes exactly at the centre. The measurement also tells the reader what to expect: on a central parameter no error appears at all, which is why the mistake survives inspection on scalar examples and only shows itself away from the centre.

**Example.** Take $\tilde Q=e_t+2\vec e_x$, so that $\natural(\tilde Q)=e_t-2\vec e_x$ and the gap is $4\vec e_x$. On the input $e_t$ the right multiplication gives $e_t+2\vec e_x$ and the composite gives $e_t-2\vec e_x$. The two operators disagree on the unit alone, before any other input is tried.

**Proposition (the parameter of the conversion is unique).** Fix $\tilde Q$ and let $\tilde P$ vary. Then $\natural L_{\tilde P}\natural=R_{\tilde Q}$ exactly when $\tilde P=\natural(\tilde Q)$.

*Proof.* By the first theorem the left side is $R_{\natural(\tilde P)}$, and by the unit this equals $R_{\tilde Q}$ exactly when $\natural(\tilde P)=\tilde Q$; applying the involution gives $\tilde P=\natural(\tilde Q)$.

The conversion is therefore not one choice among many. The parameter that must stand under the left multiplication is the image of the parameter that stands under the right multiplication, and no other element will do.

## Why the Exchange Is Reversal

The pair was proved by computing, but the computation contains one step that decides it, and the article would be incomplete without isolating that step from the notation of the two families.

**The same computation for an arbitrary antimultiplicative bijection.** Let $\Theta$ be a bijection of the algebra with $\Theta(XY)=\Theta(Y)\Theta(X)$ for all $X,Y$. Then, for arbitrary $X$,

$$
\bigl(\Theta L_{\tilde Q}\Theta^{-1}\bigr)(X)
=\Theta\Bigl(\tilde Q\,\Theta^{-1}(X)\Bigr)
=\Theta\bigl(\Theta^{-1}(X)\bigr)\,\Theta(\tilde Q)
=X\,\Theta(\tilde Q)
=R_{\Theta(\tilde Q)}(X),
$$

so that $\Theta L_{\tilde Q}\Theta^{-1}=R_{\Theta(\tilde Q)}$. **The same computation for an automorphism.** Let $\sigma$ preserve products, $\sigma(XY)=\sigma(X)\sigma(Y)$. Then

$$
\bigl(\sigma L_{\tilde Q}\sigma^{-1}\bigr)(X)
=\sigma\Bigl(\tilde Q\,\sigma^{-1}(X)\Bigr)
=\sigma(\tilde Q)\,\sigma\bigl(\sigma^{-1}(X)\bigr)
=\sigma(\tilde Q)\,X
=L_{\sigma(\tilde Q)}(X).
$$

The contrast is exact and it is the whole mechanism. In the first computation the two factors change places, so the parameter ends on the right of the input and the operator becomes a right multiplication. In the second they keep their places, so the parameter stays on the left and the operator remains a left multiplication. The exchange of the sides is precisely the reversal of the two factors of the product $\tilde Q\,\Theta^{-1}(X)$, and nothing else in the computation can produce it.

**Proposition (exchange forces reversal).** Let $\Theta$ be a bijection of the algebra such that $\Theta L_{\tilde Q}\Theta^{-1}=R_{\Theta(\tilde Q)}$ for every $\tilde Q$. Then $\Theta$ reverses products.

*Proof.* Let $X$ be arbitrary and put $Y=\Theta^{-1}(X)$, so that $X=\Theta(Y)$. Evaluating the hypothesis at $X$,

$$
\Theta\bigl(\tilde Q\,Y\bigr)
=\bigl(\Theta L_{\tilde Q}\Theta^{-1}\bigr)(X)
=R_{\Theta(\tilde Q)}(X)
=X\,\Theta(\tilde Q)
=\Theta(Y)\,\Theta(\tilde Q),
$$

and the relation holds for all $\tilde Q$ and all $Y$.

Together with the computation above, the proposition says that the bijections transposing the two families are exactly the bijections reversing products. There are therefore two descriptions of one class of maps, and the class is not empty, $\natural$ being a member.

The proposition also settles a question of principle that the table of §*The Pairings That Look Alike* raises. A bijection that exchanges the families carries the parameter to its image, by the first computation, and it must reverse products, by the proposition. So no bijection can exchange the families and leave the parameter in place. The false rows of that table are not merely unproved; they describe a map that cannot exist.

## The Sense of the Name

The article calls the pair a transposition of the two sides, and the name should be justified, because the algebra also carries a genuine transposition: the adjoint of its plain bilinear form. The two operations agree on what they move and differ on what they charge for it.

**The plain form.** Put $\langle X,Y\rangle=\mathrm{Sc}(XY)$, the scalar part of the product. It is symmetric, because the scalar part is invariant under the exchange of its two factors, and it is non-degenerate, because the units read the coefficients: $\langle X,e_t\rangle=x_t$ and $\langle X,\vec e_k\rangle=-x_k$ for the three vector units.

**The transpose.** For a $\mathbb{C}$-linear operator $F$, the **transpose** for the plain form is the operator $F^{\approx}$ with $\langle F(X),Y\rangle=\langle X,F^{\approx}(Y)\rangle$ for all $X,Y$. It exists and is unique, because the relation determines $F^{\approx}(Y)$ by its pairings with all elements and the form is non-degenerate. The corpus names this operator the **plain bilinear adjoint**.

**Proposition (the plain bilinear adjoint exchanges the sides and keeps the parameter).** $L_{\tilde Q}^{\approx}=R_{\tilde Q}$ and $R_{\tilde Q}^{\approx}=L_{\tilde Q}$.

*Proof.* The left side of the defining relation for $F=L_{\tilde Q}$ is $\langle\tilde QX,Y\rangle=\mathrm{Sc}(\tilde QXY)$. The scalar part is invariant under the cyclic permutation of the three factors, so $\mathrm{Sc}(\tilde QXY)=\mathrm{Sc}(XY\tilde Q)=\langle X,R_{\tilde Q}(Y)\rangle$, which is the defining relation of $R_{\tilde Q}$; the transpose is unique. The second identity is the same computation run the other way.

The comparison is now immediate. Both the plain bilinear adjoint and the conjugation turn $L_{\tilde Q}$ into a right multiplication by $\tilde Q$, and the pair reconciles them:

$$
L_{\tilde Q}^{\approx}=R_{\tilde Q}=\natural\,L_{\natural(\tilde Q)}\,\natural .
$$

They reach the same operator and they differ in what they do to the parameter. The plain bilinear adjoint keeps it and needs no conjugation; the conjugation carries it and needs two. The pair is therefore the statement that the two prices buy the same operator, and the article's title is the record of the second price.

## Summary

For every element $\tilde Q$, each of the two families is the conjugate of the other: $L_{\tilde Q}=\natural R_{\natural(\tilde Q)}\natural$ and $R_{\tilde Q}=\natural L_{\natural(\tilde Q)}\natural$. Each display was proved by computing the conjugated composite on an arbitrary element. In the first, the composite conjugates the input, multiplies by $\tilde Q$ on the left, and conjugates again; the outer conjugation meets the product $\tilde Q\natural(X)$, reverses it, and in reversing it moves $\tilde Q$ across the other factor while putting it through $\natural$. The parameter therefore lands on the right of the input, which makes the result a right multiplication, and it lands there as $\natural(\tilde Q)$, which makes the display exact for every element. The second display is the same computation with the two factors of that product written in the other order, so the parameter is carried the other way and the result is a left multiplication.

The pair is one orbit of one involution. The map $\mathsf K(F)=\natural F\natural$ is $\mathbb{C}$-linear, involutive, product-preserving, and exchanges the two families, so $\{L_{\tilde Q},R_{\natural(\tilde Q)}\}$ is carried into itself with its two members exchanged. The orbit collapses to a single operator exactly at the centre, and off the centre the exchange is genuine.

The consequences are the working tool. Any right multiplication is a conjugated left multiplication, so a couple of one-sided operators can be brought to a single side by converting one of them; a composite operator is converted factor by factor, because $\mathsf K$ preserves products; and since $\mathsf K$ is an involution, an equation transformed on both sides remains equivalent. The law of the right family, with its exchanged parameters, follows from the law of the left family and the reversal property alone, so the two laws are one law.

The displays that omit the carried parameter are false, and the failure is measured: $R_{\tilde Q}-\natural L_{\tilde Q}\natural=R_{2\vec Q}$, so the error vanishes exactly at the centre and is a right multiplication by twice the vector part everywhere else. The parameter of the conversion is moreover unique, the element under the left multiplication being forced to be the image of the element under the right one.

Finally the mechanism and the name. The exchange of the sides is exactly the reversal of the two factors of the product inside the conjugation, which is why only antimultiplicative maps transpose the families, and why no such map can keep the parameter. The genuine transpose of the plain form, the plain bilinear adjoint, exchanges the sides as well and keeps the parameter; the conjugation exchanges them and carries it. The two agree on the operator they produce and differ on the price, and the pair is the statement of that agreement.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{\tilde Q}(X)=\tilde QX$, $R_{\tilde Q}(X)=X\tilde Q$ | the left and the right multiplication by $\tilde Q$ |
| $L_{\tilde Q}L_{\tilde P}=L_{\tilde Q\tilde P}$, $R_{\tilde Q}R_{\tilde P}=R_{\tilde P\tilde Q}$, $L_{\tilde Q}R_{\tilde P}=R_{\tilde P}L_{\tilde Q}$ | the three laws, from associativity alone |
| $L_{\tilde Q}(e_t)=\tilde Q=R_{\tilde Q}(e_t)$ | the unit reads the parameter, and separates two operators |
| $L_{\tilde Q}=R_{\tilde Q}$ exactly at the centre | the two families meet only over the scalars |
| $\natural(\tilde Q)=q_te_t-q_x\vec e_x-q_y\vec e_y-q_z\vec e_z$ | the quaternion conjugation: involutive and antimultiplicative |
| $\natural L_{\tilde Q}\natural=R_{\natural(\tilde Q)}$ | the first identity: what the conjugation does to a left multiplication |
| $\natural R_{\tilde Q}\natural=L_{\natural(\tilde Q)}$ | the second identity: what it does to a right multiplication |
| $L_{\tilde Q}=\natural R_{\natural(\tilde Q)}\natural$, $R_{\tilde Q}=\natural L_{\natural(\tilde Q)}\natural$ | the pair: each family is the conjugate of the other |
| $\mathsf K(F)=\natural F\natural$ | the involution: linear, involutive, product-preserving, exchanging the families |
| $\{L_{\tilde Q},R_{\natural(\tilde Q)}\}$ | the orbit of $\mathsf K$, a pair off the centre and a point on it |
| $R_{\tilde Q}-\natural L_{\tilde Q}\natural=R_{2\vec Q}$ | the measured failure of the pairing without the carried parameter |
| $\langle X,Y\rangle=\mathrm{Sc}(XY)$, $L_{\tilde Q}^{\approx}=R_{\tilde Q}$ | the plain form and the plain bilinear adjoint, which transposes and keeps the parameter |

## Further Reading

- [Operators Acting on One Side](operators-acting-on-one-side.html), for the two families, their images, their commutants and the laws used here
- [Operators Acting on Two Sides](operators-acting-on-two-sides.html), for the products $L_{\tilde Q}R_{\tilde P}$, their adjoints and their isometries
- [Adjoint Pair of $L$ and $R$ Operators](adjoint-pair-of-l-and-r-operators.html), for the plain bilinear adjoint $L_{\tilde Q}^{\approx}=R_{\tilde Q}$ as the first of the four adjoints, and for the other three
- [The Hermitian Pair of Operators Acting on One Side](the-hermitian-pair-of-operators-acting-on-one-side.html), for the two-sided operators whose parameters are related by the conjugation, which are the operators fixed by the involution of this article
- [Operator Chirality on the Biquaternion Algebra](operator-chirality-on-the-biquaternion-algebra.html), for the exchange of the sides as the corpus records it, and for its difference from the swap of the two slots
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for the generation of the endomorphism algebra by two families, one of which this article derives from the other
- [The Group of Involutions](the-group-of-involutions.html), for $\natural$, $\ast$ and the coefficient conjugation, their linearity and their grades
- [Bilinear Forms](bilinear-forms.html), §*Isometries*, for the transpose of a bilinear form, of which the plain bilinear adjoint is the biquaternion case
