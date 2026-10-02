
# __The Left and Right Multiplication Operators on a Topological Vector Space__

## Introduction

A topological vector space that carries a continuous multiplication turns every element into two operators on itself, the **left multiplication** $L_{a}(x) = ax$ and the **right multiplication** $R_{a}(x) = xa$. These operators are linear, they are continuous because the multiplication is, and they compose by the rules $L_{a}L_{b} = L_{ab}$, $R_{a}R_{b} = R_{ba}$ and $L_{a}R_{b} = R_{b}L_{a}$, so the left multiplications form a representation of the algebra and the right multiplications an anti-representation, and each acts on the other by commuting. The space is then a module over the algebra of left multiplications, and the whole two-sided operator family of this group — the sandwiches, the signed operators and their adjoints — is built from these two families.

This article fixes the one-sided operators on a topological vector space that carries a continuous multiplication, their continuity, their composition, the representations they define, and the module structure they induce. The topological vector spaces, the neighbourhoods and the bounded sets are *Topological Modules and Vector Spaces*; the topology of bounded convergence and the operator space are *Operators on a Locally Convex Space*; the operator norm and the operator algebra are *Bounded Operators and the Operator Norm*; the abstract theory of topological algebras, where the multiplication carries its own topology, is *Topological Algebras* in the next category of this Part. The signed one-sided operator is *The Signed Left Multiplication on a Topological Vector Space*, and the two-sided sandwich is *The Signed Sandwich on a Topological Vector Space*. No form, no involution and no grading is used here; the element involution starts with the group `- * Theory`.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, $E$ is a Hausdorff topological vector space over $\mathbb{K}$ carrying a multiplication

$$
E \times E \longrightarrow E, \qquad (a, b) \longmapsto ab ,
$$

which is bilinear and separately continuous, so that $E$ is a topological algebra; the identity, when it exists, is written $1$. The multiplication need not be associative or commutative, but associativity is assumed from the point where the composition laws are read. For $a \in E$ the **left and right multiplications** are

$$
L_{a}(x) = ax, \qquad R_{a}(x) = xa \qquad (x \in E),
$$

and $\mathcal{L}(E)$ is the algebra of continuous operators on $E$.

## The One-Sided Multiplications

**Proposition (linearity and continuity).** For every $a \in E$ the maps $L_{a}$ and $R_{a}$ are linear and continuous, so $L_{a}, R_{a} \in \mathcal{L}(E)$; the assignments $a \mapsto L_{a}$ and $a \mapsto R_{a}$ are linear, and the multiplication is recovered as $ab = L_{a}(b) = R_{b}(a)$.

**Proof.** Linearity is the bilinearity of the multiplication: $L_{a}(x + \lambda y) = a(x + \lambda y) = ax + \lambda ay$, and the same for $R_{a}$. Continuity is the separate continuity of the multiplication: $L_{a}$ is continuous at $0$ because $a \cdot 0 = 0$ and the multiplication is continuous in its second variable, and likewise $R_{a}$ in its first variable. Linearity of $a \mapsto L_{a}$ and $a \mapsto R_{a}$ is the bilinearity again, and the recovery formula is the definition.

**Proposition (composition laws).** Assume the multiplication associative. Then for all $a, b \in E$,

$$
L_{a}L_{b} = L_{ab}, \qquad R_{a}R_{b} = R_{ba}, \qquad L_{a}R_{b} = R_{b}L_{a} .
$$

Thus $a \mapsto L_{a}$ is a homomorphism and $a \mapsto R_{a}$ an anti-homomorphism of $E$ into $\mathcal{L}(E)$, and the two images commute with one another.

**Proof.** $L_{a}L_{b}(x) = a(bx) = (ab)x = L_{ab}(x)$ by associativity; $R_{a}R_{b}(x) = (xb)a = x(ba) = R_{ba}(x)$; $L_{a}R_{b}(x) = a(xb) = (ax)b = R_{b}L_{a}(x)$. Commutation of the images is the third identity.

**Proposition (identity and faithfulness).** If the multiplication is associative and unital with unit $1$, then $L_{1} = R_{1} = \mathrm{id}$, the algebras $\{L_{a}\}$ and $\{R_{a}\}$ are the images of the regular representations, and the kernels are the annihilators,

$$
\ker(L_{\bullet}) = \{a : aE = 0\}, \qquad \ker(R_{\bullet}) = \{a : Ea = 0\} .
$$

If the multiplication is associative with unit and the representation is faithful on one side, then $E$ acts faithfully as operators on itself on that side.

**Proof.** $L_{1}(x) = 1x = x$ and $R_{1}(x) = x1 = x$; the kernel computation is the definition, $L_{a} = 0$ exactly when $ax = 0$ for all $x$; the faithfulness statement is that a coalgebra of the representations vanishes identically.

## The Module Structure

**Definition.** The **left regular module** of $E$ is the space $E$ with the action $a \cdot x = L_{a}(x) = ax$, and the **right regular module** is $E$ with the action $x \cdot a = R_{a}(x) = xa$; both actions are continuous, because the multiplications are. The **two-sided** action is the pair $(L_{a}, R_{b})$, and the operators that commute with every $L_{a}$ form the **commutant**, likewise on the right.

**Proposition (the module axioms and the commutant).** With the left regular action $E$ is a left module over itself, with the right regular action a right module, and the two actions commute, so $E$ is a bimodule over itself. If $E$ is associative with unit, the commutant of the family $\{L_{a}\}$ in $\mathcal{L}(E)$ is exactly the family $\{R_{b}\}$ of right multiplications, and the commutant of $\{R_{b}\}$ is exactly $\{L_{a}\}$.

**Proof.** The module axioms are the associativity and the unit laws; the commutation of the two actions is $L_{a}R_{b} = R_{b}L_{a}$, which also exhibits $\{R_{b}\}$ inside the commutant of $\{L_{a}\}$. Conversely, if $S$ commutes with every $L_{a}$, then for every $a$ one has $S(a) = S(a \cdot 1) = aS(1) = R_{S(1)}(a)$, so $S = R_{S(1)}$; the symmetric argument identifies the other commutant. This is the double centraliser computation for the regular representation of a unital associative algebra.

**Proposition (the bimodule of operators).** Let $F$ be a topological vector space and let $E = \mathcal{L}(F)$ be its algebra of continuous operators. Then the left and right multiplications on $E$ are the operators

$$
L_{A}(T) = AT, \qquad R_{B}(T) = TB \qquad (A, B, T \in E),
$$

they are continuous for the topology of bounded convergence, and the two-sided operator $T \mapsto ATB = L_{A}R_{B}(T)$ is the general product operator. This is the primary instance of the construction, and the two-sided family of this group is formed on it.

**Proof.** Composition of operators is associative and bilinear, and it is separately continuous for the topology of bounded convergence by *Operators on a Locally Convex Space*; hence $L_{A}$ and $R_{B}$ are continuous, and the composition law $L_{A}R_{B}(T) = ATB$ is the associativity of composition.

## Continuity and the Operator Norm

**Proposition (continuity of the representations).** If the multiplication of $E$ is jointly continuous, then $a \mapsto L_{a}$ and $a \mapsto R_{a}$ are continuous maps $E \to \mathcal{L}(E)$ when the target carries the topology of bounded convergence; if $E$ is a normed algebra with submultiplicative norm, then $\lVert L_{a}\rVert \leq \lVert a\rVert$ and $\lVert R_{a}\rVert \leq \lVert a\rVert$, with equality when $\lVert 1\rVert = 1$.

**Proof.** For the continuity, a basic neighbourhood of $0$ in $\mathcal{L}_{b}(E)$ is $N(B, V)$ with $B$ bounded and $V$ a neighbourhood of $0$; $L_{a} \in N(B, V)$ means $aB \subseteq V$, which holds when $a$ is small and $B$ is bounded, by joint continuity and boundedness. For the norm, $\lVert L_{a}x\rVert = \lVert ax\rVert \leq \lVert a\rVert\lVert x\rVert$ gives $\lVert L_{a}\rVert \leq \lVert a\rVert$, and $\lVert L_{a}1\rVert = \lVert a\rVert$ gives equality when $\lVert 1\rVert = 1$; the right multiplication is the same computation.

**Proposition (the images are closed under products and contain the identity).** The set $\{L_{a}\}$ is a subalgebra of $\mathcal{L}(E)$ with the same multiplication table as $E$, and it contains $\mathrm{id}$ exactly when $E$ is unital; the centre of $E$ acts by both multiplications, $L_{z} = R_{z}$ for $z$ central.

**Proof.** Closure under products is $L_{a}L_{b} = L_{ab}$, and the identity statement is $L_{1} = \mathrm{id}$; centrality gives $L_{z}(x) = zx = xz = R_{z}(x)$.

## Examples

**Example (the endomorphism algebra).** For $E = M_{n}(\mathbb{K})$ with the matrix product the left multiplication $L_{A}$ is the operator $X \mapsto AX$ on the matrix space, with matrix $A \otimes I$ in the natural basis, and the right multiplication $R_{B}$ is $X \mapsto XB$, with matrix $I \otimes B^{\mathsf{T}}$; they commute, and the map $(A, B) \mapsto L_{A}R_{B}$ is injective on pairs modulo the scalars.

**Example (the operator algebra).** For $E = \mathcal{L}(F)$ with composition, the left multiplication by $A$ is the operator $T \mapsto AT$ and the right multiplication by $B$ is $T \mapsto TB$; on a Hilbert space these are the operators whose matrix in an orthonormal basis is the Kronecker product, and the two-sided operator $T \mapsto ATB$ is the sandwich of the next article.

**Example (commutative and noncommutative cases).** On $E = C(K)$ with the pointwise product the multiplication is commutative, so $L_{f} = R_{f}$ is the multiplication operator $M_{f}$ of *Bounded Operators and the Operator Norm*, and the algebra generated is isometric to $C(K)$; on a noncommutative $E$, such as $M_{n}(\mathbb{K})$ with $n \geq 2$, the two families differ and the composition laws $L_{a}L_{b} = L_{ab}$, $R_{a}R_{b} = R_{ba}$ exhibit the opposite multiplication.

## Summary

On a topological vector space carrying a separately continuous bilinear multiplication, the left and right multiplications $L_{a}(x) = ax$ and $R_{a}(x) = xa$ are continuous linear operators, the assignments $a \mapsto L_{a}$ and $a \mapsto R_{a}$ are linear, and under associativity they obey $L_{a}L_{b} = L_{ab}$, $R_{a}R_{b} = R_{ba}$ and $L_{a}R_{b} = R_{b}L_{a}$, so the left multiplications form a representation and the right multiplications an anti-representation of the algebra on itself and the two images commute. With these actions the space is a bimodule over itself, and the operators commuting with all left multiplications are the right multiplications by central elements when the algebra is unital and associative. The continuity of the two families is automatic from the separate continuity of the multiplication; for the topology of bounded convergence it follows from joint continuity, and on a normed algebra the operator norms satisfy $\lVert L_{a}\rVert \leq \lVert a\rVert$ and $\lVert R_{a}\rVert \leq \lVert a\rVert$, with equality when the unit has norm one. The primary instance is the operator algebra $E = \mathcal{L}(F)$, where $L_{A}(T) = AT$, $R_{B}(T) = TB$ and the two-sided product $T \mapsto ATB$ is the operator on which the sandwich of the next article is built; the matrix algebra and the commutative algebra $C(K)$ are the standard examples.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E$ | Topological vector space with a continuous multiplication |
| $L_{a}(x) = ax$, $R_{a}(x) = xa$ | Left and right multiplications |
| $L_{a}L_{b} = L_{ab}$, $R_{a}R_{b} = R_{ba}$ | Composition laws |
| $L_{a}R_{b} = R_{b}L_{a}$ | Commutation of the two families |
| $a \mapsto L_{a}$, $a \mapsto R_{a}$ | Regular representation and anti-representation |
| left, right regular module | $E$ as a bimodule over itself |
| $L_{A}(T) = AT$, $R_{B}(T) = TB$ | The instance $E = \mathcal{L}(F)$ |
| commutant | Operators commuting with all $L_{a}$ |
| $\lVert L_{a}\rVert \leq \lVert a\rVert$ | Operator norm bound in the normed case |

## Further Reading

- Nicolas Bourbaki, *Topological Vector Spaces, Chapters 1–5* (Springer, 1987), for topological algebras, the regular representations and the continuity of the multiplications.
- Gottfried Köthe, *Topological Vector Spaces I* and *II* (Springer, 1969 and 1979), for the operator spaces and the multiplication operators.
- Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces* (Springer, second edition, 1999), for the topological algebra structure, the regular representations and the module structure.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the left and right multiplications on an operator algebra and the double centraliser.
- John B. Conway, *A Course in Functional Analysis* (Springer, second edition, 1990), for the multiplication operators and the regular representations of the algebra of operators.
