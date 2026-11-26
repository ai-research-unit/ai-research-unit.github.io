# __The Copy Acting on Sixteen Dimensions__

## Introduction

**The subject.** One copy acts on the sixteen-dimensional operator space in two ways, and the two ways give opposite pictures: the left action is isotypic, four copies of the module, while the conjugation action splits into the four carriers. The article proves both statements, computes the two Casimirs, and draws the consequence for invariants: an invariant of the left action is a single number, while an invariant of the conjugation is a quadruple.

**The order of the article.** The two actions come first; the isotypic theorem second. The four carriers of the conjugation follow, then the commutativity of the actions, and the reading closes.

**It assumes** *The Conjugation Labels Are Integer*, *The Four Carrier Lists* and *The Clebsch–Gordan Decomposition of the Operators*. **The row of the elements is** where the same two actions act on the four-dimensional algebra, with the left action isotypic of multiplicity two and the conjugation splitting into two carriers.

**The result in one line.** The left action has the single isotypic component of multiplicity four and the scalar Casimir $\tfrac{15}{4}$; the conjugation action has the four isotypic components of dimensions $7,5,3,1$ and the four Casimir values $12,6,2,0$.

**Boundaries.** The integrality of the conjugation labels is *The Conjugation Labels Are Integer*; the four lists are *The Four Carrier Lists*; the actions themselves are *Operators Acting on Two Sides*.

## The Two Actions

**Definition.** The **left action** is $O\mapsto \xi O$; the **conjugation action** is $O\mapsto \xi O-O\xi$, both for $\xi$ in the copy.

**Proposition.** Both actions are representations of the copy on the sixteen, and the second is the difference of the left action and the right action.

*Proof.* The left multiplication is a representation because the algebra is associative; the commutator is a derivation in $\xi$, and it is the difference of the left and right multiplications.

**Corollary.** The two actions have the same dimension and different weights: half-integers for the first, integers for the second.

*Proof.* The weights of the left action are the weights of the module, and those of the conjugation are the differences.

**Corollary.** The two actions commute with one another, the left multiplication by $\xi$ commuting with the commutator by $\eta$.

*Proof.* The left multiplication acts on the first factor of the tensor square, the commutator on the difference of the factors.

**The reading.** One space, two representations, and a commutation relation. The article separates them because their decompositions are as different as possible.

## The Isotypic Theorem

**Theorem.** Under the left action the space is isotypic of multiplicity four:
$$
\operatorname{End}(\mathbb{B})\cong V_{3/2}^{\oplus4}.
$$

*Proof.* Choose a basis of the module; an operator is determined by its four values on the basis, and each value is an element of the module. Left multiplication acts on the values, so the space is the direct sum of four copies of the module, and the copies are isomorphic and irreducible.

**Corollary.** The endomorphism algebra of the left action is the full algebra of the four copies, and its centre is four-dimensional.

*Proof.* The commutant of four copies of an irreducible module is the algebra of the four-by-four scalar combinations.

**Corollary.** The Casimir of the left action is the scalar $\tfrac{15}{4}$, and the only invariant of the left action on the space is this number: every other invariant is a function of it, and none distinguishes a vector from its copy in another block.

*Proof.* The Casimir acts by $j(j+1)$ on each copy, with $j=\tfrac32$.

**The reading.** The left action is blind: it sees sixteen dimensions as four identical blocks and cannot distinguish a vector from its copy in another block. This is why the four carriers cannot be read off the left action.

## The Conjugation Splitting

**Theorem.** Under the conjugation action the space splits into four irreducible pieces of dimensions $7,5,3,1$.

*Proof.* The weights are the differences of the module weights; grouping them by highest weight gives the four carrier strings, and each carrier is irreducible since its weights are simple and its highest weight is annihilated by the raising operator alone.

**Corollary.** The Casimir of the conjugation action has the four eigenvalues $12,6,2,0$, each with the multiplicity of the dimension of its carrier.

*Proof.* The Casimir acts by $k(k+1)$ on the carrier of label $k$.

**Corollary.** The four projectors onto the carriers are polynomials in the Casimir, of degree three.

*Proof.* The Lagrange interpolation of the four eigenvalues.

**The reading.** The conjugation action sees everything: the four carriers, their dimensions, and their labels, all from one operator. The price is that the operator is the commutator and not the product, so the carriers are not subalgebras.

## The Commutation

**Proposition.** The left action and the conjugation action commute, and their joint decomposition is the carrier decomposition refined by the multiplicity.

*Proof.* Left multiplication by $\xi$ commutes with the commutator by $\eta$; the joint eigenspaces are the intersections of the carriers with the four copies of the left action.

**Corollary.** Each carrier is a module for the left action, and it splits into copies of the module of dimension four.

*Proof.* The carrier is stable under the conjugation and under the left action, and the only irreducible module of the left action is the module of dimension four.

**Corollary.** The carrier of dimension seven cannot split into copies of a four-dimensional module, so the two actions do not decompose the space simultaneously.

*Proof.* Seven is not a multiple of four.

**The reading.** The two actions commute, and their joint decomposition is finer than either. The dimensions show that no carrier is a sum of whole copies of the module, so the commutation does not produce a simultaneous isotypic decomposition: the two structures genuinely cross.

## The Commutants of the Two Actions

**Proposition.** The operators commuting with the left action are the right multiplications, and they form a four-dimensional algebra.

*Proof.* Left multiplication by the rotors generates the whole algebra, since $\vec e_x,\vec e_y,\vec e_z$ and the identity multiply to everything; an operator commuting with every $L_\xi$ therefore commutes with $L_a$ for every element $a$, and putting $a$ equal to the identity shows that it is the right multiplication by its own value at the identity. Conversely $R_bL_a=L_aR_b$ for all $a$ and $b$, by associativity.

**Corollary.** The multiplicity four of the isotypic left action is the dimension of the commutant.

*Proof.* For an isotypic semisimple module the multiplicity of the single summand equals the dimension of the algebra of intertwining operators, and the intertwining operators are the right multiplications, of dimension four.

**Corollary.** The commutant of the conjugation action contains both copies and is strictly larger, since it also contains the operators that exchange the two sides.

*Proof.* The conjugation is the difference of the two left actions, so it commutes with both of them; and the exchange of the two factors of the operator space commutes with the conjugation while it does not commute with the left action alone.

**The reading.** The two actions are told apart by their commutants. The left action has the smallest possible commutant consistent with an isotypic module of multiplicity four, and the conjugation action has a larger one, which is why its decomposition is finer. The size of the commutant is the number of copies in one case and the number of carriers in the other.

## The Matrix of the Coefficients

**Theorem.** The coefficients of the change of basis between the sixteen products and the sixteen coupled states form a $16\times16$ orthogonal matrix, real in the Condon–Shortley convention.

*Proof.* Both families are orthonormal bases of the same space, so the matrix of the passage is orthogonal, and the phase convention makes it real.

**Corollary.** The rows are orthonormal, the columns are orthonormal, and the matrix multiplied by its transpose is the identity.

*Proof.* The two statements are the same statement read twice on an orthogonal matrix.

**The reading.** The four carriers are the four blocks of rows of one orthogonal matrix, and the Casimir is diagonal on the coupled side because it acts by a scalar on each block. The sixteen dimensions of this article are the sixteen rows, and the four carriers are the four sizes $7,5,3,1$.

## The Ladder

**Proposition.** The copy contains a raising operator $E$ and a lowering operator $F$ with $[H,E]=E$, $[H,F]=-F$ and $[E,F]=2H$, where $H$ is the Cartan element of the copy.

*Proof.* The copy is $\mathfrak{sl}_2(\mathbb{C})$. Take $H$ to be the Cartan element, $E$ the combination of the two remaining generators that raises the weight by one, and $F$ the combination that lowers it; the three brackets are then the defining relations of the algebra, with the factor two that the normalisation of the matrix elements fixes.

**Proposition (the matrix elements).** In the standard normalisation
$$
E\lvert j,m\rangle=\sqrt{(j-m)(j+m+1)}\lvert j,m+1\rangle,\qquad F\lvert j,m\rangle=\sqrt{(j+m)(j-m+1)}\lvert j,m-1\rangle .
$$

*Proof.* The two operators are adjoint to each other for the invariant form, and the product $EF$ must act on $\lvert j,m\rangle$ by the value that makes $[E,F]=2H$ hold; the two square roots are the unique positive solution of that equation at each step, with the top state annihilated by $E$ and the bottom by $F$.

**Corollary.** A finite string must end, so the label is a half-integer and the string has $2j+1$ members, and the sixteen dimensions of this article are the sums of four such strings.

*Proof.* A string that can be raised must reach a vector annihilated by $E$; a vector of weight $m$ is annihilated exactly when $m=j$, and the same at the bottom.

**The reading.** The ladder is the reason the four carriers exist and the reason their sizes are odd numbers: each carrier is one string, and a string has $2J+1$ members. The blocks of rows of the matrix of this article are those strings, of sizes $7,5,3,1$.

## The Reading

**What the left action knows.** One number, the Casimir, and one multiplicity, four. A statement about the left action that uses any other invariant is either trivial or wrong.

**What the conjugation knows.** Four numbers and four dimensions, and with them the labels, the carriers and the filtration of the algebra.

**What the crossing means.** The two actions are the two halves of the same multiplication: the left action is the product, the conjugation is the commutator. The product is isotypic, the commutator is multiplicity-free, and the algebra of the operators is the place where the two readings meet.

## Further Reading

- [The Conjugation Labels Are Integer](the-conjugation-labels-are-integer.html), for the weights of the conjugation action.
- [The Four Carrier Lists](the-four-carrier-lists-of-one-algebra.html), for the four actions and their decompositions.
- [Operators Acting on Two Sides](operators-acting-on-two-sides.html), for the two-sided structure.
- [The Clebsch–Gordan Decomposition of the Operators](the-clebsch-gordan-decomposition-of-the-operators.html), for the four carriers.
