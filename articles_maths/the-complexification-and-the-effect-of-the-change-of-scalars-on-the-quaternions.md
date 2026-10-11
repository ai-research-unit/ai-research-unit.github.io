# __The Complexification and the Effect of the Change of Scalars on the Quaternions__

## Introduction

Everything the chapter has said about the quaternion algebra $\mathbb{H}$ holds over the field $\mathbb{R}$ of the scalars, and this article performs the **change of scalars** $\mathbb{R}\to\mathbb{C}$ and records its effect. The complexification is the algebra

$$
\mathbb{B}=\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}=\mathbb{H}\oplus i\mathbb{H} ,
$$

the **biquaternion algebra** of the biquaternion chapter, of real dimension eight where $\mathbb{H}$ has real dimension four, and of complex dimension four. The change of scalars alters every count of the chapter at once: the two general products become four, the six products and the six structures become twelve, the two forms become four and the two algebraic norms four, the group of involutions grows from two elements to four, and the division property is lost with the appearance of the zero divisors.

The article gives the complexification and its dimension, the **central imaginary** $i$ as the carrier of the new scalars, the **appearance of the sesquilinear family** and of the **second involution** ${}^{*}$, the **appearance of the zero divisors**, the **dictionary** of the statements about $\mathbb{H}$ against the statements about $\mathbb{B}$, and the **contrast with the realification** that the biquaternion chapter performs in the opposite direction. It assumes the two products, the six structures, the two forms and the two norms of the articles preceding it in this category, and it uses the four products, the twelve structures, the four forms and the four norms of the biquaternion chapter, which are *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* and *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*.

**Conventions.** Throughout, $\mathbb{H}=\{p_0e_0+\mathbf p\}$ is the real quaternion algebra with basis $e_0,e_1,e_2,e_3$, $\mathbb{C}=\mathbb{R}+i\mathbb{R}$ is the field of the scalars, and $\mathbb{B}=\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}$ is the biquaternion algebra with the same symbols $e_0,e_1,e_2,e_3$ over the complex scalars and the central imaginary $i$. The quaternion conjugation is ${}^{\natural}$, $\tilde Q^{\natural}=Q_0e_0-\mathbf Q$; complex conjugation of the coefficients is written $\bar{\cdot}$, $\overline{\tilde Q}=(\bar Q_0)e_0+\sum_k(\bar Q_k)e_k$; and the Hermitian conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$.

## The Complexification

**Proposition (the dimension count).** The complexification $\mathbb{B}=\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}$ has complex dimension four and real dimension eight, twice the real dimension of $\mathbb{H}$; its real basis is $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ and its complex basis $e_0,e_1,e_2,e_3$.

*Proof.* Extension of scalars tensors the real space $\mathbb{H}$ with the complex field, so a real basis of four elements becomes a complex basis of four elements and a real basis of eight; the elements $ie_k$ are the images of the $e_k$ under multiplication by the central imaginary.

So the change of scalars **doubles the dimension**, from four real to eight real, keeping the complex dimension at four; the two readings of the same algebra are $\mathbb{B}$ as a complex algebra of dimension four, the reading of the biquaternion chapter, and $\mathbb{B}$ as a real algebra of dimension eight, the reading of *Biquaternions as a Vector Space over $\mathbb{R}$*. The product of $\mathbb{H}$ extends to $\mathbb{B}$ unchanged, remaining $\mathbb{C}$-bilinear and associative, so the complexified algebra carries the multiplication of the quaternion algebra over the new field.

## The Central Imaginary

**Proposition (the carrier).** The imaginary unit $i$ is **central** in $\mathbb{B}$: it commutes with every element, $i\tilde Q=\tilde Q i$; it satisfies $i^2=-e_0$; and it realises the decomposition $\mathbb{B}=\mathbb{H}\oplus i\mathbb{H}$.

*Proof.* The imaginary unit is a scalar of the field of scalars, and the scalars of an algebra commute with every element; its square is $-1$ in the field, that is $-e_0$ in the algebra; and every element of $\mathbb{B}$ writes uniquely as $\tilde P+i\tilde Q$ with $\tilde P,\tilde Q\in\mathbb{H}$, which is the stated decomposition.

So the central imaginary $i$ is the **carrier of the change of scalars**: it is the element that the new field adds, it is central, and it is the complex structure $J$ of the realified algebra, of square $-e_0$. In the real reading of $\mathbb{B}$ the multiplication by $i$ is a real-linear map $J$ with $J^2=-\mathrm{id}$, a complex structure on the eight-dimensional real space, and the complex action on $\mathbb{B}$ is the real action together with $J$; this is *Biquaternions as a Vector Space over $\mathbb{R}$*.

## The Appearance of the Sesquilinear Family

**Theorem (the general products over the two fields).** A general product is read with a conjugation in each of its two slots, the conjugations being drawn from the involution group of the element and from the involution group of the base. Over $\mathbb{R}$ the base has the one involution, the identity, so the second slot of every general product is the identity and there are $\mathbf{2}$ general products; over $\mathbb{C}$ the base has the two involutions, the identity and complex conjugation $\bar{\cdot}$, so the second slot has two choices and there are $\mathbf{4}$ general products. The two new ones are **conjugate-linear** in their second slot: they are the **sesquilinear family**, absent over $\mathbb{R}$ and present over $\mathbb{C}$.

*Proof.* A product with the identity in the second slot is bilinear; a product with $\bar{\cdot}$ in the second slot is conjugate-linear there. Over $\mathbb{R}$ the identity is the only involution of the base, so no product is conjugate-linear and the four biquaternion products collapse to the two of *The Two General Products of the Quaternion $\mathbb{R}$ Space*; over $\mathbb{C}$ the two involutions of the base give two second-slot choices against the two first-slot choices, hence four products.

So the change of scalars **creates** the two sesquilinear general products, and with them the whole family the quaternion chapter has refused at each step: the second form of each family, the conjugate exchange, the conjugate-linear slot. The **counts of the chapter double** in the same way. The general products are $2$ over $\mathbb{R}$ and $4$ over $\mathbb{C}$; the products, the general products with their symmetric and antisymmetric halves, are $6$ over $\mathbb{R}$ and $12$ over $\mathbb{C}$; the structures are $6$ and $12$; the forms are $2$, both bilinear, and $4$, two bilinear and two sesquilinear; and the algebraic norms are $2$ and $4$. Each of these is the collapse to the smaller count recorded in *The 6 Products of the Quaternion Real Space*, *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, *The 2 Forms over the Quaternion $\mathbb{R}$ Space* and *The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space*.

## The Second Involution

**Proposition (the involution group).** The Hermitian conjugation ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ is an anti-automorphism of $\mathbb{B}$, of order two, **conjugate-linear** where ${}^{\natural}$ is linear, and it commutes with ${}^{\natural}$. Over $\mathbb{R}$ the coefficient conjugation $\bar{\cdot}$ is the identity and ${}^{*}$ coincides with ${}^{\natural}$; over $\mathbb{C}$ it is new, and the four maps $\mathrm{id},{}^{*},{}^{\natural},\bar{\cdot}$ form the Klein four-group.

*Proof.* The composition of the coefficientwise conjugation, an anti-automorphism of order two, with the quaternion conjugation, an anti-automorphism of order two, is an anti-automorphism of order two; the two commute because they act on the two independent structures of $\mathbb{B}$, the coefficients and the quaternion units; and $\bar{\cdot}$ is the composite of ${}^{*}$ and ${}^{\natural}$. Over $\mathbb{R}$ the coefficients are real, so $\bar{\cdot}=\mathrm{id}$ and ${}^{*}={}^{\natural}$; over $\mathbb{C}$ the four maps are distinct and every pair of non-identity elements generates the group, which is $V_4$, the group of *The Group of Involutions*.

So the change of scalars **doubles the group of involutions**, from $\{\mathrm{id},{}^{\natural}\}$ of two elements over $\mathbb{R}$ to the Klein four-group $\{\mathrm{id},{}^{*},{}^{\natural},\bar{\cdot}\}$ over $\mathbb{C}$. The new involution ${}^{*}$ is the one that creates the sesquilinear family, since it is the conjugate-linear involution the second slot draws its conjugation from; the two involutions ${}^{*}$ and ${}^{\natural}$ cut out the six remarkable subspaces of $\mathbb{B}$ in place of the two of $\mathbb{H}$, and the **invariant** and **anti-invariant** spaces of the two involutions are those of *Introduction to the Remarkable Subspaces*.

## The Appearance of the Zero Divisors

**Theorem (the loss of the division property).** The algebra $\mathbb{H}$ is a division algebra, every nonzero element being invertible and the quaternion norm $N_Q(\tilde p)=|\tilde p|^2e_0$ vanishing only at the origin. The algebra $\mathbb{B}$ has zero divisors: the bilinear norm $N(\tilde Q)=\sum_\mu Q_\mu^2$ is complex-valued and vanishes on nonzero elements, and its vanishing set is the **zero-divisor cone** $\mathcal{N}$, of complex dimension two and real dimension four; the elements $\tilde Q=e_0\pm ie_1$ are zero divisors of $\mathbb{B}$.

*Proof.* Over $\mathbb{R}$ the norm $\sum_\mu p_\mu^2$ is a sum of squares of real numbers, hence vanishes only when every coordinate vanishes, and *Comparison Between the Two General Products* gives the division property. Over $\mathbb{C}$ the same sum is a sum of complex squares, and the two equations $\mathrm{Re}\,\sum_\mu Q_\mu^2=0$ and $\mathrm{Im}\,\sum_\mu Q_\mu^2=0$ cut a cone of real dimension four in the eight real coordinates; the element $e_0+ie_1$ has $N=1+i^2=0$ and is a zero divisor, annihilating itself on one side, since $(e_0+ie_1)^{\natural}(e_0+ie_1)=N e_0=0$.

So the change of scalars **destroys the division property**: the definite multiplicative norm of $\mathbb{H}$ becomes the complex norm of $\mathbb{B}$, whose vanishing set is the zero-divisor cone, and with the zero divisors come the nilpotents, the non-trivial idempotents, the Peirce decomposition and the whole ring-theoretic vocabulary that the quaternion chapter has not needed. This is the sharpest single effect of the change of scalars, and the statement that no function of $\mathbb{B}$ is at once definite and multiplicative is the reason the two properties separate there; the zero-divisor cone, with its two families of maximal totally isotropic subspaces and its projective geometry, is owned by *The Isotropic Structure of the General Quaternionic Algebra* and *Nilpotents of the General Plain Algebra*.

## The Change of Scalars Structure by Structure

The six structures of *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* are read over the two fields, one line to a structure. Each of the six gains exactly one new structure over $\mathbb{C}$, its **sesquilinear twin**, the same product read with the star in the second slot; the six become the twelve structures of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

| structure over $\mathbb{R}$ | its rule | what the change of scalars does |
|---|---|---|
| $\mathrm{GPA}$, the general plain | $\tilde p\tilde q$ | associativity and the two-sided unit survive, the division property is lost, the norm becomes complex and the zero divisors appear; twin $\mathrm{GPS}$, the rule $\tilde P\tilde Q^{*}$ |
| $\mathrm{SPA}$, the symmetric plain | $\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$ | commutativity survives, the value becomes complex and the zero divisors are joined by the isotropic elements; twin $\mathrm{SPS}$ |
| $\mathrm{APA}$, the antisymmetric plain | $\tfrac12(\tilde p\tilde q-\tilde q\tilde p)$ | the alternation survives and the bracket complexifies, the extension remaining a Lie bracket; twin $\mathrm{APS}$ |
| $\mathrm{GQA}$, the general quaternionic | $\tilde p^{\natural}\tilde q$ | the left unit survives and the associativity is still absent; the value $N$ becomes complex and loses definiteness; twin $\mathrm{GQS}$ |
| $\mathrm{SQA}$, the symmetric quaternionic | $\tfrac12(\tilde p^{\natural}\tilde q+\tilde q^{\natural}\tilde p)$ | the commutativity survives; the scalar-valued definite value becomes a complex-valued one, so definiteness is lost; twin $\mathrm{SQS}$ |
| $\mathrm{AQA}$, the antisymmetric quaternionic | $\tfrac12(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)$ | the alternation survives and the Jacobi identity still fails; twin $\mathrm{AQS}$ |

The table records, for each structure, the fate of its **$\mathbb{C}$-bilinear extension**, the same product over the larger field: the associativity, the commutativity, the unit, the alternation and the Jacobi identity are **properties of the polynomial identities** and are unchanged by the extension of the field, while the division property and the definiteness are **properties of the diagonal** and are lost, the diagonal becoming complex-valued. The law of each twin is a separate reading, its second slot being conjugate-linear: the general plain twin is not associative and has the right unit alone, and the antisymmetric plain twin $\mathrm{APS}$ fails the Jacobi identity that its parent satisfies, so a law is not inherited by the twin automatically; the laws of the twelve structures are recorded in the biquaternion chapter. The doubling from six to twelve is the same doubling as that of the products and the forms, and it is the second slot alone that produces the six twins.

## The Dictionary of the Statements

The change of scalars gives a dictionary from the statements about $\mathbb{H}$ to the statements about $\mathbb{B}$, one line to a count or a property.

| statement about $\mathbb{H}$ | statement about $\mathbb{B}$ |
|---|---|
| real dimension $4$ | real dimension $8$, complex dimension $4$ |
| the base $\mathbb{R}$ with one involution | the base $\mathbb{C}$ with two involutions |
| group of involutions $\{\mathrm{id},{}^{\natural}\}$, two elements | Klein four-group $\{\mathrm{id},{}^{*},{}^{\natural},\bar{\cdot}\}$ |
| $2$ general products, both bilinear | $4$ general products, two bilinear and two sesquilinear |
| $6$ products and $6$ structures | $12$ products and $12$ structures |
| $2$ forms, both bilinear | $4$ forms, two bilinear and two sesquilinear |
| $2$ algebraic norms | $4$ algebraic norms |
| two remarkable subspaces | six remarkable subspaces |
| division algebra, no zero divisor | zero divisors, the zero-divisor cone $\mathcal{N}$ |
| norm real-valued and definite | norms complex-valued, definiteness lost on the cones |
| the quaternion norm definite and multiplicative | no function definite and multiplicative at once |

The dictionary is not a list of analogies but a list of **collapses**: each line of the right column is the statement over $\mathbb{C}$, and the left column is what it becomes when the coefficient conjugation $\bar{\cdot}$ is set equal to the identity and the sesquilinear family is deleted. Reading the left column upwards gives the extension of scalars; reading the right column downwards gives the collapse to the real field.

## The Contrast with the Realification

The biquaternion chapter performs the **change of scalars in the opposite direction**, reading $\mathbb{B}$ as an algebra over the subfield $\mathbb{R}$ by restriction of scalars; that is the **realification**, of *The Realification and the Effect of the Change of Scalars*, and it is not the inverse operation but the two readings of one and the same object.

| operation | direction | effect |
|---|---|---|
| complexification | $\mathbb{H}$ over $\mathbb{R}$, then $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}$ | dimension doubles, the sesquilinear family appears, the second involution appears, the zero divisors appear |
| realification | $\mathbb{B}$ over $\mathbb{C}$, then $\mathbb{B}$ over $\mathbb{R}$ | dimension doubles on the other side, the complex structure $J$ appears, the sesquilinear forms realify to signature-doubled real forms |

The two operations double the dimension in two different senses — the complexification of a real algebra adds an imaginary direction, and the realification of a complex algebra adds the real and imaginary parts of every complex coordinate — and they are the two readings of the ladder whose middle rungs are $\mathbb{C}$ over $\mathbb{R}$, $\mathbb{H}$ over $\mathbb{R}$ and $\mathbb{B}$ over $\mathbb{C}$. The complexification of the quaternion chapter and the realification of the biquaternion chapter meet at the real algebra $\mathbb{B}$, of real dimension eight, and the ladder is the object of *The Realification and the Effect of the Change of Scalars*, in the biquaternion chapter.

## Summary

The change of scalars $\mathbb{R}\to\mathbb{C}$ complexifies the quaternion algebra to $\mathbb{B}=\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}$, of real dimension eight where $\mathbb{H}$ has four; the carrier is the central imaginary $i$, of square $-e_0$, the complex structure of the realified algebra. The change creates the **sesquilinear family**: the second slot of a general product draws its conjugation from the involution group of the base, so the two products of $\mathbb{H}$ become the four of $\mathbb{B}$, two bilinear and two sesquilinear, and the counts of products, structures, forms and norms double, from $2,6,2,2$ to $4,12,4,4$. It creates the **second involution** ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, conjugate-linear and commuting with ${}^{\natural}$, and the group of involutions grows from two elements to the four of the Klein group, cutting out six remarkable subspaces in place of two.

It destroys the **division property**: the quaternion norm becomes the complex norm $\sum_\mu Q_\mu^2$, whose vanishing set is the zero-divisor cone $\mathcal{N}$, of real dimension four, so that $\mathbb{B}$ has zero divisors and $\mathbb{H}$ has none. The dictionary collects the statements of the two chapters as a list of collapses, and the operation is the inverse reading of the realification that the biquaternion chapter performs, the two meeting at the real algebra of dimension eight.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}$ | the complexification, the biquaternion algebra |
| $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ | the real basis of $\mathbb{B}$ |
| $i$, central, $i^2=-e_0$, $J^2=-\mathrm{id}$ | the carrier of the change of scalars |
| ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ | the Hermitian conjugation, conjugate-linear |
| $2\to4$ general products; $6\to12$ products | the doubling of the counts |
| $N(\tilde Q)=\sum_\mu Q_\mu^2$, $\mathcal N$ | the complex norm and the zero-divisor cone |
| $\mathbb{B}=\mathbb{H}\oplus i\mathbb{H}$ | the real splitting of the complexified algebra |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the complexification of the quaternion algebra and the two involutions of the biquaternions.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for extension and restriction of scalars and the effect on division algebras and their norms.
- Serge Lang, *Algebra* (Springer, Graduate Texts in Mathematics 211, 3rd ed. 2002), for the tensor product with a field extension, the central element and the change of the involution group.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the quaternion algebra over the complex field and its zero divisors.
