# __The Cup Product as an Operator__

## Introduction

The cohomology of a space is a graded ring, and a graded ring is a family of operators: the class $\varphi$ acts on the cohomology by left multiplication $\psi \mapsto \varphi \smile \psi$, and this **multiplication operator** $L_\varphi$ is a degree-$|\varphi|$ endomorphism. The product is recovered from the operators, the associativity of the product is the composition law of the operators, the graded commutativity of the product is the statement that the operators commute up to the Koszul sign, the Leibniz rule of the coboundary is the statement that $\delta$ is a derivation of the operator algebra, and the cap product is the action of the same classes on homology. Reading the cup product as an operator is not a restatement: it is the reading in which the cohomology appears as a ring of operators on itself, the pairing with homology appears as the adjointness of two representations, and the product appears as the operator induced by the diagonal.

The article develops the operator algebra of the cup product. It defines the left and right multiplication operators on cochains and on cohomology, proves that the two commute up to the Koszul sign and that the assignment $\varphi \mapsto L_\varphi$ is an injective graded ring homomorphism, exhibits the coboundary as a graded derivation and the multiplication by a cocycle as a chain map, identifies $L_\varphi$ and the cap product with $\varphi$ as adjoint operators under the evaluation pairing, and records the cases in which the operator is nilpotent, square-zero or of infinite order. The product itself — its cochain formula, the shuffle proof of graded commutativity, its naturality and the computations — is that of *Cup and Cap Products*; the evaluation pairing and the universal coefficient theorem are those of *Cohomology and the Universal Coefficient Theorem*; and the differential graded algebra of the cochains, of which these operators are the structure, is the instance in this category of the general theory of the planned *Homological Algebra* of Part I, written in parallel. The further operators that are not given by multiplication, the Steenrod operations, are the subject of *Classifying Spaces and Cohomology Operations*, and the operator that the multiplication by the Euler class defines on the cohomology of a double cover is the subject of *The Gysin Sequence of a Two-Fold Covering*.

Nothing analytic and nothing geometric is used. The article is the algebra of a graded ring acting on itself and on its dual; the manifold applications of the adjointness belong to *Poincaré Duality* and to the geometry of Part IV, and no distance, no norm and no measure is chosen. Throughout, $R$ is a commutative ring with identity $1 \neq 0$, the cohomology is the singular cohomology of *Cohomology and the Universal Coefficient Theorem*, $H^*(X;R)$ is its graded ring with the product of *Cup and Cap Products*, and $|\varphi|$ is the degree of a homogeneous class. The operators are written $L_\varphi$ and $R_\psi$ and the cap product operator is written $C_\varphi$; the Koszul sign $(-1)^{|\varphi||\psi|}$ is the one fixed in *Cup and Cap Products*.

## The Multiplication Operators

### The Left and the Right Operator

**Definition.** For a cohomology class $\varphi \in H^k(X;R)$, the **left multiplication operator** and the **right multiplication operator** are

$$
L_\varphi : H^n(X;R) \longrightarrow H^{n+k}(X;R), \qquad L_\varphi(\psi) = \varphi \smile \psi,
$$

$$
R_\varphi : H^n(X;R) \longrightarrow H^{n+k}(X;R), \qquad R_\varphi(\psi) = \psi \smile \varphi .
$$

The same symbols denote the operators on the cochain complex, defined by the same formulas on cochains.

The operator $L_\varphi$ is $R$-linear, it raises the degree by $|\varphi|$, and it is determined by $\varphi$ because $L_\varphi(1) = \varphi$ with $1$ the unit class; so the assignment is injective as soon as the cohomology is unital. At the cochain level $L_\varphi$ need not commute with $\delta$, and the computation of the failure is the Leibniz rule.

**Theorem.** The multiplication operator descends to cohomology: if $\varphi$ is a cocycle then $L_\varphi$ is a chain map of the cochain complex, $L_\varphi \delta = \delta L_\varphi$, and it induces the operator $L_{[\varphi]}$ on cohomology. For a general cochain the operator descends to cohomology as well, because the Leibniz rule writes the failure as a coboundary.

*Proof.* The Leibniz rule of *Cup and Cap Products*,

$$
\delta(\varphi \smile \psi) = (\delta\varphi) \smile \psi + (-1)^{|\varphi|} \varphi \smile (\delta\psi),
$$

reads $\delta L_\varphi = L_{\delta\varphi} + (-1)^{|\varphi|} L_\varphi \delta$ as operators on cochains. If $\delta\varphi = 0$ the second term vanishes and $L_\varphi$ commutes with $\delta$; in general the formula shows that $L_\varphi$ carries cocycles to cocycles modulo coboundaries and coboundaries to coboundaries, so it induces a well-defined operator on cohomology. $\square$

### The Composition and the Koszul Sign

**Theorem.** For cohomology classes $\varphi$ and $\psi$,

$$
L_\varphi L_\psi = L_{\varphi \smile \psi}, \qquad\qquad
L_\varphi L_\psi = (-1)^{|\varphi||\psi|}\, L_\psi L_\varphi ,
$$

and the assignment $\varphi \mapsto L_\varphi$ is an injective homomorphism of graded rings from the graded-commutative ring $H^*(X;R)$ to the graded-commutative ring of endomorphisms of the graded module $H^*(X;R)$.

*Proof.* The first identity is associativity of the cup product, $(\varphi\smile\psi)\smile\theta = \varphi\smile(\psi\smile\theta)$. The second is graded commutativity: $L_\varphi L_\psi(\theta) = \varphi\smile\psi\smile\theta$ and $L_\psi L_\varphi(\theta)=\psi\smile\varphi\smile\theta$, and moving $\varphi$ past $\psi$ contributes the sign $(-1)^{|\varphi||\psi|}$ while $\theta$ is unaffected because $L_\varphi$ moves with its own sign only against the classes it passes. The two identities are consistent: applying graded commutativity to $\varphi\smile\psi$ gives $L_\varphi L_\psi = L_{\varphi\smile\psi} = (-1)^{|\varphi||\psi|}L_{\psi\smile\varphi} = (-1)^{|\varphi||\psi|}L_\psi L_\varphi$. Injectivity is $L_\varphi(1)=\varphi$. $\square$

So the cohomology ring acts on itself by multiplication, the action is faithful, and the only deviation from an honest commutative algebra of operators is the Koszul sign: the operators of odd classes anticommute, and those of even classes commute with everything. When $2$ is not invertible the relation $L_\varphi L_\psi = -L_\psi L_\varphi$ for odd $\varphi,\psi$ is compatible with $L_\varphi^2 = -L_\varphi^2$, so $L_\varphi^2 = 0$ on the classes of odd degree.

### Unitality and the Algebra of Operators

The unit $1 \in H^0(X;R)$ gives $L_1 = \mathrm{id}$, so the image of the homomorphism is a subalgebra containing the identity. The **operator algebra of the cohomology** is the image

$$
\mathcal{L}(X;R) = \{L_\varphi : \varphi \in H^*(X;R)\} \subseteq \operatorname{End}_R\bigl(H^*(X;R)\bigr),
$$

isomorphic to $H^*(X;R)$ as a graded ring and acting faithfully and transitively on the left on the module $H^*(X;R)$. The set of all $R$-linear endomorphisms of the graded module is much larger; the operators that are multiplications are exactly the module endomorphisms over the ring, and the two agree with the whole endomorphism ring exactly when the cohomology is generated as a module over itself by the unit, which it is, so that the multiplications are the *left $H^*$-module endomorphisms* of the regular module.

## The Coboundary as a Derivation

### The Derivation Algebra

**Definition.** A **graded derivation** of degree $d$ of the cochain algebra is an $R$-linear operator $D : C^n \to C^{n+d}$ with

$$
D(\varphi \smile \psi) = (D\varphi)\smile\psi + (-1)^{d|\varphi|}\,\varphi\smile(D\psi).
$$

The graded derivations form a graded Lie algebra under the **graded commutator** $[D,E] = D E - (-1)^{|D||E|} E D$.

**Theorem.** The coboundary $\delta$ is a graded derivation of degree $1$ with $\delta^2 = 0$; the left multiplication $L_\varphi$ is a graded derivation of degree $|\varphi|$ exactly when $\delta\varphi = 0$; and the derivations of the cochain algebra generated by $\delta$ and the multiplications by cocycles have as their induced operators on cohomology the multiplications $L_{[\varphi]}$ and the zero operator for $\delta$.

*Proof.* The derivation property of $\delta$ is the Leibniz rule. For $L_\varphi$, its defect as a derivation is measured by $\delta(\varphi\smile\psi) - L_\varphi(\delta\psi) = (\delta\varphi)\smile\psi$, so the defect vanishes identically exactly when $\delta\varphi = 0$. On cohomology $\delta$ induces the zero operator because the cohomology is the quotient by the coboundaries, while a multiplication by a cocycle induces the multiplication by its class. $\square$

The operator algebra of the cohomology is therefore the quotient of the differential graded algebra of the cochains by the operators that are coboundaries, and it inherits the graded derivation $\delta$ as the zero operator: the differential that creates the cohomology disappears on passing to it, and what remains is the algebra of the multiplications together with the higher operations that are not derivations.

### The Operators of Non-Multiplicative Kind

The derivations of a graded-commutative algebra are themselves a graded Lie algebra, and the operators of the cochain algebra that are *not* multiplications are the higher operations. The **Steenrod operations** are the first family of these: they are additive operators on the mod-2 and mod-$p$ cohomology, they satisfy the Cartan formula, and they are not given by multiplication; their construction from the cup-product-of-chains and their axioms belong to *Classifying Spaces and Cohomology Operations*, and the operator reading is that they are elements of the algebra of natural cohomology operators, of which the multiplications of *Cup and Cap Products* are the degree-zero part for the classes in positive degrees.

## The Bicommutant and the Module Structure

### The Operators Commuting with the Multiplications

**Definition.** The **bicommutant** of the operator algebra $\mathcal{L}(X;R)$ is the set of $R$-linear endomorphisms $T$ of the graded module $H^*(X;R)$ that commute honestly with every left multiplication,

$$
\mathcal{L}(X;R)' = \bigl\{T \in \operatorname{End}_R(H^*(X;R)) : T L_\varphi = L_\varphi T \ \text{ for all } \varphi\bigr\},
$$

which is the ring of endomorphisms of $H^*(X;R)$ as a module over the ring, in the sense of the module theory of Part I.

**Theorem.** The bicommutant is exactly the set of **right multiplications**: an $R$-linear endomorphism $T$ of $H^*(X;R)$ commutes honestly with every $L_\varphi$ if and only if it is $R_\psi$ for the unique class $\psi = T(1)$, so that $\mathcal{L}(X;R)' = \{R_\psi\} \cong H^*(X;R)$ and it is isomorphic to the operator algebra. In particular the multiplications are exactly the module endomorphisms of the regular module, and the ring acts faithfully on itself.

*Proof.* A right multiplication commutes honestly with every left multiplication by associativity of the cup product: $R_\psi L_\varphi(\theta) = \varphi\smile\theta\smile\psi = L_\varphi R_\psi(\theta)$, with no sign because both orders multiply the three classes in the same sequence. Conversely, if $TL_\varphi = L_\varphi T$ for all $\varphi$ then $T(\varphi) = T(\varphi\smile1) = TL_\varphi(1) = L_\varphi T(1) = \varphi\smile T(1) = R_{T(1)}(\varphi)$, so $T = R_{T(1)}$; the class $T(1)$ is unique because $R_\psi(1)=\psi$, and the assignment $\psi\mapsto R_\psi$ is an isomorphism of graded rings because $R_\psi R_\theta = R_{\psi\smile\theta}$ by associativity. $\square$

So the honest commutant of the left multiplications is the right multiplications, and it is the ring itself; the module-theoretic structure of the cohomology over itself is thus completely described by the operator algebra.

### The Two Actions and the Koszul Sign

**Theorem.** A left multiplication $L_\varphi$ is $H^*(X;R)$-linear, that is it lies in the bicommutant, exactly when its Koszul sign against every class is trivial:

$$
L_\varphi \in \mathcal{L}(X;R)' \iff (-1)^{|\varphi||\psi|} = 1 \ \text{ for every } \psi \text{ with } L_\psi \neq 0 ,
$$

which holds in particular for every class $\varphi$ of even degree and for every class when the product is honestly commutative. In general $L_\varphi$ commutes with $L_\psi$ only up to the factor $(-1)^{|\varphi||\psi|}$, and the left action lies in the **graded** bicommutant, defined with that sign, whose elements are the signed right multiplications $\varphi \mapsto (-1)^{|\psi||\varphi|}\varphi\smile\psi$.

*Proof.* The relation $L_\varphi L_\psi = (-1)^{|\varphi||\psi|}L_\psi L_\varphi$ of the previous section is exactly the assertion that the honest commutator of the two operators is zero precisely when the sign is trivial; the description of the graded bicommutant is the same computation with the sign retained, giving $T(\varphi)=(-1)^{|T||\varphi|}\varphi\smile T(1)$ for a graded-commuting $T$. $\square$

So the graded commutativity of the cohomology is precisely the statement that the left action is central in the graded sense, and the honest center of the operator algebra consists of the multiplications by the classes of even degree together with the odd classes whose multiplication vanishes.

## The Product as the Diagonal Operator

### The Diagonal and the Cross Product

**Definition.** The **diagonal** of a space $X$ is $\Delta : X \to X \times X$, $\Delta(x) = (x,x)$; the **cross product** of classes is $\varphi \times \psi = \mathrm{pr}_1^*\varphi \smile \mathrm{pr}_2^*\psi \in H^{|\varphi|+|\psi|}(X \times X;R)$ of *Cup and Cap Products*.

**Theorem.** The cup product is the pullback of the cross product along the diagonal,

$$
\varphi \smile \psi = \Delta^*(\varphi \times \psi),
$$

and more generally for a map $f : X \to Y$ the multiplication operators intertwine the pullbacks:

$$
f^* L_\varphi = L_{f^*\varphi} f^* .
$$

Consequently the product is the operator induced by the diagonal, and a continuous map is a morphism of the operator algebra in the sense that $f^*$ is a ring homomorphism carrying $L_\varphi$ to $L_{f^*\varphi}$.

*Proof.* The identity $\Delta^*(\varphi\times\psi)=\varphi\smile\psi$ is the computation of *Cup and Cap Products* from the definition of the cross product and the pullbacks of the projections along the diagonal; the intertwining is the naturality of the cup product, $f^*(\varphi\smile\psi)=f^*\varphi\smile f^*\psi$, read as operators. $\square$

So the whole product structure of the cohomology is encoded in the single operator $\Delta^*$ on the cohomology of the square: the multiplication operators are the images under the pullback along the diagonal of the external multiplications, and the associativity and graded commutativity of the cup product are the corresponding properties of the diagonal $(X\times X)\times X \to X$ and the twist $X\times X\to X\times X$. The operator reading makes the product natural in the strongest sense: any construction that is natural for maps and multiplicative is determined by the diagonal.

### The Adjoint: the Cap Product

**Definition.** For a class $\varphi$, the **cap product operator** is

$$
C_\varphi : H_n(X;R) \longrightarrow H_{n-|\varphi|}(X;R), \qquad C_\varphi(c) = c \frown \varphi,
$$

the cap product of *Cup and Cap Products*. The operators pair with the evaluation pairing $\langle-,-\rangle$ of *Cohomology and the Universal Coefficient Theorem*.

**Theorem.** The cap product operator is the adjoint of the left multiplication operator under the evaluation pairing: for cohomology classes $\varphi,\psi$ and a homology class $c$,

$$
\langle L_\varphi \psi,\, c\rangle = \langle \psi,\, C_\varphi c\rangle .
$$

The operators compose contravariantly, $C_\psi C_\varphi = C_{\varphi\smile\psi}$, so that the assignment $\varphi \mapsto C_\varphi$ is a representation of the ring $H^*(X;R)$ on the graded module $H_*(X;R)$ up to the Koszul sign, and it is the same module structure as the cap product $H_*(X;R) \times H^*(X;R)\to H_*(X;R)$ of *Cup and Cap Products* read with the cohomology acting on the left.

*Proof.* At the cochain level, for $\varphi\in C^p$, $\psi\in C^q$ and a simplex $\sigma$ of degree $p+q$, the definition of the cup product gives $(\varphi\smile\psi)(\sigma)=\varphi(\sigma_{[0..p]})\psi(\sigma_{[p..p+q]})$, while the cap product is $C_\varphi(\sigma) = \varphi(\sigma_{[0..p]})\,\sigma_{[p..p+q]}$ and hence $\psi(C_\varphi\sigma) = \varphi(\sigma_{[0..p]})\psi(\sigma_{[p..p+q]})$, the same value. The contravariant composition is the associativity $c\frown(\varphi\smile\psi)=(c\frown\varphi)\frown\psi$. $\square$

**Corollary (Poincaré duality).** If $X$ is a closed oriented $n$-manifold, the cap product with the fundamental class, $c \mapsto c \frown [X]$, is an isomorphism $H^k(X;R)\cong H_{n-k}(X;R)$, and under it the operator $C_\varphi$ on homology corresponds to the multiplication $L_{\varphi^*}$ by the Poincaré dual of $\varphi$; the intersection form is the transport of the evaluation pairing. The manifold theory is that of *Poincaré Duality*, where the orientation, the fundamental class and the signature are treated, and the operator statement is used there.

## Examples

**Example (the projective space).** For $\mathbb{CP}^n$ the cohomology ring is $R[x]/(x^{n+1})$ with $|x|=2$, so $L_x$ is the shift operator on the free module with basis $1,x,\dots,x^n$, nilpotent of index $n+1$; the operator algebra is the whole quotient ring, and its order is the dimension. The two spaces $S^2\vee S^4$ and $\mathbb{CP}^2$ have isomorphic cohomology modules and non-isomorphic operator algebras: for the wedge the class of degree two satisfies $L_x = 0$ on the degree-four part (the product of the two generators is zero), while for $\mathbb{CP}^2$ it does not, and this is the operator form of the separation by the ring in *Cup and Cap Products*.

**Example (the torus and the exterior algebra).** For the torus, $H^*(T^n;R)\cong\Lambda_R(\alpha_1,\dots,\alpha_n)$ on classes of degree one, and the operators $L_{\alpha_i}$ are odd, square-zero and anticommuting: $L_{\alpha_i}^2 = 0$ and $L_{\alpha_i}L_{\alpha_j} = -L_{\alpha_j}L_{\alpha_i}$ for $i\neq j$. The operator algebra is the exterior algebra, and the module on which it acts is the same exterior algebra: multiplication is the wedge product, and the operators are the contractions of the exterior algebra with its dual basis up to the identification.

**Example (a Gysin operator).** For $\mathbb{RP}^n$ with $\mathbb{F}_2$ coefficients, $H^*(X;\mathbb{F}_2)=R[x]/(x^{n+1})$ with $|x|=1$ and $x^2\neq 0$, so $L_x$ is nilpotent of index $n+1$ and the operator measures the projective dimension. For the double cover $S^n\to\mathbb{RP}^n$, the multiplication by the Euler class $e=x$ is the operator whose kernel and image give the Gysin sequence of *The Gysin Sequence of a Two-Fold Covering*: the exactness of the Gysin sequence is the statement that the homology of the operator $L_e$ in its two middle degrees describes the cohomology of the cover and of the base.

## Summary

A cohomology class $\varphi$ acts on the cohomology by left multiplication, giving a degree-$|\varphi|$ operator $L_\varphi$; the operator descends to cohomology, and the assignment $\varphi\mapsto L_\varphi$ is an injective homomorphism of graded rings carrying the product to composition and the graded commutativity to the Koszul-sign commutation $L_\varphi L_\psi = (-1)^{|\varphi||\psi|}L_\psi L_\varphi$, so that the cohomology is faithfully represented as a ring of operators on itself. The honest bicommutant of the operator algebra is the ring of right multiplications, isomorphic to $H^*(X;R)$, and the left multiplications are exactly the operators that commute honestly with all the multiplications when the Koszul signs vanish. The coboundary is a graded derivation, $\delta L_\varphi = L_{\delta\varphi} + (-1)^{|\varphi|}L_\varphi\delta$, so the multiplication by a cocycle is a chain map and the multiplication by an arbitrary class still descends to cohomology; the graded derivations form a graded Lie algebra, and the operators that are not multiplications begin with the Steenrod operations. The product is the pullback of the cross product along the diagonal, $\varphi\smile\psi=\Delta^*(\varphi\times\psi)$, so the whole product is induced by the diagonal and is natural; the cap product operator $C_\varphi$ is the adjoint of $L_\varphi$ under the evaluation pairing, $\langle L_\varphi\psi,c\rangle=\langle\psi,C_\varphi c\rangle$, and composes contravariantly, $C_\psi C_\varphi=C_{\varphi\smile\psi}$, so that the cohomology acts on the homology as well as on itself. The product, its cochain formula, its naturality and its computations are those of *Cup and Cap Products*; what this article adds is the operator algebra, its derivation, its adjointness and the diagonal. Nothing analytic and nothing geometric was used.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\smile$ | Cup product, as in *Cup and Cap Products* |
| $L_\varphi$ | Left multiplication operator $\psi\mapsto\varphi\smile\psi$ |
| $R_\psi$ | Right multiplication operator $\varphi\mapsto\varphi\smile\psi$ |
| $\mathcal{L}(X;R)$ | The operator algebra $\{L_\varphi\}$ of the cohomology |
| $L_\varphi L_\psi = L_{\varphi\smile\psi}$ | Composition law: the product is composition |
| $L_\varphi L_\psi = (-1)^{|\varphi||\psi|}L_\psi L_\varphi$ | Graded commutativity as an operator identity |
| $\delta L_\varphi = L_{\delta\varphi}+(-1)^{|\varphi|}L_\varphi\delta$ | Leibniz rule: $\delta$ is a graded derivation |
| $[D,E]=DE-(-1)^{|D||E|}ED$ | Graded commutator of derivations |
| $\Delta : X\to X\times X$ | Diagonal; $\varphi\smile\psi=\Delta^*(\varphi\times\psi)$ |
| $\times$ | Cross product on a product of spaces |
| $\frown$, $C_\varphi(c)=c\frown\varphi$ | Cap product and the cap product operator |
| $\langle L_\varphi\psi,c\rangle=\langle\psi,C_\varphi c\rangle$ | Adjointness under the evaluation pairing |
| $C_\psi C_\varphi=C_{\varphi\smile\psi}$ | Contravariant composition of the cap operators |

## Further Reading

- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the cup and cap products, their associativity, graded commutativity and the relation to the diagonal.
- Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology* (Springer, 1982), for the product as the operator of the diagonal, the derivation property of the differential and the module structure on homology.
- Glen E. Bredon, *Topology and Geometry* (Springer, 1993), for the cohomology ring as a ring of operators, the cap product and the evaluation pairing.
- James R. Munkres, *Elements of Algebraic Topology* (Addison-Wesley, 1984), for the simplicial cup and cap products, the Leibniz rule and the diagonal approximation.
- Saunders Mac Lane, *Homology* (Springer, 1995), for the differential graded algebra of cochains, the graded derivations and the Koszul sign rule.
- Norman E. Steenrod and David B. A. Epstein, *Cohomology Operations* (Princeton University Press, 1962), for the Steenrod operations as the first non-multiplicative cohomology operators.
