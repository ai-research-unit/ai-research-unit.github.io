
# __The Left and Right Multiplications of the General Quaternionic Sesquilinear Product__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ carries four general products on its underlying $\mathbb{C}$-vector space (*The Four General Products of the Biquaternion $\mathbb{C}$ Space*), and the fourth of them,

$$
\tilde Q_1 \star \tilde Q_2 = \tilde Q_1^{\natural}\tilde Q_2^{*} ,
$$

is the subject of this group. The rule and the scalar–vector form are *The Four General Products of the Biquaternion $\mathbb{C}$ Space* §*The General Quaternionic Sesquilinear Product*; the sesqualgebra it defines and its one-sided actions of the unit are *Introduction to the General Quaternionic Sesqualgebra*; the associator is *The Associator of the General Quaternionic Sesquilinear Product*. The symbols are those of the group: ${}^{\natural}$ is the natural conjugation $\tilde Q^{\natural} = Q_t - \vec Q$, ${}^{*}$ is the star conjugation, and the bar is the coefficientwise complex conjugation.

The subject of this article is the pair of **multiplication operators** attached to the multiplication,

$$
L_{\tilde Q_5}(\tilde Q_1) = \tilde Q_5 \star \tilde Q_1 = \tilde Q_5^{\natural}\tilde Q_1^{*} , \qquad R_{\tilde Q_5}(\tilde Q_1) = \tilde Q_1 \star \tilde Q_5 = \tilde Q_1^{\natural}\tilde Q_5^{*} ,
$$

the left and the right multiplication by a fixed element. The left multiplication is conjugate-linear in its argument, the right multiplication is linear, and this asymmetry, together with the absence of a unit (*The Two One-Sided Actions and the Absence of a Unit*) and the failure of associativity, makes the family of these operators the smallest nontrivial operator theory of the batch. The article establishes three things. First, the parities: the map $\tilde Q_5 \mapsto L_{\tilde Q_5}$ is $\mathbb{C}$-linear and the map $\tilde Q_5 \mapsto R_{\tilde Q_5}$ is conjugate-linear, so the two families are two different images of $\mathbb{B}$ rather than a single regular representation. Second, the composition laws:

$$
L_{\tilde Q_5} \circ L_{\tilde Q_2} = T_{\tilde Q_5^{\natural},\,\overline{\tilde Q_2}} , \qquad R_{\tilde Q_5} \circ R_{\tilde Q_2} = T_{\overline{\tilde Q_2},\,\tilde Q_5^{*}} ,
$$

where $T_{\tilde Q_1,\tilde Q_2}(\tilde Q_3) = \tilde Q_1\tilde Q_3\tilde Q_2$ is the ordinary two-sided operator. Third, the **absence of a monoid**: the composition of two left multiplications is $\mathbb{C}$-linear whereas every left multiplication is conjugate-linear, so the class is not closed under composition and the left multiplications do not form a monoid. They are sandwiches in the sense of *The Sesquilinear Sandwich Operator*, $L_{\tilde Q_5} = S_{\tilde Q_5^{\natural},e_t}$, and the monoid they generate is the sandwich monoid of that article.

The article owns the two families, their parities, their composition laws and the failure of the monoid property. It cites the general operator theory to *The Left and Right Multiplication Operators of a Sesqualgebra*; it cites the sandwich and its composition table to *The Sesquilinear Sandwich Operator*; it cites the composition of the left multiplications of the four general products to *Relations Between the Four General Products* §*The Left Multiplications*; and it does not treat the ternary operator, which is *The Ternary Product and the Failure of the Jordan Triple Identity*, nor the matrix realization, which is *The General Quaternionic Sesquilinear Product in the 2×2 Matrix Model*.

## The Two Families

### The Definitions

**Definition.** The **left multiplication** by $\tilde Q_5$ and the **right multiplication** by $\tilde Q_5$ are

$$
L_{\tilde Q_5}(\tilde Q_1) = \tilde Q_5 \star \tilde Q_1 = \tilde Q_5^{\natural}\tilde Q_1^{*} , \qquad R_{\tilde Q_5}(\tilde Q_1) = \tilde Q_1 \star \tilde Q_5 = \tilde Q_1^{\natural}\tilde Q_5^{*} .
$$

The two families are $\mathcal{L} = \{ L_{\tilde Q_5} : \tilde Q_5 \in \mathbb{B} \}$ and $\mathcal{R} = \{ R_{\tilde Q_5} : \tilde Q_5 \in \mathbb{B} \}$.

**Proposition (the closed forms).** For every $\tilde Q_5$ and $\tilde Q_1$,

$$
L_{\tilde Q_5}(\tilde Q_1) = \tilde Q_5^{\natural}\tilde Q_1^{*} = S_{\tilde Q_5^{\natural},\,e_t}(\tilde Q_1) , \qquad R_{\tilde Q_5}(\tilde Q_1) = \tilde Q_1^{\natural}\tilde Q_5^{*} ,
$$

where $S_{a,b}(\tilde Q_1) = a\tilde Q_1^{*}b$ is the sesquilinear sandwich of *The Sesquilinear Sandwich Operator*; so every left multiplication is the sandwich with parameters $\tilde Q_5^{\natural}$ and $e_t$.

**Proof.** The first display is the rule; the sandwich with second parameter $e_t$ is $a\tilde Q_1^{*}e_t = a\tilde Q_1^{*}$, which is the left multiplication with $a = \tilde Q_5^{\natural}$. The second display is the rule read on the right slot.

**Remark.** The left multiplication is a sandwich and the right multiplication is not: $R_{\tilde Q_5}(\tilde Q_1) = \tilde Q_1^{\natural}\tilde Q_5^{*}$ carries the natural conjugation in the first factor rather than the star in the middle, and it is a $\mathbb{C}$-linear operator, whereas every sandwich is conjugate-linear. The asymmetry of the two slots of the multiplication therefore appears at the operator level as the asymmetry between a sandwich and a linear two-sided operator.

### The Parities

**Proposition (the parities of the operators).** For every $\tilde Q_5$, the operator $L_{\tilde Q_5}$ is **conjugate-linear** and the operator $R_{\tilde Q_5}$ is $\mathbb{C}$-**linear**:

$$
L_{\tilde Q_5}(\lambda\tilde Q_1) = \bar\lambda\, L_{\tilde Q_5}(\tilde Q_1) , \qquad R_{\tilde Q_5}(\lambda\tilde Q_1) = \lambda\, R_{\tilde Q_5}(\tilde Q_1) .
$$

**Proof.** $L_{\tilde Q_5}(\tilde Q_1) = \tilde Q_5^{\natural}\tilde Q_1^{*}$ and the star conjugation is conjugate-linear, $(\lambda\tilde Q_1)^{*} = \bar\lambda\tilde Q_1^{*}$, while $\tilde Q_5^{\natural}$ is fixed; hence the first identity. $R_{\tilde Q_5}(\tilde Q_1) = \tilde Q_1^{\natural}\tilde Q_5^{*}$ and the natural conjugation is $\mathbb{C}$-linear, $(\lambda\tilde Q_1)^{\natural} = \lambda\tilde Q_1^{\natural}$, and $\tilde Q_5^{*}$ is fixed; hence the second.

**Proposition (the parities of the parametrisations).** The map $\tilde Q_5 \mapsto L_{\tilde Q_5}$ is injective and $\mathbb{C}$-**linear**, and the map $\tilde Q_5 \mapsto R_{\tilde Q_5}$ is injective and **conjugate-linear**.

**Proof.** For the linearity of the first, $L_{\tilde Q_5 + \lambda\tilde Q_2}(\tilde Q_1) = (\tilde Q_5 + \lambda\tilde Q_2)^{\natural}\tilde Q_1^{*} = \tilde Q_5^{\natural}\tilde Q_1^{*} + \lambda\tilde Q_2^{\natural}\tilde Q_1^{*}$; the natural conjugation is $\mathbb{C}$-linear, so $(\lambda\tilde Q_2)^{\natural} = \lambda\tilde Q_2^{\natural}$ and $L_{\tilde Q_5+\lambda\tilde Q_2} = L_{\tilde Q_5} + \lambda L_{\tilde Q_2}$. Injectivity: $L_{\tilde Q_5} = 0$ means $\tilde Q_5^{\natural}\tilde Q_1^{*} = 0$ for every $\tilde Q_1$, which at $\tilde Q_1 = e_t$ gives $\tilde Q_5^{\natural} = 0$, hence $\tilde Q_5 = 0$. For the second, $R_{\tilde Q_5+\lambda\tilde Q_2}(\tilde Q_1) = \tilde Q_1^{\natural}(\tilde Q_5 + \lambda\tilde Q_2)^{*} = \tilde Q_1^{\natural}\tilde Q_5^{*} + \bar\lambda\tilde Q_1^{\natural}\tilde Q_2^{*}$, since the star is conjugate-linear; injectivity is as before at $\tilde Q_1 = e_t$.

**Remark.** The two families are therefore two different images of $\mathbb{B}$: the left one is a $\mathbb{C}$-linear image inside the conjugate-linear endomorphisms, and the right one a conjugate-linear image inside the linear endomorphisms. The left family is a copy of $\mathbb{B}$ and not a representation of the multiplication, because the multiplication is not associative; the right family is the conjugate copy. This is the operator-level reason the group has no regular representation in the sense of an algebra, and it is the first of the two negative results of the article.

### The Two Families in the Plain Operators

Writing $\lambda_{\tilde Q_5}(\tilde Q_1) = \tilde Q_5\tilde Q_1$ and $\rho_{\tilde Q_5}(\tilde Q_1) = \tilde Q_1\tilde Q_5$ for the left and right multiplications of the plain product, the two multiplication operators are the plain multiplications composed with the two conjugations:

$$
L_{\tilde Q_5} = \lambda_{\tilde Q_5^{\natural}} \circ {}^{*} , \qquad R_{\tilde Q_5} = \rho_{\tilde Q_5^{*}} \circ {}^{\natural} .
$$

**Proposition.** The left multiplication is the plain left multiplication by $\tilde Q_5^{\natural}$ after the star conjugation, and the right multiplication is the plain right multiplication by $\tilde Q_5^{*}$ after the natural conjugation.

**Proof.** $\lambda_{\tilde Q_5^{\natural}}(\tilde Q_1^{*}) = \tilde Q_5^{\natural}\tilde Q_1^{*} = L_{\tilde Q_5}(\tilde Q_1)$, and $\rho_{\tilde Q_5^{*}}(\tilde Q_1^{\natural}) = \tilde Q_1^{\natural}\tilde Q_5^{*} = R_{\tilde Q_5}(\tilde Q_1)$.

**Remark.** The reading is the one of *Relations Between the Four General Products* §*The Left Multiplications*: the left multiplication of the fourth product is a plain multiplication re-indexed by the natural sign and composed with the star, while the right multiplication is the conjugate of a plain right multiplication re-indexed. The re-indexing by ${}^{\natural}$ is the operator form of the isotope by which the fourth product differs from the derived operation (*The Two One-Sided Actions and the Absence of a Unit*), and the asymmetric placement of the two conjugations is the operator form of the two different slots of the multiplication.

## The Composition of Two Left Multiplications

### The Law

**Theorem (the composition).** For all $\tilde Q_5, \tilde Q_2$,

$$
\boxed{\; L_{\tilde Q_5} \circ L_{\tilde Q_2} = T_{\tilde Q_5^{\natural},\,\overline{\tilde Q_2}} \;},
$$

where $T_{\tilde Q_1,\tilde Q_2}(\tilde Q_3) = \tilde Q_1\tilde Q_3\tilde Q_2$ is the ordinary two-sided operator of the plain product.

**Proof.** Expanding the rule twice and using the anti-multiplicativity of the star and the identity $(\tilde Q_1^{*})^{\natural} = \overline{\tilde Q_1}$,

$$
L_{\tilde Q_5}\bigl(L_{\tilde Q_2}(\tilde Q_1)\bigr) = \tilde Q_5^{\natural}\bigl(\tilde Q_2^{\natural}\tilde Q_1^{*}\bigr)^{*} = \tilde Q_5^{\natural}\,(\tilde Q_1^{*})^{*}\,(\tilde Q_2^{\natural})^{*} = \tilde Q_5^{\natural}\,\tilde Q_1\,\overline{\tilde Q_2} ,
$$

which is $T_{\tilde Q_5^{\natural},\overline{\tilde Q_2}}(\tilde Q_1)$.

### The Composition Leaves the Class

**Corollary.** The composition of two left multiplications is $\mathbb{C}$-linear, whereas every left multiplication is conjugate-linear; hence the composition is a left multiplication if and only if it is zero, and for nonzero $\tilde Q_5, \tilde Q_2$ it is not one. The class $\mathcal{L}$ is not closed under composition.

**Proof.** The operator $T_{\tilde Q_5^{\natural},\overline{\tilde Q_2}}$ is a plain two-sided multiplication and therefore $\mathbb{C}$-linear, being the composition of two $\mathbb{C}$-linear maps; but every element of $\mathcal{L}$ is conjugate-linear by the parity proposition. A map that is both $\mathbb{C}$-linear and conjugate-linear is zero, and the plain two-sided operator $T_{\tilde Q_1,\tilde Q_2}$ vanishes identically only when $\tilde Q_1 = 0$ or $\tilde Q_2 = 0$: a rank-one $\tilde Q_3$ gives the value $\tilde Q_1\tilde Q_3\tilde Q_2$, a rank-one element of the matrix model of *The General Quaternionic Sesquilinear Product in the 2×2 Matrix Model*, which is nonzero as soon as $\tilde Q_1$ and $\tilde Q_2$ are. Hence for nonzero $\tilde Q_5$ and $\tilde Q_2$ the composition $T_{\tilde Q_5^{\natural},\overline{\tilde Q_2}}$ is a nonzero $\mathbb{C}$-linear operator and is not in $\mathcal{L}$.

**Remark.** The composition law is the reason the left multiplications do not form a monoid, and it is the same phenomenon as the failure of associativity read on the operators: the associator $\tilde Q_5 \star (\tilde Q_2 \star \tilde Q_1) - (\tilde Q_5 \star \tilde Q_2) \star \tilde Q_1$ measures the difference between $L_{\tilde Q_5} \circ L_{\tilde Q_2}$ and $L_{\tilde Q_5 \star \tilde Q_2}$, both of which are operators on $\tilde Q_1$. The composition is a two-sided operator of the plain product, while the left multiplication of the product is a sandwich, and the two classes are disjoint.

### The Sandwich Algebra

**Theorem (the generated monoid).** The left multiplications are the sandwiches $L_{\tilde Q_5} = S_{\tilde Q_5^{\natural},e_t}$, and the monoid they generate under composition is the sandwich monoid of *The Sesquilinear Sandwich Operator*, the set

$$
\{ T_{\tilde Q_1,\tilde Q_2} : \tilde Q_1, \tilde Q_2 \in \mathbb{B} \} \cup \{ S_{a,b} : a, b \in \mathbb{B} \} ,
$$

with unit $T_{e_t,e_t} = \mathrm{id}$.

**Proof.** The identification $L_{\tilde Q_5} = S_{\tilde Q_5^{\natural},e_t}$ is the closed form of the first proposition. The composition table of *The Sesquilinear Sandwich Operator* gives $S_{a,b} \circ S_{c,d} = T_{a d^{*},\, c^{*} b}$ and $T_{p,q} \circ T_{r,s} = T_{pr,\, sq}$, so the product of two left multiplications is

$$
S_{\tilde Q_5^{\natural},e_t} \circ S_{\tilde Q_2^{\natural},e_t}
= T_{\tilde Q_5^{\natural} e_t^{*},\, (\tilde Q_2^{\natural})^{*} e_t} 
= T_{\tilde Q_5^{\natural},\,\overline{\tilde Q_2}} ,
$$

in agreement with the composition law above; the products of a sandwich and a two-sided operator are a sandwich, by the same table, and the two-sided operators close among themselves. The generated set is therefore the union displayed, and it is a monoid with unit $T_{e_t,e_t}$, the identity operator.

**Remark.** The composition of two conjugate-linear operators is linear, which is the passage from the two sandwiches to the two-sided operator $T_{\tilde Q_5^{\natural},\overline{\tilde Q_2}}$; this is the same computation as the composition of two elements of $\mathcal{L}$, and it shows that the operator closure of the multiplication is a different, larger structure than the multiplication. The multiplication's left multiplications are the sandwiches with second parameter $e_t$, and the sandwich monoid is their operator closure.

## The Other Compositions

### The Composition of Two Right Multiplications

**Theorem.** For all $\tilde Q_5, \tilde Q_2$,

$$
\boxed{\; R_{\tilde Q_5} \circ R_{\tilde Q_2} = T_{\overline{\tilde Q_2},\,\tilde Q_5^{*}} \;}.
$$

**Proof.** Expanding, $R_{\tilde Q_5}(R_{\tilde Q_2}(\tilde Q_1)) = (\tilde Q_1^{\natural}\tilde Q_2^{*})^{\natural}\tilde Q_5^{*} = (\tilde Q_2^{*})^{\natural}(\tilde Q_1^{\natural})^{\natural}\tilde Q_5^{*} = \overline{\tilde Q_2}\,\tilde Q_1\,\tilde Q_5^{*}$, using the anti-multiplicativity of ${}^{\natural}$ and $(\tilde Q_2^{*})^{\natural} = \overline{\tilde Q_2}$.

**Corollary.** The composition of two right multiplications is $\mathbb{C}$-linear, and every right multiplication is itself $\mathbb{C}$-linear, so parity alone does not separate the two classes here; the class is nevertheless not closed under composition, and the smallest witness is $R_{e_t} \circ R_{e_t} = \mathrm{id} \notin \mathcal{R}$. In general $R_{\tilde Q_5}\circ R_{\tilde Q_2} = R_{\tilde Q_3}$ would require

$$
\tilde Q_1^{\natural}\tilde Q_3^{*} = \overline{\tilde Q_2}\,\tilde Q_1\,\tilde Q_5^{*}
$$

for every $\tilde Q_1$; at $\tilde Q_1 = e_t$ this gives $\tilde Q_3^{*} = \overline{\tilde Q_2}\tilde Q_5^{*}$, and at $\tilde Q_1 = \vec e_k$ it gives $\overline{\tilde Q_2}\vec e_k\tilde Q_5^{*} + \vec e_k\overline{\tilde Q_2}\tilde Q_5^{*} = 0$. When $\tilde Q_5$ is a unit of the algebra these conditions force $\tilde Q_2 = 0$, so with $\tilde Q_5$ invertible the only composition $R_{\tilde Q_5}\circ R_{\tilde Q_2}$ that is a right multiplication is the zero operator.

**Proof.** The composition is the plain two-sided operator $T_{\overline{\tilde Q_2},\tilde Q_5^{*}}$, which is linear, so the parity argument of the left case is unavailable. For the witness, $R_{e_t}(\tilde Q_1) = \tilde Q_1^{\natural}$, so $R_{e_t}\bigl(R_{e_t}(\tilde Q_1)\bigr) = (\tilde Q_1^{\natural})^{\natural} = \tilde Q_1$; if this were $R_{\tilde Q_3}$ then at $\tilde Q_1 = e_t$ it would give $\tilde Q_3^{*} = e_t$ and at $\tilde Q_1 = \vec e_x$ it would give $\vec e_x^{\natural}\tilde Q_3^{*} = -\vec e_x$, contradicting $\tilde Q_3^{*} = e_t$. For the general condition, write $\tilde Q_4 = \overline{\tilde Q_2}$; the three conditions read $(\tilde Q_4\vec e_k + \vec e_k\tilde Q_4)\tilde Q_5^{*} = 0$, and $\tilde Q_4\vec e_k + \vec e_k\tilde Q_4 = 2Q_{4t}\vec e_k - 2Q_ke_t$ for $\tilde Q_4 = \sum_\mu Q_{4,\mu} e_\mu$. If $\tilde Q_5$ is a unit then $\tilde Q_5^{*}$ is invertible, so $Q_{4t}\vec e_k - Q_ke_t = 0$ for $k = 1, 2, 3$, hence $Q_{4t} = Q_{4x} = Q_{4y} = Q_{4z} = 0$ and $\tilde Q_4 = 0$, that is $\tilde Q_2 = 0$.

### The Mixed Compositions

**Theorem (the mixed products).** For all $\tilde Q_5, \tilde Q_2$ and every $\tilde Q_1$,

$$
\boxed{\; L_{\tilde Q_5}\bigl(R_{\tilde Q_2}(\tilde Q_1)\bigr) = \tilde Q_5^{\natural}\tilde Q_2\,\overline{\tilde Q_1} , \qquad R_{\tilde Q_2}\bigl(L_{\tilde Q_5}(\tilde Q_1)\bigr) = \overline{\tilde Q_1}\,\tilde Q_5\,\tilde Q_2^{*} \;},
$$

both operators being conjugate-linear in $\tilde Q_1$.

**Proof.** For the first, $L_{\tilde Q_5}(R_{\tilde Q_2}(\tilde Q_1)) = \tilde Q_5^{\natural}(\tilde Q_1^{\natural}\tilde Q_2^{*})^{*} = \tilde Q_5^{\natural}(\tilde Q_2^{*})^{*}(\tilde Q_1^{\natural})^{*} = \tilde Q_5^{\natural}\tilde Q_2\overline{\tilde Q_1}$. For the second, $R_{\tilde Q_2}(L_{\tilde Q_5}(\tilde Q_1)) = (\tilde Q_5^{\natural}\tilde Q_1^{*})^{\natural}\tilde Q_2^{*} = (\tilde Q_1^{*})^{\natural}(\tilde Q_5^{\natural})^{\natural}\tilde Q_2^{*} = \overline{\tilde Q_1}\,\tilde Q_5\,\tilde Q_2^{*}$.

**Remark.** The mixed composites are conjugate-linear two-sided operators of the form $C\,\overline{\tilde Q_1}$ and $\overline{\tilde Q_1}\,C'$; they are not sandwiches, whose form is $a\tilde Q_1^{*}b$, and they are not two-sided multiplications, which are linear. They are the remaining composite class, and they complete the four-product table of the compositions below.

### The Table of the Four Compositions

**Theorem.** The compositions of the two families are as follows, with the parity of each result and whether it lies in $\mathcal{L}$, in $\mathcal{R}$, in neither, or in both:

| composition | value | parity | class |
|---|---|---|---|
| $L_{\tilde Q_5} \circ L_{\tilde Q_2}$ | $T_{\tilde Q_5^{\natural},\,\overline{\tilde Q_2}}(\tilde Q_1) = \tilde Q_5^{\natural}\tilde Q_1\overline{\tilde Q_2}$ | $\mathbb{C}$-linear | neither |
| $R_{\tilde Q_5} \circ R_{\tilde Q_2}$ | $T_{\overline{\tilde Q_2},\,\tilde Q_5^{*}}(\tilde Q_1) = \overline{\tilde Q_2}\tilde Q_1\tilde Q_5^{*}$ | $\mathbb{C}$-linear | neither |
| $L_{\tilde Q_5} \circ R_{\tilde Q_2}$ | $\tilde Q_5^{\natural}\tilde Q_2\,\overline{\tilde Q_1}$ | conjugate-linear | neither |
| $R_{\tilde Q_2} \circ L_{\tilde Q_5}$ | $\overline{\tilde Q_1}\,\tilde Q_5\,\tilde Q_2^{*}$ | conjugate-linear | neither |

**Proof.** The four values are the four theorems above. For the class: a left multiplication is conjugate-linear and a right multiplication is linear, so a $\mathbb{C}$-linear composite cannot be a left multiplication and a conjugate-linear composite cannot be a right multiplication; the two linear composites are excluded from the class of the left multiplications by the same parity, and from the class of the right multiplications by the closed-form tests of the two corollaries above.

**Remark.** Apart from the degenerate composite of the zero multiplications, no composition of two multiplication operators is again a multiplication operator — the closest the family comes is $R_{e_t} \circ R_{e_t} = \mathrm{id}$, and the identity is not a multiplication operator either — so neither family is closed and neither is a monoid; the only element common to $\mathcal{L}$ and $\mathcal{R}$ is zero, since a map that is both linear and conjugate-linear is zero. The table is the operator form of the group's negative statements: the absence of a unit, the failure of associativity and the failure of flexibility all read as the failure of the operator families to close.

## The Absence of a Monoid

### The Failure of Closure

**Theorem.** Neither the left multiplications nor the right multiplications form a monoid under composition.

**Proof.** A monoid of operators requires closure under composition and an identity in the class. The left multiplications are not closed, by the corollary after the composition law; the right multiplications are not closed, by the corollary after their composition law. For the identity, no $L_{\tilde Q_5}$ is the identity operator, since $L_{\tilde Q_5}(\tilde Q_1) = \tilde Q_5^{\natural}\tilde Q_1^{*}$ equals $\tilde Q_1$ for all $\tilde Q_1$ only if $\tilde Q_5^{\natural} = e_t$ and $\tilde Q_1^{*} = \tilde Q_1$ for all $\tilde Q_1$, which fails; and no $R_{\tilde Q_5}$ is the identity for the same reason.

**Remark.** The identity of the operator monoid is the plain two-sided operator $T_{e_t,e_t}$, which is the identity of the sandwich monoid and is not a multiplication operator of the product; the left and right multiplications sit inside the sandwich monoid and generate it, but they do not contain its identity. This is the operator-level form of the absence of a unit of the multiplication.

### The Regular Map Is Not Multiplicative

**Proposition.** The regular map $\ell : \mathbb{B} \to \operatorname{End}(\mathbb{B})$, $\tilde Q_5 \mapsto L_{\tilde Q_5}$, is injective and $\mathbb{C}$-linear, but it is not multiplicative,

$$
\ell(\tilde Q_5)\ell(\tilde Q_2) = T_{\tilde Q_5^{\natural},\,\overline{\tilde Q_2}} \neq L_{\tilde Q_5 \star \tilde Q_2} = L_{\tilde Q_5^{\natural}\tilde Q_2^{*}} ,
$$

for generic $\tilde Q_5, \tilde Q_2$.

**Proof.** The injectivity and the linearity are the two propositions of the parity section; the equality $\ell(\tilde Q_5)\ell(\tilde Q_2) = T_{\tilde Q_5^{\natural},\overline{\tilde Q_2}}$ is the composition law; the value $L_{\tilde Q_5\star\tilde Q_2}$ is the left multiplication by the product. The two operators differ, one being linear and the other conjugate-linear, except for vanishing parameters.

**Remark.** A regular map that is linear and injective but not multiplicative is a **linear embedding of the module that is not a representation of the multiplication**, and it is the exact operator form of the statement that $\mathbb{B}$ is not a module over $(\mathbb{B},\star)$: the module axiom $L_{\tilde Q_5}L_{\tilde Q_2} = L_{\tilde Q_5\star\tilde Q_2}$ fails. The associator of *The Associator of the General Quaternionic Sesquilinear Product* is the obstruction, since the associator's vanishing is exactly the multiplicativity of the regular map.

### The Comparison with the Four General Products

**Theorem (the left multiplications of the four general products).**

| product | $L_{\tilde Q_5}(\tilde Q_1)$ | parity | $L_{\tilde Q_5} \circ L_{\tilde Q_2}$ | monoid |
|---|---|---|---|---|
| $\tilde Q_5\tilde Q_1$ | $\tilde Q_5\tilde Q_1$ | $\mathbb{C}$-linear | $L_{\tilde Q_5\tilde Q_2}$ | yes |
| $\tilde Q_5^{\natural}\tilde Q_1$ | $\tilde Q_5^{\natural}\tilde Q_1$ | $\mathbb{C}$-linear | $L^{\natural}_{\tilde Q_2\tilde Q_5}$ | yes, opposite |
| $\tilde Q_5\tilde Q_1^{*}$ | $\tilde Q_5\tilde Q_1^{*}$ | conjugate-linear | $\tilde Q_5\tilde Q_1\tilde Q_2^{*}$ | no |
| $\tilde Q_5^{\natural}\tilde Q_1^{*}$ | $\tilde Q_5^{\natural}\tilde Q_1^{*}$ | conjugate-linear | $\tilde Q_5^{\natural}\tilde Q_1\overline{\tilde Q_2}$ | no |

**Proof.** The first row is the associativity of the plain product. The second is the composition $L^{\natural}_{\tilde Q_5}L^{\natural}_{\tilde Q_2}(\tilde Q_1) = \tilde Q_5^{\natural}\tilde Q_2^{\natural}\tilde Q_1 = (\tilde Q_2\tilde Q_5)^{\natural}\tilde Q_1 = L^{\natural}_{\tilde Q_2\tilde Q_5}(\tilde Q_1)$, which is the opposite monoid (*Introduction to the General Quaternionic Algebra*) and is recorded in *Relations Between the Four General Products* §*The Left Multiplications*. The third is the sibling sesquilinear composition $L^{*}_{\tilde Q_5}L^{*}_{\tilde Q_2}(\tilde Q_1) = \tilde Q_5(\tilde Q_2\tilde Q_1^{*})^{*} = \tilde Q_5\tilde Q_1\tilde Q_2^{*}$, which is $\mathbb{C}$-linear whereas $L^{*}$ is conjugate-linear, so the class is not closed. The fourth is the composition law of this article.

**Remark.** The comparison is the row of *Comparison Between the Four General Products* that reads the monoid property, and it separates the four general products into two classes: the two bilinear products, whose left multiplications form monoids, and the two sesquilinear products, whose left multiplications do not. The dividing line is the parity of the left multiplication: it is linear for the bilinear products, so that the composition of two of them has the same parity as the factors and stays in the class, and conjugate-linear for the sesquilinear products, so that the composition has the opposite parity and leaves the class.

## Worked Cases

### The Unit Candidate

**Proposition.** At $\tilde Q_5 = e_t$ the two multiplications are the two conjugations,

$$
L_{e_t} = {}^{*} , \qquad R_{e_t} = {}^{\natural} ,
$$

and they satisfy $L_{e_t}^{2} = R_{e_t}^{2} = \mathrm{id}$ and $L_{e_t} \circ R_{e_t} = R_{e_t} \circ L_{e_t} = \bar{\cdot}$, the coefficientwise conjugation.

**Proof.** The first two are the two actions of $e_t$ (*The Two One-Sided Actions and the Absence of a Unit*). For the squares, the composition law gives $L_{e_t}^{2} = T_{e_t^{\natural},\overline{e_t}} = T_{e_t,e_t} = \mathrm{id}$ and $R_{e_t}^{2} = T_{\overline{e_t},e_t^{*}} = T_{e_t,e_t} = \mathrm{id}$. For the mixed product, $L_{e_t}(R_{e_t}(\tilde Q_1)) = e_t^{\natural}e_t\overline{\tilde Q_1} = \overline{\tilde Q_1}$, and $R_{e_t}(L_{e_t}(\tilde Q_1)) = \overline{\tilde Q_1}e_te_t^{*} = \overline{\tilde Q_1}$.

**Remark.** The operator identity $\mathrm{id}$ is the composition $L_{e_t}^{2}$, and it is not a left multiplication; this is the smallest instance of the failure of closure, and it is the operator form of the absence of a unit: the closest the family comes to containing the identity is the square of the left multiplication by $e_t$.

### The Idempotents and the Units

**Proposition.** Let $\tilde\Pi$ be a nontrivial idempotent of the multiplication, $\tilde\Pi \star \tilde\Pi = \tilde\Pi$. Then

$$
L_{\tilde\Pi}(\tilde\Pi) = \tilde\Pi , \qquad L_{\tilde\Pi}\bigl(\tilde\Pi^{\natural}\bigr) = \langle\tilde\Pi\rangle_{\natural}\,e_t . 
$$

**Proof.** The first is the idempotent equation, $L_{\tilde\Pi}(\tilde\Pi) = \tilde\Pi \star \tilde\Pi = \tilde\Pi$. For the second, the nontrivial idempotents have real coordinates (*Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra*), so $\overline{\tilde\Pi} = \tilde\Pi$ and $(\tilde\Pi^{\natural})^{*} = \overline{\tilde\Pi} = \tilde\Pi$; hence $L_{\tilde\Pi}(\tilde\Pi^{\natural}) = \tilde\Pi^{\natural}(\tilde\Pi^{\natural})^{*} = \tilde\Pi^{\natural}\tilde\Pi = \langle\tilde\Pi\rangle_{\natural}e_t$, the plain product of an element with its natural conjugate being the norm times the identity.

**Remark.** With $\langle\tilde\Pi\rangle_{\natural} = 1$ for the nontrivial idempotents of *Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra*, the second value is $e_t$, and the two values together show that the left multiplication by an idempotent fixes the idempotent and sends its natural conjugate to the identity. This is the operator reading of the two-sided nature of an idempotent, and it is the closest the operator theory comes to the unit that the multiplication does not have.

## Summary

The left and right multiplications of the general quaternionic sesquilinear multiplication are $L_{\tilde Q_5}(\tilde Q_1) = \tilde Q_5^{\natural}\tilde Q_1^{*}$ and $R_{\tilde Q_5}(\tilde Q_1) = \tilde Q_1^{\natural}\tilde Q_5^{*}$. The left multiplication is conjugate-linear and the right one is linear; the map $\tilde Q_5 \mapsto L_{\tilde Q_5}$ is $\mathbb{C}$-linear and the map $\tilde Q_5 \mapsto R_{\tilde Q_5}$ is conjugate-linear, both injective, so the two families are two different images of $\mathbb{B}$ and not a single regular representation. The composition laws are $L_{\tilde Q_5} \circ L_{\tilde Q_2} = T_{\tilde Q_5^{\natural},\overline{\tilde Q_2}}$ and $R_{\tilde Q_5} \circ R_{\tilde Q_2} = T_{\overline{\tilde Q_2},\tilde Q_5^{*}}$, both compositions $\mathbb{C}$-linear; the mixed compositions $L_{\tilde Q_5}R_{\tilde Q_2} = \tilde Q_5^{\natural}\tilde Q_2\overline{\tilde Q_1}$ and $R_{\tilde Q_2}L_{\tilde Q_5} = \overline{\tilde Q_1}\tilde Q_5\tilde Q_2^{*}$ are conjugate-linear. Since every left multiplication is conjugate-linear and every right one is linear, the compositions leave the two classes, and neither family is closed under composition or contains an identity: neither is a monoid. The left multiplications are the sandwiches $S_{\tilde Q_5^{\natural},e_t}$, and the monoid they generate is the sandwich monoid of *The Sesquilinear Sandwich Operator*, whose identity is the ordinary two-sided operator $T_{e_t,e_t}$. The regular map is a linear injection that is not multiplicative, which is the operator form of the failure of associativity, and the four general products split into the two bilinear ones, whose left multiplications form monoids, and the two sesquilinear ones, whose left multiplications do not.

## Summary of Notation

| symbol | meaning |
|---|---|
| $L_{\tilde Q_5}(\tilde Q_1) = \tilde Q_5 \star \tilde Q_1 = \tilde Q_5^{\natural}\tilde Q_1^{*}$ | the left multiplication, conjugate-linear |
| $R_{\tilde Q_5}(\tilde Q_1) = \tilde Q_1 \star \tilde Q_5 = \tilde Q_1^{\natural}\tilde Q_5^{*}$ | the right multiplication, linear |
| $L_{\tilde Q_5} = S_{\tilde Q_5^{\natural},e_t}$ | the left multiplication as a sandwich |
| $T_{\tilde Q_1,\tilde Q_2}(\tilde Q_3) = \tilde Q_1\tilde Q_3\tilde Q_2$ | the ordinary two-sided operator |
| $L_{\tilde Q_5} \circ L_{\tilde Q_2} = T_{\tilde Q_5^{\natural},\overline{\tilde Q_2}}$ | the composition of two left multiplications |
| $R_{\tilde Q_5} \circ R_{\tilde Q_2} = T_{\overline{\tilde Q_2},\tilde Q_5^{*}}$ | the composition of two right multiplications |
| $L_{\tilde Q_5} \circ R_{\tilde Q_2} = \tilde Q_5^{\natural}\tilde Q_2\overline{\tilde Q_1}$ | a mixed composition, conjugate-linear |
| $R_{\tilde Q_2} \circ L_{\tilde Q_5} = \overline{\tilde Q_1}\tilde Q_5\tilde Q_2^{*}$ | the other mixed composition |
| $\ell : \tilde Q_5 \mapsto L_{\tilde Q_5}$ | the regular map, linear and injective but not multiplicative |
| $L_{e_t} = {}^{*}$, $R_{e_t} = {}^{\natural}$ | the two actions of the unit candidate |

## Further Reading

- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the regular representation of an algebra and the multiplication operators.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the structure of the multiplication operators and the Peirce decomposition of an algebra by them.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the semilinear operators attached to an algebra with an involution.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the operator closure of a non-associative multiplication and the derivations it generates.
