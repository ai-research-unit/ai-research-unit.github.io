
# __The Left and Right Multiplications of the Quaternionic Sesquilinear Product__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ carries four products on its underlying $\mathbb{C}$-vector space (*The Four Biquaternion Complex Products*), and the fourth of them,

$$
\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q^{*} ,
$$

is the subject of this group. The rule and the scalar–vector form are *The Four Biquaternion Complex Products* §*The Complex Quaternionic Sesquilinear Product*; the sesqualgebra it defines and its one-sided actions of the unit are *Biquaternions as a General Quaternionic Sesqualgebra (GQS) over $\mathbb{C}$*; the associator is *The Associator of the Quaternionic Sesquilinear Product*. The symbols are those of the group: ${}^{\natural}$ is the natural conjugation $\tilde P^{\natural} = P_0 - \mathbf P$, ${}^{*}$ is the star conjugation, and the bar is the coefficientwise complex conjugation.

The subject of this article is the pair of **multiplication operators** attached to the multiplication,

$$
L_{\tilde A}(\tilde X) = \tilde A \star \tilde X = \tilde A^{\natural}\tilde X^{*} , \qquad R_{\tilde A}(\tilde X) = \tilde X \star \tilde A = \tilde X^{\natural}\tilde A^{*} ,
$$

the left and the right multiplication by a fixed element. The left multiplication is conjugate-linear in its argument, the right multiplication is linear, and this asymmetry, together with the absence of a unit (*The Two One-Sided Actions and the Absence of a Unit*) and the failure of associativity, makes the family of these operators the smallest nontrivial operator theory of the batch. The article establishes three things. First, the parities: the map $\tilde A \mapsto L_{\tilde A}$ is $\mathbb{C}$-linear and the map $\tilde A \mapsto R_{\tilde A}$ is conjugate-linear, so the two families are two different images of $\mathbb{B}$ rather than a single regular representation. Second, the composition laws:

$$
L_{\tilde A} \circ L_{\tilde B} = T_{\tilde A^{\natural},\,\overline{\tilde B}} , \qquad R_{\tilde A} \circ R_{\tilde B} = T_{\overline{\tilde B},\,\tilde A^{*}} ,
$$

where $T_{\tilde P,\tilde Q}(\tilde X) = \tilde P\tilde X\tilde Q$ is the ordinary two-sided operator. Third, the **absence of a monoid**: the composition of two left multiplications is $\mathbb{C}$-linear whereas every left multiplication is conjugate-linear, so the class is not closed under composition and the left multiplications do not form a monoid. They are sandwiches in the sense of *The Sesquilinear Sandwich Operator*, $L_{\tilde A} = S_{\tilde A^{\natural},e_0}$, and the monoid they generate is the sandwich monoid of that article.

The article owns the two families, their parities, their composition laws and the failure of the monoid property. It cites the general operator theory to *The Left and Right Multiplication Operators of a Sesqualgebra*; it cites the sandwich and its composition table to *The Sesquilinear Sandwich Operator*; it cites the composition of the left multiplications of the four products to *Relations Between the Four Biquaternion Products* §*The Left Multiplications*; and it does not treat the ternary operator, which is *The Ternary Product and the Failure of the Jordan Triple Identity*, nor the matrix realization, which is *The Quaternionic Sesquilinear Product in the 2×2 Matrix Model*.

## The Two Families

### The Definitions

**Definition.** The **left multiplication** by $\tilde A$ and the **right multiplication** by $\tilde A$ are

$$
L_{\tilde A}(\tilde X) = \tilde A \star \tilde X = \tilde A^{\natural}\tilde X^{*} , \qquad R_{\tilde A}(\tilde X) = \tilde X \star \tilde A = \tilde X^{\natural}\tilde A^{*} .
$$

The two families are $\mathcal{L} = \{ L_{\tilde A} : \tilde A \in \mathbb{B} \}$ and $\mathcal{R} = \{ R_{\tilde A} : \tilde A \in \mathbb{B} \}$.

**Proposition (the closed forms).** For every $\tilde A$ and $\tilde X$,

$$
L_{\tilde A}(\tilde X) = \tilde A^{\natural}\tilde X^{*} = S_{\tilde A^{\natural},\,e_0}(\tilde X) , \qquad R_{\tilde A}(\tilde X) = \tilde X^{\natural}\tilde A^{*} ,
$$

where $S_{a,b}(\tilde X) = a\tilde X^{*}b$ is the sesquilinear sandwich of *The Sesquilinear Sandwich Operator*; so every left multiplication is the sandwich with parameters $\tilde A^{\natural}$ and $e_0$.

**Proof.** The first display is the rule; the sandwich with second parameter $e_0$ is $a\tilde X^{*}e_0 = a\tilde X^{*}$, which is the left multiplication with $a = \tilde A^{\natural}$. The second display is the rule read on the right slot. $\square$

**Remark.** The left multiplication is a sandwich and the right multiplication is not: $R_{\tilde A}(\tilde X) = \tilde X^{\natural}\tilde A^{*}$ carries the natural conjugation in the first factor rather than the star in the middle, and it is a $\mathbb{C}$-linear operator, whereas every sandwich is conjugate-linear. The asymmetry of the two slots of the multiplication therefore appears at the operator level as the asymmetry between a sandwich and a linear two-sided operator.

### The Parities

**Proposition (the parities of the operators).** For every $\tilde A$, the operator $L_{\tilde A}$ is **conjugate-linear** and the operator $R_{\tilde A}$ is $\mathbb{C}$-**linear**:

$$
L_{\tilde A}(\lambda\tilde X) = \bar\lambda\, L_{\tilde A}(\tilde X) , \qquad R_{\tilde A}(\lambda\tilde X) = \lambda\, R_{\tilde A}(\tilde X) .
$$

**Proof.** $L_{\tilde A}(\tilde X) = \tilde A^{\natural}\tilde X^{*}$ and the star conjugation is conjugate-linear, $(\lambda\tilde X)^{*} = \bar\lambda\tilde X^{*}$, while $\tilde A^{\natural}$ is fixed; hence the first identity. $R_{\tilde A}(\tilde X) = \tilde X^{\natural}\tilde A^{*}$ and the natural conjugation is $\mathbb{C}$-linear, $(\lambda\tilde X)^{\natural} = \lambda\tilde X^{\natural}$, and $\tilde A^{*}$ is fixed; hence the second. $\square$

**Proposition (the parities of the parametrisations).** The map $\tilde A \mapsto L_{\tilde A}$ is injective and $\mathbb{C}$-**linear**, and the map $\tilde A \mapsto R_{\tilde A}$ is injective and **conjugate-linear**.

**Proof.** For the linearity of the first, $L_{\tilde A + \lambda\tilde B}(\tilde X) = (\tilde A + \lambda\tilde B)^{\natural}\tilde X^{*} = \tilde A^{\natural}\tilde X^{*} + \lambda\tilde B^{\natural}\tilde X^{*}$; the natural conjugation is $\mathbb{C}$-linear, so $(\lambda\tilde B)^{\natural} = \lambda\tilde B^{\natural}$ and $L_{\tilde A+\lambda\tilde B} = L_{\tilde A} + \lambda L_{\tilde B}$. Injectivity: $L_{\tilde A} = 0$ means $\tilde A^{\natural}\tilde X^{*} = 0$ for every $\tilde X$, which at $\tilde X = e_0$ gives $\tilde A^{\natural} = 0$, hence $\tilde A = 0$. For the second, $R_{\tilde A+\lambda\tilde B}(\tilde X) = \tilde X^{\natural}(\tilde A + \lambda\tilde B)^{*} = \tilde X^{\natural}\tilde A^{*} + \bar\lambda\tilde X^{\natural}\tilde B^{*}$, since the star is conjugate-linear; injectivity is as before at $\tilde X = e_0$. $\square$

**Remark.** The two families are therefore two different images of $\mathbb{B}$: the left one is a $\mathbb{C}$-linear image inside the conjugate-linear endomorphisms, and the right one a conjugate-linear image inside the linear endomorphisms. The left family is a copy of $\mathbb{B}$ and not a representation of the multiplication, because the multiplication is not associative; the right family is the conjugate copy. This is the operator-level reason the group has no regular representation in the sense of an algebra, and it is the first of the two negative results of the article.

### The Two Families in the Plain Operators

Writing $\lambda_{\tilde P}(\tilde X) = \tilde P\tilde X$ and $\rho_{\tilde P}(\tilde X) = \tilde X\tilde P$ for the left and right multiplications of the plain product, the two multiplication operators are the plain multiplications composed with the two conjugations:

$$
L_{\tilde A} = \lambda_{\tilde A^{\natural}} \circ {}^{*} , \qquad R_{\tilde A} = \rho_{\tilde A^{*}} \circ {}^{\natural} .
$$

**Proposition.** The left multiplication is the plain left multiplication by $\tilde A^{\natural}$ after the star conjugation, and the right multiplication is the plain right multiplication by $\tilde A^{*}$ after the natural conjugation.

**Proof.** $\lambda_{\tilde A^{\natural}}(\tilde X^{*}) = \tilde A^{\natural}\tilde X^{*} = L_{\tilde A}(\tilde X)$, and $\rho_{\tilde A^{*}}(\tilde X^{\natural}) = \tilde X^{\natural}\tilde A^{*} = R_{\tilde A}(\tilde X)$. $\square$

**Remark.** The reading is the one of *Relations Between the Four Biquaternion Products* §*The Left Multiplications*: the left multiplication of the fourth product is a plain multiplication re-indexed by the natural sign and composed with the star, while the right multiplication is the conjugate of a plain right multiplication re-indexed. The re-indexing by ${}^{\natural}$ is the operator form of the isotope by which the fourth product differs from the derived operation (*The Two One-Sided Actions and the Absence of a Unit*), and the asymmetric placement of the two conjugations is the operator form of the two different slots of the multiplication.

## The Composition of Two Left Multiplications

### The Law

**Theorem (the composition).** For all $\tilde A, \tilde B$,

$$
L_{\tilde A} \circ L_{\tilde B} = T_{\tilde A^{\natural},\,\overline{\tilde B}} ,
$$

where $T_{\tilde P,\tilde Q}(\tilde X) = \tilde P\tilde X\tilde Q$ is the ordinary two-sided operator of the plain product.

**Proof.** Expanding the rule twice and using the anti-multiplicativity of the star and the identity $(\tilde X^{*})^{\natural} = \overline{\tilde X}$,

$$
L_{\tilde A}\bigl(L_{\tilde B}(\tilde X)\bigr) = \tilde A^{\natural}\bigl(\tilde B^{\natural}\tilde X^{*}\bigr)^{*} = \tilde A^{\natural}\,(\tilde X^{*})^{*}\,(\tilde B^{\natural})^{*} = \tilde A^{\natural}\,\tilde X\,\overline{\tilde B} ,
$$

which is $T_{\tilde A^{\natural},\overline{\tilde B}}(\tilde X)$. $\square$

### The Composition Leaves the Class

**Corollary.** The composition of two left multiplications is $\mathbb{C}$-linear, whereas every left multiplication is conjugate-linear; hence the composition is a left multiplication if and only if it is zero, and for nonzero $\tilde A, \tilde B$ it is not one. The class $\mathcal{L}$ is not closed under composition.

**Proof.** The operator $T_{\tilde A^{\natural},\overline{\tilde B}}$ is a plain two-sided multiplication and therefore $\mathbb{C}$-linear, being the composition of two $\mathbb{C}$-linear maps; but every element of $\mathcal{L}$ is conjugate-linear by the parity proposition. A map that is both $\mathbb{C}$-linear and conjugate-linear is zero, and the plain two-sided operator $T_{\tilde P,\tilde Q}$ vanishes identically only when $\tilde P = 0$ or $\tilde Q = 0$: a rank-one $\tilde X$ gives the value $\tilde P\tilde X\tilde Q$, a rank-one element of the matrix model of *The Quaternionic Sesquilinear Product in the 2×2 Matrix Model*, which is nonzero as soon as $\tilde P$ and $\tilde Q$ are. Hence for nonzero $\tilde A$ and $\tilde B$ the composition $T_{\tilde A^{\natural},\overline{\tilde B}}$ is a nonzero $\mathbb{C}$-linear operator and is not in $\mathcal{L}$. $\square$

**Remark.** The composition law is the reason the left multiplications do not form a monoid, and it is the same phenomenon as the failure of associativity read on the operators: the associator $\tilde A \star (\tilde B \star \tilde X) - (\tilde A \star \tilde B) \star \tilde X$ measures the difference between $L_{\tilde A} \circ L_{\tilde B}$ and $L_{\tilde A \star \tilde B}$, both of which are operators on $\tilde X$. The composition is a two-sided operator of the plain product, while the left multiplication of the product is a sandwich, and the two classes are disjoint.

### The Sandwich Algebra

**Theorem (the generated monoid).** The left multiplications are the sandwiches $L_{\tilde A} = S_{\tilde A^{\natural},e_0}$, and the monoid they generate under composition is the sandwich monoid of *The Sesquilinear Sandwich Operator*, the set

$$
\{ T_{\tilde P,\tilde Q} : \tilde P, \tilde Q \in \mathbb{B} \} \cup \{ S_{a,b} : a, b \in \mathbb{B} \} ,
$$

with unit $T_{e_0,e_0} = \mathrm{id}$.

**Proof.** The identification $L_{\tilde A} = S_{\tilde A^{\natural},e_0}$ is the closed form of the first proposition. The composition table of *The Sesquilinear Sandwich Operator* gives $S_{a,b} \circ S_{c,d} = T_{a d^{*},\, c^{*} b}$ and $T_{p,q} \circ T_{r,s} = T_{pr,\, sq}$, so the product of two left multiplications is

$$
S_{\tilde A^{\natural},e_0} \circ S_{\tilde B^{\natural},e_0}
= T_{\tilde A^{\natural} e_0^{*},\, (\tilde B^{\natural})^{*} e_0} 
= T_{\tilde A^{\natural},\,\overline{\tilde B}} ,
$$

in agreement with the composition law above; the products of a sandwich and a two-sided operator are a sandwich, by the same table, and the two-sided operators close among themselves. The generated set is therefore the union displayed, and it is a monoid with unit $T_{e_0,e_0}$, the identity operator. $\square$

**Remark.** The composition of two conjugate-linear operators is linear, which is the passage from the two sandwiches to the two-sided operator $T_{\tilde A^{\natural},\overline{\tilde B}}$; this is the same computation as the composition of two elements of $\mathcal{L}$, and it shows that the operator closure of the multiplication is a different, larger structure than the multiplication. The multiplication's left multiplications are the sandwiches with second parameter $e_0$, and the sandwich monoid is their operator closure.

## The Other Compositions

### The Composition of Two Right Multiplications

**Theorem.** For all $\tilde A, \tilde B$,

$$
R_{\tilde A} \circ R_{\tilde B} = T_{\overline{\tilde B},\,\tilde A^{*}} .
$$

**Proof.** Expanding, $R_{\tilde A}(R_{\tilde B}(\tilde X)) = (\tilde X^{\natural}\tilde B^{*})^{\natural}\tilde A^{*} = (\tilde B^{*})^{\natural}(\tilde X^{\natural})^{\natural}\tilde A^{*} = \overline{\tilde B}\,\tilde X\,\tilde A^{*}$, using the anti-multiplicativity of ${}^{\natural}$ and $(\tilde B^{*})^{\natural} = \overline{\tilde B}$. $\square$

**Corollary.** The composition of two right multiplications is $\mathbb{C}$-linear, and every right multiplication is itself $\mathbb{C}$-linear, so parity alone does not separate the two classes here; the class is nevertheless not closed under composition, and the smallest witness is $R_{e_0} \circ R_{e_0} = \mathrm{id} \notin \mathcal{R}$. In general $R_{\tilde A}\circ R_{\tilde B} = R_{\tilde C}$ would require

$$
\tilde X^{\natural}\tilde C^{*} = \overline{\tilde B}\,\tilde X\,\tilde A^{*}
$$

for every $\tilde X$; at $\tilde X = e_0$ this gives $\tilde C^{*} = \overline{\tilde B}\tilde A^{*}$, and at $\tilde X = e_k$ it gives $\overline{\tilde B}e_k\tilde A^{*} + e_k\overline{\tilde B}\tilde A^{*} = 0$. When $\tilde A$ is a unit of the algebra these conditions force $\tilde B = 0$, so with $\tilde A$ invertible the only composition $R_{\tilde A}\circ R_{\tilde B}$ that is a right multiplication is the zero operator.

**Proof.** The composition is the plain two-sided operator $T_{\overline{\tilde B},\tilde A^{*}}$, which is linear, so the parity argument of the left case is unavailable. For the witness, $R_{e_0}(\tilde X) = \tilde X^{\natural}$, so $R_{e_0}\bigl(R_{e_0}(\tilde X)\bigr) = (\tilde X^{\natural})^{\natural} = \tilde X$; if this were $R_{\tilde C}$ then at $\tilde X = e_0$ it would give $\tilde C^{*} = e_0$ and at $\tilde X = e_1$ it would give $e_1^{\natural}\tilde C^{*} = -e_1$, contradicting $\tilde C^{*} = e_0$. For the general condition, write $P = \overline{\tilde B}$ and $Z = \tilde A^{*}$; the three conditions read $(Pe_k + e_kP)Z = 0$, and $Pe_k + e_kP = 2p_0e_k - 2p_ke_0$ for $P = \sum_\mu p_\mu e_\mu$. If $\tilde A$ is a unit then $Z$ is invertible, so $p_0e_k - p_ke_0 = 0$ for $k = 1, 2, 3$, hence $p_0 = p_1 = p_2 = p_3 = 0$ and $P = 0$, that is $\tilde B = 0$. $\square$

### The Mixed Compositions

**Theorem (the mixed products).** For all $\tilde A, \tilde B$ and every $\tilde X$,

$$
L_{\tilde A}\bigl(R_{\tilde B}(\tilde X)\bigr) = \tilde A^{\natural}\tilde B\,\overline{\tilde X} , \qquad R_{\tilde B}\bigl(L_{\tilde A}(\tilde X)\bigr) = \overline{\tilde X}\,\tilde A\,\tilde B^{*} ,
$$

both operators being conjugate-linear in $\tilde X$.

**Proof.** For the first, $L_{\tilde A}(R_{\tilde B}(\tilde X)) = \tilde A^{\natural}(\tilde X^{\natural}\tilde B^{*})^{*} = \tilde A^{\natural}(\tilde B^{*})^{*}(\tilde X^{\natural})^{*} = \tilde A^{\natural}\tilde B\overline{\tilde X}$. For the second, $R_{\tilde B}(L_{\tilde A}(\tilde X)) = (\tilde A^{\natural}\tilde X^{*})^{\natural}\tilde B^{*} = (\tilde X^{*})^{\natural}(\tilde A^{\natural})^{\natural}\tilde B^{*} = \overline{\tilde X}\,\tilde A\,\tilde B^{*}$. $\square$

**Remark.** The mixed composites are conjugate-linear two-sided operators of the form $C\,\overline{\tilde X}$ and $\overline{\tilde X}\,C'$; they are not sandwiches, whose form is $a\tilde X^{*}b$, and they are not two-sided multiplications, which are linear. They are the remaining composite class, and they complete the four-product table of the compositions below.

### The Table of the Four Compositions

**Theorem.** The compositions of the two families are as follows, with the parity of each result and whether it lies in $\mathcal{L}$, in $\mathcal{R}$, in neither, or in both:

| composition | value | parity | class |
|---|---|---|---|
| $L_{\tilde A} \circ L_{\tilde B}$ | $T_{\tilde A^{\natural},\,\overline{\tilde B}}(\tilde X) = \tilde A^{\natural}\tilde X\overline{\tilde B}$ | $\mathbb{C}$-linear | neither |
| $R_{\tilde A} \circ R_{\tilde B}$ | $T_{\overline{\tilde B},\,\tilde A^{*}}(\tilde X) = \overline{\tilde B}\tilde X\tilde A^{*}$ | $\mathbb{C}$-linear | neither |
| $L_{\tilde A} \circ R_{\tilde B}$ | $\tilde A^{\natural}\tilde B\,\overline{\tilde X}$ | conjugate-linear | neither |
| $R_{\tilde B} \circ L_{\tilde A}$ | $\overline{\tilde X}\,\tilde A\,\tilde B^{*}$ | conjugate-linear | neither |

**Proof.** The four values are the four theorems above. For the class: a left multiplication is conjugate-linear and a right multiplication is linear, so a $\mathbb{C}$-linear composite cannot be a left multiplication and a conjugate-linear composite cannot be a right multiplication; the two linear composites are excluded from the class of the left multiplications by the same parity, and from the class of the right multiplications by the closed-form tests of the two corollaries above. $\square$

**Remark.** Apart from the degenerate composite of the zero multiplications, no composition of two multiplication operators is again a multiplication operator — the closest the family comes is $R_{e_0} \circ R_{e_0} = \mathrm{id}$, and the identity is not a multiplication operator either — so neither family is closed and neither is a monoid; the only element common to $\mathcal{L}$ and $\mathcal{R}$ is zero, since a map that is both linear and conjugate-linear is zero. The table is the operator form of the group's negative statements: the absence of a unit, the failure of associativity and the failure of flexibility all read as the failure of the operator families to close.

## The Absence of a Monoid

### The Failure of Closure

**Theorem.** Neither the left multiplications nor the right multiplications form a monoid under composition.

**Proof.** A monoid of operators requires closure under composition and an identity in the class. The left multiplications are not closed, by the corollary after the composition law; the right multiplications are not closed, by the corollary after their composition law. For the identity, no $L_{\tilde A}$ is the identity operator, since $L_{\tilde A}(\tilde X) = \tilde A^{\natural}\tilde X^{*}$ equals $\tilde X$ for all $\tilde X$ only if $\tilde A^{\natural} = e_0$ and $\tilde X^{*} = \tilde X$ for all $\tilde X$, which fails; and no $R_{\tilde A}$ is the identity for the same reason. $\square$

**Remark.** The identity of the operator monoid is the plain two-sided operator $T_{e_0,e_0}$, which is the identity of the sandwich monoid and is not a multiplication operator of the product; the left and right multiplications sit inside the sandwich monoid and generate it, but they do not contain its identity. This is the operator-level form of the absence of a unit of the multiplication.

### The Regular Map Is Not Multiplicative

**Proposition.** The regular map $\ell : \mathbb{B} \to \operatorname{End}(\mathbb{B})$, $\tilde A \mapsto L_{\tilde A}$, is injective and $\mathbb{C}$-linear, but it is not multiplicative,

$$
\ell(\tilde A)\ell(\tilde B) = T_{\tilde A^{\natural},\,\overline{\tilde B}} \neq L_{\tilde A \star \tilde B} = L_{\tilde A^{\natural}\tilde B^{*}} ,
$$

for generic $\tilde A, \tilde B$.

**Proof.** The injectivity and the linearity are the two propositions of the parity section; the equality $\ell(\tilde A)\ell(\tilde B) = T_{\tilde A^{\natural},\overline{\tilde B}}$ is the composition law; the value $L_{\tilde A\star\tilde B}$ is the left multiplication by the product. The two operators differ, one being linear and the other conjugate-linear, except for vanishing parameters. $\square$

**Remark.** A regular map that is linear and injective but not multiplicative is a **linear embedding of the module that is not a representation of the multiplication**, and it is the exact operator form of the statement that $\mathbb{B}$ is not a module over $(\mathbb{B},\star)$: the module axiom $L_{\tilde A}L_{\tilde B} = L_{\tilde A\star\tilde B}$ fails. The associator of *The Associator of the Quaternionic Sesquilinear Product* is the obstruction, since the associator's vanishing is exactly the multiplicativity of the regular map.

### The Comparison with the Four Products

**Theorem (the left multiplications of the four products).**

| product | $L_{\tilde A}(\tilde X)$ | parity | $L_{\tilde A} \circ L_{\tilde B}$ | monoid |
|---|---|---|---|---|
| $\tilde A\tilde X$ | $\tilde A\tilde X$ | $\mathbb{C}$-linear | $L_{\tilde A\tilde B}$ | yes |
| $\tilde A^{\natural}\tilde X$ | $\tilde A^{\natural}\tilde X$ | $\mathbb{C}$-linear | $L^{\natural}_{\tilde B\tilde A}$ | yes, opposite |
| $\tilde A\tilde X^{*}$ | $\tilde A\tilde X^{*}$ | conjugate-linear | $\tilde A\tilde X\tilde B^{*}$ | no |
| $\tilde A^{\natural}\tilde X^{*}$ | $\tilde A^{\natural}\tilde X^{*}$ | conjugate-linear | $\tilde A^{\natural}\tilde X\overline{\tilde B}$ | no |

**Proof.** The first row is the associativity of the plain product. The second is the composition $L^{\natural}_{\tilde A}L^{\natural}_{\tilde B}(\tilde X) = \tilde A^{\natural}\tilde B^{\natural}\tilde X = (\tilde B\tilde A)^{\natural}\tilde X = L^{\natural}_{\tilde B\tilde A}(\tilde X)$, which is the opposite monoid (*Biquaternions as a General Quaternionic Algebra (GQA) over $\mathbb{C}$*) and is recorded in *Relations Between the Four Biquaternion Products* §*The Left Multiplications*. The third is the sibling sesquilinear composition $L^{*}_{\tilde A}L^{*}_{\tilde B}(\tilde X) = \tilde A(\tilde B\tilde X^{*})^{*} = \tilde A\tilde X\tilde B^{*}$, which is $\mathbb{C}$-linear whereas $L^{*}$ is conjugate-linear, so the class is not closed. The fourth is the composition law of this article. $\square$

**Remark.** The comparison is the row of *Comparison Between the Four Biquaternion Products* that reads the monoid property, and it separates the four products into two classes: the two bilinear products, whose left multiplications form monoids, and the two sesquilinear products, whose left multiplications do not. The dividing line is the parity of the left multiplication: it is linear for the bilinear products, so that the composition of two of them has the same parity as the factors and stays in the class, and conjugate-linear for the sesquilinear products, so that the composition has the opposite parity and leaves the class.

## Worked Cases

### The Unit Candidate

**Proposition.** At $\tilde A = e_0$ the two multiplications are the two conjugations,

$$
L_{e_0} = {}^{*} , \qquad R_{e_0} = {}^{\natural} ,
$$

and they satisfy $L_{e_0}^{2} = R_{e_0}^{2} = \mathrm{id}$ and $L_{e_0} \circ R_{e_0} = R_{e_0} \circ L_{e_0} = \bar{\cdot}$, the coefficientwise conjugation.

**Proof.** The first two are the two actions of $e_0$ (*The Two One-Sided Actions and the Absence of a Unit*). For the squares, the composition law gives $L_{e_0}^{2} = T_{e_0^{\natural},\overline{e_0}} = T_{e_0,e_0} = \mathrm{id}$ and $R_{e_0}^{2} = T_{\overline{e_0},e_0^{*}} = T_{e_0,e_0} = \mathrm{id}$. For the mixed product, $L_{e_0}(R_{e_0}(\tilde X)) = e_0^{\natural}e_0\overline{\tilde X} = \overline{\tilde X}$, and $R_{e_0}(L_{e_0}(\tilde X)) = \overline{\tilde X}e_0e_0^{*} = \overline{\tilde X}$. $\square$

**Remark.** The operator identity $\mathrm{id}$ is the composition $L_{e_0}^{2}$, and it is not a left multiplication; this is the smallest instance of the failure of closure, and it is the operator form of the absence of a unit: the closest the family comes to containing the identity is the square of the left multiplication by $e_0$.

### The Idempotents and the Units

**Proposition.** Let $\tilde\Pi$ be a nontrivial idempotent of the multiplication, $\tilde\Pi \star \tilde\Pi = \tilde\Pi$. Then

$$
L_{\tilde\Pi}(\tilde\Pi) = \tilde\Pi , \qquad L_{\tilde\Pi}\bigl(\tilde\Pi^{\natural}\bigr) = N(\tilde\Pi)\,e_0 . 
$$

**Proof.** The first is the idempotent equation, $L_{\tilde\Pi}(\tilde\Pi) = \tilde\Pi \star \tilde\Pi = \tilde\Pi$. For the second, the nontrivial idempotents have real coordinates (*Idempotents of the Quaternionic Sesquilinear Product*), so $\overline{\tilde\Pi} = \tilde\Pi$ and $(\tilde\Pi^{\natural})^{*} = \overline{\tilde\Pi} = \tilde\Pi$; hence $L_{\tilde\Pi}(\tilde\Pi^{\natural}) = \tilde\Pi^{\natural}(\tilde\Pi^{\natural})^{*} = \tilde\Pi^{\natural}\tilde\Pi = N(\tilde\Pi)e_0$, the plain product of an element with its natural conjugate being the norm times the identity. $\square$

**Remark.** With $N(\tilde\Pi) = 1$ for the nontrivial idempotents of *Idempotents of the Quaternionic Sesquilinear Product*, the second value is $e_0$, and the two values together show that the left multiplication by an idempotent fixes the idempotent and sends its natural conjugate to the identity. This is the operator reading of the two-sided nature of an idempotent, and it is the closest the operator theory comes to the unit that the multiplication does not have.

## Summary

The left and right multiplications of the complex quaternionic sesquilinear multiplication are $L_{\tilde A}(\tilde X) = \tilde A^{\natural}\tilde X^{*}$ and $R_{\tilde A}(\tilde X) = \tilde X^{\natural}\tilde A^{*}$. The left multiplication is conjugate-linear and the right one is linear; the map $\tilde A \mapsto L_{\tilde A}$ is $\mathbb{C}$-linear and the map $\tilde A \mapsto R_{\tilde A}$ is conjugate-linear, both injective, so the two families are two different images of $\mathbb{B}$ and not a single regular representation. The composition laws are $L_{\tilde A} \circ L_{\tilde B} = T_{\tilde A^{\natural},\overline{\tilde B}}$ and $R_{\tilde A} \circ R_{\tilde B} = T_{\overline{\tilde B},\tilde A^{*}}$, both compositions $\mathbb{C}$-linear; the mixed compositions $L_{\tilde A}R_{\tilde B} = \tilde A^{\natural}\tilde B\overline{\tilde X}$ and $R_{\tilde B}L_{\tilde A} = \overline{\tilde X}\tilde A\tilde B^{*}$ are conjugate-linear. Since every left multiplication is conjugate-linear and every right one is linear, the compositions leave the two classes, and neither family is closed under composition or contains an identity: neither is a monoid. The left multiplications are the sandwiches $S_{\tilde A^{\natural},e_0}$, and the monoid they generate is the sandwich monoid of *The Sesquilinear Sandwich Operator*, whose identity is the ordinary two-sided operator $T_{e_0,e_0}$. The regular map is a linear injection that is not multiplicative, which is the operator form of the failure of associativity, and the four products split into the two bilinear ones, whose left multiplications form monoids, and the two sesquilinear ones, whose left multiplications do not.

## Summary of Notation

| symbol | meaning |
|---|---|
| $L_{\tilde A}(\tilde X) = \tilde A \star \tilde X = \tilde A^{\natural}\tilde X^{*}$ | the left multiplication, conjugate-linear |
| $R_{\tilde A}(\tilde X) = \tilde X \star \tilde A = \tilde X^{\natural}\tilde A^{*}$ | the right multiplication, linear |
| $L_{\tilde A} = S_{\tilde A^{\natural},e_0}$ | the left multiplication as a sandwich |
| $T_{\tilde P,\tilde Q}(\tilde X) = \tilde P\tilde X\tilde Q$ | the ordinary two-sided operator |
| $L_{\tilde A} \circ L_{\tilde B} = T_{\tilde A^{\natural},\overline{\tilde B}}$ | the composition of two left multiplications |
| $R_{\tilde A} \circ R_{\tilde B} = T_{\overline{\tilde B},\tilde A^{*}}$ | the composition of two right multiplications |
| $L_{\tilde A} \circ R_{\tilde B} = \tilde A^{\natural}\tilde B\overline{\tilde X}$ | a mixed composition, conjugate-linear |
| $R_{\tilde B} \circ L_{\tilde A} = \overline{\tilde X}\tilde A\tilde B^{*}$ | the other mixed composition |
| $\ell : \tilde A \mapsto L_{\tilde A}$ | the regular map, linear and injective but not multiplicative |
| $L_{e_0} = {}^{*}$, $R_{e_0} = {}^{\natural}$ | the two actions of the unit candidate |

## Further Reading

- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the regular representation of an algebra and the multiplication operators.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the structure of the multiplication operators and the Peirce decomposition of an algebra by them.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the semilinear operators attached to an algebra with an involution.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the operator closure of a non-associative multiplication and the derivations it generates.
