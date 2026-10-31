# __Operator Family Conventions__

## Introduction

This article belongs to the nine conventions articles of the mathematical corpus. It follows *Operator and Calculus Conventions* and precedes *Index, Notation and Corpus Conventions*. It fixes the vocabulary of the operator families: the four letters, the two slots and the index of a basis operator, the names of the four sets, the units of the algebra and of the operator space, the matrix and its frame, the four strata and the two halves, the three words, and the four adjoint signs.

**The article names, and it does not prove.** No dimension is stated here, no closure, no inclusion, no properness and no property of a family. A name is fixed once, so that the article which proves a property can write it once. Where a sentence below reads like a theorem, it is a rule for reading a glyph: it says what the symbol denotes, not what the object is.

The order follows the dependence. The four letters come first, because the names of the sets and the superscripts of the matrices are built from them. The slots follow, because a name carrying a subscript is read through its slots. The names of the sets follow the slots; the units and the frame follow the names; and the strata, the words and the adjoint signs close, because the operator articles read a family on a stratum with the words and the signs fixed last.

**Boundaries.** The element, its subspaces and its marks are *Algebra and Element Conventions*; the twelve products and the four forms are *Product and Form Conventions*; the norms and the unitary convention are *Norm and Unitary Conventions*; the root, the idempotent and the nilpotent are *Special Element and Peirce Conventions*; the frames are *Frame Conventions*; the two matrix models and their regular representation are *Matrix Representations Conventions*; the operator that is its element, the dagger and the array rule are *Operator and Calculus Conventions*; and the superscripts and the typography are *Index, Notation and Corpus Conventions*. Every citation in this article is to one of these eight.

## The Four Families and Their Letters

### $L$, $R$, $T$, $\Theta$

**Four families, four letters.** The operator articles write four families, and an operator of one of them carries the letter of its family:

| Family | Letter | Glyph | Parameters |
|---|---|---|---|
| left | $L$ | $L_{\tilde Q}$ | one |
| right | $R$ | $R_{\tilde Q}$ | one |
| two-sided | $T$ | $T_{\tilde Q,\tilde P}$ | two |
| sandwich | $\Theta$ | $\Theta_{\tilde Q}$ | one |

**The letter is upright, the parameter is in the subscript.** The letter names the family and is a capital roman; the subscript names the element and keeps that element's own mark, the tilde included. $L_{\tilde Q}$ is read as one glyph: the operator of the left family whose parameter is $\tilde Q$. The tilde is never moved to the letter, and the letter never takes a tilde of its own.

**The letters are actions, not slots.** $L$ names left multiplication and $R$ names right multiplication. The same two letters name the two copies of the algebra in *Matrix Representations Conventions*, §*The 4×4 Regular Representation*, and the convention there holds here: the letter names the action, and a change of frame does not exchange the two actions even where it exchanges the two tensor slots.

**No fifth letter is implied.** An involution, a change of frame and a derivation also occur in the operator articles, and each carries the letter that its own article gives it. The four letters are the vocabulary of the four families assembled from the multiplication; they do not assert that every operator belongs to one of the four.

## The Slots

### The Left Multiplier, the Right Multiplier, the Argument

In $T_{\tilde Q,\tilde P}$ the first subscript is the left multiplier and the second the right multiplier, and the operator acts by $X\mapsto\tilde QX\tilde P$. For $L$ and $R$ the same rule holds with one subscript: $L_{\tilde Q}$ acts by $X\mapsto\tilde QX$ and $R_{\tilde P}$ by $X\mapsto X\tilde P$. The order of the subscripts is the order of the factors around the argument, left factor first.

**The argument is never a subscript.** The argument of an operator occupies a third slot that is written in parentheses when it is named, as in $T_{\tilde Q,\tilde P}(\tilde X)$. A glyph with three subscripts is not written, and the two subscripts of $T$ are always the two multipliers.

**The sandwich has one free slot.** The sandwich is $\Theta_{\tilde Q}=T_{\tilde Q,\tilde Q^{\ast}}$. Its second subscript is the star of the first and is not chosen, so the family has one parameter and the letter $\Theta$ is reserved for the member whose second slot is the star of the first. A two-sided operator with two free parameters is written $T_{\tilde Q,\tilde P}$, never $\Theta$.

### The Index of a Basis Operator

A Greek index on $L$ or $R$ is the index of a basis element: $L_\mu=L_{e_\mu}$ and $R_\nu=R_{e_\nu}$. A Greek pair on $T$ is the pair of its slots, $T_{\mu\nu}=L_\mu R_\nu$, read in that order, the first index belonging to the left slot. The sandwich carries the index of its one free slot, $\Theta_\mu=\Theta_{e_\mu}$. A roman letter stands for a general element and a Greek letter for a basis element; the index names the element and never a matrix entry, so $L_\mu$ is the left multiplication by $e_\mu$ and its matrix is written $\mathsf M_4^{L}(e_\mu)$.

## The Names of the Sets

### $\operatorname{End}_L$, $\operatorname{End}_R$, $\operatorname{End}_{LR}$, $\operatorname{End}_{LR\ast}$

**The ambient and the four sets.** The ambient operator space is $\operatorname{End}(\mathbb{B})=\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, and the field subscript is written whenever the field is in view. The four sets are named from the four families:

| Set | Members | Read as |
|---|---|---|
| $\operatorname{End}_L(\mathbb{B})$ | $L_{\tilde Q}$ | the left multipliers |
| $\operatorname{End}_R(\mathbb{B})$ | $R_{\tilde Q}$ | the right multipliers |
| $\operatorname{End}_{LR}(\mathbb{B})$ | $T_{\tilde Q,\tilde P}$ | the two-sided operators |
| $\operatorname{End}_{LR\ast}(\mathbb{B})$ | $\Theta_{\tilde Q}$ | the sandwiches |

**The subscript is the family's.** The subscript of a set repeats the letters of the family that populates it and is not a tensor slot. The star in $\operatorname{End}_{LR\ast}$ repeats the star of the sandwich's second slot; it is part of the name.

### The Four Matrix Letters

A matrix of a named family carries the family's letters in the superscript, and its arguments are the parameters in the order of the slots:

| Matrix | Family | Arguments |
|---|---|---|
| $\mathsf M_4^{L}$ | left | the element |
| $\mathsf M_4^{R}$ | right | the element |
| $\mathsf M_4^{LR}$ | two-sided | the left and the right multiplier |
| $\mathsf M_4^{LR\ast}$ | sandwich | the parameter |

The superscript is written as a letter or a pair of letters, never as a second subscript: $\mathsf M_4^{L}$, not $\mathsf M_{4,L}$. A matrix of a general operator carries no family superscript and is written with the bracket of §*The Matrix and Its Frame*. A matrix of the $2\times2$ model is written $\mathsf M_2(\tilde Q)$ and belongs to no family of this article.

### What the Names Do Not Assert

**The names are labels.** Five readings are excluded by construction.

- A name asserts no dimension. The dimension of a set is stated, with its field, by the article that proves it.
- A name asserts no closure, under addition, under composition or under an adjoint.
- A name asserts no inclusion between two sets, and no properness where an inclusion holds. The letters of a longer name do not entail the shorter name.
- A name with two letters is one name. $\operatorname{End}_{LR}$ is not the sum $\operatorname{End}_L+\operatorname{End}_R$, and it is not a product of two sets.
- The star of $\operatorname{End}_{LR\ast}$ is part of the name and does not mean that the set is stable under an adjoint.

## The Units

### The Units of the Algebra

The units of $\mathbb{B}$ are $e_t,\vec e_x,\vec e_y,\vec e_z$, in that order, the coefficient basis of *Algebra and Element Conventions* and *Frame Conventions*. The unit $e_t$ is the identity of the algebra. A direction index $\mu$ or $\nu$ runs over $t,x,y,z$ in that order.

### The Units $E_{ij}$ of the Operator Space

The units of the operator space are the matrix units $E_{ij}$ of *Special Element and Peirce Conventions*, §*The General Peirce Convention*, with $1$-based indices: the first index is the row and the second the column. The identity operator is $\mathrm{I}_4$, and the identity matrix of the $2\times2$ model is $\mathrm{I}_2$; the identity of the algebra stays $e_t$.

**The two alphabets are not exchanged.** A direction index names a unit of the algebra, and a row-column pair names a unit of the operator space. The two are never interchanged: $L_{e_\mu}$ is an operator and $E_{\mu\mu}$ is a matrix unit, and neither glyph stands for the other. The identity of the algebra $e_t$ is never written $\mathrm{I}$, and the identity operator $\mathrm{I}_4$ is never written $e_t$.

## The Matrix and Its Frame

### The Bracket $[F]_{\mathcal{B}}$

The matrix of an operator $F$ in a basis $\mathcal{B}$ is written $[F]_{\mathcal{B}}$. The frame is the subscript of the bracket, it is always written, and it is never inherited from a preceding display: a matrix written without its frame is the matrix of no operator.

**The two writings are distinct.** The bracket carries an operator; the sans-serif $\mathsf M$ carries a family or the $2\times2$ model. Thus $[F]_{\mathcal{B}}$ is the matrix of a general operator in the frame $\mathcal{B}$, $\mathsf M_4^{L}(\tilde Q)$ is the matrix of a left multiplier, and $\mathsf M_2(\tilde Q)$ is the image of an element in the $2\times2$ model. The three glyphs are not interchangeable: the bracket on an operator gives a matrix, the bracket on an element gives a coordinate column.

### The Change $C_{\Pi}$

The change from the Peirce frame to the coefficient frame is written $C_{\Pi}$. Its columns are the four Peirce elements read in coefficient coordinates; it carries a coordinate column from the Peirce frame to the coefficient frame, and its inverse carries the other way. A display that uses the change writes it with its inverse, $C_{\Pi}[\cdot]C_{\Pi}^{-1}$ or $C_{\Pi}^{-1}[\cdot]C_{\Pi}$, and the side of the inverse is the side of the frame being left. The subscript $\Pi$ records the Peirce frame and is not an index.

**Every display declares its frame.** The coefficient basis and the Peirce frame are both used in the operator articles, and no display inherits a frame from another display or from another article. An entry is read only with the frame that produced it.

## The Four Strata and the Two Halves

### $\Sigma_{11}$, $\Sigma_{10}$, $\Sigma_{01}$, $\Sigma_{00}$

**The two bits.** The strata of the algebra are labelled by two bits:

| Label | First bit | Second bit |
|---|---|---|
| $\Sigma_{11}$ | $N\neq0$ | $B^2\neq0$ |
| $\Sigma_{10}$ | $N\neq0$ | $B^2=0$ |
| $\Sigma_{01}$ | $N=0$ | $B^2\neq0$ |
| $\Sigma_{00}$ | $N=0$ | $B^2=0$ |

The first bit records the norm $N$ of *Product and Form Conventions* and the second the square $B^2$ of the vector part, each bit being $1$ when the quantity is non-zero and $0$ when it vanishes. The label is read from left to right in that order.

**The label is not an algebra.** No arithmetic is done on the two bits: $\Sigma_{11}$ is not the sum of $\Sigma_{10}$ and $\Sigma_{01}$, and the subscripts are not exponents. A stratum is a name for a domain on which an operator is read, and it is not an index of the operator.

### $\mathbb{M}_+$ and $\mathbb{M}_-$

**Fixed and anti-fixed.** The two halves of the algebra are $\mathbb{M}_+$ and $\mathbb{M}_-$, the Hermitian and anti-Hermitian subspaces of *Algebra and Element Conventions*, §*The Hermitian and Anti-Hermitian Subspaces*. The plus records the fixed space of the star and the minus the anti-fixed space; the two signs record fixed and anti-fixed, and never positivity or negativity.

## The Words

### Rank, Length, Dimension

**Rank.** The rank of an operator $F$ is written $\operatorname{rank}F$, and it is written of an operator and of a matrix. It is never written of an element of the algebra.

**Length.** The length of a two-sided operator $M$ is written $\ell(M)$. It is the number of one-sided factors in a decomposition of $M$, and it is not an alternative name for rank: the two words are not interchangeable, even where an article proves the two numbers equal.

**Dimension.** A dimension is written $\dim_{\mathbb{C}}$ or $\dim_{\mathbb{R}}$, and the field is never omitted. A bare dimension is not written. A dimension is written of a set, never of an operator: an operator has a rank.

### The Unit, the Identity and the Closed Ray

**Three words.** The unit of the algebra is $e_t$; the identity of the operator space is $\mathrm{I}_4$. The closed ray of the identity is written as a set,

$$
\{\lambda\,\mathrm{I}_4:\lambda\geq0\},
$$

and never with the letter $R$, which names the right family.

## The Four Adjoints

### The Signs ${}^{\approx}$, ${}^{N}$, ${}^{\ast}$, ${}^{\natural\ast}$

The four adjoints of the four pairings of *Product and Form Conventions* are written on the operator with four signs:

| Sign | Adjoint | Pairing |
|---|---|---|
| ${}^{\approx}$ | plain | plain bilinear |
| ${}^{N}$ | quaternionic | quaternionic bilinear |
| ${}^{\ast}$ | Hermitian | Hermitian |
| ${}^{\natural\ast}$ | Krein | Krein |

**The sign is written on the operator.** The sign is a superscript on the operator, after a bracket where the operator carries subscripts: $(L_{\tilde Q}R_{\tilde P})^{\approx}$ and $(L_{\tilde Q})^{N}$. It is never written on the parameter, and the parameter keeps its own mark.

**The letter $N$ is not the natural sign.** The quaternionic adjoint of an operator is written with the capital roman $N$, and the natural conjugation of an element with the sign ${}^{\natural}$. The two marks are distinct because the objects are: the sign conjugates an element, and the letter names the form whose adjoint is taken.

**The dagger is not one of the four.** The general adjoint of an operator is the dagger ${}^{\dagger}$ of *Operator and Calculus Conventions*, §*The Operators*. It covers the four signs and is not a fifth one, and it is never written on an element.

## Summary

The four families are written $L$, $R$, $T$ and $\Theta$: left multiplication, right multiplication, the two-sided operator and the sandwich. The letter is an upright capital and names the family; the parameter is in the subscript and keeps its own mark. The subscripts of $T$ are positional, the left multiplier first and the right multiplier second, and the argument is never a subscript. The sandwich has one free slot, because its second subscript is the star of the first. A Greek index is the index of a basis element, $L_\mu=L_{e_\mu}$ and $T_{\mu\nu}=L_\mu R_\nu$, and it never names a matrix entry.

The four sets are $\operatorname{End}_L(\mathbb{B})$, $\operatorname{End}_R(\mathbb{B})$, $\operatorname{End}_{LR}(\mathbb{B})$ and $\operatorname{End}_{LR\ast}(\mathbb{B})$, named from the four families, with the ambient written $\operatorname{End}(\mathbb{B})=\operatorname{End}_{\mathbb{C}}(\mathbb{B})$. A named family's matrix carries the family's letters in the superscript, $\mathsf M_4^{L}$, $\mathsf M_4^{R}$, $\mathsf M_4^{LR}$ and $\mathsf M_4^{LR\ast}$; a general operator's matrix is written with the bracket $[F]_{\mathcal{B}}$. The names assert no dimension, no closure, no inclusion and no properness, and a name of two letters is one name, not a sum of sets.

The units of the algebra are $e_t,\vec e_x,\vec e_y,\vec e_z$ and its identity is $e_t$; the units of the operator space are the matrix units $E_{ij}$ and its identity is $\mathrm{I}_4$. The two alphabets are never exchanged. The bracket carries its frame and never omits it, and the Peirce change is $C_{\Pi}$, written with its inverse. Every display declares its frame.

The strata are labelled by two bits, the norm first and the square of the vector part second, and the label is not an algebra. The two halves $\mathbb{M}_+$ and $\mathbb{M}_-$ record fixed and anti-fixed under the star, not positivity and negativity. Rank is written of an operator, length of a two-sided operator and dimension of a set with its field; the unit of the algebra is $e_t$, the identity of the operator space is $\mathrm{I}_4$, and the closed ray of the identity is written as a set. The four adjoint signs are ${}^{\approx}$, ${}^{N}$, ${}^{\ast}$ and ${}^{\natural\ast}$; the quaternionic sign is the capital letter $N$ and not the natural sign; and the dagger is the general adjoint, not a fifth of them.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{\tilde Q}$, $R_{\tilde P}$ | The left and the right multiplier |
| $T_{\tilde Q,\tilde P}$ | The two-sided operator, left multiplier first |
| $\Theta_{\tilde Q}=T_{\tilde Q,\tilde Q^{\ast}}$ | The sandwich, with one free slot |
| $L_\mu$, $R_\nu$, $T_{\mu\nu}$, $\Theta_\mu$ | The basis operators, $L_\mu=L_{e_\mu}$ and $T_{\mu\nu}=L_\mu R_\nu$ |
| $\operatorname{End}(\mathbb{B})=\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ | The ambient operator space |
| $\operatorname{End}_L(\mathbb{B})$, $\operatorname{End}_R(\mathbb{B})$ | The sets of the left and the right multipliers |
| $\operatorname{End}_{LR}(\mathbb{B})$, $\operatorname{End}_{LR\ast}(\mathbb{B})$ | The sets of the two-sided operators and of the sandwiches |
| $\mathsf M_4^{L}$, $\mathsf M_4^{R}$, $\mathsf M_4^{LR}$, $\mathsf M_4^{LR\ast}$ | The matrices of the four families |
| $[F]_{\mathcal{B}}$ | The matrix of a general operator in the frame $\mathcal{B}$ |
| $C_{\Pi}$ | The change from the Peirce frame to the coefficient frame |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | The units of the algebra; $e_t$ is its identity |
| $E_{ij}$, $\mathrm{I}_4$, $\mathrm{I}_2$ | The matrix units and the two identities |
| $\Sigma_{11}$, $\Sigma_{10}$, $\Sigma_{01}$, $\Sigma_{00}$ | The four strata, norm bit first |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | The two halves, fixed and anti-fixed under the star |
| $\operatorname{rank}$, $\ell$, $\dim_{\mathbb{C}}$, $\dim_{\mathbb{R}}$ | Rank, length and dimension with its field |
| $\{\lambda\,\mathrm{I}_4:\lambda\geq0\}$ | The closed ray of the identity |
| ${}^{\approx}$, ${}^{N}$, ${}^{\ast}$, ${}^{\natural\ast}$ | The four adjoint signs, plain, quaternionic, Hermitian and Krein |
| ${}^{\dagger}$ | The general adjoint of an operator |

## Further Reading

- [Algebra and Element Conventions](conventions-in-mathematics.html). The base, the units, the element and its coefficients, the remarkable subspaces and the conjugations.
- [Product and Form Conventions](conventions-of-the-twelve-products-and-the-four-forms.html). The twelve products and their names, the four forms and their letters.
- [Norm and Unitary Conventions](conventions-of-the-norms-and-the-unitary-convention.html). The four algebraic norms, the qualified regular and degenerate, and the unitary convention.
- [Special Element and Peirce Conventions](conventions-of-the-special-elements-and-the-peirce-decomposition.html). The root, the idempotent, the nilpotent and the matrix units.
- [Frame Conventions](conventions-of-the-frames.html). The two frames of the corpus, the Clifford map and the metric each frame carries.
- [Matrix Representations Conventions](conventions-of-the-matrix-models.html). The $2\times2$ isomorphism and the $4\times4$ regular representation with its two copies.
- [Operator and Calculus Conventions](conventions-of-the-operators-and-the-differential-calculus.html). The operator that is its element, the named operators and the dagger.
- [Index, Notation and Corpus Conventions](conventions-of-the-indices-the-notation-and-the-corpus.html). The superscripts, the subscript rules and the typography of the source.
