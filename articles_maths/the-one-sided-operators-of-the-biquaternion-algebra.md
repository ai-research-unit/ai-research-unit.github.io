# __The One-Sided Operators of the Biquaternion Algebra__

## Introduction

**The subject.** Two four-dimensional families sit inside the sixteen-dimensional algebra of the operators: the left multiplications $L_a(X)=aX$ and the right multiplications $R_b(X)=Xb$. The article computes what the two families do to one another. They obey two opposite multiplication laws, they commute with one another, they meet in a line, their linear sum is seven-dimensional, each is the commutant of the other, and the remaining nine dimensions consist of operators that are neither. The count $1+3+3+9=16$ organises the whole operator algebra.

**The order of the article.** The families and their laws come first; the commutation of the two sides second. The intersection is computed third, the sum fourth, and the double centraliser fifth. The complement closes the count.

**It assumes** *Operators Acting on One Side* and *The Endomorphisms of the Biquaternion Algebra*. **The row of the elements is** four-dimensional and has only the two families; here the same two families sit inside a sixteen-dimensional space whose remaining nine dimensions have no counterpart there.

**The result in one line.** $L_{\mathbb{B}}\cap R_{\mathbb{B}}=\mathbb{C}\mathrm{I}$ is a line, $L_{\mathbb{B}}+R_{\mathbb{B}}$ is a seven-dimensional subspace, each family is the commutant of the other, and a nine-dimensional complement consists of operators that are neither left nor right.

**Boundaries.** The generation of the whole space by the products of the two families is *$\operatorname{End}(\mathbb{B})$ as an Algebra: the Regular Representation*; the images of a single left multiplication are *The Left Ideals and the Image of a Left Multiplication*; the operators of the complement, written as sums of products, are *The Length and the Two Ranks*.

## The Two Families and Their Laws

**Definition.** For an element $a$, the **left multiplication** and the **right multiplication** are
$$
L_a(X)=aX,\qquad R_a(X)=Xa ,
$$
operators on $\mathbb{B}$, complex-linear because the product is bilinear.

**Proposition.** The two families are multiplicative, one directly and one in the reversed order:
$$
L_aL_b=L_{ab},\qquad R_aR_b=R_{ba}.
$$

*Proof.* Apply each side to an arbitrary $X$. On the left, $a(bX)=(ab)X$ is associativity. On the right, $(Xa)b=X(ab)$, so $R_aR_b=R_{ba}$: the composite multiplies by $b$ first and by $a$ second, and the parameter of the composite is $ba$.

**Corollary.** Each family is the image of a faithful representation of the algebra, the first an isomorphism of algebras and the second an isomorphism onto the opposite algebra.

*Proof.* Injectivity holds because $L_a(e_t)=a$ and $R_a(e_t)=a$; the two laws say that the first respects the product and the second reverses it.

**Proposition.** The two sides commute:
$$
L_aR_b=R_bL_a .
$$

*Proof.* Both send $X$ to $aXb$.

**The reading.** The asymmetry of the two laws is the whole content of the word *opposite* in the isomorphism $\operatorname{End}(\mathbb{B})=\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}$. A left multiplication is a representation of the algebra; a right multiplication is a representation of the algebra with the product read backwards, and the two representations commute because they act on different sides of the same symbol.

## The Intersection

**Theorem.** The two families meet in the scalars:
$$
L_{\mathbb{B}}\cap R_{\mathbb{B}}=\mathbb{C}\,\mathrm{I},\qquad \dim_{\mathbb{C}}=1 .
$$

*Proof.* Suppose $L_a=R_b$. At $X=e_t$ the two values are $a$ and $b$, so $a=b$; then $aX=Xa$ for every $X$, so $a$ commutes with the algebra, and the centre is the line of scalars. Conversely a scalar $\lambda$ gives $L_\lambda=R_\lambda=\lambda\mathrm{I}$.

**Corollary.** The intersection consists of the operators that are both left and right, and each of them is a scalar operator.

*Proof.* The theorem, and the description of the centre.

**Corollary.** The two families are not disjoint and are not equal: their meeting is one line, and each family is four-dimensional.

*Proof.* Each family is a faithful image of the four-dimensional algebra, and the intersection has dimension one.

**The reading.** The one operator that is both a left and a right multiplication is the identity and its multiples, and the multiple is the same on both sides. There is no operator that is a nontrivial left multiplication and also a nontrivial right multiplication: the two readings of an operator are exclusive away from the scalars.

## The Sum

**Theorem.** The linear sum of the two families is seven-dimensional:
$$
L_{\mathbb{B}}+R_{\mathbb{B}}=\{L_a+R_b\},\qquad \dim_{\mathbb{C}}=7 .
$$

*Proof.* The sum of the dimensions is $4+4=8$, and the intersection has dimension one, so the sum has dimension $8-1=7$.

**Corollary.** Every element of the sum has a unique expression $L_a+R_b$ with $\mathrm{Sc}(a)=0$, and the seven parameters are the three coordinates of $a$ and the four of $b$.

*Proof.* Two expressions differ by an element of the intersection, which is a scalar; the scalar is absorbed into the left parameter, and the condition that the left parameter have zero scalar part fixes the expression.

**Proposition.** The sum is not a subalgebra of the operator algebra.

*Proof.* The product of $L_a+R_c$ with $L_b+R_d$ is $L_{ab}+R_{dc}+L_aR_d+R_cL_b$; the two mixed terms are two-sided and are not in the sum unless both vanish, and they do not vanish for general parameters, since $L_aR_d$ is zero only when $a$ or $d$ is zero.

**The reading.** The seven-dimensional sum is a subspace and not an algebra: it is closed under addition and under scalar multiplication, and its product leaves it at the second step. This is the first sign that the one-sided structure is a linear layer and not a multiplicative one, and it is why the operators outside the sum are needed to close the product.

## The Double Centraliser

**Theorem.** Each family is the commutant of the other:
$$
\{T:TL_a=L_aT\ \text{for all }a\}=R_{\mathbb{B}},\qquad \{T:TR_b=R_bT\ \text{for all }b\}=L_{\mathbb{B}}.
$$

*Proof.* If $T$ commutes with every $L_a$, put $b=T(e_t)$. For arbitrary $X$ the identity $X=L_X(e_t)$ gives $T(X)=T(L_Xe_t)=L_XT(e_t)=Xb=R_b(X)$, so $T=R_b$. The converse is the commutation of the two sides, and the second statement is the same argument with the sides exchanged.

**Corollary.** The algebra generated by one family is its own double commutant, so the two families form a pair of mutual centralisers and neither can be enlarged without meeting the other.

*Proof.* The commutant of the commutant of $L_{\mathbb{B}}$ is the commutant of $R_{\mathbb{B}}$, which is $L_{\mathbb{B}}$ again.

**Corollary.** The four-dimensional families are the maximal commutative-free pieces of the operator algebra: any operator commuting with a family lies in the other family.

*Proof.* The theorem.

**The reading.** The double centraliser statement is the operator form of the simplicity of the algebra. It says that the two sides know each other completely: to know which operators commute with all left multiplications is to know the right multiplications, and conversely. Nothing else commutes with either family.

## The Complement

**Definition.** The **complement of the one-sided layers** is any subspace $W$ with
$$
\operatorname{End}(\mathbb{B})=(L_{\mathbb{B}}+R_{\mathbb{B}})\oplus W,\qquad \dim_{\mathbb{C}}W=9 .
$$

**Proposition.** The complement exists and its elements are neither left nor right multiplications.

*Proof.* A subspace of dimension $16-7=9$ exists by the dimension formula, and an element of it that were a left multiplication would lie in the sum, hence in the intersection with the sum, contrary to the directness.

**Proposition.** The operator $T_{a,b}$ with both parameters noncentral lies in the complement modulo the sum, and its class in the quotient of dimension nine is nonzero.

*Proof.* If $T_{a,b}=L_c+R_d$, then applying both sides to $e_t$ gives $ab=c+d$; applying to $X$ gives $aXb=cX+Xd$; the two together force $a$ and $b$ to be central, since the identity $aXb=Xab$ for all $X$ says that $aX=Xa$ for all $X$ after multiplying by $b$ on the right.

**Corollary.** The nine-dimensional complement contains the genuine two-sided operators, and the count of the space is $1+3+3+9=16$: the scalars, the traceless left parameters, the traceless right parameters and the nine.

*Proof.* The scalars are the intersection; the left parameters split as the scalars plus the three-dimensional traceless part, and so do the right ones; the remainder is nine.

**The reading.** Seven of the sixteen dimensions are one-sided and nine are not. The seven are the two families together with their common line; the nine are the part of the operator space that needs both sides at once, and it is on the nine that every phenomenon of the row that has no one-sided description lives.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_a(X)=aX$, $R_b(X)=Xb$ | the two one-sided families |
| $L_aL_b=L_{ab}$, $R_aR_b=R_{ba}$ | the two multiplication laws |
| $L_aR_b=R_bL_a$ | the commutation of the sides |
| $L_{\mathbb{B}}\cap R_{\mathbb{B}}=\mathbb{C}\mathrm{I}$ | the intersection, a line |
| $\dim(L_{\mathbb{B}}+R_{\mathbb{B}})=7$ | the sum of the families |
| $\{T:TL_a=L_aT\}=R_{\mathbb{B}}$ | the double centraliser |
| $1+3+3+9=16$ | the count of the operator space |

## Further Reading

- [Operators Acting on One Side](operators-acting-on-one-side.html), for the families and their first properties.
- [The Endomorphisms of the Biquaternion Algebra](the-endomorphisms-of-the-biquaternion-algebra.html), for the operator space and its centre.
- [$\operatorname{End}(\mathbb{B})$ as an Algebra: the Regular Representation](end-b-as-an-algebra-the-regular-representation.html), for the generation of the sixteen by the products.
- [The Left Ideals and the Image of a Left Multiplication](the-left-ideals-and-the-image-of-a-left-multiplication.html), for the images of a single family.
- [The Length and the Two Ranks](the-length-and-the-two-ranks.html), for the operators of the nine-dimensional complement written as sums.
