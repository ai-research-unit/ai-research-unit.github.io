
# __Convolution on a Topological Group__

## Introduction

Convolution turns the space of functions on a group into an algebra: the **convolution** of two functions $f$ and $g$ is the function whose value at $x$ collects the products $yz = x$, and the operation is bilinear, associative and compatible with the translation structure of the group. On a topological group the question is which topology on the function space makes convolution continuous, and the answer links the algebra of functions to the operator layer of the category. This article defines convolution, proves its associativity and its elementary algebra, identifies the algebra it generates, and separates the part that uses no measure from the part that uses the invariant integral.

The article assumes the topological group, its translations and their continuity from *Topological Groups* and *Operators on a Topological Group*, the abstract translations and their laws from *Left and Right Multiplication in a Group*, and the group algebra of finitely supported functions from *Group Algebras*. The invariant integral used to define convolution of continuous functions on a locally compact group is the **Haar integral**, which is *Locally Compact Groups and Haar Measure* in Part III: it is named here, and integrated in that cited sense, but it is not constructed and nothing is proved with it. The convolution algebra $L^1(G)$, its approximate identities and its Fourier transform are Part III, *Analysis on Groups*. Nothing analytic beyond the boundary named here, and nothing geometric, is used.

Throughout, $G$ is a topological group with identity $e$, $k$ is a field, functions are $k$-valued, $C(G)$ is the algebra of continuous functions with the topology of uniform convergence on compacta, and $k[G] \subseteq C(G)$ is the group algebra of finitely supported functions. The **delta** at $a$ is the basis element $\delta_a$, with $\delta_a(a) = 1$ and $\delta_a(x) = 0$ for $x \neq a$.

## Convolution of Finitely Supported Functions

### Definition and Bilinearity

**Definition.** For functions $f, g : G \to k$ whose supports are finite, the **convolution** $f * g$ is

$$
(f*g)(x) = \sum_{y \in G} f(y)\,g(y^{-1}x) = \sum_{yz = x} f(y)\,g(z) .
$$

The two sums agree by the substitution $z = y^{-1}x$, and both are finite: only the finitely many $y$ in $\operatorname{supp} f$ contribute, and for each of them only the finitely many $z$ in $\operatorname{supp} g$ contribute.

**Proposition (bilinearity).** Convolution is bilinear: $(f_1+f_2)*g = f_1*g + f_2*g$, $f*(g_1+g_2) = f*g_1 + f*g_2$, and $(\lambda f)*g = f*(\lambda g) = \lambda(f*g)$ for $\lambda \in k$. Its support satisfies

$$
\operatorname{supp}(f*g) \subseteq (\operatorname{supp} f)(\operatorname{supp} g),
$$

and in particular is finite.

**Proof.** Bilinearity is the distributivity of the finite sum. If $yz = x$ with $f(y) \neq 0$ and $g(z) \neq 0$ then $x$ is a product of an element of $\operatorname{supp} f$ and one of $\operatorname{supp} g$, which is the inclusion; it is finite because a product of two finite sets is finite.

### Associativity

**Theorem.** Convolution is associative: $(f*g)*h = f*(g*h)$ for all finitely supported $f, g, h$.

**Proof.** For every $x$,

$$
((f*g)*h)(x) = \sum_{yz=x} (f*g)(y)\,h(z) = \sum_{yz=x}\ \sum_{uv=y} f(u)\,g(v)\,h(z),
$$

and the triples $(u,v,z)$ occurring are exactly those with $uvz = x$; the sum is over a finite set, so it may be reorganised as

$$
\sum_{uvz=x} f(u)\,g(v)\,h(z) = \sum_{ut=x}\ \sum_{vw=t} f(u)\,g(v)\,h(w) = (f*(g*h))(x).
$$

The only point to check is that the reorganisation is legitimate, and it is: the index set is finite, so the sum is a finite sum and associativity of addition applies term by term.

**Corollary.** The finitely supported functions form an associative $k$-algebra under convolution, with identity $\delta_e$. The map $a \mapsto \delta_a$ is an injective homomorphism of the group $G$ into the units of this algebra, and

$$
\delta_a * \delta_b = \delta_{ab}, \qquad \delta_a^{-1} = \delta_{a^{-1}} .
$$

**Proof.** The identity is $\delta_e$, since $(\delta_e*g)(x) = g(e^{-1}x) = g(x)$ and $(g*\delta_e)(x) = g(xe^{-1}) = g(x)$. For the products, $\delta_a*\delta_b = \delta_{ab}$ by the definition with the unique contributing pair $y = a$, $z = b$. Injectivity is clear from $\delta_a(e) \neq \delta_b(e)$ for $a \neq b$.

The corollary identifies the convolution algebra of finitely supported functions with the **group algebra** $k[G]$ of *Group Algebras*: the definition above is the multiplication of that algebra, written on functions instead of on formal sums. The identification is the reason convolution is the natural product on functions on a group, and it is used without further comment.

### The Algebra Generated

**Theorem.** The convolution algebra $k[G]$ is generated as a $k$-algebra by the deltas $\{\delta_a : a \in G\}$, and it is commutative if and only if $G$ is abelian.

**Proof.** Every finitely supported $f$ is the finite sum $f = \sum_a f(a)\,\delta_a$, so the deltas generate. For commutativity, $\delta_a*\delta_b = \delta_{ab}$ and $\delta_b*\delta_a = \delta_{ba}$, so commutativity of the algebra forces $ab = ba$ for all $a, b$; conversely, if $G$ is abelian then $yz = zy$ and the substitution $y \leftrightarrow z$ in $(f*g)(x) = \sum_{yz=x}f(y)g(z)$ gives $(g*f)(x)$.

**Corollary (the centre and the augmentation).** The centre of $k[G]$ consists of the functions constant on the conjugacy classes of $G$, and the **augmentation** $\epsilon(f) = \sum_a f(a)$ is an algebra homomorphism $k[G] \to k$.

**Proof.** $f$ is central if and only if $\delta_a * f = f * \delta_a$ for every $a$, that is $f(a^{-1}x) = f(xa^{-1})$ for every $x$, which is the constancy on conjugacy classes. For the augmentation, $\epsilon(f*g) = \sum_x \sum_{yz=x}f(y)g(z) = \sum_y\sum_z f(y)g(z) = \epsilon(f)\epsilon(g)$, a reorganisation of a finite sum.

## The Convolution Operators

### Convolution with a Delta

**Proposition.** Left and right convolution by a delta are the translations:

$$
\delta_a * f = L_a f, \qquad f * \delta_b = R_{b^{-1}} f,
$$

where $(L_af)(x) = f(a^{-1}x)$ and $(R_bf)(x) = f(xb)$ are the translations of functions.

**Proof.** $(\delta_a*f)(x) = f(a^{-1}x)$ and $(f*\delta_b)(x) = f(xb^{-1})$, both by the definition and the single contributing term.

**Corollary.** The convolution operators by deltas are exactly the translation operators, and they are homeomorphisms of $C(G)$ for the topology of uniform convergence on compacta.

**Proof.** The first statement is the proposition, read for every $a$; for the second, $L_a$ carries a function to a function whose values are those of $f$ at points translated by $a$, so it preserves the supremum on each compact set and its inverse is $L_{a^{-1}}$.

### Convolution as an Operator

**Definition.** For a finitely supported $\phi$ the **convolution operator** $T_\phi$ is the map $f \mapsto \phi * f$ on functions.

**Proposition.** $T_\phi$ is a continuous linear operator on $C(G)$, and it is a finite linear combination of translations,

$$
T_\phi = \sum_{a} \phi(a)\,L_a .
$$

**Proof.** $\phi = \sum_a \phi(a)\delta_a$ as a finite sum, and convolution is bilinear, so $\phi * f = \sum_a \phi(a)(\delta_a * f) = \sum_a \phi(a) L_a f$, a finite linear combination of the continuous operators $L_a$; a finite linear combination of continuous operators is continuous.

**Corollary.** The assignment $\phi \mapsto T_\phi$ is an injective algebra homomorphism from $k[G]$ into the algebra of continuous operators on $C(G)$; its image is the algebra of finite linear combinations of translations, and $T_{\phi*\psi} = T_\phi \circ T_\psi$.

**Proof.** $T_{\phi*\psi}(f) = (\phi*\psi)*f = \phi*(\psi*f) = T_\phi(T_\psi f)$ by associativity, and injectivity follows from $T_\phi(\delta_e) = \phi$.

## Continuity

### What the Finitely Supported Case Proves

**Theorem.** The map $k[G] \times k[G] \to k[G]$, $(f,g) \mapsto f*g$, is continuous for the topology of uniform convergence on compacta restricted to the finitely supported functions, and for each fixed $f$ the operator $T_f$ is continuous on $C(G)$.

**Proof.** The second statement is the proposition above. For the first, $f*g$ is a finite bilinear combination of the products $\delta_a*\delta_b = \delta_{ab}$; a finite bilinear combination of continuous maps is continuous, and the deltas depend continuously on $a$ in the discrete image $G \subseteq C(G)$.

The theorem is the topological content of the purely algebraic associativity: on the finitely supported functions, where the product is a finite sum, convolution is continuous without any hypothesis on $G$.

### The Case of Continuous Functions

For general continuous functions the product is no longer a finite sum, and the definition requires the invariant integral.

**Definition (cited).** Let $G$ be locally compact Hausdorff and let $dx$ be a left Haar measure, *Locally Compact Groups and Haar Measure*, Part III. For $f, g \in C_c(G)$ the **convolution** is

$$
(f*g)(x) = \int_G f(y)\,g(y^{-1}x)\,dy ,
$$

the integral being taken in the cited sense of Part III.

**Theorem (cited).** Convolution is a bilinear, associative product on $C_c(G)$ making it an algebra; it extends to $L^1(G)$, which is a Banach algebra under the $L^1$ norm, and $C_c(G)$ is dense in it. Convolution is commutative exactly when $G$ is abelian, and it is continuous as a map $L^1(G)\times L^1(G)\to L^1(G)$.

**Proof.** The construction of the integral, the invariance that makes the definition independent of the choice of the measure, the Fubini step in associativity, the density and the norm inequality $\lVert f*g\rVert_1 \le \lVert f\rVert_1\lVert g\rVert_1$ are all Part III, *Locally Compact Groups and Haar Measure* and *The Convolution Algebra $L^1(G)$*; the present article cites them and does not reprove them.

**Remark.** The finitely supported functions are the intersection of the two treatments: $k[G] \subseteq C_c(G)$ when $G$ is discrete, and each finitely supported function is integrable for the counting measure, so the algebra of the first sections is the subalgebra of the cited $C_c(G)$-algebra spanned by the deltas. The continuity of the finitely supported product is thus a special case of the cited continuity, recovered without the integral.

**Remark (compact groups).** On a compact group with the normalised Haar measure the integral of the constant $1$ is $1$, and the pointwise estimate $\lvert(f*g)(x)\rvert \le \sup_y \lvert f(y)\rvert \sup_z\lvert g(z)\rvert$ shows that convolution is continuous on $C(G)$ with the supremum metric; this is the finite-measure case of the cited theorem, and the measure is still Part III's.

## Summary

Convolution of finitely supported functions on a topological group is the product $(f*g)(x) = \sum_{yz=x}f(y)g(z)$; it is bilinear and associative, the deltas satisfy $\delta_a*\delta_b = \delta_{ab}$, and the algebra it generates is the group algebra $k[G]$, commutative exactly when the group is abelian, with centre the class functions and augmentation the sum of the coefficients. Left and right convolution by a delta are the translations, $\delta_a*f = L_af$ and $f*\delta_b = R_{b^{-1}}f$, so the algebra acts on the functions by finite linear combinations of translations, and the assignment $\phi\mapsto T_\phi$ is an injective homomorphism into the continuous operators on $C(G)$. On the finitely supported functions the product is continuous for the topology of uniform convergence on compacta without any hypothesis, while for general continuous functions on a locally compact group the definition uses the Haar integral and the associativity, the continuity and the algebra $L^1(G)$ are Part III's *The Convolution Algebra $L^1(G)$*, cited here and not reproved.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(f*g)(x) = \sum_{yz=x}f(y)g(z)$ | convolution of finitely supported functions |
| $\delta_a$ | the delta at $a$, $\delta_a(a) = 1$ and $\delta_a(x) = 0$ for $x\neq a$ |
| $k[G]$ | the convolution algebra of finitely supported functions, the group algebra |
| $\delta_a*\delta_b = \delta_{ab}$ | the deltas multiply as the group does |
| $\delta_e$ | the identity of the convolution algebra |
| $Z(k[G])$ | the class functions, constant on conjugacy classes |
| $\epsilon(f) = \sum_a f(a)$ | the augmentation, an algebra homomorphism |
| $L_af(x) = f(a^{-1}x)$, $R_bf(x) = f(xb)$ | the translations of functions |
| $\delta_a*f = L_af$, $f*\delta_b = R_{b^{-1}}f$ | convolution by a delta is a translation |
| $T_\phi$, $T_\phi = \sum_a\phi(a)L_a$ | the convolution operator by a finitely supported $\phi$ |
| $dx$ | the left Haar measure of Part III, cited for the continuous case |
| $L^1(G)$ | the convolution algebra of Part III, cited |

## Further Reading

- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis I* (Springer, second edition, 1979), for the convolution algebra of a locally compact group and the algebra of measures.
- Lynn H. Loomis, *An Introduction to Abstract Harmonic Analysis* (Van Nostrand, 1953; reprinted Dover, 2011), for the group algebra, the convolution product and its continuity.
- Walter Rudin, *Fourier Analysis on Groups* (Interscience, 1962; reprinted Wiley, 1990), for convolution on a locally compact abelian group.
- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, second edition, 2015), for the measure-theoretic construction of convolution and the approximate identities.
- Nicolas Bourbaki, *General Topology*, Chapters 3 and 4 (Springer, 1995), for the topology of uniform convergence on compacta used on the function spaces.
